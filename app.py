import email
from os import name

from phase1_user_intake.language import detect_language
from phase1_user_intake.extractor import extract_issue
from phase3_rti_generator.rti_generator import generate_rti
from phase2_department_mapper.contact_finder import get_contact
import json
from phase4_review_risk.risk_checker import analyze_rti
from phase5_filing.filing_manager import file_rti

def main():
    text = input("Enter complaint: ")

    lang = detect_language(text)
    extracted = extract_issue(text)

    extracted_json = json.loads(extracted)

    name = input("Enter your full name: ")
    address = input("Enter your address: ")
    phone = input("Enter your phone number: ")
    email = input("Enter your email address: ")

    contact = get_contact(extracted_json["issue_type"])
    
    user_details = {
    "name": name,
    "address": address,
    "phone": phone,
    "email": email
    }

    rti = generate_rti(
        extracted_json,
        contact,
        user_details
    )
    combined_text = text + "\n" + rti
    risk_report = analyze_rti(combined_text)
    if risk_report["status"] != "Risky":

        mode = input("\nChoose filing mode (email/speedpost/manual): ")

        filing_result = file_rti(
            mode,
            rti,
            contact
        )
        print("\nPhase 5 Output:", filing_result)
    else:
        print("\nRTI is risky. Fix before filing.")

    print("\nDetected Language:", lang)
    print("\nPhase 1 Output:", extracted_json)
    print("\nPhase 2 Output:", contact)
    print("\nPhase 3 Output:", rti)
    print("\nRisk Analysis:", risk_report)
    

if __name__ == "__main__":
    main()