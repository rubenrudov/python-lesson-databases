import sqlite3
# Our module for SQL functions

db_connection = sqlite3.connect('database_sql.db')
cursor = db_connection.cursor()

# Create table query

# cursor.execute('''CREATE TABLE users(Name text UNIQUE, Password text)''')   # Table creating query

# INSERT query

try:
    INSERT_QUERY = '''INSERT INTO users VALUES('Ruby_USER2', '12345678')'''
    cursor.execute(INSERT_QUERY)
    db_connection.commit()  # Committing the updates

except sqlite3.IntegrityError as unique_exception:
    print(f"{unique_exception}, User already exists")

# SELECT query
SELECT_QUERY = '''SELECT * FROM users'''
table_data = cursor.execute(SELECT_QUERY)

for row in table_data:
    print(row)


SELECT_SPEC = '''SELECT Name FROM users WHERE Name="Ruby_USER"'''
table_data = cursor.execute(SELECT_SPEC)

for row in table_data:
    print(row)

db_connection.close()
