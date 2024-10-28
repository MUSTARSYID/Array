# Deklarasi matriks
matriks = []

# Meminta input pengguna untuk mengisi matrix 3x3
print("masukkan elemen untuk matrix 3x3:")
for i in range(3):
    baris = []
    for j in range(3):
        nilai =int(input(f"Masukkan elemen baris {i+1}, kolom {j+1}"))
        baris.append(nilai)
    matriks.append(baris)
    
# Transpose matrix 
transpose = []
for i in range(3):
    baris = []
    for j in range(3):
        baris.append(matriks[j][i])
    transpose.append(baris)
    
# Menampilkan hasil transpose
print("\nHasil transpose matriks:")
for baris in transpose:
    print(baris)                