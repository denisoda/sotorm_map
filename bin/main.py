import json
import parse
import webbrowser
import os

# json_loc
json_loc = "data/json/loc.json"

arr=[]


def parser(year):
 for i in range(parse.size_csv(year)):
    arr.append(({i:(parse.csv_parse(year)[1][i],  parse.csv_parse(year)[2][i])}))
    update_progress(i+1, parse.size_csv(year))

def update_progress(progress,size):
    print ('\r[{0} of {1}]  element parsed'.format(progress, size))

def write_JSON():
    with open('json.js', 'w') as f:
        f.write("var data = '" + json.dumps(arr) + "'")


def main():
    inp = int(input("Enter year of storm location: "))
    if (inp >= 1960 and inp <=2017):
        parser(inp)
        write_JSON()
        webbrowser.open('file:///'+os.getcwd()+'/' + 'index.html')
    else: print("Available only data from 1960 to 2017 "), main()


arr = []


with open('json.js', 'w') as f:
    f.write("var data = '" + json.dumps(arr) + "'")


main()







