import os
import json
import streamlit as st

# ---------------------------------------------------------
# Streamlit secrets -> environment variable
# This lets the existing Gemini backend work both locally
# (.env) and on Streamlit Community Cloud (Secrets).
# ---------------------------------------------------------
try:
    if "GEMINI_API_KEY" in st.secrets:
        os.environ["GEMINI_API_KEY"] = st.secrets["GEMINI_API_KEY"]
except Exception:
    pass

# Existing project backend
from phase1_user_intake.extractor import extract_issue
from phase3_rti_generator.rti_generator import generate_rti


# ---------------------------------------------------------
# Page configuration
# ---------------------------------------------------------
st.set_page_config(
    page_title="RTI-Filler | AI RTI Assistant",
    page_icon="📄",
    layout="wide",
    initial_sidebar_state="expanded",
)


# ---------------------------------------------------------
# Styling
# ---------------------------------------------------------
st.markdown(
    """
    <style>
    .main {
        background-color: #f7f9fc;
    }

    .block-container {
        padding-top: 2rem;
        padding-bottom: 3rem;
        max-width: 1250px;
    }

    .hero {
        padding: 1.5rem 1.8rem;
        border-radius: 18px;
        background: linear-gradient(135deg, #0f172a, #1e3a8a);
        color: white;
        margin-bottom: 1.5rem;
    }

    .hero h1 {
        margin: 0;
        font-size: 2.2rem;
    }

    .hero p {
        margin-top: .5rem;
        color: #dbeafe;
        font-size: 1.05rem;
    }

    .step-card {
        padding: 1rem;
        border-radius: 14px;
        border: 1px solid #e5e7eb;
        background: white;
        min-height: 110px;
    }

    .step-number {
        font-size: .85rem;
        font-weight: 700;
        color: #2563eb;
    }

    .step-title {
        font-weight: 700;
        font-size: 1rem;
        margin-top: .3rem;
    }

    .step-text {
        color: #64748b;
        font-size: .88rem;
        margin-top: .25rem;
    }

    .section-title {
        font-size: 1.25rem;
        font-weight: 700;
        margin-top: 1rem;
        margin-bottom: .7rem;
    }

    .status-box {
        padding: .8rem 1rem;
        border-radius: 10px;
        background: #eff6ff;
        border: 1px solid #bfdbfe;
        color: #1e40af;
    }

    [data-testid="stSidebar"] {
        background-color: #0f172a;
    }

    [data-testid="stSidebar"] * {
        color: white;
    }
    </style>
    """,
    unsafe_allow_html=True,
)


# ---------------------------------------------------------
# Header
# ---------------------------------------------------------
st.markdown(
    """
    <div class="hero">
        <h1>📄 RTI-Filler</h1>
        <p>AI-assisted RTI drafting, department identification and complaint analysis.</p>
    </div>
    """,
    unsafe_allow_html=True,
)


# ---------------------------------------------------------
# Sidebar
# ---------------------------------------------------------
with st.sidebar:
    st.markdown("## RTI-Filler")
    st.caption("AI-powered RTI filing assistant")

    st.markdown("---")
    st.markdown("### Pipeline")
    st.markdown("🗣️ **1. User Intake**")
    st.markdown("🔎 **2. Issue Analysis**")
    st.markdown("🏛️ **3. Department Mapping**")
    st.markdown("📄 **4. RTI Generation**")
    st.markdown("🛡️ **5. Review & Filing**")

    st.markdown("---")
    st.caption("Gemini + ChromaDB + Streamlit")


# ---------------------------------------------------------
# Pipeline overview
# ---------------------------------------------------------
cols = st.columns(4)

steps = [
    ("01", "Describe Issue", "Enter your complaint in simple language."),
    ("02", "AI Analysis", "Extract issue type, location and severity."),
    ("03", "RTI Draft", "Generate a formal RTI application."),
    ("04", "Download", "Review and download the final application."),
]

for col, (num, title, desc) in zip(cols, steps):
    with col:
        st.markdown(
            f"""
            <div class="step-card">
                <div class="step-number">STEP {num}</div>
                <div class="step-title">{title}</div>
                <div class="step-text">{desc}</div>
            </div>
            """,
            unsafe_allow_html=True,
        )


st.markdown("")


# ---------------------------------------------------------
# User details
# ---------------------------------------------------------
st.markdown('<div class="section-title">👤 Applicant Details</div>', unsafe_allow_html=True)

c1, c2 = st.columns(2)

with c1:
    name = st.text_input("Full Name *", placeholder="Enter your full name")
    phone = st.text_input("Phone Number *", placeholder="Enter phone number")

with c2:
    email = st.text_input("Email *", placeholder="Enter email address")
    address = st.text_area(
        "Full Address *",
        placeholder="House/Street, Area, City, State, PIN",
        height=100,
    )


# ---------------------------------------------------------
# Complaint
# ---------------------------------------------------------
st.markdown('<div class="section-title">📝 Complaint / Issue</div>', unsafe_allow_html=True)

complaint = st.text_area(
    "Describe your issue",
    placeholder=(
        "Example: My street has had severe potholes for several months. "
        "Despite complaints, no repair work has been carried out. "
        "I want to know the current status, responsible officer and expected timeline."
    ),
    height=180,
)

st.caption("You can describe the issue in normal language. The AI will extract the relevant details.")


# ---------------------------------------------------------
# Department / PIO details
# ---------------------------------------------------------
st.markdown('<div class="section-title">🏛️ Public Authority Details</div>', unsafe_allow_html=True)

d1, d2 = st.columns(2)

with d1:
    department = st.text_input(
        "Department / Public Authority *",
        placeholder="Example: Municipal Corporation",
    )
    pio_name = st.text_input(
        "PIO Name",
        placeholder="Public Information Officer",
    )

with d2:
    department_address = st.text_area(
        "Department Address *",
        placeholder="Official department / PIO address",
        height=100,
    )


# ---------------------------------------------------------
# Generate
# ---------------------------------------------------------
st.markdown("")

generate_button = st.button(
    "🚀 Analyze Issue & Generate RTI",
    type="primary",
    use_container_width=True,
)

if generate_button:

    # Basic validation
    required = {
        "Full Name": name,
        "Phone": phone,
        "Email": email,
        "Address": address,
        "Complaint": complaint,
        "Department": department,
        "Department Address": department_address,
    }

    missing = [label for label, value in required.items() if not value.strip()]

    if missing:
        st.error("Please fill in: " + ", ".join(missing))

    else:
        try:
            # ---------------------------------------------
            # Phase 1: AI issue extraction
            # ---------------------------------------------
            with st.spinner("🔎 Analyzing your complaint..."):
                issue_data = extract_issue(complaint)

            if not issue_data:
                st.error("The issue analyzer did not return valid data.")
                st.stop()

            # Save for display
            st.session_state["issue_data"] = issue_data

            # ---------------------------------------------
            # Contact data for existing RTI generator
            # ---------------------------------------------
            contact_data = {
                "department": department,
                "pio_name": pio_name if pio_name.strip() else "Public Information Officer",
                "address": department_address,
            }

            user_details = {
                "name": name,
                "address": address,
                "phone": phone,
                "email": email,
            }

            # ---------------------------------------------
            # Phase 3: RTI generation
            # ---------------------------------------------
            with st.spinner("📄 Generating your RTI application..."):
                rti_text = generate_rti(
                    issue_data,
                    contact_data,
                    user_details,
                )

            st.session_state["rti_text"] = rti_text

            st.success("RTI application generated successfully.")

        except Exception as e:
            st.error("Something went wrong while processing the request.")
            st.exception(e)


# ---------------------------------------------------------
# Results
# ---------------------------------------------------------
if "issue_data" in st.session_state:

    st.markdown("---")
    st.markdown('<div class="section-title">🔎 AI Issue Analysis</div>', unsafe_allow_html=True)

    issue_data = st.session_state["issue_data"]

    # Display JSON cleanly
    try:
        analysis_cols = st.columns(3)

        issue_type = issue_data.get("issue_type", "Not detected")
        location = issue_data.get("location", "Not detected")
        severity = issue_data.get("severity", "Not detected")
        confidence = issue_data.get("confidence", "N/A")

        with analysis_cols[0]:
            st.metric("Issue Type", str(issue_type))

        with analysis_cols[1]:
            st.metric("Location", str(location))

        with analysis_cols[2]:
            st.metric("Severity", str(severity))

        st.caption(f"AI confidence: {confidence}")

        with st.expander("View complete extracted data"):
            st.json(issue_data)

    except Exception:
        st.json(issue_data)


# ---------------------------------------------------------
# RTI output
# ---------------------------------------------------------
if "rti_text" in st.session_state:

    st.markdown("---")
    st.markdown('<div class="section-title">📄 Generated RTI Application</div>', unsafe_allow_html=True)

    rti_text = st.session_state["rti_text"]

    st.text_area(
        "Review before filing",
        value=rti_text,
        height=650,
        label_visibility="collapsed",
    )

    st.download_button(
        label="⬇️ Download RTI as TXT",
        data=rti_text,
        file_name="RTI_Application.txt",
        mime="text/plain",
        use_container_width=True,
    )

    st.info(
        "Review the generated application and verify the PIO details, "
        "department address and factual information before filing."
    )


# ---------------------------------------------------------
# Footer
# ---------------------------------------------------------
st.markdown("---")
st.caption("RTI-Filler • AI-assisted drafting system • Verify official details before submission.")
