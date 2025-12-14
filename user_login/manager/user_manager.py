from model.user import User

#This class manages the user objects and performs certain operations to manage the database
class UserManager():
    def __init__(self):
        self.users = {} #Stores userdata()during the runtime of application
        self.authenticatedUser = []
        self.userauthdata = {}

    # Login function, enables the user to access the meta-data of the respective application
    def login(self, username, password):
        if username in self.userauthdata.keys():
            if password == self.userauthdata[username]:
                self.authenticatedUser.append(username)
                return ["Login successful.", 1]
            return ["Invalid password!", 0]
        return [f"User [{username}] not found!", 0]

    # Register function, enables the user to register themselves (create an account) in the application's database
    def register(self, Username, Password):
        if Username in self.userauthdata.keys():
            return [f"User [{Username}] already exists!", 0]
        else:
            newUser = User(Username, Password)
            self.users.update({newUser.userID: newUser})
            return ["User successfully registered!", 1]
    
    # Takes raw data as the input, builds user objects so that UserManager class can perform it's business functions
    def importData(self, rawdata):
        try:
            for k, v in rawdata.items():
                newUser = User(userID=k, username=v["Username"], password=v["Password"], metadata=v["Metadata"])
                self.users.update({k:newUser})
            return ["User-data imported successfully!", 1]
        except Exception as e:
            return [f"{e}", 0]

    # Takes the data created/modified during the business functions and converts into locally storable data, to pass on to the storage class to store.
    def exportData(self):
        try:
            rawdata = {}
            for userID in self.users.keys():
                for k, v in self.users[userID].userdict().items():
                    rawdata.update({k:v})
            return [rawdata, 1, "User-class data exported successfully"]
        except Exception as e:
            return [f"Could not export data.\n{e}", 0]
    
    #Seperates and collects only the data required for login/registeration functions
    def authdata(self):
        try:
            for k, v in self.users.items():
                for key, value in v.userdict().items():
                    self.userauthdata.update({value["Username"] : value["Password"]})
            return ["Completed authentication data loading.", 1]
        except Exception as e:
            return [e, 0]