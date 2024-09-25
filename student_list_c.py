import student_c as stu


class student_list_c:
    def __init__(self):
        self.stu_list = []


    def check_student(self):
        """Check if student with the given ID existing in the list"""
        id = int(input("Enter the ID of student you want to check: "))
        flag = False
        for student in self.stu_list:
            if student.ID == id:
                flag = True
                print("Existed this student!")
                student.infor()
                break
        if flag == False:
            print(f"There is no student with ID {id} in the list")
            
            
    def add_student(self):
        """Add a student to the list."""
        print("Enter the student's information:")
        name = input("Enter student's name: ")
        id = int(input("Enter student's ID: "))
        classroom = input("Enter student's class: ")
        gpa = float(input("Enter student's GPA: "))
        student = stu.student_c(name, id, gpa, classroom)
        self.stu_list.append(student)
        print(f"{name} has been added to the student list." )


    def remove_student(self):
        """Remove a student with given id from the list"""
        id = int(input("Enter the ID of the student you want to remove: "))
        flag = False
        for student in self.stu_list:
            if student.ID == id:
                flag = True
                self.stu_list.remove(student)
                print(f"Student with ID {id} has been removed.")
                break
        if flag == False:
            print(f"No student found with ID {id}.")
                
                
    def update_student(self):
        """Update student information"""
        id = int(input("Enter student ID to update: "))
        flag = False
        for student in self.stu_list:
            if student.ID == id:
                flag = True
                print(f"Current infomation for student with ID {id}:")
                student.show_infor()
        
                new_name = input("Enter updated name: ")
                student.name = new_name if new_name else student.name
                new_id = int(input("Enter updated ID: "))
                student.ID = new_id if new_id else student.ID
                new_class = input("Enter updated classroom: ")
                student.classroom = new_class if new_class else student.classroom
                new_gpa = float(input("Enter updated gpa: "))
                student.gpa = new_gpa if new_gpa else student.gpa
                
                print("Updated information of student{new_name}:")
                student.show_infor()
                break
        if flag == False:
            print(f"There is no student with ID {id} to update")
            
            
    def print_list(self):
        """print student info in current list"""
        if(len(self.stu_list) != 0):
            print(f"There are {len(self.stu_list)} students in the list:")
            for student in self.stu_list:
                student.show_infor()
        else:
            print("There is no student in the list.")
        
    def sort_student(self):
        choice = int(input("""What's kind of order do you want to sort?(Choose 1 or 2)\n1. Descendant\n2. Ascendant\nChoice: """))
        if choice == 1:
            self.stu_list.sort(reverse = True)
            self.print_list()
        elif choice == 2:
            self.stu_list.sort()
            self.print_list()