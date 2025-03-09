from RSA_algorithm import *

# Phân tích số nguyên tố n
def factor_n(n):
    if n % 2 == 0:
        return 2, n // 2
    limit = int(math.sqrt(n)) + 1
    for i in range(3, limit, 2):
        if n % i == 0:
            return i, n // i
    return None, None

info_file = "info.txt"
info = {}
with open(info_file, 'r') as f:
    for line in f:
        if line.strip():
            k, v = line.strip().split(':')
            info[k.strip()] = v.strip()
                
n = int(info["n"])
d = int(info["d"])
ext = info["ext"]

print("-" * 100)
print(f"Bắt đầu phân tích n = {n}")
start_time = time.time()
    
p, q = factor_n(n)
phi = (p - 1) * (q - 1)
e = modinv(d, phi)

print(f"Tìm được p = {p} và q = {q}")
print(f"Tính được phi(n) = {phi}")
print(f"Tính được e = {e}")
    
ciphertext_file = "ciphertext.txt"
with open(ciphertext_file, 'r') as f:
    ciphertext = list(map(int, f.read().split()))
        
# Giải mã ciphertext sử dụng khóa riêng d ban đầu và n
decrypted = decrypt(ciphertext, d, n)
decrypted_file = "attacked_decrypted" + ext
with open(decrypted_file, 'wb') as f:
    f.write(bytes(decrypted))
    
elapsed_time = time.time() - start_time
print(f"File đã được giải mã thành công tại: {decrypted_file}")
print(f"Thời gian thực hiện phân tích: {elapsed_time:.6f} giây")
print("-" * 100)