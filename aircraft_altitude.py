from aircraft import Aircraft

def main():
    model_name = input("Enter aircraft model: ")
    avion = Aircraft(model_name)

    while True:
        entrada = input("Enter command (A for ascent, D for descent, X to exit): ")

        if entrada == 'X':
            break

        partes = entrada.split()
        comando = partes[0]
        pies = int(partes[1])

        if comando == 'A':
            avion.ascent(pies)
        elif comando == 'D':
            avion.descent(pies)
    print("Final altitude:", avion.altitude, "feet")

if __name__ == "__main__":
    main()