from phase5_filing.pdf_generator import generate_pdf
from phase5_filing.cover_letter_generator import generate_cover_letter
from phase5_filing.envelope_generator import generate_envelope
from phase5_filing.tracking_manager import save_tracking

def prepare_speed_post(rti_text, contact):

    rti_pdf = generate_pdf(rti_text, "rti_speedpost.pdf")
    cover_letter = generate_cover_letter(contact)
    envelope = generate_envelope(contact)

    print("\nPrint these and attach ₹10 IPO.")
    tracking_id = input("Enter Speed Post Tracking ID after dispatch: ")

    tracking_info = save_tracking(tracking_id)

    return {
        "status": "ready_for_tracking",
        "rti_pdf": rti_pdf,
        "cover_letter": cover_letter,
        "envelope_label": envelope,
        "tracking_info": tracking_info
    }