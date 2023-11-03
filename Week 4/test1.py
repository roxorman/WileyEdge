from flask import Flask, render_template, request, redirect, url_for
import mysql.connector

def connectToDatabase(user, password, host, database):
    mydb = mysql.connector.connect(
        user=user,
        password=password,
        host=host,
        database=database
    )
    return mydb

mydb = connectToDatabase("root", "Stelladog97!", "localhost", "wileydataanalysis")
mycursor = mydb.cursor()  
create_query = "CREATE TABLE IF NOT EXISTS test1 (id INT AUTO_INCREMENT PRIMARY KEY, name VARCHAR(255), email VARCHAR(255))"
mycursor.execute(create_query)
insert_query = "INSERT INTO test1 (name, age) VALUES (%s, %s)"
name = "John"
age = 36
val = (name, age)
mycursor.execute(insert_query, val)
mydb.commit()
search_query = "SELECT * FROM test1 where name = John"