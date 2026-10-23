# Fungsi menghitung rata-rata
def rata_rata(data):
    if len(data) == 0:
        return 0
    return sum(data) / len(data)


# Fungsi mencari nilai yang lulus
def nilai_lulus(data, batas=60):
    hasil = []

    for nilai in data:
        if nilai >= batas:
            hasil.append(nilai)

    return hasil


# Data nilai mahasiswa
nilai = [78, 55, 90, 67, 60, 82, 45, 71, 88, 59]

# Pengolahan data
lulus = nilai_lulus(nilai)

banyak_data = len(nilai)
total = sum(nilai)
rata = rata_rata(nilai)
minimum = min(nilai)
maksimum = max(nilai)

jumlah_lulus = len(lulus)
jumlah_tidak_lulus = banyak_data - jumlah_lulus

# Output
print("=" * 40)
print("ANALISIS NILAI MAHASISWA")
print("=" * 40)

print(f"Data Nilai      : {nilai}")
print(f"Banyak Data     : {banyak_data}")
print(f"Total Nilai     : {total}")
print(f"Rata-rata       : {rata:.2f}")
print(f"Nilai Minimum   : {minimum}")
print(f"Nilai Maksimum  : {maksimum}")
print(f"Nilai Lulus     : {lulus}")
print(f"Jumlah Lulus    : {jumlah_lulus}")
print(f"Belum Lulus     : {jumlah_tidak_lulus}")