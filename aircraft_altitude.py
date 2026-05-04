from aircraft import Aircraft

def main():
    model = input("Enter aircraft model: ")
    avion = Aircraft(model)

    while True:

        user_input = input("Enter command (A for ascent, D for descent, X to exit): ")

        if user_input == "X":
            break

        parts = user_input.split()
        command = parts[0]
        feet = int(parts[1])

        if command == "A":
            avion.ascent(feet)
        elif command == "D":
            avion.descent(feet)

    print(f"Final altitude: {avion.altitude} feet")

if __name__ == "__main__":
    main()