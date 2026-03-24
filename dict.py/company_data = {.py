company_data = {
    "company_name": "TechNova Pvt Ltd",
    "founded": 2015,
    "head_office": {
        "city": "Bangalore",
        "state": "Karnataka",
        "country": "India"
    },
    "departments": {
        "development": {
            "employees": 120,
            "technologies": ["Python", "Java", "React", "Node.js"]
        },
        "marketing": {
            "employees": 40,
            "channels": ["SEO", "Social Media", "Email Marketing"]
        },
        "hr": {
            "employees": 15
        },
        "finance": {
            "employees": 20
        }
    },
    "projects": [
        {
            "name": "AI Chatbot",
            "status": "Completed",
            "team_size": 10
        },
        {
            "name": "E-commerce Platform",
            "status": "Ongoing",
            "team_size": 15
        },
        {
            "name": "Cloud Migration",
            "status": "Planned",
            "team_size": 8
        }
    ],
    "clients": ["Amazon", "Flipkart", "Infosys", "TCS"],
    "revenue": {
        "2022": 5000000,
        "2023": 7500000,
        "2024": 10000000
    },
    "is_profitable": True
}

print(company_data)
print("Company:", company_data["company_name"])
print("Head Office City:", company_data["head_office"]["city"])
print("Development Employees:", company_data["departments"]["development"]["employees"])
print("First Project:", company_data["projects"][0]["name"])
print("Revenue 2024:", company_data["revenue"]["2024"])