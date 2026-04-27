import json
import os

TXT_FILE = "data.txt"
JSON_FILE = "data.json"


# ================= SYSTEM =================
def clear_screen():
    os.system("cls" if os.name == "nt" else "clear")


def display_menu():
    clear_screen()
    print("\n" + "=" * 60)
    print("        🚗 VEHICLE MANAGEMENT SYSTEM 🚗")
    print("=" * 60)
    print("1. Add new vehicle")
    print("2. Display all vehicles")
    print("3. Search vehicle by name")
    print("4. Sort vehicles by price")
    print("5. Show statistics")
    print("6. Save to TXT file")
    print("7. Load from TXT file")
    print("8. Advanced search")
    print("9. Export to JSON")
    print("0. Exit")
    print("=" * 60)


# ================= FILE =================
def save_to_txt(vehicles):
    with open(TXT_FILE, "w") as f:
        for v in vehicles:
            f.write(f"{v['id']}|{v['name']}|{v['type']}|{v['price']}|{v['status']}\n")
    print("Saved to TXT!")


def load_from_txt():
    vehicles = []
    if not os.path.exists(TXT_FILE):
        print("No file found!")
        return vehicles

    with open(TXT_FILE, "r") as f:
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
    print("Loaded from TXT!")
    return vehicles


def export_json(vehicles):
    with open(JSON_FILE, "w") as f:
        json.dump(vehicles, f, indent=4)
    print("Exported JSON!")


# ================= CORE =================
def add_vehicle(vehicles):
    vid = input("Enter ID: ").strip()

    for v in vehicles:
        if v["id"] == vid:
            print("ID already exists!")
            return

    name = input("Enter name: ")
    vtype = input("Enter type: ")

    try:
        price = float(input("Enter price: "))
    except:
        print("Invalid price!")
        return

    status = input("Enter status (Available/Rented): ")

    vehicles.append({
        "id": vid,
        "name": name,
        "type": vtype,
        "price": price,
        "status": status
    })

    print("Added!")


def display_vehicles(vehicles):
    if not vehicles:
        print("No data!")
        return

    print(f"{'ID':<10}{'Name':<20}{'Type':<15}{'Price':<10}{'Status':<10}")
    print("-" * 65)

    for v in vehicles:
        print(f"{v['id']:<10}{v['name']:<20}{v['type']:<15}{v['price']:<10}{v['status']:<10}")


# ================= SEARCH =================
def search_vehicle(vehicles):
    keyword = input("Enter name: ").lower()
    result = [v for v in vehicles if keyword in v["name"].lower()]
    display_vehicles(result)


# ================= SORT (FIX CHUẨN) =================
def sort_vehicles(vehicles):
    if not vehicles:
        print("No data!")
        return

    print("1. Ascending (Low → High)")
    print("2. Descending (High → Low)")
    opt = input("Choose: ")

    if opt == "1":
        vehicles.sort(key=lambda x: x["price"])
        print("Sorted ascending!")
    elif opt == "2":
        vehicles.sort(key=lambda x: x["price"], reverse=True)
        print("Sorted descending!")
    else:
        print("Invalid choice!")
        return

    # 👉 IN RA SAU KHI SORT (QUAN TRỌNG)
    display_vehicles(vehicles)


# ================= STAT =================
def statistics(vehicles):
    if not vehicles:
        print("No data!")
        return

    total = sum(v["price"] for v in vehicles)
    avg = total / len(vehicles)

    print("Total vehicles:", len(vehicles))
    print("Average price:", round(avg, 2))


# ================= ADVANCED =================
def advanced_search(vehicles):
    keyword = input("Keyword: ").lower()
    result = [
        v for v in vehicles
        if keyword in v["name"].lower() or keyword in v["type"].lower()
    ]
    display_vehicles(result)


# ================= MAIN =================
def main():
    vehicles = []

    while True:
        display_menu()
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
            save_to_txt(vehicles)
        elif choice == "7":
            vehicles = load_from_txt()
        elif choice == "8":
            advanced_search(vehicles)
        elif choice == "9":
            export_json(vehicles)
        elif choice == "0":
            print("Bye!")
            break
        else:
            print("Invalid!")

        input("\nPress Enter to continue...")


if __name__ == "__main__":
    main()
    
