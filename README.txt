
# 🧾 Invoice Data Extraction

**Submitted by:** Mayank Arya

---

## 📂 Folder Structure

```
Invoice-Data-Extraction/
├── Input/        # Contains 4 sample invoice PDFs (2 Amazon, 2 Flipkart)
├── Output/       # Contains the extracted Excel file with structured data
└── Coding/       # Contains the Python script used for extraction
```

---

## ⚙️ Instructions

1. 📥 **Add PDFs**
   Place the invoice PDFs inside the `Input/` folder.

2. 🖥️ **Run the Script**
   Execute `invoice_extraction.py` located in the `Coding/` folder.

3. 📊 **Get the Output**
   The structured Excel file will be generated in the `Output/` folder.

---

## 🧰 Libraries Used

* `pandas` – for data handling and Excel export
* `pymupdf (fitz)` – for PDF parsing
* `openpyxl` – for writing Excel files

*Install them using:*

```bash
pip install pandas pymupdf openpyxl
```

---

## 💼 Professional Notes

* ✅ All data is **programmatically extracted** from PDF invoices — no manual intervention.
* 🧾 Each invoice includes buyer name as **"Mayank Arya"** for reference.
* 🧱 The code is modular, clean, and **ready to scale** to multiple or dynamic file inputs.
* 📁 Folder structure ensures clarity and easy reproducibility.

---

## 🙏 Thank You!

For any suggestions or collaboration ideas, feel free to connect.
Happy Automating! 🚀

