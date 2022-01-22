# simple cipher encryption using class methods and objects
class cipher:
    # initializing the variables only need to set shift number
    def __init__(self, shift):
        try:
            self.text = ""
            self.shift = int(shift)
            self.result = ""
        except ValueError:
            print(f"Enter integer for shift count {shift} is not acceptable")

    # method to encrypt text
    def encrypt(self, text):
        # text is initialized here so it can be passed on latter
        self.text = text
        result = ""
        for i in range(len(text)):
            char = text[i]
            if char == " ":
                result += " "
            elif char.isupper():
                result += chr((ord(char) + self.shift - 65) % 26 + 65)
            else:
                result += chr((ord(char) + self.shift - 97) % 26 + 97)
        return result

    def decrypt(self):
        result = ""
        # encrypting the text, so it can be decrypted using this method
        text = self.encrypt(self.text)
        s = 26 - self.shift
        for i in range(len(text)):
            char = text[i]
            if char == " ":
                result += " "
            elif char.isupper():
                result += chr((ord(char) + s - 65) % 26 + 65)
            else:
                result += chr((ord(char) + s - 97) % 26 + 97)
        return result


# change number(0<x<26) and text
test = cipher(2)
encrypted = test.encrypt("Cipher text is changed")
decrypted = test.decrypt()

print(f"""Shift: {test.shift}
Encrypted: {encrypted}
Decrypted: {decrypted}""")
