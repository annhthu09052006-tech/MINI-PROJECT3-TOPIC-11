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


def search_vehicle(vehicles):
    keyword = input("Enter keyword: ").lower()
    result = [v for v in vehicles if keyword in v["name"].lower()]
    display_vehicles(result)


def sort_vehicles(vehicles):
    vehicles.sort(key=lambda x: x["price"])
    print("Sorted!")


# ===== STATISTICS =====
def statistics(vehicles):
    if not vehicles:
        print("No data!")
        return

    total_price = sum(v["price"] for v in vehicles)
    avg_price = total_price / len(vehicles)

    available = sum(1 for v in vehicles if v["status"].lower() == "available")
    rented = sum(1 for v in vehicles if v["status"].lower() == "rented")

    print("\n===== STATISTICS =====")
    print(f"Total vehicles : {len(vehicles)}")
    print(f"Total price    : {total_price}")
    print(f"Average price  : {avg_price:.2f}")
    print(f"Available      : {available}")
    print(f"Rented         : {rented}")


def menu():
    vehicles = load_data()

    while True:
        print("\n1. Add")
        print("2. Display")
        print("3. Search")
        print("4. Sort")
        print("5. Statistics")
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
        elif choice == "0":
            break
        else:
            print("Invalid!")


if __name__ == "__main__":
    menu()