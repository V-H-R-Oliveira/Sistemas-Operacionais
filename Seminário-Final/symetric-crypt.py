import string 

def menu():
    print("Cifra de cesar - strings com caracteres maiúsculos")

def generateAlphabet() -> dict:
    alpha: str = string.ascii_uppercase
    mapped: dict = {}

    for index, char in enumerate(alpha):
        mapped[char] = index
    
    return mapped

alpha: dict = generateAlphabet()
lookup: dict = dict((value,key) for key, value in alpha.items()) 

def encriptar(plaintext: str, rot: int = 3) -> str:
    ciphertext: str = ""

    for char in plaintext:
        if char == ' ':
            ciphertext += ' '
        else:
            ciphertext += lookup[(alpha[char] + rot) % 26]
    
    return ciphertext

def desencriptar(ciphertext: str, rot: int = 3) -> str:
    plaintext: str = ""

    for char in ciphertext:
        if char == ' ':
            plaintext += ' '
        else:
            plaintext += lookup[(alpha[char] - rot) % 26]
    return plaintext

def main():
    menu()
    
    while True:
        message: str = input("Digite a sua mensagem(! para terminar): ").upper()
        
        if message == '!':
            break

        rot: int = int(input("Digite a rotação (default=3): "))

        try:
            assert(message.isupper() and isinstance(rot, int))
        except AssertionError as error:
            print("Mensagem inválida ou rotação inválida")
            return 
    
        ciphertext: str = encriptar(message, rot)
        print("Mensagem cifrada:", ciphertext)
        plaintext: str = desencriptar(ciphertext, rot)
        print("Mensagem original:", plaintext)

if __name__  == "__main__":
    main()
