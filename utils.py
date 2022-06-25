import smtplib
from email.message import EmailMessage as EM
import datetime as dt
import re
import sqlite3 as sq 
import time

#---------------------room validator------------------------------------------------
def room_validator(room_number):
    
    try:
        if (int(room_number) >= 1) and (int(room_number) <= 5):
            x=1
        else:
            x=0
    except:
        x=0
    return x
#---------------------time validator--------------------------------------------------
def time_validator(user_input_2):
    if len(user_input_2) == 10 and user_input_2[4] == '-' and user_input_2[7] == '-' and int(user_input_2[-2:])<=31 and int(user_input_2[5:7])<=12:
        initial_check = 1
    else:
        initial_check = 0
    ct = dt.datetime.now().timetuple()
    if initial_check == 1 and int(user_input_2[0:4]) >= ct[0]:
        if int(user_input_2[5]) == 0:
            if int(user_input_2[6]) >= ct[1]:
                if int(user_input_2[8]) == 0:
                    if int(user_input_2[9]) > ct[2]:
                        x = 1
                    else:
                        x = 0
                else:
                    if int(user_input_2[8:10]) > ct[2]:
                        x = 1
                    else:
                        x = 0
            else:
                x=0
        else:
            if int(user_input_2[5:7]) >= ct[1]:
                if int(user_input_2[8]) == 0:
                    if int(user_input_2[9]) > ct[2]:
                        x=1
                    else:
                        x=0
                else:
                    if int(user_input_2[8:10]) > ct[2]:
                        x = 1
                    else:
                        x = 0
        
            else:
                x=0
    else:
        x=0
    return x

#----------------------Time Slots validator---------------------------------------------    

def time_slots_validator(in1):
    
    if in1 == '1ts' or in1 == '2ts' or in1 == '3ts' or in1 == '4ts':
        x = 1
    else:
        x = 0
    return x

#---------------------------User Name Validator------------------------------------------


def UserNameValidator(username):
    
    if re.match("^[a-zA-Z0-9_.-]+$", username):
        x = 1

    else:
        x = 0
    return x


#---------------------------User Email Validator------------------------------------------


def UserEmailValidator(email):
    regex = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'
    if(re.fullmatch(regex, email)):
        x=1

    else:
        x=0
    return x

#----------------------------------database part-------------------------------------------


def create_table():
    connection = sq.connect('data.db')
    cur = connection.cursor()

    cur.execute('''CREATE TABLE IF NOT EXISTS bookings
               (room_number INTEGER, date TIMESTAMP, time_slot TEXT, state integer, username TEXT, Email TEXT )''')

    connection.commit()
    connection.close()


create_table()

def insert_into_table(room_number, date, time_slot, state, username, Email):
    connection = sq.connect('data.db')
    cur = connection.cursor()

    cur.execute(
        f"INSERT INTO bookings VALUES ('{room_number}', '{date}', '{time_slot}', '{state}', '{username}', '{Email}')")

    connection.commit()
    connection.close()


def list_all():
    con = sq.connect('data.db')
    cur = con.cursor()
    for row in cur.execute('SELECT * FROM bookings'):
        print(row)
    con.commit()
    con.close()


def checking(rn,d,ts):
    con = sq.connect('data.db')
    cur = con.cursor()
    row = cur.execute(
        f"SELECT * FROM (SELECT * FROM (SELECT * FROM bookings where room_number=='{rn}') where date=='{d}') where time_slot =='{ts}' ").fetchall()
    con.commit()
    con.close()
    if len(row)==0:
        x=1
        #print('The room you chose is available for booking!')
    else:
        if row[0][3] == 1:
            x=0 #print('The room you chose for the date and time is already booked')  
        else:
            x=1 # print('The room you chose is available for booking!')
    return x


def mailto(row):

    email_to = row[5]

    email_from = "cons_app_add@mail.ru"

    password3 = "Q4QqqAm9eegEtTpJ9oBf"

   
    if row[2] == '1ts':
        hs='9:00-11:00'
    elif row[2] == '2ts':
        hs = '11:00-13:00'
    elif row[2] == '3ts':
        hs = '14:00-16:00'
    elif row[2] == '4ts':
        hs = '16:00-18:00' 


    xabar = f"""\
    
    Dear {row[4]},

    You have successfully booked  #{row[0]} room for {row[1]} and {hs}. 

    Thanks for using the console app."""

    msg = EM()
    msg.set_content(xabar)
                    
    msg['Subject'] = 'A notification from a console app'
    msg['From'] = email_from
    msg['To'] = email_to

    server = smtplib.SMTP("smtp.mail.yahoo.com", 587)

    server.starttls()

    server.login(email_from, password3)

    server.send_message(msg)

    server.quit()


#-------------------------------------------------------------------------------------------
def wait():
    time.sleep(1)
