# Invoice Data Extraction

**Author:** Mayank Arya

## Overview

This project provides an automated solution for extracting structured data from PDF invoices and converting it into Excel format. The system currently supports Amazon and Flipkart invoice formats and can be easily extended to handle additional invoice types.

## Project Structure

```
Invoice-Data-Extraction/
├── Input/        # Sample invoice PDFs (2 Amazon, 2 Flipkart)
├── Output/       # Generated Excel files with extracted data
└── Coding/       # Python extraction script
```

## Getting Started

### Prerequisites

Install the required Python packages:

```bash
pip install pandas pymupdf openpyxl
```

### Usage

1. **Input Preparation**
   - Place your invoice PDF files in the `Input/` directory

2. **Execution**
   - Run the extraction script:
     ```bash
     python Coding/invoice_extraction.py
     ```

3. **Output**
   - The structured data will be saved as an Excel file in the `Output/` directory

## Technical Details

### Dependencies

- **pandas**: Data manipulation and Excel file generation
- **pymupdf (fitz)**: PDF text extraction and parsing
- **openpyxl**: Excel file writing capabilities

### Key Features

- **Automated Processing**: Fully programmatic extraction with no manual intervention required
- **Modular Design**: Clean, scalable code architecture suitable for extension
- **Multi-Vendor Support**: Currently handles Amazon and Flipkart invoice formats
- **Structured Output**: Exports data in organized Excel format for easy analysis

## Sample Data

The project includes sample invoices with buyer information listed as "Mayank Arya" for demonstration purposes.

## Contributing

This project is designed with extensibility in mind. The modular structure allows for easy addition of new invoice formats and processing rules.

## Contact

For questions, suggestions, or collaboration opportunities, please feel free to reach out.
