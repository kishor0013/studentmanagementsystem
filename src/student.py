import json
import re
from teacher import *

class NotUniqueRollNumberError(Exception):
    pass


class Student():
    def __init__(self, name=None, roll_number=None, email=None, phone_number=None, marks=None, address=None):
        """
        Initializes the Student object with given attributes.
        """
        self.name = name
        self.roll_number = roll_number
        self.email = self.validate_email(email) if email else None
        self.phone_number =self.validate_phone_number(phone_number)
        self.marks = marks
        self.address = address
     
    @staticmethod
    def pass_fail_determination(name):
        """
        Determines if a student has passed or failed based on their marks.
        """
        with open('../datafiles/students_data.json', "r") as file:
            student_data=json.load(file)
            for student in student_data:
                    if student['name'] == name:
                        for mark in student['marks'].values():
                            if mark >=40:
                                pass
                            else:
                                return "Fail"
                        return "Pass"    
        return "Student not found"

    @staticmethod
    def highest_and_lowest_scores(name):
        """
        Calculates and returns the highest and lowest scores of a student.
        """
        with open('../datafiles/students_data.json', "r") as file:
            student_data=json.load(file)
            for student in student_data:
                    if student['name'] == name:
                        mark =student['marks'].values()
                        print(f"Your highest mark is :{max(mark)}")
                        print(f"Your lowest mark is : {min(mark)}")
            

    @staticmethod
    def calculate_percentage(name):
        """
        Calculates and returns the percentage of marks for a student.
        """
        with open('../datafiles/students_data.json', "r") as file:
          student_data=json.load(file)
        for student in student_data:
            if student['name'] == name:
                mark =student['marks'].values()
                return (sum(mark)/ 500) * 100
        return None

    @staticmethod
    def rank_calculation(name):
        """
        Calculates and displays the rank of each student based on their marks.
        """
        rank=1
        with open('../datafiles/students_data.json', "r") as file:
            student_data=json.load(file)
            for student in student_data:
                if student['name'] == name:
                    mark =sum(student['marks'].values())
            for student in student_data:
                if student['name']!=name:
                    current_student_mark=sum(student['marks'].values())
                    if current_student_mark >= mark:
                        rank+=1
        return rank
    
    @staticmethod
    def check_name_duplication(name):
        with open('../datafiles/students_data.json', "r") as file:
            student_data=json.load(file)
        for student in student_data:
            if student['name']==name:
                raise  DuplicateNameFound("The student of this name already exists !!")
        return name    
    
    @staticmethod
    def check_unique_roll_no(roll_no):
          with open('../datafiles/students_data.json', "r") as file:
            student_data=json.load(file)
            for student in student_data:
              if student['roll_number']==roll_no:
                  raise NotUniqueRollNumberError("Student of this roll number already exists !")

    @staticmethod
    def accept():
        """
        Accepts student details from the user and stores them in the JSON file.
        """
        name_of_teacher=input("You should be a teacher to add data\nEnter your name : ")
        if Teacher.Authenticate_Teacher(name_of_teacher)==False:
            raise AuthenticationError("You are not found as a teacher !!")
        name =Student.check_name_duplication(input("Enter name: "))
        roll_number = Student.check_unique_roll_no(int(input("Enter roll number: ")))
        email = Teacher.validate_email(input("Enter email: "))
        phone_number = Teacher.validate_phone_number(int(input("Enter phone number: ")))
        marks = {}
        marks["Math"]=int(input("Enter the marks in math :"))
        marks["Science"]=int(input("Enter the marks in Science :"))
        marks["English"]=int(input("Enter the marks in English :"))
        marks["History"]=int(input("Enter the marks in History :"))
        marks["Geography"]=int(input("Enter the marks in Geography:"))
        address = input("Enter address: ")
        with open("../datafiles/students_data.json","r") as file:
              student_data=json.load(file)

        student_data.append({
            "name": name,
            "roll_number":roll_number,
            "email": email,
            "phone_number":phone_number,
            "marks": marks,
            "address": address
        })

        with open('../datafiles/students_data.json', "w") as file:
           json.dump(student_data,file)

    @staticmethod
    def display_all():
        """
        Displays general public information of all students.
        """
        student_data=[]
        with open('../datafiles/students_data.json', "r") as file:
            student_data=json.load(file)
            for student in student_data:
                print(f"Name: {student['name']}\nRoll No : {student['roll_number']}\nEmail: {student['email']}\nPhone: {student['phone_number']}\n" )

    # @staticmethod
    def search(name):
        """
        Displays full details of the requested student.
        """
        with open('../datafiles/students_data.json', "r") as file:
            student_data=json.load(file)
            for student in student_data:
                    if student['name'] == name:
                        print(f"Name: {student['name']}, Roll Number: {student['roll_number']}, Email: {student['email']}, Phone: {student['phone_number']}, Marks: {student['marks']}, Address: {student['address']}")
                        print(f" You are :  {Student.pass_fail_determination(name)}")
                        Student.highest_and_lowest_scores(name)
                        print(f" your percentage was : {Student.calculate_percentage(name)}")
                        print(f"Your rank is : {Student.rank_calculation(name)}")
                        return
        print(f"No student found with name: {name}")

    @staticmethod
    def delete_student_data(name):
        """
        Deletes the record of the student with the given name.
        """
        count=0

        student_data=[]
        with open('../datafiles/students_data.json', "r") as file:
            student_data=json.load(file)
            len_of_data=len(student_data)
            # print(teacher_data)
        for element in student_data:
            if element["name"] == name:
                student_data.remove(element)
            else:
                count+=1
                pass
        with open('../datafiles/students_data.json', "w") as file:
            json.dump(student_data,file) 
        if count==len_of_data:
            raise  NoMatchingNameError("Studnet of your given name wasn't found !!") 
if __name__=="__main__":
    #a_student=Student
    print( Student.display_all()) 