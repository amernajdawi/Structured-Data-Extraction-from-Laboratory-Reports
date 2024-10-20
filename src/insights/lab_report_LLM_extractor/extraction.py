from typing import List, Optional
import os
from dotenv import load_dotenv

from openai import OpenAI
from pydantic import BaseModel, Field


class RangeValue(BaseModel):
    upper_limit: float
    lower_limit: float


class Entity(BaseModel):
    entity_type: str
    value: float
    unit: str
    range: RangeValue


class LabReportExtraction(BaseModel):
    Auftragsdatum: str
    Befunddatum: str
    Auftragsnummer: str
    entities: List[Entity]
    gender: str
    dateofbirth: str


# Load environment variables
load_dotenv()

def extract_lab_results(report_text: str) -> List[LabReportExtraction]:
    # Get API key from environment variable
    api_key = os.getenv("OPENAI_API_KEY")
    model = os.getenv("OPENAI_MODEL", "gpt-4o-mini")  # Use default if not set

    client = OpenAI(api_key=api_key)

    try:
        completion = client.beta.chat.completions.parse(
            model=model,
            messages=[
                {
                    "role": "system",
                    "content": """Act like a medical consultant, who can extract information from lab report and then responds to the user using JSON.
                    Please provide all Lab Results information in the text in a JSON format.
                    The JSON should contain the following fields: Type, Value, Unit, Range {"lowerBound":" ","upperBound":" "}, indicator.
                    Type "None" if the information is missing. No additional information should be provided, only answer as the assistant.""",
                },
                {
                    "role": "user",
                    "content": f"Please extract the lab results from the following report:\n\n{report_text}",
                },
            ],
            response_format=LabReportExtraction,
        )
        return completion.choices[0].message

    except Exception as e:
        print(f"An error occurred: {e}")
        return []
