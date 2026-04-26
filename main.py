vehicles = []

def add_vehicle():
    vid = input("Enter ID: ")
    name = input("Enter name: ")
    vtype = input("Enter type: ")
    price = float(input("Enter price: "))

    vehicles.append({
        "id": vid,
        "name": name,
        "type": vtype,
        "price": price,
        "status": "Available"
    })

    print("Added successfully!")

def menu():
    while True:
        print("\n===== VEHICLE MANAGEMENT =====")
        print("1. Add vehicle")
        print("2. Display vehicles")
        print("3. Search")
        print("4. Sort")
        print("5. Statistics")
        print("6. Save to file")
        print("7. Export JSON")
        print("0. Exit")

        choice = input("Choose: ")

        if choice == "1":
            add_vehicle()
        elif choice == "0":
            print("Goodbye!")
            break
        else:
            print("Feature not implemented yet!")

if __name__ == "__main__":
    menu()