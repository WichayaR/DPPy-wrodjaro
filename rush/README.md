# 42 Express Bus Ticket Kiosk

## Project Purpose
This project is a command-line self-service bus ticket kiosk written in Python for the Discovery Piscine Rush00 project. It allows passengers to check available seats on a 28-seat bus, book tickets across different zones, cancel their bookings for a refund, and view their payment summary directly in the terminal.

## Main Features
1. **View Bus Seat Map**: Displays the current layout of all 28 seats (Rows A-D for VIP Zone at 500 THB, and Rows F-H for Standard Zone at 350 THB, skipping Row E for the exit door). Shows available (`o`) and taken (`x`) seats.
2. **Book a Seat**: Lets users reserve an available seat by entering the seat code, passenger name, and payment amount. Calculates change automatically.
3. **Cancel Booking**: Allows users to cancel a ticket from their booking list, refunds the ticket price, and updates the seat status back to available (`o`).
4. **My Tickets & Seat Finder (Data Processing)**:
   - **Receipt Summary**: Calculates total tickets booked, total amount paid, average ticket price, and the highest ticket price.
   - **Available Seat Finder**: Filters and lists remaining available seats by zone (`VIP`, `Standard`, or `ALL`).
5. **Validation & Error Handling**:
   - Checks if the entered seat code actually exists on the bus.
   - Prevents double booking on seats that are already taken (`x`).
   - Rejects payments that are less than the ticket price.
   - Handles invalid menu choices and non-numeric payment inputs (`try-except`) without crashing.

## How to Run
Make sure you have Python 3 installed. Open your terminal, navigate to the `rush` directory, and run:

```bash
python3 main.py
```

Or run it directly as an executable script:

```bash
chmod +x main.py
./main.py
```

## Authors
- wrodjaro
- ajommuen
