Student = {}

while True:
    print("\n----STUDENT MANAGER APP----")
    print("\n1.ADD STUDENTS")
    print("2. VIEW STUDENTS")
    print("3. CHECK RESULTS")
    print("4. DELETE STUDENT")
    print("5. EXIT")
    
    choice = input("\nEnter your choice: ")
    #Add stu
    if choice == '1':
        name = input("Enter student name: ")
        roll_no = int(input("Enter student roll number: "))
        marks = int(input("Enter student marks: "))
        Student[roll_no] = {'name': name, 'marks': marks}
        print(f"{name} (Roll No: {roll_no}) Student added successfully!")
        
        
    #view stu
    elif choice == '2':
        if not Student:
            print("No student found!")
        else:
            for roll_no ,data in Student.items():
                print(f"Name: {data['name']}, Roll No: {roll_no}, Marks: {data['marks']}")    
            
            
    # check result
    elif choice == '3':
        roll_no = int(input("Enter student roll number: "))
        
        if roll_no in Student:
            marks = int(Student[roll_no]['marks'])
            
            if marks >= 40:
                print("PASS")
                
            else:
                print("FAIL")
        else:
            print("Student not found!")
            
    # delete stu
    elif choice == '4':
        roll_no = int(input("Enter student roll number: "))
        
        if roll_no in Student:
            del Student[roll_no]
            print(f"Student with Roll No: {roll_no} deleted successfully!")
        else:
            print("Student not found!")        
            
            
    # exit        
    elif choice == '5':
        print("Exiting the program...")
        break
    else:
        print("Invalid choice!!!!!! Please try again......")
        
    

