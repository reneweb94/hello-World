import os
import platform

def main():
  user = os.getlogin()
  machine = platform.node()
  print("*** {0} running on {1} ***".format(user, machine))
  print("1) script to install venv on the first time.")
  print("2) Activate venv and run testcase from command line")
  print("-python pymint.py %FullName% --count=%count%")
  print("upload logs to respository")
  
if __name__ == "__main__":
  main()
