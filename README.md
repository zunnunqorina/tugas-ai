# Tugas 5 – Sistem Pakar Gangguan WiFi di Rumah
a
**Nama:ZUNNUN QORINA** 
**NIM: F1D02410030** 

## 1. Topik dan cara menjalankan

Program menanyakan 7 hal tentang kondisi WiFi di rumah (jawab `y` atau `t`), lalu menyimpulkan kemungkinan penyebab gangguan beserta alasannya.

- Bahasa: Python 3 (diuji dengan Python 3.12.3), hanya memakai modul bawaan `json`.
- File: `main.py` (program) dan `kb_wifi.json` (aturan dan sumber).
- Menjalankan, di folder repository:

```
python main.py
```

## 2. Sumber

| ID | Judul | Penerbit | URL | Diakses |
|----|-------|----------|-----|---------|
| S1 | Slow Internet or Network Performance: Diagnosing and Improving Slow Connections | Oklahoma State University IT | https://services.okstate.edu/TDClient/856/Portal/KB/Article/20802/Slow-Internet-or-Network-Performance-Diagnosing-and-Improving-Slow-Connections | 13 Nov 2026 |
| S2 | Troubleshooting Basic Problems with WIFI/Connection | Clemson University | https://forever.clemson.edu/di/self-service/connecting | 13 Nov 2026 |
| S3 | My Network Connection is Slow: Troubleshooting Slow Network | University of Wyoming IT | https://uwyo.teamdynamix.com/TDClient/1940/Portal/KB/PrintArticle?ID=143600 | 13 Nov 2026 |

Aturan ditulis dengan kalimat sendiri (parafrasa) dalam bahasa Indonesia, bukan kutipan.

## 3. Tabel aturan

| Aturan | IF | THEN | Sumber |
|--------|----|------|--------|
| R1 | posisi jauh dari router/terhalang dinding **OR** sinyal WiFi di perangkat lemah | sinyal WiFi bermasalah | S1, S2 |
| R2 | banyak perangkat terhubung **OR** ada unduhan/pembaruan besar | bandwidth terpakai banyak | S1 |
| R3 | sinyal WiFi bermasalah **AND** internet normal saat memakai kabel LAN | **penyebab: sinyal WiFi lemah** | S2, S3 |
| R4 | bandwidth terpakai banyak **AND** internet lambat di semua perangkat | **penyebab: bandwidth terbagi terlalu banyak** | S1 |
| R5 | internet lambat di semua perangkat **AND** masalah tetap ada setelah modem dan router di-restart | **penyebab: gangguan dari penyedia internet (ISP)** | S2 |

- 5 aturan, 3 kesimpulan akhir (R3, R4, R5).
- Rantai aturan: hasil R1 dipakai R3, hasil R2 dipakai R4.

## 4. Metode: Forward Chaining

Dipilih karena semua fakta sudah diketahui dari jawaban pengguna di awal, lalu aturan dijalankan dari fakta menuju kesimpulan (data-driven).

Langkah program:
1. Baca `kb_wifi.json`.
2. Fakta yang tidak pernah menjadi hasil aturan (R1 sampai R5) ditanyakan ke pengguna.
3. Jawaban `y` disimpan di `memori`.
4. Ulangi: ambil aturan pertama yang syaratnya terpenuhi (`dan` = semua syarat ada, `atau` = salah satu ada) dan hasilnya belum ada di memori. Tambahkan hasilnya ke memori dan catat aturannya.
5. Berhenti jika tidak ada aturan yang cocok.
6. Tampilkan kesimpulan akhir dan alasannya (aturan yang dipakai).

## 5. Kasus uji

Urutan pertanyaan: (1) posisi jauh/terhalang, (2) sinyal lemah, (3) banyak perangkat, (4) unduhan besar, (5) normal saat kabel LAN, (6) lambat di semua perangkat, (7) tetap bermasalah setelah restart.

| # | Jawaban "ya" | Kesimpulan yang diharapkan |
|---|--------------|----------------------------|
| 1 | no. 1 dan 5 | sinyal WiFi lemah |
| 2 | no. 6 saja | tidak ada (kasus negatif) |
| 3 | no. 3, 6, 7 | bandwidth terbagi terlalu banyak dan gangguan ISP |

### Kasus 1
![Kasus 1](screenshot/kasus1.png)

```
Siklus 1: R1 -> sinyal WiFi bermasalah
Siklus 2: R3 -> penyebab: sinyal WiFi lemah (saran: dekatkan perangkat atau pindahkan router)
Siklus 3: tidak ada aturan baru, berhenti.
ALASAN:
  penyebab: sinyal WiFi lemah ...  <- R3 (sinyal WiFi bermasalah, internet normal saat memakai kabel LAN) [S2, S3]
    sinyal WiFi bermasalah  <- R1 (posisi Anda jauh dari router atau terhalang banyak dinding) [S1, S2]
```

### Kasus 2 (negatif)
![Kasus 2](screenshot/kasus2.png)

```
Siklus 1: tidak ada aturan baru, berhenti.
KESIMPULAN: penyebab belum dapat ditentukan dari jawaban Anda.
```

### Kasus 3
![Kasus 3](screenshot/kasus3.png)

```
Siklus 1: R2 -> bandwidth terpakai banyak
Siklus 2: R4 -> penyebab: bandwidth terbagi terlalu banyak ...
Siklus 3: R5 -> penyebab: gangguan dari penyedia internet (saran: hubungi ISP)
Siklus 4: tidak ada aturan baru, berhenti.
```

## 6. Batas keberlakuan

Pengetahuan dalam sistem ini berasal dari tiga panduan layanan TI universitas (Oklahoma State University, Clemson University, dan University of Wyoming) untuk menangani WiFi rumahan. Aturannya sudah disederhanakan dan hanya mencakup tiga penyebab: sinyal lemah, bandwidth terbagi terlalu banyak, dan gangguan dari penyedia internet. Penyebab lain seperti router rusak, interferensi perangkat lain, atau kerusakan kabel tidak tercakup. Hasilnya hanya saran awal untuk membantu pengguna, bukan keputusan akhir; jika masalah berlanjut, hubungi penyedia internet atau teknisi. Catatan ini juga ditampilkan di akhir program.

## 7. Penggunaan alat bantu AI

(Sesuaikan dengan yang benar-benar terjadi.) Saya memakai Claude untuk membantu mencari sumber, menyusun aturan, menyederhanakan kode `main.py`, dan membuat draf README. Saya sudah membaca dan memahami kode serta aturannya.
