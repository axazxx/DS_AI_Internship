#task 1

with open("Daily Logs", 'a') as file:
    log = input("Enter your name and Daily goal:")
    file.write("\n" +log)
        
with open("Daily Logs", "r") as file:
    content=file.read()
    print(content)
    
#task 2

import csv

with open("student.csv", "r") as file:
    reader = csv.reader(file)
    for row in reader:
         if row[2]=="Pass":
             print(row)
             
#task 3

file = input("Enter file:")
try:
    with open(file) as f:
        r = f.read()
        print(r)
except:
    print("Oops! That file doesn't exist yet")
