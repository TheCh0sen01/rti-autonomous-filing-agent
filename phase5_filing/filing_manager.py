from phase5_filing.pdf_generator import generate_pdf
from phase5_filing.email_sender import send_email
from phase5_filing.portal_filer import file_portal
from phase5_filing.speed_post_handler import prepare_speed_post

def file_rti(mode, rti_text, contact):

    if mode == "email":
        pdf_path = generate_pdf(rti_text, "rti_email.pdf")
        return send_email(contact["email"], pdf_path)

    elif mode == "portal":
        return file_portal(rti_text)

    elif mode == "speedpost":
        pdf_path = generate_pdf(rti_text, "rti_speedpost.pdf")
        return prepare_speed_post(rti_text, contact)

    elif mode == "manual":
        pdf_path = generate_pdf(rti_text, "rti_manual.pdf")
        return {
            "status": "pdf_generated",
            "path": pdf_path
        }

    return {"status": "invalid_mode"}