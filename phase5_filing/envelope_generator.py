from reportlab.platypus import SimpleDocTemplate, Paragraph
from reportlab.lib.styles import getSampleStyleSheet

def generate_envelope(contact, filename="envelope_label.pdf"):

    filepath = f"phase5_filing/generated_docs/{filename}"

    content = f"""
To,
Public Information Officer
{contact['pio_name']}
{contact['department']}
{contact['address']}
"""

    doc = SimpleDocTemplate(filepath)
    styles = getSampleStyleSheet()

    elements = []

    for line in content.split("\n"):
        elements.append(Paragraph(line, styles["BodyText"]))

    doc.build(elements)

    return filepath