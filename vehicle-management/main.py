import json
import os

DATA_TXT = "data.txt"
DATA_JSON = "data.json"

# ================= LOAD =================
def load_from_txt():
    vehicles = []
    if not os.path.exists(DATA_TXT):
        return vehicles

    with open(DATA_TXT, "r") as f:
        for line in f:
            parts = line.strip().split("|")
            if len(parts) == 3:
                vehicles.append({
                    "id": parts[0],
                    "name": parts[1],
                    "price": float(parts[2])
                })
    return vehicles


# ================= SAVE =================
def save_to_txt(vehicles):
    with open(DATA_TXT, "w") as f:
        for v in vehicles:
            f.write(f"{v['id']}|{v['name']}|{v['price']}\n")


def save_to_json(vehicles):
    with open(DATA_JSON, "w") as f:
        json.dump(vehicles, f, indent=4)


# ================= FEATURES =================
def add_vehicle(vehicles):
    id = input("Enter ID: ")
    name = input("Enter name: ")
    price = float(input("Enter price: "))

    vehicles.append({
        "id": id,
        "name": name,
        "price": price
    })

    save_to_txt(vehicles)  # 👈 tự lưu luôn
    print("Added successfully!")


def display_vehicles(vehicles):
    if not vehicles:
        print("Empty list")
        return

    for v in vehicles:
        print(v["id"], v["name"], v["price"])


def search_vehicle(vehicles):
    keyword = input("Enter name to search: ")
    for v in vehicles:
        if keyword.lower() in v["name"].lower():
            print(v)


def sort_vehicles(vehicles):
    vehicles.sort(key=lambda x: x["price"])
    print("Sorted!")


def statistics(vehicles):
    if not vehicles:
        print("No data")
        return

    total = sum(v["price"] for v in vehicles)
    print("Total price:", total)


# ================= MENU =================
def menu():
    vehicles = load_from_txt()  # 👈 load ngay từ đầu

    while True:
        print("\n===== VEHICLE MANAGEMENT =====")
        print("1. Add vehicle")
        print("2. Display vehicles")
        print("3. Search vehicle")
        print("4. Sort by price")
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
            save_to_txt(vehicles)  # 👈 lưu sau khi sort

        elif choice == "5":
            statistics(vehicles)

        elif choice == "6":
            save_to_json(vehicles)
            print("Exported to JSON!")

        elif choice == "0":
            print("Bye!")
            break

        else:
            print("Invalid choice!")


# ================= RUN =================
if __name__ == "__main__":
    menu()