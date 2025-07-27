
#Creates and populates a SQLite database with online food dellivery data from csv file
#Import csv
#import sqlite3
import csv
import sqlite3
print("Hola liz")
#creates a connection to a sqlite file called"onlinefood.db" in the "data" directory
connection = sqlite3.connect("data/onlinefood.db")
#Create a cursor
cursor = connection.cursor()
#create the table named "onlinefood.db with 12 colummns includind demographics(age,geneder,marital status,),economic data(occupation,income),and location information(lantitude,longitude,pin code)
cursor.execute("CREATE TABLE IF NOT EXISTS onlinefood (age Real, Gender TEXT, Marital Status TEXT, Occupation TEXT, Monthly Income TEXT, Educational Qualifications TEXT, Family size REAL, latitude REAL, longitude REAL, Pin code REAL, Output TEXT, Feedback TEXT)")
#open and reads a csv file called onlinefoods.csv fron the data directory.
#process the file row by row:
#Skips the header row and prints the column names
#For each data row,extracts all 12 fields
#prints each row´s datain a formatted way to the console
#instert each row into the SQLite database unsing iNSERT statement
with open ('data/onlinefoods.csv', 'r') as csv_file:
    csv_reader = csv.reader(csv_file,delimiter = ',')
    line_count = 0
    for row in csv_reader:
        if line_count== 0:
            print(f' Column names are {", ".join(row)}')
            line_count += 1
        else:
             age = row[0]
             Gender = row[1]
             Marital_Status = row[2]
             Occupation = row[3]
             Monthly_Income = row[4]
             Educational_Qualifications = row[5]
             Family_size = row[6]
             latitude = row[7]
             longitude = row[8]
             Pin_code = row[9]
             Output = row[10]
             Feedback = row[11]

             print(f'Age: {age} \t Gender: {Gender} \t Marital_Status: {Marital_Status} \t Occupation: {Occupation} \t Monthly_Income: {Monthly_Income} \t Educational_Qualifications: {Educational_Qualifications}\t Family_size: {Family_size} \t latitude: {latitude}\t longitude: {longitude}\t Pin_code: {Pin_code}\t Output: {Output}\t Feedback: {Feedback}')

              # TO-DO: Don't add data if its a duplicate
             cursor.execute(f"INSERT INTO onlinefood VALUES ('{age}', '{Gender}', '{Marital_Status}', '{Occupation}', '{Monthly_Income}', '{Educational_Qualifications}', '{Family_size}', '{latitude}', '{longitude}', '{Pin_code}', '{Output}', '{Feedback}')")

             connection.commit()
             line_count += 1
    print(f'Processed {line_count} lines.')
    print("query the database and print on the screen")
rows = cursor.execute("SELECT age, Gender, Marital Status,  Occupation, Monthly Income, Educational Qualifications, Family size, latitude, longitude, Pin code, Output, Feedback FROM onlinefood").fetchall()
print(rows)
#loop through databse and print the data nicely
#lets do some analytics: count how many birds we have? 
connection.close()