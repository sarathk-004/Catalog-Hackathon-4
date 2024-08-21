import datetime

children = {}
appointments = {}
vaccination_records = {}

def register_child():
    child_id = input("Enter Child ID: ")
    name = input("Enter Child's Name: ")
    age = int(input("Enter Child's Age: "))
    parent_name = input("Enter Parent's Name: ")
    contact = input("Enter Contact Number: ")

    children[child_id] = {
        'name': name,
        'age': age,
        'parent_name': parent_name,
        'contact': contact
    }

    vaccination_records[child_id] = []
    print(f"\nChild {name} registered successfully!\n")

def book_appointment():
    child_id = input("Enter Child ID: ")
    if child_id in children:
        vaccine = input("Enter Vaccine Name: ")
        date_str = input("Enter Appointment Date (YYYY-MM-DD): ")
        appointment_date = datetime.datetime.strptime(date_str, "%Y-%m-%d").date()

        if child_id not in appointments:
            appointments[child_id] = []
        appointments[child_id].append({'vaccine': vaccine, 'date': appointment_date, 'vaccinated': False})

        print(f"\nAppointment for {vaccine} on {appointment_date} booked successfully!\n")
    else:
        print("Child not registered.\n")

def update_vaccination_status():
    child_id = input("Enter Child ID: ")
    if child_id in children and child_id in appointments:
        for i, appointment in enumerate(appointments[child_id]):
            print(f"{i+1}. {appointment['vaccine']} on {appointment['date']} (Vaccinated: {appointment['vaccinated']})")

        choice = int(input("Enter the number of the appointment to update: "))
        if 1 <= choice <= len(appointments[child_id]):
            appointments[child_id][choice-1]['vaccinated'] = True
            vaccination_records[child_id].append(appointments[child_id][choice-1])
            print("\nVaccination status updated successfully!\n")
        else:
            print("Invalid choice.\n")
    else:
        print("No appointments found for this child.\n")

def view_records():
    child_id = input("Enter Child ID: ")
    if child_id in vaccination_records:
        print(f"\nVaccination Records for {children[child_id]['name']}:\n")
        records = vaccination_records[child_id]
        if records:
            print(f"{'Vaccine':<15}{'Date':<15}{'Status':<10}")
            print("-" * 40)
            for record in records:
                status = "Vaccinated" if record['vaccinated'] else "Pending"
                print(f"{record['vaccine']:<15}{record['date']:<15}{status:<10}")
        else:
            print("No vaccination records found.\n")
    else:
        print("Child not registered.\n")

def get_reminders():
    today = datetime.date.today()
    for child_id, child_appointments in appointments.items():
        for appointment in child_appointments:
            if today <= appointment['date'] <= today + datetime.timedelta(days=7):
                print(f"Reminder: {children[child_id]['name']} has a vaccination appointment for {appointment['vaccine']} on {appointment['date']}.")

def main_menu():
    while True:
        print("\n--- Child Vaccination Management System ---")
        print("1. Register Child")
        print("2. Book Vaccination Appointment")
        print("3. Update Vaccination Status")
        print("4. View Vaccination Records")
        print("5. Get Reminders for Upcoming Appointments")
        print("6. Exit")

        choice = input("Enter your choice: ")

        if choice == '1':
            register_child()
        elif choice == '2':
            book_appointment()
        elif choice == '3':
            update_vaccination_status()
        elif choice == '4':
            view_records()
        elif choice == '5':
            get_reminders()
        elif choice == '6':
            print("Exiting the system. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main_menu()
