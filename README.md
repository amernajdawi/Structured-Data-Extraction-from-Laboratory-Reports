# Structured Data Extraction from Laboratory Reports

## Description

This project automates the extraction of structured data from laboratory reports using advanced natural language processing techniques. It provides a streamlined solution for parsing and organizing critical information from medical lab documents.

## Features

- Automated extraction of key data points from lab reports
- Conversion of unstructured text to structured, machine-readable formats
- User-friendly Streamlit interface for uploading and processing reports
- Integration with OpenAI's GPT models for intelligent data extraction
- Containerized development environment using devcontainers

## Prerequisites

- Docker
- Visual Studio Code with Remote - Containers extension
- Git

## Getting Started with Devcontainer

1. Clone the repository:
   ```
   git clone https://github.com/amernajdawi/Structured-Data-Extraction-from-Laboratory-Reports.git
   ```

2. Open the project in Visual Studio Code.

3. When prompted, click "Reopen in Container" or use the command palette (F1) and select "Remote-Containers: Reopen in Container".

4. VS Code will build the devcontainer and set up the environment. This may take a few minutes the first time.

5. Once inside the devcontainer, open a new terminal in VS Code.

6. Install dependencies using Poetry:
   ```
   poetry install
   ```

7. Run the Streamlit app:
   ```
   poetry run streamlit run src/insights/app.py
   ```

## Usage

1. With the Streamlit app running, open a web browser and navigate to the URL displayed in the terminal (usually `http://localhost:8501`).
2. Use the file uploader to select a PDF lab report.
3. The application will process the PDF and display extracted information, including:
   - Auftragsdatum (Order Date)
   - Befunddatum (Report Date)
   - Auftragsnummer (Order Number)
   - Date of Birth
   - Gender
   - A table of extracted lab results with entity type, value, unit, and reference ranges

## Environment Variables

The project uses the following environment variables:
- `OPENAI_API_KEY`: Your OpenAI API key
- `OPENAI_MODEL`: The OpenAI model to use (default is "gpt-4o-mini")

These should be set in the `.env` file in the project root.

## Project Structure

- `src/insights/`: Main application code
  - `app_2.py`: Streamlit application entry point
  - `lab_report_LLM_extractor/`: Contains extraction logic
  - `utility/`: Utility functions for PDF processing and text preprocessing
- `.devcontainer/`: Devcontainer configuration files
- `pyproject.toml`: Poetry project configuration

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## Contact

Amer Najdawi - amernajdawi8@gmail.com

Project Link: [https://github.com/amernajdawi/Structured-Data-Extraction-from-Laboratory-Reports](https://github.com/amernajdawi/Structured-Data-Extraction-from-Laboratory-Reports)