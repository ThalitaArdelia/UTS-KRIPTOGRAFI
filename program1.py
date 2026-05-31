import hashlib
import os

def hitung_hash(nama_file, algoritma):
    hash_obj = hashlib.new(algoritma)

    try:
        with open(nama_file, "rb") as file:
            while True:
                data = file.read(4096)

                if not data:
                    break

                hash_obj.update(data)

        return hash_obj.hexdigest()

    except FileNotFoundError:
        return None
    
def bandingkan_hash(hash1, hash2):

    if hash1 == hash2:
        return "File Sama / Tidak Berubah"

    else:
        return "File Berubah / Integritas Berubah"

print("=" * 50)
print(" APLIKASI PENGECEKAN INTEGRITAS FILE ")
print(" Menggunakan MD5 dan SHA-256 ")
print("=" * 50)

# Input file
file_asli = input("\nMasukkan nama file asli      : ")
file_modif = input("Masukkan file modifikasi    : ")

# Cek file ada atau tidak
if not os.path.exists(file_asli):
    print("\nFile asli tidak ditemukan!")
    exit()

if not os.path.exists(file_modif):
    print("\nFile modifikasi tidak ditemukan!")
    exit()

md5_asli = hitung_hash(file_asli, "md5")
md5_modif = hitung_hash(file_modif, "md5")

sha_asli = hitung_hash(file_asli, "sha256")
sha_modif = hitung_hash(file_modif, "sha256")

print("\n")
print("=" * 50)
print("HASIL HASH MD5")
print("=" * 50)

print("MD5 File Asli       :", md5_asli)
print("MD5 File Modifikasi :", md5_modif)

print("\nStatus MD5 :", bandingkan_hash(
    md5_asli,
    md5_modif
))

print("\n")
print("=" * 50)
print("HASIL HASH SHA-256")
print("=" * 50)

print("SHA-256 File Asli       :", sha_asli)
print("SHA-256 File Modifikasi :", sha_modif)

print("\nStatus SHA-256 :", bandingkan_hash(
    sha_asli,
    sha_modif
))

print("\n")
print("=" * 50)

if md5_asli == md5_modif and sha_asli == sha_modif:

    print("KESIMPULAN : FILE MASIH ASLI")

else:

    print("KESIMPULAN : FILE SUDAH DIMODIFIKASI")

print("=" * 50)