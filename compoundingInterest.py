import math

P = 200_000_000 
A = 400_000_000  
r = 0.10        
n = 12      

t = math.log(A / P) / (n * math.log(1 + (r / n)))

print(f"Waktu yang dibutuhkan agar uang Erika menjadi Rp 400 juta: {t:.2f} tahun")
