from datetime import datetime, timedelta
import re
import uuid
from app.domain.read_write import ReadWrite
from app.model.json_file import Path
from app.model.time_slots import TimeSlots
from app.model.colors import Color

class TableBooking:

    @staticmethod
    def make_reservation_id(reservations_list):
        while True:
            reservation_id = uuid.uuid4().hex.upper()[:6]
            exists = False
            for r in reservations_list:
                if r.get("reservation_id") == reservation_id:
                    exists = True
                    break
            if not exists:
                return reservation_id

    @staticmethod
    def input_customer_name():
        while True:
           name = input(Color.BRIGHT_BLUE+"Enter customer name: "+Color.YELLOW).strip()
           if name == "":
               print(Color.RED+"Customer name cannot be empty.")
               continue
           if len(name) < 2:
               print(Color.RED+"Customer name must be at least 2 characters.")
               continue
           if re.fullmatch(r"[A-Za-z ]+", name) is None:
               print(Color.RED+"Customer name must contain only letters and spaces.")
               continue
           if name.replace(" ", "") == "":
               print(Color.RED+"Customer name cannot be only spaces.")
               continue
           return name.title()

    @staticmethod
    def input_booking_date():
        while True:
           date_str = input(Color.BRIGHT_BLUE+"Enter booking date (YYYY-MM-DD): "+Color.YELLOW).strip()
           try:
               booking_date = datetime.strptime(date_str, "%Y-%m-%d").date()
           except ValueError:
               print(Color.RED+"Invalid date format. Example: 2026-01-11")
               continue
           today = datetime.now().date()
           if booking_date < today:
               print(Color.RED+"Past date not allowed.")
               continue
           max_date = today + timedelta(days=30)
           if booking_date > max_date:
               print(Color.RED+"Booking allowed only up to next 30 days.")
               continue
           return date_str 

    @staticmethod
    def input_seats(max_capacity):
        while True:
            try:
                seats = int(input(Color.BRIGHT_BLUE+"Enter number of seats: "+Color.YELLOW))
                if seats <= 0:
                    print(Color.RED+"Seats must be greater than 0.")
                    continue
                if seats > max_capacity:
                    print(Color.RED+f"Seats cannot be more than {max_capacity}.")
                    continue
                return seats
            except ValueError:
                print(Color.RED+"Seats must be a number.")

    @staticmethod
    def input_option_number(max_number):
        while True:
            try:
                n = int(input(Color.BRIGHT_BLUE+"Select option number: "+Color.YELLOW))
                if 1 <= n <= max_number:
                    return n
                print(Color.RED+"Invalid option number.")
            except ValueError:
                print(Color.RED+"Please enter a number.")

    @staticmethod
    def parse_slot_start_time(slot_str):
        start_part = slot_str.split("-")[0].strip()
        return datetime.strptime(start_part, "%H:%M").time()

    @staticmethod
    def filter_slots_for_date(date_str):
        try:
            booking_date = datetime.strptime(date_str, "%Y-%m-%d").date()
        except ValueError:
            return []
        all_slots = TimeSlots.SLOTS
        if not all_slots:
            return []
        today = datetime.now().date()
        if booking_date != today:
            return all_slots
        now_time = datetime.now().time()
        filtered = []
        for s in all_slots:
            start_time = TableBooking.parse_slot_start_time(s)
            if start_time > now_time:
                filtered.append(s)
        return filtered

    @staticmethod
    def book_table():
        customer_name = TableBooking.input_customer_name()
        booking_date = TableBooking.input_booking_date()

        tables_data = ReadWrite.read(Path.tables_data_path)
        
        if isinstance(tables_data, list) and len(tables_data) > 0:
            tables_list = tables_data
        elif isinstance(tables_data, dict) and "tables" in tables_data and tables_data["tables"]:
            tables_list = tables_data["tables"]
        else:
            print(Color.RED+"Tables data not found.")
            input(Color.YELLOW+"\nPress Enter to continue...")
            return

        reservations_data = ReadWrite.read(Path.reservations_data_path)
        if not reservations_data:
            reservations_data = {"reservations": []}
        if "reservations" not in reservations_data:
            reservations_data["reservations"] = []

        reservations_list = reservations_data["reservations"]

        max_capacity = 0
        for t in tables_list:
            cap = t.get("capacity", 0)
            if cap > max_capacity:
                max_capacity = cap

        if max_capacity <= 0:
            print(Color.RED+"No valid table capacity found.")
            input(Color.YELLOW+"\nPress Enter to continue...")
            return

        seats = TableBooking.input_seats(max_capacity)

        slots_for_day = TableBooking.filter_slots_for_date(booking_date)
        if not slots_for_day:
            print(Color.RED+"No time slots available for this date.")
            input(Color.YELLOW+"\nPress Enter to continue...")
            return

        print(Color.YELLOW+"\nSelect Time Slot:")
        for i, slot in enumerate(slots_for_day, 1):
            print(Color.WHITE+f"{i}. {slot}")

        slot_number = TableBooking.input_option_number(len(slots_for_day))
        selected_slot = slots_for_day[slot_number - 1]

        available_tables = []
        for t in tables_list:
            if t.get("capacity", 0) < seats:
                continue
            booked = False
            for r in reservations_list:
                if (
                    r.get("status") == "booked"
                    and r.get("table_id") == t.get("table_id")
                    and str(r.get("date")) == booking_date
                    and r.get("time_slot") == selected_slot
                ):
                    booked = True
                    break
            if not booked:
                available_tables.append(t)

        if len(available_tables) == 0:
            print(Color.RED+f"No table available for {selected_slot} on {booking_date}.")
            input(Color.YELLOW+"\nPress Enter to continue...")
            return

        available_tables.sort(key=lambda x: x.get("capacity", 0))

        print(Color.YELLOW+f"\nAvailable Tables for {selected_slot}:")
        for j, t in enumerate(available_tables):
            print(Color.CYAN+f"{j + 1}. {t.get('table_name')} (cap {t.get('capacity')})")

        table_number = TableBooking.input_option_number(len(available_tables))
        chosen_table = available_tables[table_number - 1]

        reservation_id = TableBooking.make_reservation_id(reservations_list)

        current_datetime = datetime.now().strftime("%Y-%m-%d %I:%M %p")

        new_reservation = {
            "reservation_id": reservation_id,
            "customer_name": customer_name,
            "table_id": chosen_table.get("table_id"),
            "table_name": chosen_table.get("table_name"),
            "date": booking_date,                   
            "time_slot": selected_slot,                   
            "seats": seats,
            "status": "booked",
            "created_datetime": current_datetime,           
            "created_at": datetime.now().strftime("%Y-%m-%d %H:%M:%S")  
        }

        reservations_list.append(new_reservation)
        ReadWrite.write_json(reservations_data, Path.reservations_data_path)

        print(Color.GREEN+f"\nBooked: ID {Color.CYAN}{reservation_id}")
        print(Color.GREEN+f"  Table: {Color.CYAN}{chosen_table.get('table_name')} ({seats} seats)")
        print(Color.GREEN+f"  Date: {Color.CYAN}{booking_date} at {selected_slot}")
        print(Color.GREEN+f"  Created: {Color.CYAN}{current_datetime}")
        input(Color.YELLOW+"\nPress Enter to continue...")
