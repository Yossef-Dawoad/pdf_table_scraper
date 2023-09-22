from collections import Counter

import pandas as pd
import tabula
from fastapi import Request

from .schemas import ScrapedData


def clean_process_data(dfs: list[pd.DataFrame]) -> pd.DataFrame:
    cleandf = []
    for df in dfs:
        df.dropna(how='all', inplace=True)
        new_columns = ['BALLOT NAME', 'PARTY', 'OFFICE TITLE', 'FILED DATE']
        df.columns = new_columns

        # Drop the first row which contains column descriptions
        df = df.iloc[1:]
        df.reset_index(drop=True, inplace=True)

        to_be_removed = ["OFFICE CATEGORY:",
                         "SECRETARY OF STATE", 'BALLOT NAME']
        removed_rows = df[df.isin(to_be_removed).any(axis=1)]
        df = df.drop(removed_rows.index)
        cleandf.append(df)

    # Print the cleaned DataFrame
    preprocessed = pd.concat(cleandf)
    return preprocessed.drop_duplicates()


def scrape_pdf(req: Request, pdf_file) -> list[ScrapedData]:
    """
    scrape the pdf file and return extracted data
    """
    dfs = tabula.read_pdf(pdf_file, stream=True, pages='1-10')
    clean_df = clean_process_data(dfs)

    clean_df = clean_df[['BALLOT NAME', 'PARTY', 'OFFICE TITLE']]
    clean_df.columns = ['names', 'party', 'postions']
    clean_df.to_dict('records')

    # Extract rows after header
    return clean_df
