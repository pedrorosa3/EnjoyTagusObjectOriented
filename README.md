# EnjoyTagusOO - Boat Trip Scheduler ⛵

## About the Project
**EnjoyTagusOO** is a software application designed to manage the scheduling of boat trips on the Tagus River for the "Tagus Sailing" cooperative.

Developed as an academic project for the **Programming 2** course (Object-Oriented Programming) at the Faculty of Sciences of the University of Lisbon (2022/2023), this tool automates the assignment of skippers to booking requests based on complex criteria.

## Features
* **Object-Oriented Design:** Built using Python classes and "Design by Contract" principles.
* **Schedule Management:** Updates the current cruise calendar based on new requests and time progression.
* **Skipper Assignment:** Automatically matches clients to skippers based on skills and availability.
* **Conflict Resolution:** Handles scheduling logic, ensuring trips do not overlap or exceed working hours.

## Logic & Algorithm
The core of the application processes a queue of booking requests. For each request, the system assigns a skipper based on the following hierarchy of criteria:
1.  **Capability:** The skipper must speak the client's language, hold the required license category, and match the requested specialization (speed, comfort, or price).
2.  **Availability:** The skipper who is available earliest.
3.  **Cost:** In case of a tie, the skipper with the lowest hourly tariff.
4.  **Workload:** In case of a tie, the skipper with fewer accumulated work hours.
5.  **Alphabetical:** Final tie-breaker is the lexicographical order of the name.

## Usage
The application is executed via the command line using Python 3. It requires three input files in a specific order.

### Command Syntax
```bash
python3 update.py <skippers_file> <schedule_file> <requests_file>
