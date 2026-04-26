def menu():
    print("\n===== VEHICLE RENTAL SYSTEM =====")
    print("1. Add Vehicle")
    print("0. Exit")


def main():
    while True:
        menu()
        choice = input("Choose: ")

        if choice == "0":
            break


if __name__ == "__main__":
    main()