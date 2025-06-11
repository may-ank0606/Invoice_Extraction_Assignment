import fitz  # PyMuPDF
import os
import pandas as pd

# Folders
input_folder = "./Input"
output_folder = "./Output"
output_excel = os.path.join(output_folder, "extracted_invoice_data.xlsx")

data = []

def extract_text_from_pdf(pdf_path):
    text = ""
    with fitz.open(pdf_path) as doc:
        for page in doc:
            text += page.get_text()
    return text

def parse_invoice(text, platform):
    invoice_no = "Not Found"
    date = "Not Found"
    buyer_name = "Mayank Arya"
    seller = "Not Found"
    item = "Not Found"
    quantity = 1
    price = 0
    gst = 0
    total = 0

    lines = text.split('\n')
    for line in lines:
        line = line.strip()
        if "Invoice Number" in line:
            invoice_no = line.split(":")[-1].strip()
        elif "Date" in line and date == "Not Found":
            date = line.split(":")[-1].strip()
        elif "Sold by" in line or "Seller" in line:
            seller = line.split(":")[-1].strip()
        elif "Item" in line:
            item = line.split(":")[-1].strip()
        elif "Price" in line:
            try:
                price = float(line.split(":")[-1].replace("₹", "").replace(",", "").strip())
            except:
                pass
        elif "GST" in line:
            try:
                gst = float(line.split(":")[-1].replace("₹", "").replace(",", "").strip())
            except:
                pass
        elif "Total" in line:
            try:
                total = float(line.split(":")[-1].replace("₹", "").replace(",", "").strip())
            except:
                pass

    return {
        "Invoice No": invoice_no,
        "Date": date,
        "Platform": platform,
        "Buyer Name": buyer_name,
        "Seller Name": seller,
        "Item Name": item,
        "Quantity": quantity,
        "Price (₹)": price,
        "GST (₹)": gst,
        "Total Amount (₹)": total
    }

# Main logic
for filename in os.listdir(input_folder):
    if filename.endswith(".pdf"):
        platform = "Amazon" if "amazon" in filename.lower() else "Flipkart"
        file_path = os.path.join(input_folder, filename)
        text = extract_text_from_pdf(file_path)
        parsed = parse_invoice(text, platform)
        data.append(parsed)

# Export to Excel
df = pd.DataFrame(data)
df.to_excel(output_excel, index=False)

print(f"\n✅ Extraction Completed. File saved at: {output_excel}")
