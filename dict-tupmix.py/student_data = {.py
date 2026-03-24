student_data = {
    "id": 101,
    "name": "Riya",
    "age": 20,
    "marks": (88, 92, 79, 85),
    "subjects": ("Math", "Physics", "Chemistry", "English"),
    "address": {
        "city": "Prayagraj",
        "state": "UP",
        "pincode": 211001
    },
    "performance": {
        "semester1": (85, 90, 88),
        "semester2": (87, 91, 84)
    }
}

employee_data = {
    "emp_id": 501,
    "emp_name": "Aman",
    "department": "IT",
    "salary": 50000,
    "skills": ("Python", "Java", "SQL"),
    "projects": {
        "project1": ("AI System", "Completed"),
        "project2": ("Web App", "Ongoing")
    },
    "attendance": {
        "jan": (22, 2),
        "feb": (20, 3)
    }
}

mixed_data = {
    "students": (student_data,),
    "employees": (employee_data,),
    "college": "ABC University",
    "location": ("Prayagraj", "India"),
    "details": {
        "founded": 1995,
        "courses": ("BTech", "BSc", "MCA"),
        "rating": 4.5
    }
}

print("Student Data:", student_data)
print("Employee Data:", employee_data)
print("Mixed Data:", mixed_data)

print("Student Marks:", student_data["marks"])
print("Employee Skills:", employee_data["skills"])
print("College Courses:", mixed_data["details"]["courses"])

total_marks = sum(student_data["marks"])
average_marks = total_marks / len(student_data["marks"])
print("Total Marks:", total_marks)
print("Average Marks:", average_marks)

for subject, mark in zip(student_data["subjects"], student_data["marks"]):
    print(subject, mark)

for skill in employee_data["skills"]:
    print("Skill:", skill)

for key, value in mixed_data.items():
    print(key, value)