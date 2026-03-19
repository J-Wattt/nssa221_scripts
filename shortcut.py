#Jacob Watson March 4th, 2026
#!/usr/bin/env python3
import os
import pathlib
import subprocess
import sys
def createSL():
    cwd = os.chmod()
    print("Enter a file name to turn into a symbolic link")
    filename = input("Enter file name: ")
    try:
        path = pathlib.Path(cwd,"/",filename)
        creation = subprocess.run(["sudo","ln", "-s" , path, "/student"], capture_output=True, text=True)
        print(creation)
    except FileNotFoundError:
        print("File enter doesn't exist")
    except Exception as e:
        print("An error has occured",e)

def deleteSL():
    print("Enter a file path to delete symbolic link from")
    filename = input("Enter file name: ")
    try:
        path = pathlib.Path("**/",os.path.abspath(filename))
        deletion = subprocess.run(["rm", path], capture_output=True, text=True)
        print(deletion)
    except FileNotFoundError:
        print("File enter doesn't exist")
    except Exception as e:
        print("An error has occured",e)

def sysreport():
    report = subprocess.run(["ls", "-la", "$HOME"], capture_output=True, text=True)
    print(report)

def main():
    print("Enter a number corresponding to what you want to do \n 1. Create Symbolic link \n 2. Delete Symbolic link \n 3. Report symbolic link \nEnter 0 to quit")
    while True:
        choice = int(input(""))
        try:
            if(choice == 1):
                createSL()
                break
            elif(choice == 2):
                deleteSL()
                break
            elif(choice == 3):
                sysreport()
                break
            elif(choice > 3):
                print("Choose a different number: ")
            elif(choice == 0):
                sys.exit("Exiting the program...")
        except Exception as e:
            print("Not a number", e)
    

main()
