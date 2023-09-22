from collections import Counter
from fastapi import Request
import tabula


def rename_cols_entities(req: Request, df, expected_categories: list):
    """
    rename the given columns by the Named Entity Recog entities
    """
    # getting ner mdoel from the state
    nlp = req.app.state['ner_model']

    for col in df.columns:
        # Apply the nlp model to the first 10 values in the column and extract the entity labels
        entity_labels = (df[col][:10]
                         .apply(
                             lambda x: [ent.label_ for ent in nlp(x).ents
                                        if ent.label_ in expected_categories]))
        # Count the entity labels
        entity_counts = Counter(entity_labels.sum())
        try:
            max_label, max_count = entity_counts.most_common(1)[0]
            if max_count > 2:
                # Rename the column with the entity label
                df.rename(columns={col: max_label}, inplace=True)
        except IndexError:  # we don't find any entity type for that col
            pass
    return df


def scrape_pdf(req: Request, file) -> dict:
    """
    scrape the pdf file and return extracted data
    """
    header_values_to_remove = [
        'OFFICE CATEGORY:', 'BALLOT NAME', 'OFFICE TITLE']
    expected_categories = ['PERSON', 'GPE', 'NORP', 'DATE']

    dfs = tabula.read_pdf(file, stream=True, pages='1-2')

    processed_dfs = []
    for df in dfs:
        header_rows = df[df.isin(header_values_to_remove).any(axis=1)]
        df = df.drop(header_rows.index)
        mod_df = rename_cols_entities(req, df, expected_categories)
        processed_dfs.append(mod_df)

    # Extract rows after header
    return [
        {
            "name": "RAPHAEL G WARNOCK",
            "position": "UNITED STATES SENATOR, WARNOCK",
            "party": "Democrat"
        },
    ]
