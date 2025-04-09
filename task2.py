import pandas as pd
from fpdf import FPDF

file_path = "C:/Users/uzama/Desktop/intern/task2.py/data.csv"
data = pd.read_csv(file_path)

print(data.head())
total_entries = len(data)
print("Total entries:", total_entries)
pdf = FPDF()
pdf.add_page()
pdf.set_font("Arial", size=12)

# Add a title
pdf.cell(200, 10, txt="Data Analysis Report", ln=True, align="C")

# Add data details
pdf.cell(200, 10, txt=f"Total Entries: {total_entries}", ln=True)

# Save the PDF
pdf.output("report.pdf")
from fpdf import FPDF

# Create a PDF instance
pdf = FPDF()
pdf.add_page()
pdf.set_font("Arial", size=12)

# Add Title
pdf.set_font("Arial", style="B", size=16)
pdf.cell(200, 10, txt="Data Analysis Report", ln=True, align='C')

# Add Total Entries
pdf.set_font("Arial", size=12)
pdf.cell(0, 10, f"Total Entries: {len(data)}", ln=True)

# Add Table Headers
pdf.cell(50, 10, "Name", border=1)
pdf.cell(30, 10, "Age", border=1)
pdf.cell(50, 10, "Department", border=1, ln=True)

# Add Table Data
for index, row in data.iterrows():
    pdf.cell(50, 10, row['Name'], border=1)
    pdf.cell(30, 10, str(row['Age']), border=1)
    pdf.cell(50, 10, row['Department'], border=1, ln=True)

pdf.output(r"C:\Users\uzama\Desktop\intern\task2.py\report.pdf")
print("PDF Report Generated: report.pdf")

