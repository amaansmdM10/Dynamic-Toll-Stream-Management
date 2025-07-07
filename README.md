# Toll Data Streaming and Employee Management System

This repository demonstrates a simulated toll data streaming and employee management system using Python, Kafka, Flask, and MySQL. It includes real-time data generation, processing, and storage pipelines for toll vehicle data and toll employee data.

📄 Overview

The project consists of two main workflows:

Toll Vehicle Data Stream

Toll Employee Management System

Each workflow uses Kafka producers and consumers to handle streaming data and integrates with a MySQL database for storage and analysis.

🚧 Toll Vehicle Data Workflow

## ETL.py

- Simulates real-time vehicle traffic at toll plazas.

- Randomly generates vehicle types, IDs, timestamps, and plaza IDs.

- Sends data to the Kafka topic toll.

## Streamer.py

- Kafka consumer that reads from the toll topic.

- Parses vehicle data and inserts it into the livetolldata table in MySQL.

👷 Toll Employee Management Workflow

## index.html

- A web form for entering employee details such as name, age, location, designation, email, and phone number.

## process.py

- Flask application that handles form submissions.

- Processes employee data, assigns IDs and salaries based on designation and location.

- Sends formatted data to the Kafka topic tollemployee.

## storage.py

- Kafka consumer that listens to the tollemployee topic.

- Inserts employee data into MySQL tables (tollemployers, tolldesignations, and tolllocation).

- Updates toll location tables with employee count.

💾 Database Tables

The system uses a MySQL database named tolldata with the following tables:

- livetolldata: Stores real-time vehicle passage data.

- tollemployers: Stores employee details.

- tolldesignations: Stores designation details and salaries.

- tolllocation: Stores toll location data along with the number of employees.

⚙️ Setup Instructions

## Prerequisites

- Python 3.x

- Kafka and Zookeeper running locally (default: localhost:9092)

- MySQL database setup with required tables

## Install dependencies
```bash
pip install flask kafka-python mysql-connector-python
```
## Start Kafka and Zookeeper

Make sure Kafka and Zookeeper services are running before executing producers and consumers.

## Run Vehicle Data Stream
```bash
python ETL.py
python Streamer.py
```
```bash
## Run Employee Management Workflow

# Start the Flask app
python process.py

# Open index.html in a browser and submit the form

# Start the storage consumer
python storage.py
```
🖥️ Web Interface

Open index.html in your browser to submit new employee data.

Submitted data will be processed and stored in MySQL.

💬 Contributing

Pull requests are welcome. For significant changes, please open an issue first to discuss what you'd like to change.

📄 License

This project is open-source and available under the MIT License.

✉️ Contact

For questions or suggestions, feel free to open an issue or reach out directly!

🚦 Happy streaming!
