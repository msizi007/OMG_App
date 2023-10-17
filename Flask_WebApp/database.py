import sqlite3
from tabulate import tabulate
from customer import Customer
from service import Service
from service_type import ServiceType
from appointment import Appointment

connection = None
cursor = None

def initialise_database():
    global connection, cursor
    connection = sqlite3.connect("OMG_DB.db")
    cursor = connection.cursor()

    CREATE_CUSTOMER_TABLE_QUERY = """
    CREATE TABLE IF NOT EXISTS customer (
        customerID INTEGER PRIMARY KEY AUTOINCREMENT,
        customerFirstName TEXT NOT NULL,
        customerLastName TEXT NOT NULL,
        customerPhoneNumber TEXT NOT NULL,
        customerEmail TEXT NOT NULL,
        customerAddress TEXT NOT NULL  
    )"""

    CREATE_USER_TABLE_QUERY = """
    CREATE TABLE IF NOT EXISTS users (
        userID INTEGER PRIMARY KEY AUTOINCREMENT,
        username TEXT UNIQUE NOT NULL,
        password TEXT  NOT NULL
    )"""
    
    CREATE_SERVICE_TYPE_TABLE_QUERY = """
    CREATE TABLE IF NOT EXISTS serviceType(
        serviceTypeID INTEGER PRIMARY KEY AUTOINCREMENT,
        serviceTypeName TEXT NOT NULL
    )"""
    
    CREATE_SERVICE_TABLE_QUERY = """
    CREATE TABLE IF NOT EXISTS service(
        serviceID INTEGER PRIMARY KEY AUTOINCREMENT,
        serviceName TEXT NOT NULL,
        servicePrice TEXT NOT NULL,
        serviceDescription TEXT DEFAULT 'No description provided',
        serviceTypeID INTEGER,
        FOREIGN KEY(serviceTypeID) REFERENCES serviceType(serviceTypeID)
    )"""
    
    CREATE_APPOINTMENT_TABLE_QUERY = """
    CREATE TABLE IF NOT EXISTS appointment (
        appointmentID INTEGER PRIMARY KEY AUTOINCREMENT,
        appointmentDate DATE,
        appointmentTime TIME,
        appointmentStatus TEXT NOT NULL,
        customerID INTEGER,
        serviceNumber INTEGER,
        FOREIGN KEY (customerID) REFERENCES customer(customerID),
        FOREIGN KEY (serviceNumber) REFERENCES service(serviceNumber)
        )"""

    cursor.execute(CREATE_CUSTOMER_TABLE_QUERY)
    cursor.execute(CREATE_USER_TABLE_QUERY)
    cursor.execute(CREATE_SERVICE_TYPE_TABLE_QUERY)
    cursor.execute(CREATE_SERVICE_TABLE_QUERY)
    cursor.execute(CREATE_APPOINTMENT_TABLE_QUERY)
    connection.commit()

def AddCustomer(fname, lname, phoneNum, email, address):
    try:
        initialise_database()
        cursor.execute("""
            INSERT INTO customer (
                customerFirstName, customerLastName, customerPhoneNumber, customerEmail, customerAddress
            ) VALUES (?, ?, ?, ?, ?)
        """, (fname, lname, phoneNum, email, address))
        connection.commit()
        CloseDatabase()
    except Exception as e:
        print(e)
        raise e

def AddUser(username, password):
    try:
        initialise_database()
        cursor.execute("""
            INSERT INTO users (username, password) VALUES (?, ?)
        """, (username, password))
        connection.commit()
        CloseDatabase()
    except Exception as e:
        print(e)
        raise e

def Login(username, password):
    try:
        initialise_database()
        cursor.execute("""
            SELECT userID FROM users WHERE username=? AND password=?
        """, (username, password))
        user_id = cursor.fetchone()
        
        if user_id:
            cursor.execute("""
                SELECT * FROM customer WHERE customerID=?
            """, (user_id[0],))
            record = cursor.fetchone()
            
            if record:
                num, fname, lname, cell, email, addr = record
                User = Customer(fname, lname, email, cell, addr)
                CloseDatabase()
                return User
        CloseDatabase()
        return None
    except Exception as e:
        print(e)
        raise e

def getCustomerNumber(customer):
    initialise_database()
    fname, lname, phone, email = customer.first_name, customer.last_name, customer.phoneNum, customer.email
    cursor.execute("""SELECT customerID FROM customer 
        WHERE customerFirstName=? AND customerLastName=?
        AND customerPhoneNumber=? AND customerEmail=?""", 
        (fname,lname,phone,email))
    id = cursor.fetchone()
    CloseDatabase()
    return id

def CloseDatabase(): connection.close()


initialise_database()
CloseDatabase()

# How to do services: they will be saved manually by admin.
# 1. Fade Cut

def AddService(service: Service):
    try:
        id, name, price, descr, type_id = service.serviceID, service.serviceName, service.servicePrice, service.serviceDescription, service.serviceTypeID
        cursor.execute(""""INSERT INTO service VALUES(?, ?, ?, ?, ?)""",
        (id, name, price, descr, type_id))
        connection.commit()
    except Exception as e:
        print(e)
        raise e

def AddAppointmentRequest(appointment: Appointment, cust_id):
    try:
        initialise_database()
        sched, cust_num, serv_num = appointment.schedule, appointment.customer_num, appointment.service_num
        date, time, status = appointment.appointmentDate, appointment.appointmentTime, str(appointment.appointmentStatus)
        print(date, time, status, cust_num, serv_num)
        cursor.execute("INSERT INTO appointment (appointmentDate, appointmentTime, appointmentStatus, customerID, serviceNumber) VALUES(?, ?, ?, ?, ?)", (date, time, status, cust_id, serv_num))
        connection.commit()
        CloseDatabase()
    except Exception as e:
        print(e)
        raise e
    
    
def getServiceNumber(service_name: str):
    try:
        initialise_database()
        cursor.execute('SELECT serviceID FROM service WHERE serviceName=?', service_name)
        record = cursor.fetchone()[0]
    except Exception as e:
        raise e
    
    
initialise_database()
cursor.execute("SELECT * FROM appointment")
res = cursor.fetchall()
headers = ['App_ID', 'App_date', 'App_time', 'App_status', 'Cust_ID', 'Serv_num']
print(tabulate(res, headers, "fancy_grid"))