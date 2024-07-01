import json
import re
class NoMatchingNameError(Exception):
    pass


class AuthenticationError(Exception):
    pass


class DuplicateNameFound(Exception):
    pass


class NotUniqueIDError(Exception):
    pass

class Teacher:
    @staticmethod
    def validate_phone_number(phone_number):
        str_of_ph_no=str(phone_number)
        if len(str_of_ph_no)==10 and str_of_ph_no.isdigit() ==True:
            return phone_number
        else:
            raise ValueError("Invalid Phone Number")
        
    @staticmethod    
    def validate_email( email):
        """
        Validates the email format.
        """
        if re.match(r"[^@]+@[^@]+\.[^@]+", email):
            return email
        else:
            raise ValueError("Invalid email address")

    @staticmethod
    def check_name_duplication(name):
        with open('../datafiles/teachers_data.json', "r") as file:
            teacher_data=json.load(file)
        for teacher in teacher_data:
            if teacher['name']==name:
                raise  DuplicateNameFound("The Teacher of your name already exists")
        return name       
    
    @staticmethod
    def check_unique_id(id):
        with open('../datafiles/teachers_data.json', "r") as file:
            teacher_data=json.load(file)
        for teacher in teacher_data:
            if teacher['id']==id:
                raise  NotUniqueIDError("Teacher of your id already exists !!")
        return id    


    @staticmethod
    def accept():
        """
        Accepts teacher details from the user and stores them in the JSON file.
        """
        name = Teacher.check_name_duplication(input("Enter name: "))
        subject = input("Enter subject: ")
        id = Teacher.check_unique_id(int(input("Enter id: ")))
        address = input("Enter address: ")
        email = Teacher.validate_email(input("Enter email: "))
        phone_number = Teacher.validate_phone_number(int(input("Enter phone number: ")))
        teacher_data=[]
        with open('../datafiles/teachers_data.json', "r") as file:
            teacher_data=json.load(file)
        teacher_data.append({
            "name": name,
            "subject": subject,
            "id": id,
            "address": address,
            "email": email,
            "phone_number": phone_number
        })
        with open('../datafiles/teachers_data.json', "w") as file:
           json.dump(teacher_data,file)

    @staticmethod
    def display_all():
        """
        Displays general public information of all teachers.
        """
        with open('../datafiles/teachers_data.json', "r") as file:
            teacher_data=json.load(file)
            for teacher in teacher_data:
                print(f"Name: {teacher['name']}\n Email: {teacher['email']}\nPhone: {teacher['phone_number']}\n Subject: {teacher['subject']}\n\n")

    @staticmethod
    def search(name):
        """
        Displays full details of the requested teacher.
        """
        teacher_data=[]
        with open('../datafiles/teachers_data.json', "r") as file:
            teacher_data=json.load(file)
            for teacher in teacher_data:        
                if teacher['name'] == name:
                    print(f"Name: {teacher['name']}, Subject: {teacher['subject']}, ID: {teacher['id']}, Address: {teacher['address']}, Email: {teacher['email']}, Phone: {teacher['phone_number']}")
                    return
        print(f"No teacher found with name: {name}")
    @staticmethod
    def delete_teacher_data(name):
        """
        Deletes the record of the teacher with the given name.
        """
        count=0

        teacher_data=[]
        with open('../datafiles/teachers_data.json', "r") as file:
            teacher_data=json.load(file)
            len_of_data=len(teacher_data)
            # print(teacher_data)
        for element in teacher_data:
            if element["name"] == name:
                teacher_data.remove(element)
            else:
                count+=1
                pass
        with open('../datafiles/teachers_data.json', "w") as file:
            json.dump(teacher_data,file) 
        if count==len_of_data:
            raise  NoMatchingNameError("Teacher of your given name wasn't found !!")      

    def Authenticate_Teacher(name):
        teacher_data=[]
        state=False
        with open('../datafiles/teachers_data.json', "r") as file:
            teacher_data=json.load(file)
            len_of_data=len(teacher_data)
            for teacher in teacher_data:        
                if teacher['name'] == name:
                    state= True
        return state           

    

if __name__=="__main__":
   
    Teacher.accept()