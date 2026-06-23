from filing_manager import file_rti

sample_rti = """
This is a sample RTI application for testing email filing.
"""

contact = {
    "email": "fernandoaaron0123@gmail.com"
}

result = file_rti(
    mode="email",
    rti_text=sample_rti,
    contact=contact
)

print(result)