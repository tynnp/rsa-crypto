import random
import math
import os
import time

# Kiểm tra số nguyên tố
def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True

# Sinh số nguyên tố trong khoảng [min_val, max_val]
def generate_prime(min_val, max_val):
    while True:
        p = random.randint(min_val, max_val)
        if is_prime(p):
            return p

# Tìm số e sao cho gcd(e, phi) = 1
def find_e(phi):
    while True:
        e = random.randint(3, phi - 1)
        if math.gcd(e, phi) == 1:
            return e

# Tính nghịch đảo modulo: tìm d sao cho d*e ≡ 1 (mod m)
def modinv(a, m):
    def egcd(a, b):
        if a == 0:
            return (b, 0, 1)
        g, x, y = egcd(b % a, a)
        return (g, y - (b // a) * x, x)
    g, x, _ = egcd(a, m)
    return x % m

# Sinh khóa RSA
def generate_keys(min_prime=10000, max_prime=70000):
    p = generate_prime(min_prime, max_prime)
    q = generate_prime(min_prime, max_prime)
    while p == q:
        q = generate_prime(min_prime, max_prime)
        
    n = p * q
    phi = (p - 1) * (q - 1)
    e = find_e(phi)
    d = modinv(e, phi)
    return p, q, n, phi, e, d

# Hàm mã hóa: với mỗi byte m, tính c = m^e mod n
def encrypt(plaintext, e, n):
    return [pow(m, e, n) for m in plaintext]

# Hàm giải mã: với mỗi số c, tính m = c^d mod n
def decrypt(ciphertext, d, n):
    return [pow(c, d, n) for c in ciphertext]