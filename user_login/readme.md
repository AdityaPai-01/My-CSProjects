User-login interface
- checks whether username is in database. If yes, checks whether password is correct or not.
- Allows user to add/register themselves in the database.
- logs each time a function as been performed.
- stores data locally in JSON-format database

Python Modules used:
- pathlib: for file management
- json: for reading and writing json files
- uuid: for generating random IDs for user objects
- time: for delaying certain functions to be performed
- datetime: used in logging, to know exactly at what time the function was performed
- os and sys: clearing terminal and for creating executable respectively

Models/Classes made:
- User: Creates user objects
- UserManager: Manages the user objects, performs to login, register, importing and exporting OOP data
- DataManager: Manages data to be stored and exported to the UserManager Class
- LogManager: Manages log data, takes in inputs from returns of functions and saves it in .txt format

FILE-STRUCTURE:
user_login
    helpers.py
    main.py 
    - data
        userdata.json
        logdata.json
    - manager
        user_manager.py
        data_manager.py
        log_manager.py
    - model
        user.py

NOTE FROM THE DEVELOPER:

I'm an early intermediate python developer. I've created this project to manage my code in a clean structured format. My earlier projects were not so 'well managed' as they were mainly contained in a few files (1 containing business logic and 1 integrating everything), and the elements/classes did not follow any clear boundaries and responsibilities. Hence, it was just a mess. I learned a lot logically how certain systems work. I'm still new to system design or architecture of programs, but with this specific project, I learned to keep things seperate, clear and define proper boundaries and responsibilities, get clear about OOP principles and basics and managed to create my first ever .exe program. Now currently, I'm looking forward for other, more complex python projects which can help me level up myself as a developer, get an idea of various fields as working on them, and improve my program management skills. 
