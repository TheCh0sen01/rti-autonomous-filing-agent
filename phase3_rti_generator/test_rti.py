from rti_generator import generate_rti

issue_data = {
    "issue_type": "Pothole on Public Road"
}

contact_data = {
    "department": "Municipal Corporation",
    "pio_name": "City Engineer"
}

result = generate_rti(issue_data, contact_data)

print(result)