import string
import secrets

class Task3:
    def generatedPassword():
        letters = string.ascii_letters
        digits = string.digits
        specialChars = string.punctuation
        selectionList = letters + digits + specialChars

        length = int(input("input the password length: "))

        while True:
            password = ''.join(secrets.choice(selectionList) for _ in range(length))
            if (any(char in specialChars for char in password) and sum(char in digits for char in password) >= 2):
                break

        print("auto generated password: ", password)

if __name__ == "__main__":
    Task3.generatedPassword()
