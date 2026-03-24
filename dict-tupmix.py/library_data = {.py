library_data = {
    "library_name": "Central Library",
    "location": ("Prayagraj", "UP"),
    "books": {
        "book1": ("Python Basics", "John Doe", 2020),
        "book2": ("Data Structures", "Jane Smith", 2019),
        "book3": ("AI Introduction", "Alan Turing", 2021)
    },
    "members": {
        "member1": {
            "name": "Riya",
            "issued_books": ("Python Basics", "AI Introduction")
        },
        "member2": {
            "name": "Aman",
            "issued_books": ("Data Structures",)
        }
    }
}

print("Library:", library_data)
print("Books:", library_data["books"])
print("Member1 Books:", library_data["members"]["member1"]["issued_books"])

for book, details in library_data["books"].items():
    print(book, details)

for member, info in library_data["members"].items():
    print(member, info["name"], info["issued_books"])