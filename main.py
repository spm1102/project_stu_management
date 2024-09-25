import student_list_c as stu_list


student_list = stu_list.student_list_c()
while True:
    print("WELCOME TO STUDENT MANAGEMENT SYSTEM OF EDABK LAB!!!")
    print("Choose the function you want:")
    print("1. Add Student")
    print("2. Remove Student")
    print("3. Update Student Information")
    print("4. Print Student List")
    print("5. Check Student Information")
    print("6. Sorting Student by GPA")
    print("7. Exit")
    choice = int(input("Enter your choice (1-5): "))
    
    if choice == 1:
        student_list.add_student()
    elif choice == 2:
        student_list.remove_student()
    elif choice == 3:
        student_list.update_student()
    elif choice == 4:
        student_list.print_list()
    elif choice == 5:
        student_list.check_student()
    elif choice == 6:
        student_list.sort_student()
    elif choice == 7:
        print("Exiting the program. Goodbye!")
        break
    else:
        print("Invalid input. Please try a gain!")