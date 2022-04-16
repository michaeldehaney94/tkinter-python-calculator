import psycopg2

# establish database connection
conn = psycopg2.connect(dbname='studentdb', user='postgres', password='Qwerty+1', host='localhost', port='5432')
cur = conn.cursor()
print('connection successful!')


# create database table
def create():
    cur.execute('''CREATE TABLE student(id SERIAL, name VARCHAR, age INTEGER, address TEXT);''')
    print('table created!')
    conn.commit()
    conn.close()


# insert data in table
def insert_data():
    # submitting user input to database
    name = input('Enter name: ')
    age = input('Enter age: ')
    address = input('Enter address: ')
    query = '''INSERT INTO student (name, age, address) VALUES (%s, %s, %s);'''
    cur.execute(query, (name, age, address))
    print('data added to table!')
    conn.commit()
    conn.close()


insert_data()


