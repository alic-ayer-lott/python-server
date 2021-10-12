EMPLOYEES = [
    {
        "id": 1,
        "name": "Alicia",
    },
    {
        "id": 2,
        "name": "Dylan",
    },
    {
        "id": 3,
        "name": "Henry",
    }
]

def get_all_employees():
    return EMPLOYEES

def get_single_employee(id):
    requested_employee = None

    for employee in EMPLOYEES:
        if employee["id"] == id:
            requested_employee = employee
    
    return requested_employee
