import json
import os

DATA_FILE = "data.txt"
JSON_FILE = "data.json"


# ================== FILE HANDLING ==================
def load_data():
    vehicles = []
    if not os.path.exists(DATA_FILE):
        return vehicles

    with open(DATA_FILE, "r") as f:
        for line in f:
            parts = line.strip().split("|")
            if len(parts) == 5:
                vehicle = {
                    "id": parts[0],
                    "name": parts[1],
                    "type": parts[2],
                    "price": float(parts[3]),
                    "status": parts[4]
                }
                vehicles.append(vehicle)
    return vehicles


def save_data(vehicles):
    with open(DATA_FILE, "w") as f:
        for v in vehicles:
            line = f"{v['id']}|{v['name']}|{v['type']}|{v['price']}|{v['status']}\n"
            f.write(line)


def export_json(vehicles):
    with open(JSON_FILE, "w") as f:
        json.dump(vehicles, f, indent=4)
    print("Exported to JSON successfully!")


# ================== CORE FUNCTIONS ==================
def add_vehicle(vehicles):
    vid = input("Enter ID: ")
    name = input("Enter name: ")
    vtype = input("Enter type: ")

    try:
        price = float(input("Enter price per day: "))
    except:
        print("Invalid price!")
        return

    status = input("Enter status (Available/Rented): ")

    vehicle = {
        "id": vid,
        "name": name,
        "type": vtype,
        "price": price,
        "status": status
    }

    vehicles.append(vehicle)
    save_data(vehicles)
    print("Added successfully!")


def display_vehicles(vehicles):
    if not vehicles:
        print("No data!")
        return

    print(f"{'ID':<10}{'Name':<20}{'Type':<15}{'Price':<10}{'Status':<10}")
    print("-" * 65)

    for v in vehicles:
        print(f"{v['id']:<10}{v['name']:<20}{v['type']:<15}{v['price']:<10}{v['status']:<10}")


def search_vehicle(vehicles):
    keyword = input("Enter ID or name: ").lower()

    found = []
    for v in vehicles:
        if keyword in v["id"].lower() or keyword in v["name"].lower():
            found.append(v)

    display_vehicles(found)


def sort_vehicles(vehicles):
    vehicles.sort(key=lambda x: x["price"])
    print("Sorted by price!")


def statistics(vehicles):
    if not vehicles:
        print("No data!")
        return

    total = sum(v["price"] for v in vehicles)
    avg = total / len(vehicles)

    available = sum(1 for v in vehicles if v["status"].lower() == "available")
    rented = sum(1 for v in vehicles if v["status"].lower() == "rented")

    print(f"Total vehicles: {len(vehicles)}")
    print(f"Average price: {avg}")
    print(f"Available: {available}")
    print(f"Rented: {rented}")


# ================== MENU ==================
def menu():
    vehicles = load_data()

    while True:
        print("\n===== VEHICLE MANAGEMENT =====")
        print("1. Add vehicle")
        print("2. Display vehicles")
        print("3. Search vehicle")
        print("4. Sort vehicles (by price)")
        print("5. Statistics")
        print("6. Export JSON")
        print("0. Exit")

        choice = input("Choose: ")

        if choice == "1":
            add_vehicle(vehicles)
        elif choice == "2":
            display_vehicles(vehicles)
        elif choice == "3":
            search_vehicle(vehicles)
        elif choice == "4":
            sort_vehicles(vehicles)
        elif choice == "5":
            statistics(vehicles)
        elif choice == "6":
            export_json(vehicles)
        elif choice == "0":
            print("Bye!")
            break
        else:
            print("Invalid choice!")


if __name__ == "__main__":
    menu()