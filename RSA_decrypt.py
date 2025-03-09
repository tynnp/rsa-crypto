from RSA_algorithm import *

ciphertext_file = "ciphertext.txt"
with open(ciphertext_file, 'r') as f:
    ciphertext = ciphertext = list(map(int, f.read().split()))
    
# Lấy thông tin khóa và định dạng tệp
info = {}
with open("info.txt", 'r') as f:
    for line in f:
        if line.strip():
            k, v = line.split(':')
            info[k.strip()] = v.strip()

n = int(info["n"])
d = int(info["d"])
ext = info["ext"]
    
# Giải mã ciphertext
decrypted = decrypt(ciphertext, d, n)
decrypted_file = "decrypted" + ext
with open(decrypted_file, 'wb') as f:
    f.write(bytes(decrypted))
print(f"File đã giải mã đã được lưu tại: {decrypted_file}")
