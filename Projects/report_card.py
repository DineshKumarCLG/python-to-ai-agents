def calculate_results(marks: dict)->tuple[float,str]:

    if not marks:
        raise ValueError("Marks dictionary cannot be empty")

    i=len(marks)
    total=0
    for mark in marks.values():
        if mark<0 or mark>100:
            raise ValueError("Marks must be between 0 and 100")
        total=total+mark

    avg_marks=total/i

    if avg_marks >= 90:
        grade = "A"
    elif avg_marks >= 80:
        grade = "B"
    elif avg_marks >= 70:
        grade = "C"
    elif avg_marks >= 60:
        grade = "D"
    elif avg_marks >= 50:
        grade = "E"
    else:
        grade = "F"

    return f'{avg_marks:.2f}', grade


def display_report_card(student_id, student_info)->None:
    # student_id="S101"
    # student_info = {
    # "name": "Alice Johnson", 
    # "marks": {"Math": 95, "Science": 92, "English": 88}
    # }

    avg_marks, grade = calculate_results(student_info["marks"])

    print("=" * 50)
    print("STUDENT REPORT CARD")
    print("=" * 50)
    print("ID: ", student_id)
    print("Name: ", student_info['name'])
    print("-" * 50)
    print("Subject", "Marks")
    print("-" * 50)
    for subject,mark in student_info["marks"].items():
        print(subject,mark)
    print("-" * 50)
    print(f"Average: {avg_marks}%", "Grade:", grade)
    print("=" * 50)



students = {}

# students["S101"] = {
#     "name": "Alice Johnson",
#     "marks": {"Math": 95, "Science": 92, "English": 88}
# }

# students["S102"] = {
#     "name": "Bob Smith",
#     "marks": {"Math": 65, "Science": 72, "English": 68}
# }




def get_student_input():
    student_id=input("Enter your Student ID: ")
    if student_id in students:
        print("Student ID already exists")
    student_name=input("Enter your Name: ")
    marks={}
    while True:
        subjects=input("Enter your subject or DONE to quit: ")
        if subjects.lower()=="done":
            break
        score=int(input("Enter the mark of the subject: "))
        marks[subjects]=score

    students[student_id] = {"name": student_name, "marks": marks}

get_student_input()

for student_id, student_info in students.items():
    display_report_card(student_id, student_info)

    
    



class Book:
    def __init__(self, title, author):
        self.title=title
        self.author=author
    def get_description(self):
        return f"{self.title} was written by {self.author}"

my_book=Book("Atomic Habits", "James Clear")

print(my_book.get_description())