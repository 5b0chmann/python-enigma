import string

class Enigma:

    def __init__(self,
                 rotor1,
                 rotor2,
                 rotor3,
                steckbrett):

        if not(1 <= rotor1 <= 26):
            raise ValueError("Rotor 1 muss zwischen 1 und 26 liegen")
        if not(1 <= rotor2 <= 26):
            raise ValueError("Rotor 2 muss zwischen 1 und 26 liegen")
        if not(1 <= rotor3 <= 26):
            raise ValueError("Rotor 3 muss zwischen 1 und 26 liegen")

        self.rotor1 = rotor1
        self.rotor2 = rotor2
        self.rotor3 = rotor3

        self.steckbrett = {}

        if len(steckbrett) == 2:

            a = steckbrett[0].upper()
            b = steckbrett[1].upper()

            self.steckbrett[a] = b
            self.steckbrett[b] = a

        # Feste Verdrahtung des Reflektors

        self.reflektor_mapping = {
            "A": "Y",
            "Y": "A",

            "B": "R",
            "R": "B",

            "C": "U",
            "U": "C",

            "D": "H",
            "H": "D",

            "E": "Q",
            "Q": "E",

            "F": "S",
            "S": "F",

            "G": "L",
            "L": "G",

            "I": "P",
            "P": "I",

            "J": "X",
            "X": "J",

            "K": "N",
            "N": "K",

            "M": "O",
            "O": "M",

            "T": "Z",
            "Z": "T",

            "V": "W",
            "W": "V"
        }

    def vorbereiten(self, text):
    
            text = text.upper()
    
            text = text.replace("Ä", "AE")
            text = text.replace("Ö", "OE")
            text = text.replace("Ü", "UE")
            text = text.replace("ß", "SS")
    
            return text

    def stecker_anwenden(self, text):

        ergebnis = ""

        for buchstabe in text:

            if buchstabe in self.steckbrett:
                ergebnis += self.steckbrett[buchstabe]
            else:
                ergebnis += buchstabe

        return ergebnis

    def rotor_drehen(self):

        self.rotor1 += 1

        if self.rotor1 > 26:
            self.rotor1 = 1
            self.rotor2 += 1

            if self.rotor2 > 26:
                self.rotor2 = 1
                self.rotor3 += 1

                if self.rotor3 > 26:
                    self.rotor3 = 1

    def reflektor(self, pos):

        buchstabe = chr(pos + ord('A'))

        buchstabe = self.reflektor_mapping[buchstabe]

        return ord(buchstabe) - ord('A')

    def codieren(self, text):

        text = self.vorbereiten(text)

        text = self.stecker_anwenden(text)

        ergebnis = ""

        for buchstabe in text:

            if buchstabe in string.ascii_uppercase:

                pos = ord(buchstabe) - ord('A')

                # Hinweg

                pos = (pos + self.rotor1) % 26
                pos = (pos + self.rotor2) % 26
                pos = (pos + self.rotor3) % 26

                # Reflektor

                pos = self.reflektor(pos)

                # Rückweg

                pos = (pos - self.rotor3) % 26
                pos = (pos - self.rotor2) % 26
                pos = (pos - self.rotor1) % 26

                ergebnis += chr(pos + ord('A'))

                self.rotor_drehen()
            else:
                ergebnis += buchstabe

        ergebnis = self.stecker_anwenden(ergebnis)

        return ergebnis
