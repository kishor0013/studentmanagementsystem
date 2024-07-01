from init import *

def main():
    char='y'
    while char=='y' or char=='Y':
        print("1. Add Teacher")
        print("2. Add Student")
        print("3. Display All Teachers")
        print("4. Display All Students")
        print("5. Search Teacher")
        print("6. Search Student")
        print("7. Delete Teacher")
        print("8. Delete Student")
        print("9. Calculate Student Rank")
        print("10. Determine if Student Passed/Failed")
        print("11. Find Highest and Lowest Scores")
        print("12. Calculate Student Percentage")
        print("0. Exit")
        
        choice = input("Enter your choice: ")

        if choice == '1':
            Teacher.accept()
        elif choice == '2':
            Student.accept()
        elif choice == '3':
            Teacher.display_all()
        elif choice == '4':
            Student.display_all()
        elif choice == '5':
            name = input("Enter teacher's name to search: ")
            Teacher.search(name)
        elif choice == '6':
            name = input("Enter student's name to search: ")
            Student.search(name)
        elif choice == '7':
            name = input("Enter teacher's name to delete: ")
            Teacher.delete_teacher_data(name)
        elif choice == '8':
            name = input("Enter student's name to delete: ")
            Student.delete_student_data(name)
        elif choice == '9':
            name= input("Enter your name for calculating rank :")
            print(f"Your rank is : {Student.rank_calculation(name)}")
        elif choice == '10':
            name = input("Enter student's name to determine pass/fail: ")
            result = Student.pass_fail_determination(name)
            print(result)
        elif choice == '11':
            name=input("Enter your name to know your highest and lowest marks :")
            Student.highest_and_lowest_scores(name)
        elif choice == '12':
            name = input("Enter student's name to calculate percentage: ")
            percentage = Student.calculate_percentage(name)
            if percentage is not None:
                print(f"Percentage: {percentage}%")
            else:
                print("Student not found")
        elif choice == '0':
            break
        else:
            print("Invalid choice, please try again.")
        char=input("Enter Y to continue further operations :")


if __name__ == "__main__":
    main()
