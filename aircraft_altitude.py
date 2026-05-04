from aircraft import Aircraft

def main():
    model = input("Enter aircraft model:\n")
    aircraft = Aircraft(model)

    while True:
        command = input("Enter command (A for ascent, D for descent, X to exit):\n")

        if command.strip().upper() == "X":
            break

        parts = command.split()

        if len(parts) != 2:
            continue

        action, value = parts
        feet = int(value)

        if action.upper() == "A":
            aircraft.ascend(feet)
        elif action.upper() == "D":
            aircraft.descend(feet)

    print(f"Final altitude: {aircraft.get_altitude()} feet")


if __name__ == "__main__":
    main()