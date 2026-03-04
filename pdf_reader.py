from pypdf import PdfReader
from logger import setup_logger

logger = setup_logger()


def extract_text_from_pdf(file):

    logger.info("Starting PDF text extraction")

    reader = PdfReader(file)

    text = ""

    for page_number, page in enumerate(reader.pages):

        page_text = page.extract_text()

        if page_text:
            text += page_text

        logger.info(f"Processed page {page_number + 1}")

    logger.info("PDF extraction completed")

    return text