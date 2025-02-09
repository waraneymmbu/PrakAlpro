harga_beli_per_gram = 650000
jumlah_emas_awal = 25
total_beli_awal = harga_beli_per_gram * jumlah_emas_awal

harga_jual_per_gram = 685000
total_jual_awal = harga_jual_per_gram * jumlah_emas_awal

keuntungan_rp_pertama = total_jual_awal - total_beli_awal
keuntungan_persen_pertama = (keuntungan_rp_pertama / total_beli_awal) * 100

print("Keuntungan pertama: Rp {keuntungan_rp_pertama:,} ({keuntungan_persen_pertama:.2f}%)")

jumlah_emas_tambahan = 15
harga_beli_tambahan = 685000
total_beli_tambahan = harga_beli_tambahan * jumlah_emas_tambahan

jumlah_emas_total = jumlah_emas_awal + jumlah_emas_tambahan

total_investasi = total_beli_awal + total_beli_tambahan

harga_jual_terbaru = 715000
total_jual_terbaru = harga_jual_terbaru * jumlah_emas_total

keuntungan_rp_kedua = total_jual_terbaru - total_investasi
keuntungan_persen_kedua = (keuntungan_rp_kedua / total_investasi) * 100

print("Keuntungan total setelah harga emas naik: Rp {keuntungan_rp_kedua:,} ({keuntungan_persen_kedua:.2f}%)")
