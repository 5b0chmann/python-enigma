from mystery_box import Enigma

def main():

    print("=== Python Enigma ===")

    try:

        rotor1 = int(input("Rotor 1 (1-26): "))
        rotor2 = int(input("Rotor 2 (1-26): "))
        rotor3 = int(input("Rotor 3 (1-26): "))

        stecker = input("Steckbrett (z.B. AB): ").upper()

        text = input("Text: ")

        enigma = Enigma(
            rotor1=rotor1,
            rotor2=rotor2,
            rotor3=rotor3,
            steckbrett=stecker)

        ergebnis = enigma.codieren(text)

        print("\nErgebnis:")
        print(ergebnis)

    except ValueError as fehler:

        print(f"Fehler: {fehler}")

if __name__ == "__main__":
    main()