from reportlab.platypus import SimpleDocTemplate, Paragraph
from reportlab.lib.styles import getSampleStyleSheet

def generate_cover_letter(contact, filename="cover_letter.pdf"):

    filepath = f"phase5_filing/generated_docs/{filename}"

    content = f"""
To,
Public Information Officer
{contact['pio_name']}
{contact['department']}
{contact['address']}

Subject: Submission of RTI Application

Sir/Madam,

Please find enclosed my RTI application under the RTI Act 2005 along with the required ₹10 IPO.

Enclosures:
1. RTI Application
2. IPO
3. Supporting Documents (if any)

Regards
Applicant
"""

    doc = SimpleDocTemplate(filepath)
    styles = getSampleStyleSheet()

    elements = []

    for line in content.split("\n"):
        elements.append(Paragraph(line, styles["BodyText"]))

    doc.build(elements)

    return filepath