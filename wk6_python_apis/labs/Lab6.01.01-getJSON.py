from xlwt import *
import requests
import json

url="http://127.0.01:5000/cars"

response = requests.get(url)
data = response.json()

#output to console
print(data)

#output cars individually 
for car in data["cars"]:
    print(car)

#other code
#save this to a file
filename = 'cars.json'

if filename:
    #writing JSON data
    with open(filename, 'w') as f:
        json.dump(data, f, indent=4)


# write to excel file
w = Workbook()
ws = w.add_sheet('cars', cell_overwrite_ok=True)
row = 0
ws.write(row, 0, "make")
ws.write(row, 1, "model")
ws.write(row, 2, "price")
ws.write(row, 3, "reg")
row +=1


for car in data["cars"]:
        ws.write(row, 0, car["make"])
        ws.write(row, 1, car["model"])
        ws.write(row, 2, car["price"])
        ws.write(row, 3, car["reg"])
        row +=1

w.save('cars.xls')