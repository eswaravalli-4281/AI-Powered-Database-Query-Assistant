import sqlite3

# Connect to SQLite database
connection = sqlite3.connect("student.db")

# Create a cursor object
cursor = connection.cursor()

# Create the STUDENT table
table_info = """
CREATE TABLE STUDENT(
    NAME VARCHAR(25),
    CLASS VARCHAR(25),
    SECTION VARCHAR(25),
    MARKS INT
);
"""

cursor.execute(table_info)

# Insert records
cursor.execute('''INSERT INTO STUDENT VALUES('Aarav','Artificial Intelligence','A',95)''')
cursor.execute('''INSERT INTO STUDENT VALUES('Priya','Data Analytics','B',88)''')
cursor.execute('''INSERT INTO STUDENT VALUES('Rahul','Cyber Security','A',91)''')
cursor.execute('''INSERT INTO STUDENT VALUES('Sneha','Machine Learning','C',97)''')
cursor.execute('''INSERT INTO STUDENT VALUES('Kiran','Cloud Computing','B',84)''')

# Display all records
print("The inserted records are:")

data = cursor.execute('''SELECT * FROM STUDENT''')

for row in data:
    print(row)

# Commit changes
connection.commit()

# Close connection
connection.close()
