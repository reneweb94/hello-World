import argparse
import json
import os
import platform

def main():
  user = os.getlogin()
  machine = platform.node()
  print("*** {0} running on {1} ***".format(user, machine))
  parser = argparse.ArgumentParser(description='Process some integers.')
  parser.add_argument('-p', '--project', type=str, required=True, help='Specify a Project Name')
  parser.add_argument('-t', '--testplan', type=str, required=True, help='Specify a Test Plan')
  parser.add_argument('-l', '--loops', type=int, required=True, help='Specify number of loops')
  parser.add_argument('-f', '--filename', type=str, required=True, help='Specify output file Filename')
  args = parser.parse_args()
  print('Project: {0}, Testplan: {1}, Loops: {2}'.format(args.project, args.testplan, args.loops))
  print('Load Testplan/Testlist from test Management System')
  #bring it into a list of dictionaries 
  test_plan = [{'test': "Test-1", 'label': "kepler"},
               {'test': "Test-2", 'label': "eos"}]
  json_object = json.dumps(test_plan)
  print('Writing Test list to file: {0}'.format(args.filename))
  with open(args.filename, "w") as outfile:
    outfile.write(json_object)
    
if __name__ == "__main__":
  main()
