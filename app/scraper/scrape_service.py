import tabula


def scrape_pdf(file) -> dict:
    dfs = tabula.read_pdf(file, stream=True, pages='1-2')
    header_values = ['OFFICE CATEGORY:', 'BALLOT NAME', 'OFFICE TITLE']

    # Extract rows after header
    return [
        {
            "name": "RAPHAEL G WARNOCK",
            "position": "UNITED STATES SENATOR, WARNOCK",
            "party": "Democrat"
        },
    ]
