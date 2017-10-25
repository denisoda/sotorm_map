import json
import parse


# json_loc
json_loc = "data/json/loc.json"

inp = int(input("Input year(1996 - 2017 :"))

arr = []


#the literal in the loop will be changing after parse algorithm fix
for i in range(10):
    arr.append(({i:(parse.csv_parse_row(inp)[1][i], parse.csv_parse_row(inp)[2][i])}))

print("Parsing is finished open index.html for illustrating data")

with open('json.js', 'w') as f:
    f.write("var data = '" + json.dumps(arr) + "'")









