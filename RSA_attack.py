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

# Lấy khóa nội dung công khai
pub_file = "public_key.json"
with open(pub_file, "r") as f:
    public_key = json.load(f)

e = public_key["e"]
n = public_key["n"]        

# Lấy thông nội dung dung điệp
print("-" * 100)
message_file = input("Nhập đường dẫn đến file thông điệp: ")
with open(message_file, "r") as f:
    message = json.load(f)

ciphertext = message["ciphertext"]
filename = message["filename"]

# Bắt đầu thám mã
start_time = time.time()
print(f"Bắt đầu phân tích n = {n}")

p, q = factor_n(n)
phi = (p - 1) * (q - 1)
d = modinv(e, phi)

print(f"Tìm được p = {p} và q = {q}")
print(f"Tính được phi(n) = {phi}")
print(f"Tính được d = {d}")
    
decrypted_int = decrypt(ciphertext, d, n)
file_bytes = bytes(decrypted_int)
elapsed_time = time.time() - start_time

# Kết thúc thám mã và lưu lại kết quả 
out_file = "decrypted_" + filename
with open(out_file, "wb") as f:
    f.write(file_bytes)
print(f"file đã được giải mã và lưu tại {out_file}")
print(f"Thời gian thực hiện thám mã: {elapsed_time:.6f} giây", "-" * 100, sep='\n')