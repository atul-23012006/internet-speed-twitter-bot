# Internet Speed Monitor & Dashboard

A Python-based automation project that monitors internet speed, logs historical data, and visualizes performance through a web dashboard.

This project was built as part of the **100 Days of Code Python Bootcamp by Angela Yu**, but extended with additional features such as data logging and a web-based dashboard.

---

## Features

* Automated internet speed testing using Selenium
* Logs download and upload speeds to a CSV file
* Generates speed history graphs
* Displays a web dashboard with average speeds
* Tracks internet performance over time

---

## Tech Stack

* Python
* Selenium
* Flask
* Pandas
* Matplotlib
* python-dotenv

---

## Project Structure

internet-speed-monitor

├── main.py
├── dashboard.py
├── speed_log.csv
├── templates/
│   └── index.html
├── static/
│   └── speed_graph.png
├── requirements.txt
├── .env
├── .gitignore
└── README.md

---

## Installation

Clone the repository:

git clone https://github.com/YOUR_USERNAME/internet-speed-monitor.git

Navigate to the project folder:

cd internet-speed-monitor

Install dependencies:

pip install -r requirements.txt

---

## Running the Project

Run the internet speed monitor:

python main.py

This will:

1. Run a speed test
2. Save the result to `speed_log.csv`

Start the dashboard:

python dashboard.py

Then open the browser and visit:

http://127.0.0.1:5000

---

## Example Data

speed_log.csv

2026-03-12,18:10,132.4,8.5
2026-03-12,19:00,128.7,8.1
2026-03-12,20:00,120.3,7.8

---

## Dashboard

The dashboard displays:

* Average download speed
* Average upload speed
* Internet speed history graph

---

## Future Improvements

* Automatic hourly speed testing
* Email alerts when speed drops below threshold
* Interactive dashboard
* Deployment to a cloud service

---

## Author

Atul Bharadwaj

---

## License

This project is for educational and portfolio purposes.
