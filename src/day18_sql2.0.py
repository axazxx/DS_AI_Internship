#task 1: The Insight Filter

import pandas as pd

import sqlite3

conn = sqlite3.connect("C:/Users/dell/Desktop/database/internship.db")

df = pd.read_sql_query("SELECT track, AVG(stipend) FROM interns GROUP BY track;", conn)

ef = pd.read_sql_query("SELECT track, COUNT(*) FROM interns GROUP BY track;", conn)
print("\nAVG Stipend Track wise\n",df)
print("\n")
print("\nNumber of interns in each Track\n",ef)

#task 2: The Data Connector

import pandas as pd

import sqlite3

conn = sqlite3.connect("C:/Users/dell/Desktop/database/internship.db")

af = pd.read_sql_query("SELECT interns.name,mentors.mentor_name FROM interns INNER JOIN mentors ON interns.track=mentors.track;", conn)
print(af)