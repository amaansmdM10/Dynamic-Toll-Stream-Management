#Streaming data consumer

from datetime import datetime
from kafka import KafkaConsumer
import mysql.connector

TOPIC='tollemployee'
DATABASE = 'tolldata'
USERNAME = 'root'
PASSWORD = 'root'

print("Connecting to the database")
try:
    connection = mysql.connector.connect(host='localhost', database=DATABASE, user=USERNAME, password=PASSWORD)
except Exception:
    print("Could not connect to database. Please check credentials")
else:
    print("Connected to database")
cursor = connection.cursor()

print("Connecting to Kafka")
consumer = KafkaConsumer(TOPIC)
print("Connected to Kafka")
print(f"Reading messages from the topic {TOPIC}")
for msg in consumer:
    # Extract information from kafka

    message = msg.value.decode("utf-8")

    # Transform the date format to suit the database schema
    (Emp_id, Designation_Id, Toll_id, EmployeeName,Age,PhoneNumber,Email,location,Designation,salary) = message.split(",")

    #dateobj = datetime.strptime(timestamp, '%a %b %d %H:%M:%S %Y')
    #timestamp = dateobj.strftime("%Y-%m-%d %H:%M:%S")

    # Loading data into the database table

    sql = "insert into tollemployers values(%s, %s, %s, %s, %s, %s, %s)"
    result1 = cursor.execute(sql, (Emp_id, Toll_id, EmployeeName, Age, PhoneNumber, Email, Designation_Id))
    print(f"A {EmployeeName} was inserted into the database")

    connection.commit()

    q = "SELECT count(*) FROM tolldesignations WHERE Designation_Id = %s"
    cursor.execute(q, (Designation_Id,))

    d = cursor.fetchone()
    d1 = d[0]

    if d1 == 0:
        sql = "insert into tolldesignations values(%s, %s, %s)"
        result2 = cursor.execute(sql, (Designation_Id, Designation, salary))
    connection.commit()

    query = "SELECT count(*) FROM tollemployers WHERE Toll_id = %s"
    cursor.execute(query, (Toll_id,))

    r = cursor.fetchone()
    count = r[0]

    query = "SELECT count(*) FROM tolllocation WHERE Toll_id = %s"
    cursor.execute(query, (Toll_id,))

    r1 = cursor.fetchone()
    c = r1[0]
    print(c)
    if c == 0:
        sql = "insert into tolllocation values(%s, %s, %s)"
        cursor.execute(sql, (Toll_id, count, location))
    else:
        sql = "UPDATE tolllocation SET NoOfEmployer = %s WHERE Toll_id = %s"
        cursor.execute(sql, (count, Toll_id))

    connection.commit()
    
connection.close()