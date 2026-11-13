import json

with open("kb_wifi.json", "r", encoding="utf-8") as file:
    data = json.load(file)

aturan_list = data["aturan"]

semua_hasil = []
semua_syarat = []
for aturan in aturan_list:
    semua_hasil.append(aturan["maka"])
    for syarat in aturan["jika"]:
        semua_syarat.append(syarat)

pertanyaan = []
for syarat in semua_syarat:
    if syarat not in semua_hasil and syarat not in pertanyaan:
        pertanyaan.append(syarat)

kesimpulan_akhir = []
for hasil in semua_hasil:
    if hasil not in semua_syarat:
        kesimpulan_akhir.append(hasil)

print("=" * 60)
print(data["judul"])
print("=" * 60)
print("Jawab dengan 'y' (ya) atau 't' (tidak).\n")

memori = []
nomor = 1
for tanya in pertanyaan:
    jawaban = ""
    while jawaban != "y" and jawaban != "t":
        jawaban = input(str(nomor) + ". Apakah " + tanya + "? (y/t) > ").strip().lower()
        if jawaban != "y" and jawaban != "t":
            print("   Jawab hanya 'y' atau 't'.")
    if jawaban == "y":
        memori.append(tanya)
    nomor = nomor + 1

print()
if len(memori) > 0:
    print("Fakta awal: " + ", ".join(memori))
else:
    print("Fakta awal: tidak ada")
print("-" * 60)

jejak_alasan = {}   
siklus = 1

while True:
    aturan_cocok = None

    for aturan in aturan_list:
        if aturan["maka"] in memori:
            continue             

        if aturan["mode"] == "dan":
            terpenuhi = True
            for syarat in aturan["jika"]:
                if syarat not in memori:
                    terpenuhi = False
        else:
            terpenuhi = False
            for syarat in aturan["jika"]:
                if syarat in memori:
                    terpenuhi = True

        if terpenuhi:
            aturan_cocok = aturan
            break

    if aturan_cocok is None:
        print("Siklus " + str(siklus) + ": tidak ada aturan baru, berhenti.")
        break

    memori.append(aturan_cocok["maka"])
    jejak_alasan[aturan_cocok["maka"]] = aturan_cocok
    print("Siklus " + str(siklus) + ": " + aturan_cocok["id"] + " -> " + aturan_cocok["maka"])
    siklus = siklus + 1

def tampilkan_alasan(fakta, tingkat):
    aturan = jejak_alasan[fakta]

    syarat_terpenuhi = []
    for syarat in aturan["jika"]:
        if syarat in memori:
            syarat_terpenuhi.append(syarat)

    spasi = "  " * tingkat
    print(spasi + fakta + "  <- " + aturan["id"] + " (" + ", ".join(syarat_terpenuhi) + ") [" + aturan["sumber"] + "]")

    for syarat in syarat_terpenuhi:
        if syarat in jejak_alasan:
            tampilkan_alasan(syarat, tingkat + 1)


print("=" * 60)
hasil_akhir = []
for k in kesimpulan_akhir:
    if k in memori:
        hasil_akhir.append(k)

if len(hasil_akhir) > 0:
    print("KESIMPULAN:")
    for k in hasil_akhir:
        print("- " + k)
    print("\nALASAN:")
    for k in hasil_akhir:
        tampilkan_alasan(k, 1)
else:
    print("KESIMPULAN: penyebab belum dapat ditentukan dari jawaban Anda.")

print("\nCatatan batas keberlakuan:")
print(data["batas"])
