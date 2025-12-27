from helpers import *
ApplicationRun = False

if __name__ == '__main__':
    initializeFunction = initialize()
    Log_Manager.writer(initializeFunction)
    if initializeFunction[0] == "1":
        ApplicationRun = True
    else:
        print(initializeFunction)
    Log_Manager.writer(Main(ApplicationRun))