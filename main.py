import pandas as pd
import glob
from fpdf import FPDF
from pathlib import Path


filepaths = glob.glob("invoices/*.xlsx")

for filepath in filepaths:
    df = pd.read_excel(filepath, sheet_name="Sheet 1")
    pdf = FPDF(orientation="P", unit="mm", format="A4")
    pdf.add_page()
    filename = Path(filepath).stem
    invoice_nr,date = filename.split("-")

    pdf.set_font(family="Times", size=16, style="B")
    pdf.cell(w=50, h=8, txt=f"Invoice nr.{invoice_nr}",ln=1 )

    pdf.set_font(family="Times", size=16, style="B")
    pdf.cell(w=50, h=8, txt=f"Date:{date}", ln=1)

    df = pd.read_excel(filepath, sheet_name="Sheet 1")
    # Add a header
    columns_aa=list(df.columns)
    columns_a=[items.replace("_"," ").title() for items in columns_aa]
    pdf.set_font(family="Times", size=10, style="B")
    pdf.set_text_color(80, 80, 80)
    pdf.cell(w=30, h=8, txt=columns_a[0], border=1)
    pdf.cell(w=30, h=8, txt=columns_a[1], border=1)
    pdf.cell(w=30, h=8, txt=columns_a[2], border=1)
    pdf.cell(w=30, h=8, txt=columns_a[3], border=1)
    pdf.cell(w=30, h=8, txt=columns_a[4], border=1,ln=1)
    # A dd rows
    for index, row in df.iterrows():
        pdf.set_font(family="Times", size=10)
        pdf.set_text_color(80,80,80)
        pdf.cell(w=30, h=8, txt=str(row["product_id"]),border=1)
        pdf.cell(w=30, h=8, txt=str(row["product_name"]),border=1)
        pdf.cell(w=30, h=8, txt=str(row["amount_purchased"]),border=1)
        pdf.cell(w=30, h=8, txt=str(row["price_per_unit"]),border=1)
        pdf.cell(w=30, h=8, txt=str(row["total_price"]),border=1, ln=1)

    pdf.output("PDFs/{filename}.pdf")

