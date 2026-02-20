#task 1: The Database Architect

import pandas as pd

import sqlite3

conn = sqlite3.connect("C:/Users/dell/Desktop/database/internship.db")

df = pd.read_sql_query("SELECT name, track FROM interns", conn)
print(df)