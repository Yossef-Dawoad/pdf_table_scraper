import os

from fastapi import APIRouter, HTTPException, Request, UploadFile, status

from app.limit_config import limiter

from .schemas import ScrapedData
from .scrape_service import scrape_pdf

# SETTING UPLOAD DIR
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
UPLOAD_DIR = os.path.join(BASE_DIR, "uploads")
# Create the upload directory if it doesn't exist
if not os.path.exists(UPLOAD_DIR):
    os.makedirs(UPLOAD_DIR)

router = APIRouter(
    prefix="/api/v1",
    tags=["pdf scraper endpoints"],
)


@router.post("/scraper", response_model=list[ScrapedData])
@limiter.limit("30/minute")
async def receive_file(request: Request, file: UploadFile) -> list[ScrapedData]:
    """
    Process a PDF file upload and return filtered scraped data contailn {names, party, }
    """

    if file.content_type != "application/pdf":
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Invalid document type Uploaded file must be a pdf type",
        )

    scraped_data = scrape_pdf(request, file.file)

    return scraped_data
