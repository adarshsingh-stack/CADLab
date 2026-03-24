company_data = {
    "company_name": "Tech Solutions",
    "head_office": ("Delhi", "India"),
    "departments": {
        "IT": {
            "employees": (
                {"name": "Ravi", "age": 25},
                {"name": "Neha", "age": 27}
            ),
            "projects": ("App Dev", "AI Model")
        },
        "HR": {
            "employees": (
                {"name": "Suman", "age": 30},
                {"name": "Kiran", "age": 28}
            ),
            "tasks": ("Recruitment", "Payroll")
        }
    }
}

print("Company:", company_data)
print("Departments:", company_data["departments"])

for dept, details in company_data["departments"].items():
    print("Department:", dept)
    for emp in details["employees"]:
        print(emp["name"], emp["age"])
    for key, value in details.items():
        print(key, value)