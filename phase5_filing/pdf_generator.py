from reportlab.platypus import SimpleDocTemplate, Paragraph
from reportlab.lib.styles import getSampleStyleSheet
import os

def generate_pdf(rti_text, filename):

    BASE_DIR = os.path.dirname(os.path.abspath(__file__))
    output_dir = os.path.join(BASE_DIR, "generated_docs")

    os.makedirs(output_dir, exist_ok=True)

    filename = os.path.join(output_dir, "rti_email.pdf")

    doc = SimpleDocTemplate(filename)
    styles = getSampleStyleSheet()

    content = []

    for line in rti_text.split("\n"):
        content.append(Paragraph(line, styles["BodyText"]))

    doc.build(content)

    return filename