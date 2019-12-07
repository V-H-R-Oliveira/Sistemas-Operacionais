import math, random, datetime, time, sys

random.seed(datetime.datetime.now())

def sieve() -> list:
    n: int = 500
    values: list = [True for i in range(n + 1)]
    maxRange: int = int(math.sqrt(n))
    primes: list = []

    for i in range(2, maxRange + 1):
        if values[i]:
            for j in range(i ** 2, n + 1, i):
                values[j] = False

    for i in range(2, n + 1):
        if values[i]:
            primes.append(i)

    return primes

primes: list = sieve()

def genKeys() -> tuple:
    while True:
        p: int = primes[random.randint(0, len(primes) - 1)]
        time.sleep(1)
        q: int = primes[random.randint(0, len(primes) - 1)]
    
        try:
            assert(p != q)
            n: int = p * q
            phi: int = (p - 1) * (q - 1) 
            e: int = random.randrange(1, phi)
            g: int = math.gcd(e, phi)

            if g != 1:
                while g != 1: # verifica se é coprimo
                    e = random.randrange(1, phi)
                    g = math.gcd(e, phi)
            else:
                MMI = lambda A, n,s=1,t=0,N=0: (n < 2 and t%N or MMI(n, A%n, t, s-A//n*t, N or n),-1)[n<1] # inverso multiplicativo modular
                d: int = MMI(e, phi)
                assert(d != e)
                return ((e, n), (d, n)) # e, n => public key e d, n = private key
        except AssertionError as error:
            continue

# https://www.geeksforgeeks.org/modular-exponentiation-power-in-modular-arithmetic/
def modularPower(x: int, y: int, p: int) -> int: 
    res: int = 1   
    x %= p  
    while y > 0: 
        if (y & 1) == 1: 
            res = (res * x) % p 
        y >>= 1     
        x = (x * x) % p 
    return res 

def encrypt(publicPair: tuple, plaintext: str) -> list:
    key, n = publicPair
    cipherbuffer: list = [modularPower(ord(char), key, n) for char in plaintext]
    return cipherbuffer

def decrypt(privatePair: tuple, cipherbuffer: list) -> list:
    key, n = privatePair
    plaintext: str = ""
    plaintextbuffer: list = [modularPower(byte, key, n) for byte in cipherbuffer]
    
    for byte in plaintextbuffer:
        plaintext += chr(byte)
    return plaintext

def hexDigest(buffer: list) -> str:
    digest: str = ""
    for byte in buffer:
        digest += format(byte, "04x")
    return digest

def main():
    if len(sys.argv) == 2:
        publicPair, privatePair = genKeys()
        print("Public key pair:", publicPair)
        print("Private key pair:", privatePair)
        encodedBuffer: list = encrypt(publicPair, sys.argv[1])
        decoded: str = decrypt(privatePair, encodedBuffer)
        print("Hex digest da mensagem encriptada:", hexDigest(encodedBuffer))
        print("Mensagem decodificada: ", decoded, sep="\n")
    else:
        print("uso: {} <mensagem>".format(sys.argv[0]))
if __name__ == "__main__":
    main()
