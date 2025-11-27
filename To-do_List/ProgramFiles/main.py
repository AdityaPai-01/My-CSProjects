from programfunctions import *
import os

def clear():
    if os.name == 'nt':
        os.system('cls')
    else:
        os.system("clear")
print("Welcome to PyTasks! We help you manage and simplify your day with very limitred distractions!")
print("Please make sure to go through the command library to seamlessly use the app!")
print("-"*100)

ApplicationRunning = False
INIT_Login = loginMethod()
if INIT_Login == 1:
    ApplicationRunning = True
else:
    pass

def initialize(listarg):
    workingList = ToDoList(listarg)


def refresh():
    print(f"CurrentList: {workingList.name}")
    print("-"*100)
    workingList.showTasks("--sa")
    
clear()
while ApplicationRunning:
    print(f"Greetings {AuthenticatedUser[0]}!")
    workingList = ToDoList(CurrentList[0])
    initialize(listarg=workingList.name)
    while True:
        refresh()
        F_Input = input("Enter function command >>>: ")
        if F_Input == '--at':
            while True:
                a_taskName = input("Enter task-name: ")
                if a_taskName != '--q':
                    taskDescription = input("Enter task-description: ")
                    taskAddress = f"{workingList.name}"
                    taskID = f"{taskAddress}{random.randint(1000, 9999)}"
                    taskOBJ = Task(a_taskName, taskDescription, ID=taskID, ADDRESS=taskAddress)
                    print(workingList.addTask(taskOBJ), "\n")
                    SaveData()
                else:
                    SaveData()
                    clear()
                    break
        elif F_Input == '--rt':
            while True:
                r_taskname = input("Enter task to be removed: ")
                if r_taskname != '--q':
                    print(workingList.removeTask(r_taskname), "\n")
                    SaveData()
                else:
                    SaveData()
                    clear()
                    break
        elif F_Input == '--et':
            tasktoedit = input("Enter task to edit: ")
            workingList.editTask(tasktoedit)
            time.sleep(3)
            SaveData()
            clear()
        elif F_Input == '--sa':
            workingList.showTasks(F_Input)
        elif F_Input == '--sd':
            workingList.showTasks(F_Input)
            QuitFunc = input("Enter anything to quit:")
            SaveData()
            clear()
        elif F_Input == '--nl':
            ListName = input("Enter your list name: ")
            workingList = ToDoList(ListName)
            print(f"List: {ListName} was created!")
            time.sleep(2)
            SaveData()
            clear()
        elif F_Input == '--cl':
            print("Your To-do lists: ")
            count = 1
            for element in ToDoList.UserTDL.keys():
                print(count,".",element)
                count += 1
            while True:
                List = input("Select your list >>>: ")
                if List in ToDoList.UserTDL.keys():
                    workingList = ToDoList(List)
                    print(f"Current working list was set to: {List}. \n")
                    time.sleep(2)
                    SaveData()
                    clear()
                    initialize(List)
                    break
                elif List == '--q':
                    SaveData()
                    clear()
                    break
                else:
                    print(f"{List} not in your to-do lists. \n")
        elif F_Input == '--al':
            print("Your to-do lists: ")
            for k, v in ToDoList.UserTDL.items():
                count = 1
                print(count,". ",k)
                count += 1
            time.sleep(5)
            SaveData()
            clear()
            refresh()
        elif F_Input == '--q':
            break
        elif F_Input == '--wl':
            print(f"Current List: {workingList.name}")
        else:
            print(f"INVALID COMMAND: {F_Input} \n")
            time.sleep(2)
            clear()
    SaveData()
    break
clear()
print("You exited the program.")