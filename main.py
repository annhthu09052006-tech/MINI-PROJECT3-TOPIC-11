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

        if choice == "0":
            print("Goodbye!")
            break
        else:
            print("Feature not implemented yet!")


if __name__ == "__main__":
    menu()