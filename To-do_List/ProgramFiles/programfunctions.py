#Python OOP ToDoList application
import random, json, csv, time
from pathlib import Path

AuthenticatedUser = []
CurrentList = []
RegisteredUsers = {}
UDBFilePath = Path(f"{Path.cwd()}/AppData/ApplicationData/regusers.json")
KeepLogin = Path(f"{Path.cwd()}/AppData/ApplicationData/keeplogin.json")
AllRegisteredTasks = {}

if not UDBFilePath.exists():
    UDBFilePath.touch()
    with open(file=UDBFilePath, mode='w') as UDataFile:
            json.dump({}, UDataFile, indent=4)
else:
    with open(file=UDBFilePath, mode='r') as Udata:
            RegisteredUsers = json.load(Udata)

#This is a task blueprint, which describes the basic properties of the task object
class Task():
    def __init__(self, TITLE, DESCRIPTION="", STATUS="Pending", ADDRESS="", ID=""):
        self.title = TITLE
        self.description = DESCRIPTION
        self.status = STATUS
        self.address = ADDRESS
        self.id = ID
        AllRegisteredTasks.update({self.id: [self.title, self.status, self.description, self.address]})

    def __str__(self):
        return f'[{self.status}] {self.title}'


#To-do List class creates different forms of to-do's. Holds multiple task objects   
class ToDoList():
    global AllRegisteredTasks 
    UserTDL = {}
    def __init__(self, NAME):
        self.name = NAME
        self.TaskList = []
        try:
            allTDL = Path(f"{Path.cwd()}/AppData/{AuthenticatedUser[0]}/alltdl.json")
            with open(allTDL, 'r') as tdlFile:
                ToDoList.UserTDL = json.load(tdlFile)

            for key, value in ToDoList.UserTDL.items():
                if self.name == key:
                    for task in value:
                        if task in AllRegisteredTasks.keys():
                            self.TaskList.append(task)
                
            ToDoList.UserTDL.update({self.name: self.TaskList})
            with open(allTDL, 'w') as tdlData:
                json.dump(ToDoList.UserTDL, tdlData, indent=4)

        except Exception as e:
            print(f"Error: {e}")
            ToDoList.UserTDL.update({self.name : self.TaskList})            

    def addTask(self, TASK):
        if TASK.id in AllRegisteredTasks:
            self.TaskList.append(TASK.id)
            ToDoList.UserTDL.update({self.name: self.TaskList})
            return 'Task was added!'
        else:
            return "Task could not be added"

    def removeTask(self, TITLE):
        for taskid in AllRegisteredTasks.keys():
            if AllRegisteredTasks[taskid][0] == TITLE and AllRegisteredTasks[taskid][3] == self.name:
                AllRegisteredTasks.pop(taskid)
                self.TaskList.remove(taskid)
                ToDoList.UserTDL.update({self.name: self.TaskList})
                return "Task was removed!"
        else:
            return f"'{TITLE}' Task does not exist in the list."

    def editTask(self, TITLE):
        for taskID in AllRegisteredTasks.keys():
            if AllRegisteredTasks[taskID][0] == TITLE and AllRegisteredTasks[taskID][3] == self.name:
                print("What would you like to edit?")
                print("Enter T: Title\nEnter D: Description\n")
                choice = input("Enter your choice >>>: ").capitalize()
                if choice == 'T':
                    newtitle = input("Enter new task title: ")
                    AllRegisteredTasks[taskID][0] = newtitle
                    print("Task title updated!")
                elif choice == 'D':
                    newdescrip = input("Enter new task description >>>: ")
                    AllRegisteredTasks[taskID][2] = newdescrip
                    print("Task description updated!")
                else:
                    print("Invalid command.")
                break
        else:
            print("Task not in the list")

    def showTasks(self, callOut):
        def AllTasks():
            if len(self.TaskList) == 0:
                print("No pending tasks! \n")
            else:
                print("Your tasks:")
                for i, taskid in enumerate(self.TaskList, start=1):
                    print(f"{i}. {AllRegisteredTasks[taskid][0]}")
                print()

        def SpecificTaskDetails(tasktitle):
            print()
            for taskID in AllRegisteredTasks.keys():
                if AllRegisteredTasks[taskID][0] == tasktitle and AllRegisteredTasks[taskID][3] == self.name:
                    print("-"*50)
                    print(f"Title: {AllRegisteredTasks[taskID][0]}")
                    print(f"ID: {taskID}")
                    print(f"Status: {AllRegisteredTasks[taskID][1]}")
                    print(f"\nDescription: {AllRegisteredTasks[taskID][2]}\n")
                    print(f"Address: {AllRegisteredTasks[taskID][3]}")
                    print("-"*50)
                    break
            else:
                print("Task not found")

        if callOut == '--sa':
            return AllTasks()
        elif callOut == '--sd':
            tasktitle = input("Select Task >>>: ")
            return SpecificTaskDetails(tasktitle=tasktitle)

#This is the main loginMethod function, made up of multiple nested functions.       
def loginMethod():
    global AllRegisteredTasks
    global AuthenticatedUser

    #Basic sign-in function, which lets the user to sign-in to the app, and use its respective Data.
    #Checks whether username exists in the DB or not, then checks whether the password is correct or not.
    def singin():
        while True:
            username = input("Enter your username >>>  ")
            if username == '--q':
                break
            if username not in RegisteredUsers:
                print("User not found!\n")
                continue
            else:
                password = input("Enter your password >>> ")
                if RegisteredUsers[username] != password:
                    print("Invalid password\n")
                    continue
                else:
                    loginInfo = input("Would you like to save login info?(Y/N): ").capitalize()
                    if loginInfo == 'Y':
                        with open(KeepLogin, "w") as loginData:
                            json.dump({username: password}, loginData)
                    AuthenticatedUser.append(username)
                    return 1
        return 0
    
    #Basic registeration function, which helps user to register into the database of the application
    #If the username is unique, registers your details in the DB
    def register():
        while True:
            username = input("Enter your username >>> ")
            if username in RegisteredUsers.keys():
                print("Username already exists!\n")
                continue
            password = input("Enter your password >>> ")
            break
        RegisteredUsers.update({username: password})
        print("You have successfully registered!")
        print("Please make sure to login to access the app.\n")

    #AccessDB function is accessed when the user successfully signs in the application
    #If it is the first time user is signing in, it creates a set of files, acting as database.
    #These set of files are used to make, access and manage multiple todolists used by the user.
    def AccessDB():
        global AllRegisteredTasks
        global AuthenticatedUser
        #These are the two file Paths where the user's datafiles will be created, stored and managed.
        dbDir = Path(f"{Path.cwd()}/AppData/{AuthenticatedUser[0]}")
        DefaultL_Path = Path(f"{Path.cwd()}/AppData/{AuthenticatedUser[0]}/defaultList.csv")
        dfPath = Path(f"{dbDir}/allregtasks.json")
        dListMap = Path(f"{dbDir}/alltdl.json")
        dbDir.mkdir(parents=True, exist_ok=True)
        if not dfPath.exists():
            with open(file=dfPath, mode='w') as dbFile:
                json.dump({}, dbFile, indent=4)
        else:
            with open(file=dfPath, mode='r') as db_File:
                AllRegisteredTasks = json.load(db_File)

        if not dListMap.exists():
            with open(file=dListMap, mode='w') as dbListFile:
                json.dump({}, dbListFile, indent=4)
        else:
            with open(file=dListMap, mode='r') as dblistFile:
                ToDoList.UserTDL = json.load(dblistFile)
        
        if not DefaultL_Path.exists():
            DefaultL_Path.touch()
            with open(file=DefaultL_Path, mode='w') as dldFile:
                writer = csv.writer(dldFile)
                writer.writerow(["My Tasks"])
            CurrentList.append("My Tasks")
        else:
            with open(file=DefaultL_Path, mode='r') as dldFile:
                reader = csv.reader(dldFile)
                for row in reader:
                    if row:
                        CurrentList.append(row[0])
    
    if not KeepLogin.exists():
        KeepLogin.touch()
        with open(KeepLogin, "w") as loginInfoFile:
            json.dump({}, loginInfoFile)
    else:
        with open(KeepLogin, "r") as loginInfo:
            userData = json.load(loginInfo)
            for k, v in userData.items():
                AuthenticatedUser.append(k)

    if not AuthenticatedUser:
        while True:
            Option = input("Login or register?(L/R) >>> ").upper()
            if Option == '--Q':
                break
            elif Option == 'L':
                singinMethod = singin()
                if singinMethod == 1:
                    AccessDB()
                    print("-"*50)
                    print("You have successfully logged in!")
                    print("-"*50)
                    return 1
                if singinMethod == 0:
                    continue
            elif Option == 'R':
                register()
                with open(file=UDBFilePath, mode='w') as dataFile:
                    json.dump(RegisteredUsers, dataFile, indent=4)
        return 0
    else:
        AccessDB()
        return 1

def SaveData():
    DB_Dir = Path(f"{Path.cwd()}/AppData/{AuthenticatedUser[0]}")
    TDL_TaskFP = Path(f"{DB_Dir}/allregtasks.json")
    TDL_ListDB = Path(f"{DB_Dir}/alltdl.json")
    try:
        with open(TDL_TaskFP, "w") as TaskFile:
            json.dump(AllRegisteredTasks, TaskFile, indent=4)
        with open(TDL_ListDB, "w") as TDL_Data:
            json.dump(ToDoList.UserTDL, TDL_Data, indent=4)
    except Exception as e:
        print(f"Application didn't close properly.\nError: {e}")

def AdvancedFunctions():
    pass