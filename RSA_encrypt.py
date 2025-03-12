from RSA_algorithm import *

# Lấy nội dung file cần mã hóa
print("-" * 100)
file_path = input("Nhập đường dẫn đến file cần mã hóa: ")
with open(file_path, "rb") as f:
    plaintext_bytes = f.read()
plaintext_int = list(plaintext_bytes)

# Lấy nội dung khóa công khai
pub_file = "public_key.json"
with open(pub_file, "r") as f:
    public_key = json.load(f)

e = public_key["e"]
n = public_key["n"]

# Thực hiện mã hóa và tạo thông điệp
ciphertext = encrypt(plaintext_int, e, n)
message = {
    "filename": os.path.basename(file_path),
    "ciphertext": ciphertext
}

# Ghi lại thông điệp đã được mã hóa
message_file = "message.json"
with open(message_file, "w") as f:
    json.dump(message, f, separators=(',', ': '))
print(f"file thông điệp được lưu tại {message_file}", "-" * 100, sep='\n')