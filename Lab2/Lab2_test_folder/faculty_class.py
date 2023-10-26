from study_field_enum import StudyField


class Faculty:
    def __init__(self, faculty_id, name, abbreviation, students, study_field):
        self.id = faculty_id
        self.name = name
        self.abbrevation = abbreviation
        self.students = students
        self.study_field = study_field


    # Create a valid string entry in the database
    def create_string(self):
        return f"{self.id} | {self.name} | {self.abbrevation} | {self.students} | {self.study_field.name}"


    # Add the object to the database
    def add_faculty(self):
        with open("faculties.txt", "a") as f:
            f.write(self.create_string()+"\n")


    # Append a new object to the students list
    def append_to_students(self, student):
        self.students.append(student)
