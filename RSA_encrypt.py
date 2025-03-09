from RSA_algorithm import *

input_file = input("Nhập đường dẫn file cần mã hóa: ").strip()
base, ext = os.path.splitext(input_file)

with open(input_file, 'rb') as f:
    plaintext = f.read()
    
plaintext_file = "plaintext.txt"
with open(plaintext_file, 'w') as f:
    f.write(" ".join(map(str, plaintext)))
print("Bản rõ đã được lưu tại:", plaintext_file)
    
# Sinh khóa RSA:
p, q, n, phi, e, d = generate_keys(min_prime = 10000000, max_prime = 70000000)

print("-" * 100)
print("Thông tin mã hóa:")
print(f"p = {p}")
print(f"q = {q}")
print(f"n = {n}")
print(f"phi(n) = {phi}")
print(f"e = {e}")
print(f"d = {d}")
print(f"-> Khóa công khai: ({e}, {n})")
print(f"-> Khóa bí mật: ({d, n})")
    
# Lưu thông tin khóa và định dạng file
info = {
    "p": p, 
    "q": q,
    "n": n, 
    "phi": phi,
    "e": e,
    "d": d, 
    "ext": ext
}

with open("info.txt", 'w') as f:
    for k, v in info.items():
        f.write(f"{k}:{v}\n")
print("Thông tin khóa và định dạng file được lưu tại info.txt")

# Mã hóa và lưu lại dưới dàn file
ciphertext = encrypt(plaintext, e, n)
ciphertext_file = "ciphertext.txt"
with open(ciphertext_file, 'w') as f:
    f.write(" ".join(map(str, ciphertext)))
print(f"Bản mã đã được lưu tại: {ciphertext_file}")
print("-" * 100)