from typing import Any, Union
import pdfplumber
from pdfplumber.pdf import PDF
import logging

def pdf_to_string(path: Union[str, Any]) -> str:
    """
    Converts the PDF file content to text and returns the raw content of the lab report file.

    Args:
        path (Union[str, Any]): The path to the PDF file or a file-like object.

    Returns:
        str: The extracted text from the PDF.

    Raises:
        ValueError: If the PDF file is empty or cannot be read.
    """
    try:
        with pdfplumber.open(path) as pdf_object:
            if len(pdf_object.pages) == 0:
                raise ValueError("The PDF file is empty.")
            
            text = []
            for page in pdf_object.pages:
                page_text = page.extract_text(
                    layout=False,
                    y_tolerance=4.8,
                    x_tolerance=20,
                    y_density=20,
                    x_density=20
                )
                if page_text:
                    text.append(page_text)
            
            return "\n".join(text)
    except Exception as e:
        logging.error(f"Error processing PDF: {str(e)}")
        raise ValueError(f"Unable to read PDF file: {str(e)}")
