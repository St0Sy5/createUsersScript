#!/usr/bin/python
import mysql.connector
from intercom.client import Client

#Set variables for MySQL connections and Intercom API accesses
hostname = 'localhost'
username = 'USERNAME'
password = 'PASSWORD'
database = 'DATABASE'

#Open intercom API and connection to MySQL database
intercom = Client(personal_access_token='my_access_token')
scriptConnection = mysql.connector.connect(host=hostname, user=username, passwd=password, db=database)
cur = scriptConnection.cursor()

#Pull all users from the user table
cur.execute("SELECT * FROM user")

#Generate users from data pulled from database
for row in cur:
    intercom.users.create(user_id=str(row[0]), email=row[2], name=row[1])

#Close database connection once all users are created
scriptConnection.close()
