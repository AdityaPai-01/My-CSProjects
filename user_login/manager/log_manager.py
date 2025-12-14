from pathlib import Path
import datetime

class LogManager():
    def __init__(self, baseDir):
        self.datapath = Path(f"{baseDir}/logdata.txt")
        self.datapath.parent.mkdir(parents=True, exist_ok=True)

    def writer(self, data):
        try:
            with open(self.datapath, "a", encoding="utf-8") as datapath:
                datapath.write(f"{datetime.datetime.now()}:: {data}\n") 
        except Exception as e:
            with open(self.datapath, "a", encoding="utf-8") as dataPath:
                dataPath.write(f"{datetime.datetime.now()}:: 0: Could not log data. Error: {e}\n")