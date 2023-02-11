from fpdf import FPDF

user = input("Name: ")
pdf = FPDF()
pdf.add_page()

pdf.set_font("helvetica", style = "B", size=40)
pdf.cell(0, 60, "CS0 Shirtificate", align = "C")
pdf.image("shirtificate.png", x= 0, y=70)
pdf.set_font_size(30)
pdf.set_text_color(255,255,255)
pdf.text(x=45, y=150, txt=f"{user} took CS50")
pdf.output("shirtificate.pdf")