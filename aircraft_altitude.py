from aircraft import Aircraft

model = input("Enter aircraft model:\n")
aircraft = Aircraft(model)
while True:
    command = input("Enter command (A for ascent, D for descent, X to exit):\n")
    parts = command.split()
    if parts[0] == "A":
        aircraft.climb(int(parts[1]))
    elif parts[0] == "D":
        aircraft.descend(int(parts[1]))
    elif parts[0] == "X":
        break
print(f"Final altitude: {aircraft.altitude} feet")