# MINI-PROJECT3-TOPIC-11
# MINI PROJECT 3 - VEHICLE RENTAL MANAGEMENT

## 1. Project Description

This is a Python console application for managing a vehicle rental system,
built using procedural programming methods.

The program runs on a CLI (Command Line Interface) environment, allowing users
to interact through a menu in the console window. The system supports managing
vehicle data including adding vehicles, displaying lists, searching, sorting,
statistics, saving data, and exporting reports.

This project was developed to apply knowledge from **Programming Methods 1**, including:

- Using functions to break down the program
- Using loops to build an interactive menu
- Using conditional statements
- Using lists and dictionaries
- Validating user input
- File handling (TXT, JSON)
- Displaying formatted output

**Selected Topic:** Topic 11 – Vehicle / Car Rental Management

---

## 2. Project Objective

The system is built with the following objectives:

- Manage vehicle rental information efficiently
- Allow adding, viewing, searching, sorting vehicles
- Provide statistics about vehicles
- Save and load data from files
- Export structured JSON data
- Practice procedural programming

---

## 3. Data Structure

Each vehicle is stored as a dictionary:
{ "id": "V001", "name": "Toyota", "type": "Car", "price": 100, "status": "Available" }

Stored in a list:
vehicles = [ { "id": "V001", "name": "Toyota", "type": "Car", "price": 100, "status": "Available" } ]
---

## 4. Technologies Used

| Component | Role |
|----------|------|
| Python 3 | Main language |
| TXT File | Data storage |
| JSON File | Data export |
| Git & GitHub | Version control |
| CLI | User interaction |

---

## 5. Project Structure
vehicle-management/ |-- main.py |-- data.txt |-- data.json |-- README.md
---

## 6. Main Features

### 6.1 Add Vehicle
- Input: ID, name, type, price, status
- Validate price and basic input

### 6.2 Display Vehicles
- Show all vehicles in table format

### 6.3 Search Vehicle
- Search by keyword (ID, name, type)

### 6.4 Sort Vehicles
- Sort by price (ascending)

### 6.5 Statistics
- Total vehicles
- Average price
- Available vs Rented

### 6.6 Save & Load TXT
- Save to `data.txt`
- Load when program starts

### 6.7 Export JSON
- Export all data to `data.json`

---

## 7. Menu
============================================================
        🚗 VEHICLE MANAGEMENT SYSTEM 🚗
============================================================
1. Add new vehicle
2. Display all vehicles
3. Search vehicle by name
4. Sort vehicles by price
5. Show statistics
6. Save to TXT file
7. Load from TXT file
8. Advanced search
9. Export to JSON
0. Exit
============================================================
Choose: 
---

## 8. Input Validation

| Data | Rule |
|------|------|
| ID | Not empty |
| Price | Must be number |
| Status | Available / Rented |

---

## 9. Functions

| Function | Role |
|----------|------|
| load_data() | Load TXT |
| save_data() | Save TXT |
| export_json() | Export JSON |
| add_vehicle() | Add new vehicle |
| display_vehicles() | Show list |
| search_vehicle() | Keyword search |
| sort_vehicles() | Sort by price |
| statistics() | Calculate stats |
| menu() | Main loop |

---

## 10. How to Run
pyhon main.py
---

## 11. Advanced Features

### Keyword Search
- Search using partial keyword

### JSON Export
- Export structured data

---

## 12. Self-Assessment

| # | Component | Score |
|--|----------|------|
| 1 | CLI Menu | 1.0 |
| 2 | Input Validation | 1.0 |
| 3 | Display Table | 1.0 |
| 4 | Search | 1.0 |
| 5 | Sort | 1.0 |
| 6 | Statistics | 1.0 |
| 7 | TXT File | 1.0 |
| 8 | Advanced Search | 1.0 |
| 9 | JSON Export | 1.0 |
| 10 | Git | 1.0 |
| | TOTAL | 10.0 |

---

## 13. Student Information

- Student Name: [LÊ THỊ ANH THƯ]
- Student ID: [24S7040012]
- Class: [Tin2E]
- Course: Programming Methods 1
