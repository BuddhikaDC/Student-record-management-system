# Create the file manually or via code first
with open("country.txt", "w") as f:
    f.write("Sri Lanka\nIndia\nJapan\nAustralia")

# Reading the file
try:
    with open("country.txt", "r") as file:
        content = file.read()
        print("File Content:\n" + content)
        
        # Extension: Count lines
        file.seek(0) # Move pointer back to start
        line_count = len(file.readlines())
        print(f"\nNumber of lines: {line_count}")
except FileNotFoundError:
    print("File not found.")

# Write 3 names
with open("students.txt", "w") as file:
    file.write("Alice\nBob\nCharlie\n")

# Append 2 names
with open("students.txt", "a") as file:
    file.write("David\nEve\n")

# Read and display
with open("students.txt", "r") as file:
    print(file.read())

# Setup
with open("data.txt", "w") as f:
    f.write("Python is an amazing language.\nIt is widely used in AI.")

with open("data.txt", "r") as file:
    print(f"First 20 chars: {file.read(20)}")
    print(f"Current pointer: {file.tell()}")
    
    file.seek(0)
    print(f"First line: {file.readline().strip()}")
    
    print(f"Remaining lines as list: {file.readlines()}")

class Book:
    def __init__(self, title, author, price):
        self.title = title
        self.author = author
        self.price = price

    def display_details(self):
        print("Title: {self.title}, Author: {self.author}, Price: ${self.price}")

book1 = Book("Python Basics", "John Doe", 25)
book2 = Book("AI Mastery", "Jane Smith", 45)

book1.display_details()
book2.display_details()

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    
    def display(self):
        print(f"Name: {self.name}, Age: {self.age}")

class Student(Person):
    def __init__(self, name, age, student_id, grade):
        super().__init__(name, age)
        self.student_id = student_id
        self.grade = grade

    def display_student(self):
        self.display()
        print(f"ID: {self.student_id}, Grade: {self.grade}")

s1 = Student("Kasun", 20, "ST101", "A")
s1.display_student()

import math

class Shape:
    def area(self):
        pass

class Rectangle(Shape):
    def __init__(self, w, h):
        self.w, self.h = w, h
    def area(self):
        return self.w * self.h

class Circle(Shape):
    def __init__(self, r):
        self.r = r
    def area(self):
        return math.pi * (self.r ** 2)

shapes = [Rectangle(10, 5), Circle(7)]
for s in shapes:
    print(f"Area: {s.area():.2f}")

class Student:
    def __init__(self, name, marks):
        self.name = name
        self.marks = marks # List of 3 marks

    def get_stats(self):
        total = sum(self.marks)
        avg = total / len(self.marks)
        return total, avg

def add_student():
    try:
        name = input("Enter Name: ")
        m1 = int(input("Math: "))
        m2 = int(input("Science: "))
        m3 = int(input("English: "))
        with open("marks.txt", "a") as f:
            f.write(f"{name},{m1},{m2},{m3}\n")
        print("Record saved!")
    except ValueError:
        print("Invalid input! Please enter numeric marks.")

def view_students():
    print("\n--- Student Records ---")
    try:
        with open("marks.txt", "r") as f:
            for line in f:
                data = line.strip().split(",")
                name = data[0]
                marks = [int(x) for x in data[1:]]
                
                std = Student(name, marks)
                total, avg = std.get_stats()
                print(f"Name: {name} | Total: {total} | Avg: {avg:.2f}")
    except FileNotFoundError:
        print("No records found.")

# Main Menu Loop
while True:
    print("\n1. Add Student\n2. View Students\n3. Exit")
    choice = input("Select option: ")
    
    if choice == '1':
        add_student()
    elif choice == '2':
        view_students()
    elif choice == '3':
        break
    else:
        print("Invalid choice!")