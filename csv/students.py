import csv

students = []

with open("csv/students.csv") as file:
    reader = csv.DictReader(file)
    for row in reader:
        print(row["name"], row["home"], row["house"])

for student in sorted(students, key=lambda student: student["name"]):
    print(f"{student['name']} is from {student['home']} and belongs to {student['house']}")
