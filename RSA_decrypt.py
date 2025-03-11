from RSA_algorithm import *

# Lấy nội dung thông điệp 
print("-" * 100)
message_file = input("Nhập đường dẫn đến file thông điệp: ")
with open(message_file, "r") as f:
    message = json.load(f)

ciphertext = message["ciphertext"]
filename = message["filename"]

# Lấy nội dung khóa bí mật
priv_file = "private_key.json"
with open(priv_file, "r") as f:
    private_key = json.load(f)

d = private_key["d"]
n = private_key["n"]

# Thực hiện giải mã và chuyển về bytes
decrypted_int = decrypt(ciphertext, d, n)
file_bytes = bytes(decrypted_int)

# Lưu lại file đã giải mã
out_file = "decrypted_" + filename
with open(out_file, "wb") as f:
    f.write(file_bytes)
print(f"file đã được giải mã và lưu tại {out_file}", "-" * 100, sep='\n')