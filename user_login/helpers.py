from pathlib import Path
import time
import os
import sys

from manager.user_manager import UserManager
from manager.data_manager import JSONStorage
from manager.log_manager import LogManager

if getattr(sys, 'frozen', False): #Running script as .exe
    BaseDirectory = Path(sys.executable).resolve().parent
else: #Running script as a script
    BaseDirectory = Path(__file__).resolve().parent
DataDir = BaseDirectory / "data"
DataDir.mkdir(parents=True, exist_ok=True)
User_Manager = UserManager()
JSON_Storage = JSONStorage(DataDir)
Log_Manager = LogManager(DataDir)

def clear():
    os.system('cls' if os.name == 'nt' else 'clear')
    return "1: clear terminal executed"

def initialize():
    LoadData = JSON_Storage.load_data()
    Log_Manager.writer(f"{LoadData[2]} HP20-30")
    importData = User_Manager.importData(LoadData[0])
    Log_Manager.writer(f"{importData[0]} HP 20-30")
    AuthData = User_Manager.authdata()
    Log_Manager.writer(f"{AuthData[0]} HP 20-30")
    if importData[1] == 1 and AuthData[1] == 1 and LoadData[1] == 1:
        return "1: Initialised user-manager class"
    else:
        return f"0: Initialisation failed.\nError-importdata: {importData[0] if importData[1] == 0 else None}\nError-authdata: {AuthData[0] if AuthData[1] == 0 else None}\nError-loaddata: {LoadData[2] if LoadData[1] == 0 else None}"
    
def login():
    Success = None
    while True:
        Username = input("Enter your username: ")
        if Username == '--q':
            Success = -1
            Log_Manager.writer(clear())
            break
        Password = input("Enter your password: ")
        AuthData = User_Manager.authdata()
        Log_Manager.writer(f"{AuthData[0]} HP 40-50")
        LoginMethod = User_Manager.login(Username, Password)
        Log_Manager.writer(LoginMethod[0] + " HP 40-50")
        print(LoginMethod[0])
        time.sleep(1)
        Log_Manager.writer(clear() + " HP 50-60")
        if LoginMethod[1] == 1:
            Success = 1
            break
    if Success == 1:  
        return "1: login-method executed successfully."
    else:
        return f"-1: login-method exited by user"  
    
def regiser():
    Success = None
    while True:
        Username = input("Enter username: ")
        if Username == '--q':
            Success = -1
            Log_Manager.writer(f"{clear()} HP60-70")
            break
        Password = input("Enter password: ")
        RegisterMethod = User_Manager.register(Username, Password)
        Log_Manager.writer(RegisterMethod[0] + " HP 70-80")
        print(RegisterMethod[0])
        time.sleep(3)
        Log_Manager.writer(f"{clear()} HP70-80")
        if RegisterMethod[1] == 1:
            Success = 1
            break
    if Success == 1:
        return "1: register-method executed successfully."
    else:
        return "-1: register-method exited by user."

def savedata():
    ManagerExport = User_Manager.exportData()
    Log_Manager.writer(ManagerExport[2] + " HP80-90")
    if ManagerExport[1] == 1:
        StoreData = JSON_Storage.save_data(ManagerExport)
        Log_Manager.writer(StoreData[0] + " HP80-90")
        return "1: data storage executed successfully."
    else:
        return f"0: data storage failed.\nError-managerexport: {ManagerExport[0] if ManagerExport[1] == 0 else None}\nError-storedata: {StoreData[0] if StoreData[1] == 0 else None}"
    
def delete_account():
    Success = None
    Log_Manager.writer(f"{User_Manager.authdata()} HP90-100")
    while True:
        Condition = False
        username = input("Enter your username: ")
        if username == "--q":
            Success = -1
            Log_Manager.writer(f"{clear()} HP100-110")
            break
        UserExistence = User_Manager.user_exist(username)
        Log_Manager.writer(UserExistence[0])
        if UserExistence[1] != 1:
            print(UserExistence[0])
            time.sleep(2)
            Log_Manager.writer(f"{clear()} HP100-110")
            continue
        password = input("Enter your password to confirm deletion: ")
        passwordValidation = User_Manager.password_validation(username=username, password=password)
        Log_Manager.writer(passwordValidation[0])
        if passwordValidation[1] != 1:
            print(passwordValidation[0])
            time.sleep(2)
            Log_Manager.writer(f"{clear()} HP-110-120")
            continue
        Condition = True
        deleteAccount = User_Manager.delete_account(Condition, username)
        Log_Manager.writer(deleteAccount[0])
        if deleteAccount[1] == 1:
            Success = 1
            print(deleteAccount[0])
            SaveData = savedata()
            Log_Manager.writer(f"{SaveData} HP120-130")
            time.sleep(2)
            Log_Manager.writer(f"{clear()} HP120-130")
            break
    if Success == 1:
        return "1: delete_account-method executed successfully"
    else:
        return "-1: delete-account-method exited by the user"
    
def change_username():
    Success = None
    Log_Manager.writer(f"{User_Manager.authdata()} HP130-140")
    while True:
        Condition = False
        username = input("Enter your username: ")
        if username == "--q":
            Success = -1
            Log_Manager.writer(f"{clear()} HP140-150")
            break
        UserExistence = User_Manager.user_exist(username)
        Log_Manager.writer(UserExistence[0])
        if UserExistence[1] != 1:
            print(UserExistence[0])
            time.sleep(2)
            Log_Manager.writer(f"{clear()} HP140-150")
            continue
        password = input("Enter your password to confirm: ")
        passwordValidation = User_Manager.password_validation(username=username, password=password)
        Log_Manager.writer(passwordValidation[0])
        if passwordValidation[1] != 1:
            print(passwordValidation[0])
            time.sleep(2)
            Log_Manager.writer(f"{clear()} HP-150-160")
            continue
        new_username = input("Enter your new username: ")
        username_existence = User_Manager.user_exist(new_username)
        Log_Manager.writer(username_existence[0])
        if username_existence[1] != 0:
            print("Username already exists, please decide a new and unique username!")
            time.sleep(2)
            Log_Manager.writer(f"{clear()} HP160-170")
            continue
        Condition = True
        change_Username = User_Manager.change_username(Condition, old_username=username, new_username=new_username)
        Log_Manager.writer(change_Username[0])
        if change_Username[1] == 1:
            Success = 1
            print(change_Username[0])
            SaveData = savedata()
            Log_Manager.writer(f"{SaveData} HP170-180")
            time.sleep(2)
            Log_Manager.writer(f"{clear()} HP170-180")
            break
    if Success == 1:
        return '1: change-username method executed successfully'
    else:
        return '-1: change-username method exited by the user'




def Main(condition):
    Success = None
    while condition:
        print("Welcome to Py-USER-Interface!")
        time.sleep(1)
        print("You have the following functions to perfom: ")
        time.sleep(1)
        print("-"*30)
        print("--l: login to your account")
        print("--r: Register account")
        print("--d: Delete your account")
        print("--c: Change account name")
        print("--q: exit current interface")
        print("-"*30)
        time.sleep(1)
        Choice = input("Enter function >>> ").lower()
        if Choice == "--l":
            loginmethod = login()
            Log_Manager.writer(loginmethod + " HP200-210")
            if loginmethod[0] == "1":
                Success = 1
                break
        elif Choice == '--r':
            registermethod = regiser()
            if registermethod[0] == "1":
                print("Please login again.")
                Log_Manager.writer(registermethod + " HP210-220")
                time.sleep(3)
                SaveData = savedata()
                Log_Manager.writer(f"{SaveData} HP210-220")
                Log_Manager.writer(clear() + " HP210-220")
        elif Choice == "--d":
            deleteAccount = delete_account()
            Log_Manager.writer(deleteAccount + " HP210-220")
        elif Choice == '--c':
            changeUsername = change_username()
            Log_Manager.writer(changeUsername + "HP220-230")
        elif Choice == '--q':
            Success = -1
            break
        else:
            print("Invalid option")
            print()
            time.sleep(2)
            Log_Manager.writer(f"{clear()} + HP220-230")
    print("You exited the application")
    Log_Manager.writer(f"{savedata()} HP230-240")
    time.sleep(3)
    print()
    if Success == 1:
        return "1: User logged in to the application"
    else:
        return "-1: User exited the application without login"