
# Hotel Purchase Management System

A beginner-friendly, menu-driven Python application for creating and viewing hotel purchase requests.

## Features

- Create purchase requests with employee and item details.
- Calculate purchase totals.
- Assign approval levels based on purchase value.
- Display a warning for purchases above ₹100,000.
- View all purchase requests created during the session.
- Validate basic user inputs.

## Approval Rules

| Purchase Value | Approval Required |
|---|---|
| Up to ₹10,000 | Supervisor |
| ₹10,001–₹50,000 | Department Manager |
| Above ₹50,000 | Finance Head |

## Technology

- Python 3.10+
- Python standard library
- Command-line interface

## How to Run

1. Install Python 3.10 or newer.
2. Download or clone this repository.
3. Open a terminal in the project folder.
4. Run:

```bash
python hotel.py
```

## Menu

1. Create a Purchase Request
2. View All Orders
3. Exit

## Limitations

- Orders are stored in memory and disappear when the application closes.
- The approval level is calculated, but there is no actual manager approval workflow.
- There is no database, login system, or external integration.
- This is a learning project, not production hotel software.

## Future Improvements

- Save requests in SQLite.
- Add order status and approval workflows.
- Add search and filtering.
- Improve monetary calculations using Decimal.
- Add automated unit tests.

## About

Created as a practical Python learning project exploring basic procurement workflows and purchase approval rules.
