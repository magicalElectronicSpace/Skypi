import subprocess
from pathlib import Path
import json

class Skypi:
    def __init__(self):
        self.data = {}
        with open(Path(__file__).parent / "data.json", "r") as f:
            self.data = json.load(f)

        if self.data["set_up"] == False:
            self.data = {"username": input("Enter what your log name will be: "), "set_up": True}
            with open(Path(__file__).parent / "data.json", "w") as f:
                json.dump(self.data, f)

    def log(self):
        subprocess.run(["ssh", "skypi@skypi.club", f"echo \"\n{self.data["username"]}: {input("Enter the log to write: ")}\" >> logs.txt"])


    def logWithoutNameTag(self):
        subprocess.run(["ssh", "skypi@skypi.club", f"echo \n{input("Enter the log to write: ")} >> logs.txt"])


    def run(self):
        print("Skypi")
        print("1: Log")
        print("2: Log (without name tag)")
        print("q, e, exit, quit: exit")

        userInput = "optimum"

        while userInput not in ["q", "e", "exit", "quit"]:
            userInput = input("Enter your choice: ")
            match userInput:
                case "1":
                    self.log()
                case "2":
                    self.logWithoutNameTag()