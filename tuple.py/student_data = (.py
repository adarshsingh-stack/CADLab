student_data = (
    ("Riya", 20, "BCA", (85, 90, 88)),
    ("Aman", 21, "BBA", (78, 82, 80)),
    ("Neha", 19, "BSc", (92, 89, 95)),
    ("Rahul", 22, "BTech", (75, 70, 72))
)

print("Student Records:")
for student in student_data:
    name = student[0]
    age = student[1]
    course = student[2]
    marks = student[3]
    
    total = sum(marks)
    average = total / len(marks)
    
    print("Name:", name)
    print("Age:", age)
    print("Course:", course)
    print("Marks:", marks)
    print("Total:", total)
    print("Average:", average)
    print("----------------------")

numbers = (10, 20, 30, 40, 50, 60, 70, 80)

print("Numbers Tuple:", numbers)
print("Length:", len(numbers))
print("Max:", max(numbers))
print("Min:", min(numbers))
print("Sum:", sum(numbers))

even_numbers = tuple(x for x in numbers if x % 2 == 0)
print("Even Numbers:", even_numbers)

combined = student_data + (("Kiran", 23, "MBA", (88, 91, 87)),)
print("Updated Records:", combined)