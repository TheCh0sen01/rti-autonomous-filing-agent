import streamlit as st

from phase1_user_intake.extractor import extract_issue
from phase2_department_mapper.contact_finder import get_contact
from phase3_rti_generator.rti_generator import generate_rti
from phase4_review_risk.risk_checker import analyze_rti
from phase5_filing.filing_manager import file_rti


st.title("RTI Filing Assistant")

# Complaint Input
complaint = st.text_area("Enter your complaint")

# User Details
st.subheader("Applicant Details")

name = st.text_input("Full Name")
address = st.text_area("Address")
phone = st.text_input("Phone Number")
email = st.text_input("Email Address")

if st.button("Generate RTI"):

    extracted_json = extract_issue(complaint)
    st.write("Extracted Output:", extracted_json)
    st.write("Type:", type(extracted_json))
    issue = extracted_json.get("issue_type", complaint)
    contact = get_contact(issue)

    user_details = {
        "name": name,
        "address": address,
        "phone": phone,
        "email": email
    }

    rti = generate_rti(extracted_json, contact)

    # Replace placeholders
    rti = rti.replace("[Your Full Name]", name)
    rti = rti.replace("[Your Address]", address)
    rti = rti.replace("[Your Phone Number]", phone)
    rti = rti.replace("[Your Email Address]", email)

    st.session_state["rti"] = rti
    st.session_state["contact"] = contact
    
if "rti" in st.session_state:

    st.subheader("Edit RTI")

    edited_rti = st.text_area(
        "Modify if needed",
        st.session_state["rti"],
        height=500
    )

    st.session_state["edited_rti"] = edited_rti
    
    
if "edited_rti" in st.session_state:

    st.subheader("Ask AI to Modify")

    change_request = st.text_input(
        "Example: Make it more formal"
    )

    if st.button("Apply Changes"):

        modified_rti = st.session_state["edited_rti"] + \
                       f"\n\n[Requested Change: {change_request}]"

        st.session_state["edited_rti"] = modified_rti
        
if "edited_rti" in st.session_state:

    risk_report = analyze_rti(
        complaint + "\n" + st.session_state["edited_rti"]
    )

    st.subheader("Risk Analysis")
    st.json(risk_report)
    
if "edited_rti" in st.session_state:

    mode = st.selectbox(
        "Choose filing mode",
        ["email", "speedpost", "manual"]
    )

    if st.button("File RTI"):

        filing_result = file_rti(
            mode,
            st.session_state["edited_rti"],
            st.session_state["contact"]
        )

        st.subheader("Filing Result")
        st.json(filing_result)