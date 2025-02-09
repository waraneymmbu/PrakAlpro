import math

P = 200000000 
A = 400000000  
r = 0.10        
n = 12      

t = math.log(A / P) / (n * math.log(1 + (r / n)))

print(f"Waktu yang dibutuhkan agar uang Erika menjadi Rp 400 juta: {t:.2f} tahun")
