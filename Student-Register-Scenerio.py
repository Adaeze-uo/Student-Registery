import time
import gspread
from oauth2client.service_account import ServiceAccountCredentials


scope = ["https://spreadsheets.google.com/feeds"]
creds = ServiceAccountCredentials.from_json_keyfile_name('New-Student Registration.json', scope)
client = gspread.authorize(creds)

sheet = client.open_by_url('https://docs.google.com/spreadsheets/d/1LJ4a1I3LVgOYWXCzOePqc-wNCC_s1fMKoawcwY-HxUs/edit#gid=0').sheet1

global menu_option
global worksheet
menu_option = ""

def user_authentication():
    username = "RLeeman"
    password = "Kpop-MCND"
    user_name = input('Enter your username: ')
    pass_word = input('Enter your password: ')
    if username == user_name:
        if password == pass_word:
            print('Your username and password are valid; you will be directed to the menu')
            time.sleep
        else:
            print('Password is invalid; try again')
    else:
        print('Username is invalid; try again.')

user_authentication()

def menu():
    print("""Welcome to the Menu!
    1. Inputting student details
    2. Uploading student details
    3. Creating student reports
    4. Log out of menu""")
    option = int(input('Enter a number between 1 and 4: '))
    if option == 1:
        def StudentEntering():
            print('Enter students details for the following:')
            IDNumber = int(input('Enter student ID number: '))
            Surname = input('Enter student surname: ')
            Forename = input('Enter student forename / first name: ')
            DateofBirth = input('Enter student\'s dat of birth: ')
            Homeaddress = input('Enter student home address: ')
            homephonenumber = input('Enter student home phone number: ')
            gender = input('Enter student gender: ')
            tutorgroup = input('Enter student\'s tutor group : ')
            emailaddress = input('Enter student email address: ')
            new_student = [IDNumber, Surname, Forename, DateofBirth, Homeaddress, homephonenumber, gender, tutorgroup,
                           emailaddress]
            client.append_row(new_student)
            answer = input(print('Do you want to go back to menu(Y/N): '))
            if answer == "Y" or answer == "y":
                menu()
            else:
                print(
                    'We\'ll assume you want to enter more data of a different student so you\'ll be redirected shortly.')
                StudentEntering()

        StudentEntering()
        menu_option1 = int(input('Do you want to go back to menu(Y/N)?'))
        if menu_option1 == 'Yes' or menu_option1 == 'Y':
            menu()
        else:
            StudentEntering()

    elif option == 2:
        def StudentDetailSearch():
            student_id = input('Enter student ID: ')
            cell = sheet.find(student_id)
            values_list = sheet.row_values(cell.row)
            print(values_list)

        StudentDetailSearch()
        menu_option2 = input('Do you want to go back to menu(Y/N)?')
        if menu_option2 == 'Yes' or menu_option2 == 'Y':
            menu()
        else:
            StudentDetailSearch()

    elif option == 3:
        def Upload_reports():
            print("""You have the option of 3 reports:
                      1. Behaviour report - Used to track student behaviour.
                      2. Attendance report - Used to track student attendance.
                      3. Grade report - used ro track student's grades.""")
            menu_option3 = input('Do you want to go back to menu(Y/N)?')
            if menu_option3 == 'Yes' or menu_option3 == 'Y':
                menu()
            else:
                Upload_reports()

        Upload_reports()

    elif option == 4:
        def Log_Out():
            menu_option4 = input(print('Do you want to logout(Y/N)?'))
            if menu_option4 == 'No' or menu_option4 == 'N':
                exit()
            else:
                menu()

        Log_Out()

    else:
        print('Invalid input.')
        menu()

menu()
