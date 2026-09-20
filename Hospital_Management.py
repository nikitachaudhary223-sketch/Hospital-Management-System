print("====================================")
print("       HOSPITAL MANAGEMENT SYSTEM")
print("====================================")

patients = []


# Add Patient
def add_patient():
    print("\n---------- ADD PATIENT ----------")

    name = input("Enter patient name: ")
    age = int(input("Enter patient age: "))
    disease = input("Enter disease/problem: ")
    doctor = input("Enter doctor name: ")

    patient = {
        "name": name,
        "age": age,
        "disease": disease,
        "doctor": doctor,
        "bill": 0,
        "appointment": "Not Scheduled"
    }

    patients.append(patient)

    print("\nPatient added successfully!")


# View All Patients
def view_patients():
    print("\n---------- ALL PATIENTS ----------")

    if len(patients) == 0:
        print("No patients found.")
        return

    for i, patient in enumerate(patients, 1):
        print(f"\nPatient {i}")
        print(f"Name: {patient['name']}")
        print(f"Age: {patient['age']}")
        print(f"Disease: {patient['disease']}")
        print(f"Doctor: {patient['doctor']}")
        print(f"Bill: Rs. {patient['bill']}")
        print(f"Appointment: {patient['appointment']}")


# Search Patient
def search_patient():
    print("\n---------- SEARCH PATIENT ----------")

    search_name = input("Enter patient name: ")
    found = False

    for patient in patients:
        if patient["name"].lower() == search_name.lower():
            print("\nPatient Found!")
            print(f"Name: {patient['name']}")
            print(f"Age: {patient['age']}")
            print(f"Disease: {patient['disease']}")
            print(f"Doctor: {patient['doctor']}")
            print(f"Bill: Rs. {patient['bill']}")
            print(f"Appointment: {patient['appointment']}")

            found = True

    if not found:
        print("Patient not found.")


# Add Medical Bill
def add_bill():
    print("\n---------- ADD BILL ----------")

    search_name = input("Enter patient name: ")
    found = False

    for patient in patients:
        if patient["name"].lower() == search_name.lower():

            consultation = float(input("Enter consultation fee: "))
            medicine = float(input("Enter medicine cost: "))
            test = float(input("Enter test cost: "))

            total = consultation + medicine + test

            patient["bill"] += total

            print(f"\nBill added successfully!")
            print(f"Total bill: Rs. {patient['bill']}")

            found = True

    if not found:
        print("Patient not found.")


# Schedule Appointment
def schedule_appointment():
    print("\n---------- APPOINTMENT ----------")

    search_name = input("Enter patient name: ")
    found = False

    for patient in patients:
        if patient["name"].lower() == search_name.lower():

            doctor = input("Enter appointment doctor: ")
            time = input("Enter appointment time: ")

            patient["doctor"] = doctor
            patient["appointment"] = time

            print("\nAppointment scheduled successfully!")

            found = True

    if not found:
        print("Patient not found.")


# Main Menu
while True:

    print("\n====================================")
    print("       HOSPITAL MANAGEMENT")
    print("====================================")

    print("1. Add Patient")
    print("2. View All Patients")
    print("3. Search Patient")
    print("4. Add Medical Bill")
    print("5. Schedule Appointment")
    print("6. Exit")

    choice = input("\nEnter your choice: ")

    if choice == "1":
        add_patient()

    elif choice == "2":
        view_patients()

    elif choice == "3":
        search_patient()

    elif choice == "4":
        add_bill()

    elif choice == "5":
        schedule_appointment()

    elif choice == "6":
        print("\nThank you for using Hospital Management System!")
        break

    else:
        print("\nInvalid choice! Please try again.")