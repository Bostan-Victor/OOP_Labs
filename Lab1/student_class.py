

class Student:
    def __init__(self, student_id, first_name, last_name, email, enrollment_date, date_of_birth, is_graduated):
        self.id = student_id
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.enrollment_date = enrollment_date
        self.date_of_birth = date_of_birth
        self.is_graduated = is_graduated


    # Graduate a student object from the faculty
    def graduate(self):
        self.is_graduated = 1

    # Create a valid string entry in the database
    def create_string(self):
        return f"{self.id} | {self.first_name} | {self.last_name} | {self.email} | {self.enrollment_date} | {self.date_of_birth} | {self.is_graduated}"

    # Add the object to the database
    def add_student(self):
        with open("students.txt", "a") as f:
            f.write(self.create_string() + "\n")
