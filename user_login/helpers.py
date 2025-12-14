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
    
def Main(condition):
    Success = None
    while condition:
        Choice = input("Login or register?(L/R): ").upper()
        if Choice == "L":
            loginmethod = login()
            Log_Manager.writer(loginmethod + " HP100-110")
            if loginmethod[0] == "1":
                Success = 1
                break
        elif Choice == 'R':
            registermethod = regiser()
            if registermethod[0] == "1":
                print("Please login again.")
                Log_Manager.writer(registermethod + " HP100-110")
                time.sleep(3)
                SaveData = savedata()
                Log_Manager.writer(f"{SaveData} HP110-120")
                Log_Manager.writer(clear() + " HP110-120")
        elif Choice == '--Q':
            Success = -1
            break
        else:
            print("Invalid option")
            print()
    print("You exited the applications")
    Log_Manager.writer(f"{savedata()} HP120-130")
    print()
    if Success == 1:
        return "1: User logged in to the application"
    else:
        return "-1: User exited the application without login"