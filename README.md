# pdf table scraper

a pdf scraper service that extracts tables from PDF documents and converts them to CSV format

# Install

### Docker Run

```bash
docker-composer up -d
```

### without docker

you must have java installed on your system
and set the path in JAVA_HOME environment variable

```
pip install -r requirements.prod.txt

uvicorn app.main:app --reload
```

# Usage

head to `localhost:8000/` to see the docs & upload a PDF file
