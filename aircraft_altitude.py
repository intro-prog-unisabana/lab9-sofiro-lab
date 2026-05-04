from aircraft import Aircraft

def main():
    model_input = input("Enter aircraft model: ")
    my_aircraft = Aircraft(model_input)

    while True:
        line = input("Enter command (A for ascent, D for descent, X to exit): ")
        
        line = line.strip()
        if not line:
            continue
            
        parts = line.split()
        command = parts[0].upper()

        if command == 'X':
            break
            
        if len(parts) >= 2:
            try:
                feet = int(parts[1])
                if command == 'A':
                    my_aircraft.ascent(feet)
                elif command == 'D':
                    my_aircraft.descent(feet)
            except ValueError:
                pass 

    print(f"Final altitude: {my_aircraft.altitude} feet")

if __name__ == "__main__":
    main()