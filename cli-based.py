class Student:
    def __init__(self, id, name ,maths,physics,computer,english):

        self.student_dict = {
                "student_id" : id,
                "student_name" : name,
                "subjects" : {
                    "Maths" : maths,
                    "Physics" : physics,
                    "Computer": computer,
                    "English" : english
                }
            }
class Toppers :
    def __init__(self , id ,name,score) :
        self.toppers_dict = {
            "Student_id" : id,
            "Student_name" : name,
            "highest_score" : score
        }    
class Report : 
    def __init__(self,id,name,average,grade):
        self.report_dict = {
            "student_id" :id,
            "student_name":name,
            "average":average,
            "grade" : grade
        }
class filemanager:
    @staticmethod
    def check_data():
        with open("data.csv", "r") as file:
            return file.readlines()  

    @staticmethod
    def write_file(record):
        with open("data.csv", "w") as file:
            for student in record :
                line = f"{student['student_id']},{student['student_name']},{student['subjects']['Maths']},{student['subjects']['Physics']},{student['subjects']['Computer']},{student['subjects']['English']}\n"
                file.write(line)

    def fetch_data ():
        data = filemanager.check_data()
        record = []
        if data :
            for line in data :
                id,name,maths,physics,computer,english = line.strip().split(",")
                std = Student(id,name,maths,physics,computer,english)
                record.append(std.student_dict)
        return record

    def report_file(record):
        with open("report.csv", "w") as file:
            for student in record :
                line = f"{student['student_id']},{student['student_name']},{student['average']},{student['grade']}\n"
                file.write(line)  

    def stats_file(record):
        with open("stats.csv", "w") as file:
            for student in record :
                line = f"{student['student_id']},{student['student_name']},{student['average']},{student['grade']}\n"
                file.write(line)                           

class student_manager:

    @staticmethod
    def add_student():
        get_data = filemanager.fetch_data()
        while True:
            try:
                id = int(input("\nPlease Enter the student ID:"))
                found = False
                for student in get_data:
                    if int(student['student_id']) == id :
                        found = True
                        break
                if found :
                    print("\nPlease Enter the Unique ID\n")
                else :
                    break
            except:
                print("\nPlease Enter the Id in Numeric Form\n")                         
        while True:
            name = input("\nPlease Enter the Student Name:") 
            if name.isalpha():
                break
            else :
                print("\n\"Please Enter the Name in Alphabatic Form Only And donot add spaces\"\n")
        while True :        
            try :
                maths = int(input("\nPlease Enter the Maths Marks :"))
                physics = int(input("\nPlease Enter the Physics Marks :"))
                computer = int(input("\nPlease Enter the Computer Marks :"))            
                english = int(input("\nPlease Enter the English Marks :"))
                break
            except:
                print("\nPlease Enter the Each Subject Marks in Numeric Form\n")    
        student = Student(id, name , maths , physics , computer , english)
        get_data.append(student.student_dict)
        filemanager.write_file(get_data)
        print("\n\"Student Added Successfully\"\n")
        while True :
            next = input("\n Enter \"Y\" For Adding More student \"N\" For Main Meu \n  ")
            if next == 'y' or next =='Y' :
                student_manager.add_student()
                break
            elif next == 'n' or next == 'N':
                main_menu()
                break
            else :
                print("\n Please Enter Y or N \n")

    @staticmethod
    def update_student():
        get_data = filemanager.fetch_data()
        while True:
            try:
                id = int(input("\nPlease Enter the student ID:"))
                found = False
                for student in get_data:
                    if int(student['student_id']) == id :
                        while True:
                            student['student_name'] = input("\nPlease Enter Updated Student Name:") 
                            if student['student_name'].isalpha():
                                break
                            else :
                                print("\n\"Please Enter the Name in Alphabatic Form Only And donot add spaces\"\n")
                        while True :       
                            try :
                                student['subjects']['Maths'] = int(input("\nPlease Enter the Maths Marks :"))
                                student['subjects']['Physics'] = int(input("\nPlease Enter the Physics Marks :"))
                                student['subjects']['Computer'] = int(input("\nPlease Enter the Computer Marks :"))            
                                student['subjects']['English'] = int(input("\nPlease Enter the English Marks :"))
                                break
                            except:
                                print("\nPlease Enter the Each Subject Marks in Numeric Form\n")    
                        filemanager.write_file(get_data)
                        print("\n\"Student Data Updated Successfully\"\n")
                        found = True
                        break
                    else :
                        print("\n\"Please Enter The correct ID for Change\"\n") 
                if found:
                    break           
            except:
                print("\nPlease Enter the Id in Numeric Form\n")                         

        while True :
            next = input("\n Enter \"Y\" For Adding More student \"N\" For Main Meu \n  ")
            if next == 'y' or next =='Y' :
                student_manager.update_student()
                break
            elif next == 'n' or next == 'N':
                main_menu()
                break
            else :
                print("\n Please Enter Y or N \n")

    @staticmethod
    def search_students():
        get_data = filemanager.fetch_data()
        while True:
            name = input("\nPlease Enter the student Name for Search :")
            if name.isalpha():
                found = False
                for student in get_data:
                    if student['student_name'].lower() == name.lower() :
                        print("Roll_Number :" ,student['student_id'])
                        print("Name :",student['student_name'])
                        print("Maths Marks :",student['subjects']['Maths'])
                        print("Physics Marks :",student['subjects']['Physics'])   
                        print("Computer Marks :",student['subjects']['Computer'])
                        print("English Marks :",student['subjects']['English'])         
                        filemanager.write_file(get_data)
                        print("\n\"Student Data Searched Successfully\"\n")
                        found = True
                        break
                if found :
                    continue;     
                else :
                    print("\n \"Please Enter The correct Name For Search \" \n") 
            else:
                print("\"Please Enter Name In Aphabatic Form\"")
            if found :
                break    
        while True :
            next = input("\n Enter \"Y\" For Searching More student \"N\" For Main Meu \n  ")
            if next == 'y' or next =='Y' :
                student_manager.Search_student()
                break
            elif next == 'n' or next == 'N':
                main_menu()
                break
            else :
                print("\n Please Enter Y or N \n")

    @staticmethod
    def Delete_student() :
        data = filemanager.fetch_data()
        while True:
            try:
                id = int(input("\nPlease Enter the student ID:"))
                found = False
                for student in get_data:
                    if int(student['student_id']) == id :
                        record.remove(student)   
                        filemanager.write_file(data)
                        print("\n\"Student Data Deleted Successfully\"\n")
                        found = True
                        break
                    else :
                        print("\n \"Please Enter The correct ID for Deletetion\" \n") 
                if found:
                    break           
            except:
                print("\nPlease Enter the Id in Numeric Form\n")                         

        while True :
            next = input("\n Enter \"Y\" For Adding More student \"N\" For Main Meu \n  ")
            if next == 'y' or next =='Y' :
                student_manager.Delete_student()
                break
            elif next == 'n' or next == 'N':
                main_menu()
                break
            else :
                print("\n Please Enter Y or N \n")

    def proformance_analyzer():
        get_data = filemanager.fetch_data()
        while True:
            try :
                id = int(input("\nPlease Enter the student ID for Proformance Analyzing :"))
                found = False
                for student in get_data:
                    if int(student['student_id']) == id :
                        average = (int(student['subjects']['Maths']) + int(student['subjects']['Physics']) + int(student['subjects']['Computer']) + int(student['subjects']['English']))/4
                        if average >= 85 :
                            print("Performance : Excellent")
                            print("\n\"Student Performance Showed Successfully\"\n")
                            found = True
                            break
                        elif average >= 70 :
                            print("Performance : Good")
                            print("\n\"Student Performance Showed Successfully\"\n")
                            found = True
                            break
                        elif average >= 50:
                            print("Performance :Average")
                            print("\n\"Student Performance Showed Successfully\"\n")
                            found = True
                            break
                        else :
                            print("Performance :Poor")  
                            print("\n\"Student Performance Showed Successfully\"\n")
                            found = True
                            break
            except:
                print("\n\"Please Enter Correct ID for Performance check\"")                          
            if found :
                break     
        while True :
            next = input("\n Enter \"Y\" For Searching More student \"N\" For Main Meu \n  ")
            if next == 'y' or next =='Y' :
                student_manager.proformance_analyzer()
                break
            elif next == 'n' or next == 'N':
                main_menu()
                break
            else :
                print("\n Please Enter Y or N \n")

    def overall_topper():
        get_data = filemanager.fetch_data()
        topper_students = []
        highest_average = 0 
        for student in get_data :
            average = (int(student['subjects']['Maths']) + int(student['subjects']['Physics']) + int(student['subjects']['Computer']) + int(student['subjects']['English']))/4
            if average > highest_average :
                highest_average = average
                topper_students = []
                topper = Toppers(student['student_id'],student['student_name'],highest_average)
                topper_students.append(topper.toppers_dict)
                
            elif average == highest_average :
                topper = Toppers(student['student_id'],student['student_name'],highest_average)
                topper_students.append(topper.toppers_dict)
        print("\"\nThese Are The Toppers : \"\n")
        for topper in topper_students :
            print(topper)

        while True :
            next = input("\n Enter \"Y\" For Searching More student \"N\" For Main Meu \n  ")
            if next == 'y' or next =='Y' :
                student_manager.overall_topper()
                break
            elif next == 'n' or next == 'N':
                main_menu()
                break
            else :
                print("\n Please Enter Y or N \n")
                
    def subject_topper():
        get_data = filemanager.fetch_data()
        maths_topper = []
        physics_topper = []
        computer_topper = []
        english_topper = []
        maths_marks = 0 
        for student in get_data :
            maths = int(student['subjects']['Maths'])
            if maths > maths_marks :
                maths_marks = maths
                maths_topper = []
                topper = Toppers(student['student_id'],student['student_name'],maths_marks)
                maths_topper.append(topper.toppers_dict)
                
            elif maths == maths_marks :
                topper = Toppers(student['student_id'],student['student_name'],maths_marks)
                maths_topper.append(topper.toppers_dict)

        physics_marks = 0 
        for student in get_data :
            physics = int(student['subjects']['Physics'])
            if physics > physics_marks :
                physics_marks = physics
                physics_topper = []
                topper = Toppers(student['student_id'],student['student_name'],physics_marks)
                physics_topper.append(topper.toppers_dict)
                
            elif physics == physics_marks :
                topper = Toppers(student['student_id'],student['student_name'],physics_marks)
                physics_topper.append(topper.toppers_dict)

        computer_marks = 0 
        for student in get_data :
            computer = int(student['subjects']['Computer'])
            if computer > computer_marks :
                computer_marks = computer
                computer_topper = []
                topper = Toppers(student['student_id'],student['student_name'],computer_marks)
                computer_topper.append(topper.toppers_dict)
            elif computer == computer_marks :
                topper = Toppers(student['student_id'],student['student_name'],computer_marks)
                computer_topper.append(topper.toppers_dict)

        english_marks = 0 
        for student in get_data :
            english = int(student['subjects']['English'])
            if english > english_marks :
                english_marks = english
                english_topper = []
                topper = Toppers(student['student_id'],student['student_name'],english_marks)
                english_topper.append(topper.toppers_dict)
                
            elif english == english_marks :
                topper = Toppers(student['student_id'],student['student_name'],english_marks)
                english_topper.append(topper.toppers_dict)

        print("\"\nThese Are The Maths Topper : \"\n")
        for topper in maths_topper :
            print(topper,"\n")
        print("\"\nThese Are The Physics Topper : \"\n")    
        for topper in physics_topper :
            print(topper,"\n")     
        print("\"\nThese Are The Computer Topper : \"\n")    
        for topper in physics_topper :
            print(topper,"\n") 
        print("\"\nThese Are The English Topper : \"\n")    
        for topper in english_topper :
            print(topper,"\n")   

        while True :
            next = input("\n Enter \"Y\" For Searching More student \"N\" For Main Meu \n  ")
            if next == 'y' or next =='Y' :
                student_manager.subject_topper()
                break
            elif next == 'n' or next == 'N':
                main_menu()
                break
            else :
                print("\n Please Enter Y or N \n")

    def Generate_report():
        get_data = filemanager.fetch_data()
        generate_report = []
        while True:
            try:
                id = int(input("\nPlease Enter the student ID for Performance Analyzing : "))
                found = False
                for student in get_data:
                    if int(student['student_id']) == id:
                        found = True
                        average = (
                            int(student['subjects']['Maths']) +
                            int(student['subjects']['Physics']) +
                            int(student['subjects']['Computer']) +
                            int(student['subjects']['English'])
                        ) / 4
                        if average >= 85:
                            grade = "Excellent"
                        elif average >= 70:
                            grade = "Good"
                        elif average >= 50:
                            grade = "Average"
                        else:
                            grade = "Poor"
                        print("\nStudent ID :", student['student_id'])
                        print("Student Name :", student['student_name'])
                        print("Average :", average)
                        print("Grade :", grade)
                        report = Report(
                            student['student_id'],
                            student['student_name'],
                            average,
                            grade
                        )
                        generate_report.append(report.report_dict)
                        filemanager.report_file(generate_report)
                        print("\nStudent Performance Showed Successfully And Save In Report Successfully\n")
                        break
                if not found:
                    print("\nID not found\n")
                else:
                    break
            except ValueError:
                print("\nPlease Enter ID in Numeric Form\n")     
        while True :
            next = input("\n Enter \"Y\" For Searching More student \"N\" For Main Meu \n  ")
            if next == 'y' or next =='Y' :
                student_manager.Generate_report()
                break
            elif next == 'n' or next == 'N':
                main_menu()
                break
            else :
                print("\n Please Enter Y or N \n")

    def Students_Stats_Updated():
        get_data = filemanager.fetch_data()
        generate_report = []
        for student in get_data:
                average = (
                    int(student['subjects']['Maths']) +
                    int(student['subjects']['Physics']) +
                    int(student['subjects']['Computer']) +
                    int(student['subjects']['English'])
                ) / 4
                if average >= 85:
                    grade = "Excellent"
                elif average >= 70:
                    grade = "Good"
                elif average >= 50:
                    grade = "Average"
                else:
                    grade = "Poor"
                print("\nStudent ID :", student['student_id'])
                print("Student Name :", student['student_name'])
                print("Average :", average)
                print("Grade :", grade)
                report = Report(
                    student['student_id'],
                    student['student_name'],
                    average,
                    grade
                )
                generate_report.append(report.report_dict)
        print("\nStudent  Students Stats Updated Successfully And Save In Stats File Successfully\n")
        filemanager.stats_file(generate_report)
        while True :
            next = input("\n Enter \"Y\" For Searching More student \"N\" For Main Meu \n  ")
            if next == 'y' or next =='Y' :
                student_manager.Students_Stats_Updated()
                break
            elif next == 'n' or next == 'N':
                main_menu()
                break
            else :
                print("\n Please Enter Y or N \n")

def main_menu():

    while True:
        print("\n========== STUDENT MANAGEMENT SYSTEM ==========")
        print("1. Add Student")
        print("2. Delete Student")
        print("3. Update Student")
        print("4. Search Students")
        print("5. Proformance Analyzer")
        print("6. Overall Topper")
        print("7. Subject Toppers")
        print("8. Generate Report")
        print("9. Full Student Statistics ")
        while True:
            try:
                choice = input("Enter your choice: ")
                break
            except:
                print("\n\"Please Enter Your Choice in Numeric form\"\n")
        if choice == '1':
            student_manager.add_student()

        elif choice == '2':
            student_manager.Delete_student()

        elif choice == '3':
            student_manager.update_student()

        elif choice == '4' :
            student_manager.search_students()

        elif choice == '5':
            student_manager.proformance_analyzer()
            break
        elif choice == '6':
            student_manager.overall_topper()
            break
        elif choice == '7':
            student_manager.subject_topper()
            break 
        elif choice == '8':
            student_manager.Generate_report()
            break
        elif choice == '9':
            student_manager.Students_Stats_Updated()
            break                    
        else:
            print("Invalid Choice")

main_menu()