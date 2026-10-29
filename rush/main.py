#!/usr/bin/env python3

# Part 1: Initial Data Structure (List & Dict,Return)

def create_initial_seats():
    """Function 1: Initialize 28 bus seats and return the seat dictionary."""
    seats = {}  # Dictionary to store seat status ("o" = Available, "x" = Taken)
    rows = ["A", "B", "C", "D", "F", "G", "H"]  # Row E is skipped for the Exit Door
    cols = ["1", "2", "3", "4"]

    for r in rows:
        for c in cols:
            seat_code = r + c
            seats[seat_code] = "o"

    # Pre-book A1 and C3 to simulate existing passengers on the bus
    seats["A1"] = "x"
    seats["C3"] = "x"

    return seats  # Return the dictionary (return value)

# Part 2: Display Bus Seat Map (Menu 1 - View Records)


def display_bus_map(seats):
    """Function 2: Display the visual bus seat map using for loops."""
    print("\n--- [1] BUS SEAT MAP ---")
    print("      1   2    (Aisle)    3   4")

    # Render Front Zone (VIP)
    print("[Front Zone VIP - 500 THB]")
    for r in ["A", "B", "C", "D"]:
        s1, s2 = seats[r + "1"], seats[r + "2"]
        s3, s4 = seats[r + "3"], seats[r + "4"]
        print(f"{r}     {s1}   {s2}               {s3}   {s4}")

    print("--------- (Exit Door) ---------")

    # Render Back Zone (Standard)
    print("[Back Zone Standard - 350 THB]")
    for r in ["F", "G", "H"]:
        s1, s2 = seats[r + "1"], seats[r + "2"]
        s3, s4 = seats[r + "3"], seats[r + "4"]
        print(f"{r}     {s1}   {s2}               {s3}   {s4}")

    print("-------------------------------")

    # Count available ('o') and taken ('x') seats
    available_count = 0
    taken_count = 0
    for status in seats.values():
        if status == "o":
            available_count += 1
        else:
            taken_count += 1

    print(f"Legend: [o] = Available ({available_count}) | [x] = Taken ({taken_count})")


# Part 3: Book a Seat (Menu 2 - Add Record + 3 Validation Rules + Error Handling)

def book_seat(seats, my_tickets):
    """Function 3: Book a seat, validate 3 business rules, and append to the list."""
    print("\n--- [2] BOOK A SEAT ---")
    seat_code = input("Enter seat code to book (e.g., A2, F1): ").strip().upper()

    # Rule 1 - Invalid Seat: Check if the seat code exists on the bus
    if seat_code not in seats:
        print(f"❌ Sorry, seat '{seat_code}' does not exist on this bus!")
        return

    # Rule 2 - Prevent Duplicate Booking: Check if the seat is already taken ("x")
    if seats[seat_code] == "x":
        print(f"❌ Sorry, seat '{seat_code}' is already taken (x)!")
        return

    # Determine zone and ticket price based on row letter
    row_letter = seat_code[0]
    if row_letter in ["A", "B", "C", "D"]:
        zone = "VIP"
        price = 500
    else:
        zone = "Standard"
        price = 350

    print(f"👉 You selected Seat {seat_code} ({zone} Zone) | Ticket Price: {price} THB")

    # Get passenger name and validate non-empty input
    passenger_name = input("Enter passenger name: ").strip()
    if passenger_name == "":
        print("❌ Passenger name cannot be empty!")
        return

    # Get payment amount and handle non-numeric input (Error Handling)
    payment_input = input(f"Enter payment amount (Need at least {price} THB): ").strip()
    try:
        payment = int(payment_input)
    except ValueError:
        print("❌ Invalid input! Please enter numbers only.")
        return

    # Rule 3 - Reject Insufficient Funds: Check if payment covers the ticket price
    if payment < price:
        print(f"❌ Payment failed! You need at least {price} THB.")
        return

    # Update seat status from 'o' to 'x' and save ticket dictionary to the list
    change = payment - price
    seats[seat_code] = "x"

    new_ticket = {
        "seat": seat_code,
        "zone": zone,
        "name": passenger_name,
        "price": price
    }
    my_tickets.append(new_ticket)

    print(f"✅ Booking successful! Seat {seat_code} is reserved for '{passenger_name}'.")
    print(f"💵 Paid: {payment} THB | Change: {change} THB")


# Part 4: Cancel Booking (Menu 3 - Remove / Update Record)


def cancel_my_booking(seats, my_tickets):
    """Function 4: Cancel a user's booked ticket, revert 'x' to 'o', and remove from list."""
    print("\n--- [3] CANCEL MY BOOKING ---")

    if len(my_tickets) == 0:
        print("⚠️ You have no booked tickets to cancel.")
        return

    seat_code = input("Enter your booked seat code to cancel: ").strip().upper()

    # Search for the ticket in the user's booking list
    target_ticket = None
    for ticket in my_tickets:
        if ticket["seat"] == seat_code:
            target_ticket = ticket
            break

    # Handle case where seat is not found in user's bookings
    if target_ticket is None:
        print(f"❌ Cannot cancel! Seat '{seat_code}' is not in your booking list.")
        return

    # Revert seat status to 'o' and remove the record from the list
    seats[seat_code] = "o"
    my_tickets.remove(target_ticket)

    print(f"✅ Booking for seat '{seat_code}' (Passenger: {target_ticket['name']}) has been cancelled!")
    print(f"💰 Refunded: {target_ticket['price']} THB. (Seat {seat_code} is now 'o' Available again)")


# Part 5: Receipt Summary & Seat Finder (Menu 4 - 2 Data Processing Operations)


def show_my_tickets_and_search(seats, my_tickets):
    """Function 5: Calculate totals/averages/max and filter available seats by zone."""
    print("\n--- [4] MY TICKETS & SEAT FINDER ---")

    # 1. Display user's booked tickets
    print("🧾 Your Booked Tickets")
    if len(my_tickets) == 0:
        print("  (You have not booked any tickets yet)")
    else:
        for i in range(len(my_tickets)):
            t = my_tickets[i]
            print(f"  {i + 1}. Seat {t['seat']} ({t['zone']}) | Passenger: {t['name']} | Price: {t['price']} THB")

    # 2. Data Processing 1: Calculate Total, Average, and Maximum price
    print("\n📊 Receipt & Expense Summary")
    total_tickets = len(my_tickets)
    total_paid = 0
    max_price = 0

    for t in my_tickets:
        total_paid += t["price"]
        if t["price"] > max_price:
            max_price = t["price"]

    if total_tickets > 0:
        avg_price = total_paid / total_tickets
    else:
        avg_price = 0.0

    print(f"  - Total Tickets Booked : {total_tickets} ticket(s)")
    print(f"  - Total Amount Paid    : {total_paid} THB")
    print(f"  - Average Ticket Price : {avg_price:.2f} THB")
    print(f"  - Highest Ticket Price : {max_price} THB")

    # 3. Data Processing 2: Conditional Search (Filter available seats by zone)
    print("\n🔍 Available Seat Finder by Zone")
    zone_choice = input("Enter zone to find available seats (VIP / Standard / ALL / Enter to skip): ").strip().upper()

    if zone_choice == "":
        return
    elif zone_choice == "VIP":
        target_rows = ["A", "B", "C", "D"]
        zone_info = "VIP (500 THB)"
    elif zone_choice == "STANDARD":
        target_rows = ["F", "G", "H"]
        zone_info = "Standard (350 THB)"
    elif zone_choice == "ALL":
        target_rows = ["A", "B", "C", "D", "F", "G", "H"]
        zone_info = "All Zones (350-500 THB)"
    else:
        print("❌ Invalid option! Please type 'VIP', 'Standard', or 'ALL'.")
        return

    # Filter seats matching the selected zone that are currently available ('o')
    available_in_zone = []
    for code, status in seats.items():
        if code[0] in target_rows and status == "o":
            available_in_zone.append(code)

    print(f"  ✅ Available {zone_info} Seats: {', '.join(available_in_zone)}")
    print(f"  (Total: {len(available_in_zone)} seats available)")



# Part 6: Main Application Loop (Interactive Menu & While Loop)

def main():
    """Function 6: Main interactive loop for the Self-Service Ticket Kiosk."""
    bus_seats = create_initial_seats()  # Dictionary storing all 28 seat statuses
    my_tickets = []                     # List storing booked ticket dictionaries

    while True:
        print("\n=============================================")
        print("   🚌 WELCOME TO 42 EXPRESS TICKET KIOSK 🚌")
        print("=============================================")
        print("[1] View Bus Seat Map (Check Available Seats)")
        print("[2] Book a Seat (Buy Ticket)")
        print("[3] Cancel My Booking (Refund)")
        print("[4] My Tickets, Receipt & Seat Finder")
        print("[5] Exit Kiosk")
        print("=============================================")

        choice = input("Select an option (1-5): ").strip()

        if choice == "1":
            display_bus_map(bus_seats)
        elif choice == "2":
            book_seat(bus_seats, my_tickets)
        elif choice == "3":
            cancel_my_booking(bus_seats, my_tickets)
        elif choice == "4":
            show_my_tickets_and_search(bus_seats, my_tickets)
        elif choice == "5":
            print("\nThank you for travelling with 42 EXPRESS! Have a safe trip! 👋")
            break
        else:
            print("❌ Invalid menu option! Please enter a number from 1 to 5.")


if __name__ == "__main__":
    main()
