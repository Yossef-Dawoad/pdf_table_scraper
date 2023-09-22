# pdf table scraper

a pdf scraper service that extracts tables from PDF documents and converts them to CSV format
## Features
- extract tabuler data for any pdf 
- rate limit for safe usage
- dockerized application for instatnt run and deploy
- logger system to stout
- tests for every endpoint 

## Install

### Docker Run

```bash
docker-composer up -d
```

### without docker

you must have java installed on your system
sence tabula-py is a wrapper around the Java Implementation,  
this guide could help if you needed [here](https://devwithus.com/install-java-windows-10/) for installing 

```
pip install -r requirements.prod.txt

uvicorn app.main:app --reload
```

## Usage

head to `localhost:8000/` to see the docs & upload a PDF file

`api end-point` :  
---
`POST` ->  `api/v1/scraper` : Expect Pdf file Upload return processed data


## Todo
 - [ ] upload pdfs to firestore
 - [ ] scraper as background task 
 - [ ] maybe send an email with processed file
 - [ ] more rebust scarper with NER nlp
 - [ ]  github automated test on push for CI/CD
  
