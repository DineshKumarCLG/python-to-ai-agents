class Student:
    def __init__(self, student_id, name, marks):
        self.student_id=student_id
        self.name=name
        self.marks=marks

    def calculate_results(self):
        if not self.marks:
            raise ValueError("Marks dictionary cannot be empty")
        i=len(self.marks)
        total=0
        for mark in self.marks.values():
            if mark<0 or mark>100:
                raise ValueError("Marks must be between 0 and 100")
            total=total+mark
        avg_marks=total/i
        self.score=avg_marks

        if self.score >= 90:
            self.grades="A"
        elif self.score >= 80:
            self.grades="B"
        elif self.score >= 70:
            self.grades="C"
        elif self.score >= 60:
            self.grades="D"
        elif self.score >= 50:
            self.grades="E"
        else:
            self.grades="F"
        return f'{self.score:.2f}',self.grades 

    def display_report_card(self):
        avg_marks, grade = self.calculate_results()
        print("=" * 50)
        print("STUDENT REPORT CARD")
        print("=" * 50)
        print("ID: ", self.student_id)
        print("Name: ", self.name)
        print("-" * 50)
        print("Subject", "Marks")
        print("-" * 50)
        for subject,mark in self.marks.items():
            print(subject,mark)
        print("-" * 50)
        print(f"Average: {avg_marks}%", "Grade:", grade)
        print("=" * 50)    

    # students = {}

    # def get_student_input(self):
    #     student_id = input("Enter your Student ID: ")
    #     if student_id in self.students:
    #         print("Student ID already exists")
    #     student_name = input("Enter your Name: ")
    #     marks = {}
    #     while True:
    #         subjects = input("Enter your subject or DONE to quit: ")
    #         if subjects.lower() == "done":
    #             break
    #         score = int(input("Enter the mark of the subject: "))
    #         marks[subjects] = score
    #     self.students[student_id] = {"name": student_name, "marks": marks}

    # def get_all_report_cards(self):
    #     for student_id, student_info in self.students.items():
    #         self.display_report_card(student_id, student_info)

s1 = Student("S101", "Alice", {"Math": 95, "Science": 90})
s1.display_report_card()
