import json
import os

DATA_FILE = "data.txt"
JSON_FILE = "data.json"


def load_data():
    vehicles = []
    if not os.path.exists(DATA_FILE):
        return vehicles

    with open(DATA_FILE, "r") as f:
        for line in f:
            parts = line.strip().split("|")
            if len(parts) == 5:
                vehicles.append({
                    "id": parts[0],
                    "name": parts[1],
                    "type": parts[2],
                    "price": float(parts[3]),
                    "status": parts[4]
                })
    return vehicles


def save_data(vehicles):
    with open(DATA_FILE, "w") as f:
        for v in vehicles:
            f.write(f"{v['id']}|{v['name']}|{v['type']}|{v['price']}|{v['status']}\n")


def add_vehicle(vehicles):
    vid = input("Enter ID: ")
    name = input("Enter name: ")
    vtype = input("Enter type: ")

    try:
        price = float(input("Enter price: "))
    except:
        print("Invalid price!")
        return

    status = input("Enter status: ")

    vehicles.append({
        "id": vid,
        "name": name,
        "type": vtype,
        "price": price,
        "status": status
    })

    save_data(vehicles)
    print("Added!")


def display_vehicles(vehicles):
    if not vehicles:
        print("No data!")
        return

    print(f"{'ID':<10}{'Name':<20}{'Type':<15}{'Price':<10}{'Status':<10}")
    print("-" * 65)

    for v in vehicles:
        print(f"{v['id']:<10}{v['name']:<20}{v['type']:<15}{v['price']:<10}{v['status']:<10}")


# ===== SEARCH BASIC + ADVANCED =====
def search_vehicle(vehicles):
    keyword = input("Enter keyword (ID/Name/Type): ").lower()

    result = []
    for v in vehicles:
        if (keyword in v["id"].lower()
                or keyword in v["name"].lower()
                or keyword in v["type"].lower()):
            result.append(v)

    display_vehicles(result)


# ===== MENU =====
def menu():
    vehicles = load_data()

    while True:
        print("\n1. Add")
        print("2. Display")
        print("3. Search (keyword)")
        print("0. Exit")

        choice = input("Choose: ")

        if choice == "1":
            add_vehicle(vehicles)
        elif choice == "2":
            display_vehicles(vehicles)
        elif choice == "3":
            search_vehicle(vehicles)
        elif choice == "0":
            break
        else:
            print("Invalid!")


if __name__ == "__main__":
    menu()