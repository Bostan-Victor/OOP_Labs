from faculty_class import Faculty
from student_class import Student
from study_field_enum import StudyField


class Main():
    def __init__(self):
        self.program_loop()


    # Main program loop
    def program_loop(self):
        inp = ""
        while inp != "exit":
            inp = input("\n\n----------------------------------------------------------------------------\nOptions:\nFaculty operations:\n1. Create and assign a student to a faculty\n2. Graduate a student from a faculty\n3. Display current enroled students\n4. Display graduates\n5. Check if student in faculty\n\nGeneral operations:\n6. Create a new faculty\n7. Search unique identifier\n8. Display faculties\n9. Display all faculties belonging to a field\n\n0. exit\n\nEnter the option:")
            if inp == "1":
                self.create_assign_student()
            elif inp == "2":
                self.graduate_from_faculty()
            elif inp == "3":
                self.display_enroled()
            elif inp == "4":
                self.display_graduated()
            elif inp == "5":
                self.check_student()
            elif inp == "6":
                self.create_faculty()
            elif inp == "7":
                self.search_by_unique()
            elif inp == "8":
                self.print_faculties()
            elif inp == "9":
                self.display_by_field()


    # Get all the students in the University
    def get_students(self):
            students = []
            with open("students.txt", "r") as f:
                lines = f.readlines()
                for line in lines:
                    fields = line.split(' | ')
                    student = Student(int(fields[0]), fields[1], fields[2], fields[3], fields[4], fields[5], int(fields[6]))
                    students.append(student)
                return students
            

    # Get all the university faculties        
    def get_faculties(self):
        faculties = []
        with open("faculties.txt", "r") as f:
                lines = f.readlines()
                for line in lines:
                    fields = line.split(' | ')
                    faculty = Faculty(int(fields[0]), fields[1], fields[2], eval(fields[3]), StudyField[fields[4].strip()])
                    faculties.append(faculty)
                return faculties


    # Get the next id that will be given to a new object stored in the database
    def get_next_id(self, file_name):
        with open(file_name, "r") as f:
            lines = f.readlines()
            if lines:
                last_line = lines[-1]
                next_id = int(last_line.split(' | ')[0]) + 1
            else:
                next_id = 1
        return next_id
    

    # Get the study field name from user input
    def get_study_field_object(self):
        while True:
            study_field = input("Choose a Study Field(ME/SE/FT/UA/VM):")

            if study_field == "ME":
                study_field = StudyField.MECHANICAL_ENGINEERING
                break
            elif study_field == "SE":
                study_field = StudyField.SOFTWARE_ENGINEERING
                break
            elif study_field == "FT":
                study_field = StudyField.FOOD_TECHNOLOGY
                break
            elif study_field == "UA":
                study_field = StudyField.URBANISM_ARCHITECTURE
                break
            elif study_field == "VM":
                study_field = StudyField.VETERINARY_MEDICINE
                break
            else:
                print("There is no such field of study!")
        return study_field


    # Print all the faculties
    def print_faculties(self): 
        faculties = self.get_faculties()
        print("\nAvailable faculties:")
        for faculty in faculties:
            print(faculty.id, faculty.name)


    # Print all the students
    def print_students(self):
        students = self.get_students()
        print("\nAll students:")
        for student in students:
            print(student.id, student.first_name + " " + student.last_name)


    # Create and assign a student to a faculty
    def create_assign_student(self):
        faculties = self.get_faculties()
        students = self.get_students()
        print("\nCreate a new student:")
        first_name = input("First name: ")
        last_name = input("Last name: ")
        # Email uniqueness validation
        email = input("Email: ")
        while any(student.email == email for student in students):
            print("* This email is already taken. Please enter a different email. *")
            email = input("Email: ")
                    

        enroll_date = input("Enrollment date: ")
        date_birth = input("Date of birth: ")
        while True:
            is_grad = input("Has the student graduated(Yes/No): ")
            if is_grad == "Yes":
                is_grad = 1
                break
            elif is_grad == "No":
                is_grad = 0
                break
            else:
                print("Type Yes or No!")

        # Get the last id 
        next_id = self.get_next_id('students.txt')

        try:
            student = Student(next_id, first_name, last_name, email, enroll_date, date_birth, is_grad)
            print("\n* Student created successfully! *")
        except:
            print("\n* There was a problem when creating the student! *")

        # Writes the student in the students text file
        student.add_student()

        print("\nAssign the student to a faculty:")
        if len(faculties):
            self.print_faculties()
            f = int(input("\nAssign the student to a faculty: "))
            try:
                faculties[f-1].append_to_students(student.id)
                print(f"\n* Student {student.first_name} {student.last_name} added to {faculties[f-1].name}! *")
            except:
                print(f"\n* There was a problem when adding {student.first_name} {student.last_name} to {faculties[f-1].name}! *")
            with open('faculties.txt', 'w') as file:
                for faculty in faculties:
                    file.write(faculty.create_string()+'\n')
        else:
            print("There are no faculties available!")


    # Graduate a student from the faculty
    def graduate_from_faculty(self):
        students = self.get_students()
        faculties = self.get_faculties()
        if len(faculties):
            self.print_faculties()
            f = int(input("\nChoose the faculty of the student you want to graduate: "))
            if len(students):
                print("Available students at " + faculties[f-1].name + ":")
                for student_id in faculties[f-1].students:
                    student = students[student_id-1]
                    if not student.is_graduated:
                        print(student.id, student.first_name + " " + student.last_name)
                s = int(input("\nChoose a student to graduate: "))
                try:
                    students[s-1].graduate()
                    print(f"\n* Student {students[s-1].first_name} {students[s-1].last_name} graduated successfully! *")
                except:
                    print(f"\n* There was as problem when graduating {students[s-1].first_name} {students[s-1].last_name}! *")
                with open('students.txt', 'w') as file:
                    for student in students:
                        file.write(student.create_string() + '\n')
            else: 
                print("There are no students at this faculty!")
        else:
            print("There are no faculties available!")


    # Display all the enrolled students
    def display_enroled(self):
        students = self.get_students()
        print("\nCurrent enroled students:")
        if len(students):
            i = 1
            for student in students:
                if not student.is_graduated:
                    print(f"{i}. {student.first_name} {student.last_name}")
                    i += 1
        else:
            print("There are no students!")


    # Display all the graduated students
    def display_graduated(self):
        students = self.get_students()
        print("\nGraduated students:")
        if len(students):
            i = 1
            for student in students:
                if student.is_graduated:
                    print(f"{i}. {student.first_name} {student.last_name}")
        else:
            print("There are no graduated students!")
    

    # Check if a student belongs to the chosen faculty
    def check_student(self):
        students = self.get_students()
        faculties = self.get_faculties()
        self.print_students()
        try:
            s = int(input("\nChoose a student: "))
        except:
            print("\n* Please enter a valid integer for the id! *")
            return
        self.print_faculties()
        try:
            f = int(input("\nChoose a faculty: "))
        except:
            print("\n* Please enter a valid integer for the id! *")
            return

        if students[s-1].id in faculties[f-1].students:
            print(f"\n* The student {students[s-1].first_name} {students[s-1].last_name} is at {faculties[f-1].name} *")
        else:
            print(f"\n* The student {students[s-1].first_name} {students[s-1].last_name} is not at {faculties[f-1].name} *")


    # Create a new faculty
    def create_faculty(self):
        print("\nCreate a new faculty:")
        name = input("Name: ")
        abbr = input("Abbreviation: ")
        study_field = self.get_study_field_object()
            
        next_id = self.get_next_id('faculties.txt')
        try:
            faculty = Faculty(next_id, name, abbr, [], study_field)
            print("\n* Faculty created successfully! *")
        except:
            print("\n* There was a problem when creating the faculty! *")
        faculty.add_faculty()

    # Search by a unique identifier id or email
    def search_by_unique(self):
        students = self.get_students()
        faculties = self.get_faculties()
        c = input("What identifier to search student by id/email: ")
        faculty_name = ""

        if c == "id":
            self.print_students()
            try:
                id_input = int(input("Enter the id of the student: "))
            except:
                print("\n* Please enter a valid integer for the id! *")
                return
            for faculty in faculties:
                if students[id_input-1].id in faculty.students:
                    faculty_name = faculty.name
                    break
        elif c == "email":
            print("\nAll students:")
            for student in students:
                print(student.id, student.first_name + " " + student.last_name + " | email: " + student.email)
            email_input = input("Enter the email of the student: ")
            for student in students:
                if email_input == student.email:
                    for faculty in faculties:
                        if student.id in faculty.students:
                            faculty_name = faculty.name
                            break
                    break

        if faculty_name != "":
            print(f"\n* This student belongs to {faculty_name} faculty *")
        else:
            print("\n* The student does not belong to any faculty! *")


    # Display the faculties belonging to a field of study
    def display_by_field(self):
        faculties = self.get_faculties()
        study_field = self.get_study_field_object()

        print(f"\nAll faculties belonging to {study_field.name}:")
        i = 1
        for faculty in faculties:
            if faculty.study_field.name == study_field.name:
                print(f"{i}. {faculty.name}")
                i += 1


if __name__ == "__main__":
    Main()
