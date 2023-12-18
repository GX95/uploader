# Python File Uploader

Program ini adalah alat sederhana untuk mengunggah file ke layanan file.io melalui baris perintah.

## Instalasi
1. Pastikan Python telah terinstal di sistem Anda.
2. Unduh repositori ini atau gunakan `git clone`.
3. Buka terminal dan arahkan ke direktori program.
4. Jalankan perintah berikut:
   ```bash
   pip install -r requirements.txt
   python setup.py install
   ```

## Penggunaan
```bash
upload /path/to/file.txt --exp 1h
```

### Argumen
- `file`: Path ke file yang akan diunggah.
- `--exp`: Waktu kedaluwarsa (default: 10h). Contoh: 1h, 2d.

## Contoh
```bash
upload /path/to/example.txt --exp 2d
```
