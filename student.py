from tkinter import *
# import tkinter as tk
import psycopg2


def get_data(name, age, address):
    conn = psycopg2.connect(dbname='studentdb', user='postgres', password='Qwerty+1', host='localhost', port='5432')
    cur = conn.cursor()
    query = '''INSERT INTO student (name, age, address) VALUES (%s, %s, %s);'''
    cur.execute(query, (name, age, address))
    print('data inserted!')
    # data will be updated in realtime
    display_all()
    conn.commit()
    conn.close()


def search(id):
    conn = psycopg2.connect(dbname='studentdb', user='postgres', password='Qwerty+1', host='localhost', port='5432')
    cur = conn.cursor()
    query = '''SELECT * FROM student WHERE id=%s'''
    cur.execute(query, (id))
    row = cur.fetchone()
    display_search(row)
    conn.commit()
    conn.close()


# display's results of search
def display_search(row):
    listbox = Listbox(frame, width=40, height=1)
    listbox.grid(row=9, column=1)
    listbox.insert(END, row)


def display_all():
    conn = psycopg2.connect(dbname='studentdb', user='postgres', password='Qwerty+1', host='localhost', port='5432')
    cur = conn.cursor()
    query = '''SELECT * FROM student'''
    cur.execute(query)
    row = cur.fetchall()

    listbox = Listbox(frame, width=40, height=5)
    listbox.grid(row=10, column=1)
    for x in row:
        listbox.insert(END, x)

    conn.commit()
    conn.close()


# ---------------------GUI Window-------------------------
root = Tk()
root.title('Portal')
canvas = Canvas(root, height=480, width=900)
canvas.pack()

frame = Frame()
frame.place(relx=0.3, rely=0.1, relwidth=0.8, relheight=0.8)

label = Label(frame, text='Add Data')
label.grid(row=0, column=1)

# Name
label = Label(frame, text='Name')
label.grid(row=1, column=0)

entry_name = Entry(frame)
entry_name.grid(row=1, column=1)

# Age
label = Label(frame, text='Age')
label.grid(row=2, column=0)

entry_age = Entry(frame)
entry_age.grid(row=2, column=1)

# Address
label = Label(frame, text='Address')
label.grid(row=3, column=0)

entry_address = Entry(frame)
entry_address.grid(row=3, column=1)

# the lambda function is used to execute code at runtime
button = Button(frame, text='Submit', fg='White', bg='Blue',
                command=lambda: get_data(entry_name.get(), entry_age.get(), entry_address.get()))
button.grid(row=4, column=1)

# search field
label = Label(frame, text='Search Data')
label.grid(row=5, column=1)

label = Label(frame, text='Search by ID')
label.grid(row=6, column=0)

id_search = Entry(frame)
id_search.grid(row=6, column=1)

button = Button(frame, text='Search', fg='White', bg='Blue', command=lambda: search(id_search.get()))
button.grid(row=6, column=2)

display_all()

root.mainloop()
