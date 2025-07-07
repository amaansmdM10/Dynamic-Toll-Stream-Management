from flask import Flask, request
from time import sleep, time, ctime
from random import random, randint, choice
from kafka import KafkaProducer

app = Flask(__name__)

@app.route('/submit', methods=['POST'])
def submit():
    name = request.form['name']
    age = request.form['age']
    location = request.form['location']
    designation = request.form['designation']
    email = request.form['email']
    phone = request.form['phone']


    producer = KafkaProducer(bootstrap_servers='localhost: 9092' )

    TOPIC = 'tollemployee'
    id1,id2,id3=110,111,113
    # You can now process these details, save to DB, etc.
    #print("Received Employer Details:")
    #print(f"Name: {name}")
    #print(f"Age: {age}")
    #print(f"Location: {location}")
    #print(f"Designation: {designation}")
    #print(f"Email: {email}")
    #print(f"Phone: {phone}")
    salary=0
    Emp_id = randint(100, 9000)
    if designation == '01':
        Designation_Id = id1
        designation = 'Security Assistant'
        salary = 15000
    if designation == '02':
        Designation_Id = id2
        designation = 'Security Incharge'
        salary = 25000
    if designation == '03':
        Designation_Id = id3
        designation = 'Lane Manager'
        salary = 55000
    #Designation_Id = randint(100,500)
    #Toll_id = randint(1000,9000)

    if location == 'Hyderabad':
        Toll_id = 1011
    if location == 'Bangalore':
        Toll_id = 1012
    if location == 'Delhi':
        Toll_id = 1013
    if location == 'Chennai':
        Toll_id = 1014
    if location == 'Mumbai':
        Toll_id = 1015
    if location == 'Pune':
        Toll_id = 1016

    EmployeeName = name
    Age =  age
    PhoneNumber = phone
    Email = email
    location = location
    Designation = designation
    message = f"{Emp_id},{Designation_Id},{Toll_id},{EmployeeName}, {Age}, {PhoneNumber}, {Email},{location},{Designation},{salary}"
    message = bytearray(message.encode("utf-8"))
    print(f"A {EmployeeName} has enrolled as {Designation}.")
    producer.send(TOPIC, message)
    sleep(random() * 2)
    return f"Thank you, {name}! Your details have been received."

if __name__ == '__main__':
    app.run(debug=True)
