student_data = {
    "id": 101,
    "name": "Riya Sharma",
    "age": 20,
    "gender": "Female",
    "course": "B.Tech",
    "branch": "Computer Science",
    "year": 2,
    "subjects": {
        "math": 95,
        "physics": 88,
        "chemistry": 91,
        "programming": 97,
        "english": 85
    },
    "attendance": {
        "math": 90,
        "physics": 85,
        "chemistry": 88,
        "programming": 92,
        "english": 80
    },
    "address": {
        "house_no": "12A",
        "street": "Civil Lines",
        "city": "Prayagraj",
        "state": "Uttar Pradesh",
        "pincode": 211001
    },
    "contact": {
        "phone": "9876543210",
        "email": "riya.sharma@example.com"
    },
    "skills": ["Python", "C", "Data Structures", "Web Development"],
    "hobbies": ["Reading", "Music", "Traveling"],
    "is_active": True
}

print(student_data)
print("Name:", student_data["name"])
print("City:", student_data["address"]["city"])
print("Programming Marks:", student_data["subjects"]["programming"])
print("Skills:", student_data["skills"])