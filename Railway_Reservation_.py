import pandas as pd
import mysql.connector as sql

conn = sql.connect(host='127.0.0.1', user='root', passwd='Vikash@123', database='railway_reservation_system')
if conn.is_connected():
    print('Successfully connected')

def menu():
    print()
    print('*****************************************************')
    print('Railway Management System')
    print('1. Create Table Passenger')
    print('2. Add new Passenger detail')
    print('3. Create Table Train detail')
    print('4. Add new in train detail')
    print('5. Show all from Train detail')
    print('6. Show all from Passenger Table')
    print('7. Show PNR number')
    print('8. Reservation of Ticket')
    print('9. Cancellation of Reservation')

menu()

# PNR is the abbreviation of Passenger Name Record

def create_passengers():
    c1=conn.cursor()
    c1.execute('create table if not exists Passengers(pname varchar(60),age varchar(30),trainno varchar(60),noof varchar(60),cls varchar(60),destination varchar(60), amt varchar(60), status varchar(60), pnrno varchar(60))')
    print('Passengers Table created')

def add_passengers():
    c1=conn.cursor()
    L=[]
    pname=input('Enter Name: ')
    L.append(pname)
    age=input('Enter Age: ')
    L.append(age)
    trainno=input('Enter Train Number: ')
    L.append(trainno)
    noof=input('Enter the number of Passengers: ')
    L.append(noof)
    cls=input('Enter Class: ')
    L.append(cls)
    destination=input('Enter the name of destination: ')
    L.append(destination)
    amt=input('Enter fare: ')
    L.append(amt)
    status=input('Enter status: ')
    L.append(status)
    pnrno=input('Enter PNR number: ')
    L.append(pnrno)
    pas=(L)
    sql='insert into Passengers(pname,age,traino,noof,cls,destination,amt,status,pnrno)values(%s,%s,%s,%s,%s,%s,%s,%s,%s)'
    c1.execute(sql,pas)
    conn.commit()
    print('Record of Passenger Inserted')
    df=pd.read_sql('select * from Passengers',conn)
    print(df)


def create_tarindetail():
    c1=conn.cursor()
    c1.execute('create table if not exists TrainDetail(tname varchar(60),tnum varchar(60),source varchar(60),destination varchar(60),fare varchar(60),ac1 varchar(60),ac2 varchar(60),slp varchar(60))')
    print('Trains Detail Table Created')

def add_traindetail():
    c1=conn.cursor()
    df=pd.read_sql('select * from TrainDetail',conn)
    print(df)
    L=[]
    tname=input('Enter the Train Name: ')
    L.append(tname)
    tnum=input('Enter Train Number: ')
    L.append(tnum)
    source=input('Enter Source of the Train: ')
    L.append(source)
    destination=input('Enter the Train destination: ')
    L.append(destination)
    fare=input('Enter the fare of station: ')
    L.append(fare)
    ac1=input('Enter the number of seats for AC1: ')
    L.append(ac1)
    ac2=input('Enter the number of seats for AC2: ')
    L.append(ac2)
    slp=input('Enter the number of seats for sleeper: ')
    L.append(slp)
    f=(L)
    sql='insert into TrainDetail(tname,tnum,source,destination,fare,ac1,ac2,slp)values(%s,%s,%s,%s,%s,%s,%s,%s)'
    c1.execute(sql,f)
    conn.commit()
    print('Record in in Trains Detail Table')


def showpassengers():
    print('All Passengers Detail')
    df=pd.read_sql('Select * from Passengers',conn)
    print(df)

def showtrainsdetail():
    print('All Trains Detail')
    df=pd.read_sql('Select * from TrainDetail',conn)
    print(df)

def disp_pnrno():

    print('PNR status window')
    a=(input('Enter Train No. : '))
    qry='Select pname,status from passengers where trainno=%s;'%(a,)
    df=pd.read_sql(qry,conn)
    print(df)



def ticketreservation():
    print('We have the following seat types for you: ')
    print('Tname is 1 for Goa Express from Delhi:-')
    print()
    print('1. First Class AC Rs 6000 per person')
    print('2. Second Class AC Rs 5000 per person')
    print('1. Third Class AC Rs 4000 per person')
    print('1. Sleeper Class Rs 3000 per person')
    print()
    print('Tname is 2 for Jammu Tawi Express from Delhi:-')
    print()
    print('1. First Class AC Rs 10000 per person')
    print('2. Second Class AC Rs 9000 per person')
    print('1. Third Class AC Rs 8000 per person')
    print('1. Sleeper Class Rs 7000 per person')

    tname=(input('Enter your choice of Train Name please->'))
    print(tname)
    x=int(input('Enter your choice of Ticket please->'))
    n=int(input('How many Tickets you need: '))

    if(x==1):
        print('You have choosen First Class AC Ticket ')
        s=6000*n
    elif(x==2):
        print('You have choosen Second Class AC Ticket ')
        s=5000*n
    elif(x==3):
        print('You have choosen Third Class AC Ticket ')
        s=4000*n
    elif(x==4):
        print('You have choosen Sleeper Class Ticket ')
        s=3000*n
    else:
        print('Invalid option')

        print('Please Choose a Train')
    print('Your total Ticket price is = ',s,'\n')

    if(x==2):
        print('You have choosen First Class AC Ticket ')
        s = 10000 * n
    elif (x == 2):
        print('You have choosen Second Class AC Ticket ')
        s = 9000 * n
    elif (x == 3):
        print('You have choosen Third Class AC Ticket ')
        s = 8000 * n
    elif (x == 4):
        print('You have choosen Sleeper Class Ticket ')
        s = 7000 * n
    else:
        print('Invalid option')

        print('Please Choose a Train')
    print('your total Ticket price is = ', s, '\n')

def cancel():

    print('Before any changes in Status ')
    df=pd.read_sql('Select * from Passengers',conn)
    print(df)
    mc=conn.cursor()
    mc.execute("Update Passengers set status ='Cancelled' where pnrno='G1001'")
    #conn.commit()
    df=pd.read_sql('Select * from Passengers', conn)
    print(df)


opt=''
opt=int(input('Enter your choice: '))
if opt==1:
    create_passengers()
elif opt==2:
    add_passengers()
elif opt==3:
    create_tarindetail()
elif opt==4:
    add_traindetail()
elif opt==5:
    showtrainsdetail()
elif opt==6:
    showpassengers()
elif opt==7:
    disp_pnrno()
elif opt==8:
    ticketreservation()
else:
    print('Invalid option')