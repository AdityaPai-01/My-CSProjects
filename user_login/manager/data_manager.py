from pathlib import Path
import json

class JSONStorage():
    def __init__(self, Base_Directory):
        self.dataPath = Path(f"{Base_Directory}/userdata.json")
        self.dataPath.parent.mkdir(parents=True, exist_ok=True)

    def load_data(self):
        try:
            if not self.dataPath.exists():
                self.dataPath.touch()
                self.dataPath.write_text("{}")
                return [{}, 1, "New userdata.json file created"]
            
            with open(self.dataPath, "r") as dataFile:
                return [json.load(dataFile), 1, "Data loaded for import."]
        except Exception as e:
            return [f"Data could not be loaded.\n{e}", 0, "Data did not load"]

    def save_data(self, rawData):
        try:
            if self.dataPath.exists():
                with open(self.dataPath, "w") as dataFile:
                    json.dump(rawData[0], dataFile, indent=4)
                return ["Recieved data successfully", 1, "Data loaded."]
        except Exception as e:
            return [e, 0]