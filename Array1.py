# Deklarasi array untuk menyimpan nilai 
nilai_siswa = []

# Meminta input nilai dari pengguna 
for i in range(5):
    nilai= float(input(f"Masukkan nilai siswa ke-{i+1}: "))
    nilai_siswa.append(nilai)
    
# Menghitung total nilai 
total_nilai = sum(nilai_siswa)

# Menghitung rata-rata
rata_rata = total_nilai / len(nilai_siswa)

# Menampilkan hasil rata-rata
print(f"Rata-rata nilai siswa adalah: {rata_rata}")