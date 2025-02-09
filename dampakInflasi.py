PV = float(input("jumlah uang saat ini (Rp): "))
r = float(input("tingkat inflasi tahunan (%): ")) / 100
t = int(input("jumlah tahun ke depan: "))

print("\nTahun | Nilai Uang")
print("---------------------")

for tahun in range(t + 1):
    print(f"{tahun} | Rp {PV}")
    PV *= (1 - r)

print(f"\nSetelah {t} tahun dengan inflasi {r*100:.2f}%, uang berjumlah Rp {PV:,.2f} tinggal bernilai Rp {PV:,.2f}")
