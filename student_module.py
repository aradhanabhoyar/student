class Student:
    def __init__(self, name, roll, subjects_marks):
        self.name = name
        self.roll = roll
        self.subjects_marks = subjects_marks  

    def calculate_percentage(self):
        total_marks = sum(self.subjects_marks.values())
        number_of_subjects = len(self.subjects_marks)
        percentage = total_marks / (number_of_subjects * 100) * 100
        return percentage

    def display_info(self):
        print(f"Name: {self.name}")
        print(f"Roll No: {self.roll}")
        print("Subject-wise Marks:")
        for subject, marks in self.subjects_marks.items():
            print(f"  {subject}: {marks}")
        print(f"Percentage: {self.calculate_percentage():.2f}%")
