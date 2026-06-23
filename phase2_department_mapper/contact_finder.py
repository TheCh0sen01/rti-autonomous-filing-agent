from phase2_department_mapper.mapper import map_department
def get_contact(issue_type):
    result = map_department(issue_type)

    return {
        "department": result["department"],
        "pio_name": result["pio_name"],
        "email": result["email"],
        "address": result["address"]
    }