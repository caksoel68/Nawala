# Panduan Pengguna Modul Payroll Indonesia (TER)

## Pendahuluan
Modul ini dirancang untuk menghitung PPh 21 menggunakan skema Tarif Efektif Rata-rata (TER) sesuai PP 58 Tahun 2023.

## Konfigurasi Awal

1. **Setting Karyawan & Kontrak**
   - Buka menu **Employees > Contracts**.
   - Pada form Contract, pastikan field **Status PTKP** diisi dengan benar (misal: TK/0, K/1).
   - Sistem akan otomatis menentukan **Kategori TER** (A, B, atau C).

2. **Master Data Tarif TER**
   - Masuk ke **Payroll > Configuration > Tarif Efektif (TER)**.
   - Pastikan data tarif sudah terisi (Import file CSV jika kosong).

## Cara Penggunaan

1. Buat **Payslip** baru untuk karyawan.
2. Pastikan periode adalah **Januari - November**.
3. Klik **Compute Sheet**.
4. Sistem akan mencari Salary Rule `PPH21_TER`.
5. Sistem otomatis melihat Penghasilan Bruto (GROSS) dan mencocokkan dengan tabel TER sesuai kategori karyawan.
6. Potongan pajak akan muncul otomatis di tab Salary Computation.