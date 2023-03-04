#coding: utf-8
# module
import os,sys,time,getpass,json,requests,socket,tqdm,datetime
from tqdm import tqdm
import pathlib
import os.path
from signal import signal, SIGINT
from sys import exit
from datetime import date
#Warna
red   = '\x1b[31m' # Merah
green = '\x1b[32m' # Hijau
yellow = '\x1b[33m' # Kuning
blue  = '\x1b[34m' # Biru
magenta = '\x1b[35m' # Ungu
cyan  = '\x1b[36m' # Biru Muda
white = '\x1b[37m' # Putih
reset = '\x1b[39m' # Reset Warna ( Kembali Ke Warna Awal )
brblack = '\x1b[90m' # Hitam Terang
R = '\x1b[91m' # Merah Terang
brgreen = '\x1b[92m' # Hijau Terang
k = '\x1b[93m' # Kuning Terang
brblue = '\x1b[94m' # Biru Terang
brmgnt = '\x1b[95m' # Ungu Terang
brcyan = '\x1b[96m' # Biru Muda Terang
G = '\x1b[97m' # Putih Terang# username
x = "bima"
y = "bima"
ulang = 99999
hostname=socket.gethostname()   
IPAddr=socket.gethostbyname(hostname) 
today = date.today()

#API
def api():
  sp("Total API aktif : 2")
  sp("List: SayurBox,Carsome")
  time.sleep(3)
  spammer()
  

# mengetik otomatis cepat
def sp(a):
  for e in a + "\n":
    sys.stdout.write(e)
    sys.stdout.flush()
    time.sleep(0.002)

#spam
def spammer():
  os.system("reset")
  os.system("clear")
  sp("\x1b[91m[!]\x1b[92mPeringatan! (Gunakan awalan 8xxxx)")
  sp("")

  no = input("\x1b[96mNomor Target : ")

  if no =="":
    sp("Tidak boleh kosong!")
    time.sleep(2)
    spammer()


  head = {"Host": "www.sayurbox.com",
  "content-length": "289",
  "sec-ch-ua-mobile": "?1",
  "authorization": "eyJhbGciOiJSUzI1NiIsImtpZCI6ImY4NDY2MjEyMTQxMjQ4NzUxOWJiZjhlYWQ4ZGZiYjM3ODYwMjk5ZDciLCJ0eXAiOiJKV1QifQ.eyJhbm9ueW1vdXMiOnRydWUsImF1ZCI6InNheXVyYm94LWF1ZGllbmNlIiwiYXV0aF90aW1lIjoxNjY5MTg2NjA2LCJleHAiOjE2NzE3Nzg2MDYsImlhdCI6MTY2OTE4NjYwNiwiaXNzIjoiaHR0cHM6Ly93d3cuc2F5dXJib3guY29tIiwibWV0YWRhdGEiOnsiZGV2aWNlX2luZm8iOm51bGx9LCJuYW1lIjpudWxsLCJwaWN0dXJlIjpudWxsLCJwcm92aWRlcl9pZCI6ImFub255bW91cyIsInNpZCI6IjM2OGRkNDg3LWI1NTYtNDc0Yy04OTFiLTU0M2U5ZDI4Y2JkNiIsInN1YiI6IkdSYkpYeC1XRVdldWVJTk1VWDRaSFlaSzRhYy0iLCJ1c2VyX2lkIjoiR1JiSlh4LVdFV2V1ZUlOTVVYNFpIWVpLNGFjLSJ9.cIxcllPPAfANqSn4fPm6XUjez4weRYDkHVuR4c0QrfudK8gZjrsCG45MPDgSayHrF031ZKW7jL7QW9zMbqaC7RPGpyw25nJlMBKQghQiWNUUH7pmnihLaJNWwqXiZYTtKdd8uNd_Coy0jhbTvMnUioOqDnJZ4w8hUIjidczAov-5097vHs071dKWYzoorSrbru6rzqCAQqp5cUdOIpzLihYCr1xMj4D0YkLOpwKYh-mirokpsuqbtDa9iyNT1TvUM9HWZVOehC22h01xSsoT8O7O3DlpetG48ur-5SD3rTtQzVx1ghCexF1ecBAJ3oJLCqEz8FjuUYcRmI7WOuUvKg",
  "user-agent": "Mozilla/5.0 (Linux; Android 5.1.1; SM-G928X Build/LMY47X) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/47.0.2526.83 Mobile Safari/537.36",
  "content-type": "application/json",
  "accept": "*/*",
  "x-bundle-revision": "17.4",
  "x-sbox-tenant": "sayurbox",
  "x-binary-version": "2.5.0",
  "sec-ch-ua-platform": "Android",
  "origin": "https://www.sayurbox.com",
  "sec-fetch-site": "same-origin",
  "sec-fetch-mode": "cors",
  "sec-fetch-dest": "empty",
  "accept-encoding": "gzip, deflate, br",
  "accept-language": "id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7"}

  headers_carsome = {
  'Host': 'www.carsome.id',
  'content-length': '38',
  'accept': 'application/json, text/plain, */*',
  'x-language': 'id',
  'x-token': '',
  'country': 'ID',
  'x-amplitude-device-id': 'QbOr1g4RMMMIpnkg7JVqx7',
  'user-agent': 'Mozilla/5.0 (Linux; Android 10; Redmi 8) AppleWe>',
  'content-type': 'application/json',
  'origin': 'https://www.carsome.id',
  'sec-fetch-site': 'same-origin',
  'sec-fetch-mode': 'cors',
  'sec-fetch-dest': 'empty',
  'referer': 'https://www.carsome.id/',
  'accept-encoding': 'gzip, deflate, br',
  'accept-language': 'id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7'}

  data_carsome = json.dumps({"username":no,"optType":1})
  data = json.dumps([{"operationName":"generateOTP","variables":{"destinationType":"whatsapp","identity":"+62"+no},"query":"mutation generateOTP($destinationType: String!, $identity: String!) {\n  generateOTP(destinationType: $destinationType, identity: $identity) {\n    id\n    __typename\n  }\n}"}])
  for i in range(1):
    pos = requests.post("https://www.sayurbox.com/graphql/v1?deduplicate=1",headers=head,data=data).text
    pos_carsome = requests.post("https://www.carsome.id/website/login/sendSMS",headers=headers_carsome,data=data_carsome).text
    if "__typename" in pos:
      sp("SayurBox True")
    else:
      sp("SayurBox False")
      time.sleep(1)
   
    if "Send successfully" in pos_carsome:
      print("Carsome True")
    else:
      print("Carsome False")      
   

#tambah
def tambah():
  os.system("clear")
  sp ("Masukan nomor dengan awalan +62")
  nomort = input(">")
  with open("target.txt", "a+") as a:
      a.write(nomort)
      a.write('\n')
      a. close()
  sp ("Ingin menambahkan nomor lagi? [Y/N]")
  tmbah = input("[Y/N]")
  if tmbah == "Y":
     tambah()
  if tmbah == "N":
     menu()
  else:
     sp ("Terjadi Kesalahan !!")
     time.sleep(2)
     menu()



#pek
def handler(signal_received, frame):
    # Handle any cleanup here
    sp("\x1b[91m[!]Force Stop!")
    sp("[!]Program Terminated!")
    sp("Exit...")
    exit(2)
    exit()
    os.system("exit")

if __name__ == '__main__':
    # Tell Python to run the handler() function when SIGINT is recieved
    signal(SIGINT, handler)

#path
def path():

  if os.path.isfile('user.txt'):
   with open('user.txt') as f:
    contents = f.read()
    f.close()
    sp ("\x1b[91mLogin sebagai \x1b[95m"+contents)
    time.sleep(3)
    menu()
  else:
      sp ("Halo,selamat datang pengguna baru!")
      time.sleep(3)
      user()


# username
def user():
  os.system("clear")
  usr = input("Your name :")
  with open("user.txt", "w") as f:
    f.write( usr)
    f. close()

#Main menu
def menu():
  os.system("clear")
  os.system("clear")
  sp ("\033[1;30m<════════════[\033[1;33;41m • \033[1;37m About Me  \033[1;33m• \033[0m\033[1;30m]══════════════>")
  sp("\033[31;1m  ╔════════════════════════════════════════════════╗")
  sp(" \033[33;1m║  \033[36;1m [•] Authour  : BIMZ                           \033[33;1m ║")
  sp("\033[33;1m║  \033[36;1m  [•] gitHub   : https://github.com/Bimawawoy    \033[33;1m ║")
  sp(" \033[33;1m║  \033[36;1m [•] Insta    : bimzgz.me                      \033[33;1m ║")
  sp("\033[31;1m  ╚════════════════════════════════════════════════╝")
  sp ("\033[1;30m<════════════[\033[1;33;41m • \033[1;37m Information  \033[1;33m• \033[0m\033[1;30m]══════════════>")
  with open('user.txt') as f:
    contents = f.read()
    f.close()
  sp ("\x1b[94m [•] Your username : \x1b[91m"+contents)
  sp ("\x1b[94m [•] Ip address    : \x1b[93m"+IPAddr)
  sp ("\x1b[94m [•] Host          : \x1b[92m"+hostname)
  print ("\x1b[94m [•] Current date  :\x1b[95m",today)
  sp ("\033[1;30m<════════════[\033[1;33;41m • \033[1;37m Menu  \033[1;33m• \033[0m\033[1;30m]══════════════>")
  sp ("\x1b[96m")
  sp ("    [1]Start Spam                          ")
  sp ("    [2]Start Spam(MASSIVE)                 ")
  sp ("    [3]Setting file nomor                  ")
  sp ("    [4]List file nomor                     ")
  sp ("    [5]Reset Nomor                         ")
  sp ("    [6]Reset User                          ")
  sp ("    [7]Delete all data(*include login data)")
  sp ("    [0]Exit                                ")
  sp ("\033[1;30m<════════════[\033[1;33;41m • \033[1;37m Input  \033[1;33m• \033[0m\033[1;30m]══════════════>")
  menupilih = input(">")
  if menupilih =="1":
       os.system("clear")
       api()
       
  if menupilih == "2":
       os.system("clear")
       sp ("Tidak tersedia!")
       time.sleep(1)
       menu()

  if menupilih == "3":
      tambah()

  if menupilih == "4":
      if os.path.isfile('target.txt'):
        sp ("File detected !")
        with open('target.txt') as a:
          contents = a.read()
          sp (contents)
          time.sleep(5)
        menu()
      else:
        sp("Kamu belum menambahkan nomor!")
        time.sleep(3)
        menu()
  
  if menupilih == "5":
      if os.path.isfile('target.txt'):
        sp ("File detected !")
        time.sleep(0.5)
        sp ("Reset succesfull!")
        os.system("rm target.txt")
        time.sleep(4)
        menu()
      else:
        sp("Tidak ada nomor yang terdeteksi!")
        time.sleep(3)
        menu()

  if menupilih == "6":
      os.system("rm user.txt")
      sp("User berhasil di reset")
      time.sleep(1)
      sp("Restart program!")
      time.sleep(2)
      login()

  if menupilih == "7":
      if os.path.isfile("target.txt"):
         os.system("rm target.txt")
         sp("Deleting target number...")
      if os.path.isfile("bangsatkau"):
         os.system("rm bangsatkau")
         sp ("Deleting login data...")
      if os.path.isfile("user.txt"):
         os.system("rm user.txt")
         sp("Deleting username...")
         sp("Berhasil!")
         sp("Restarting program...")
         time.sleep(2)
         os.system("python main.py")
       
  if menupilih == "0":
      sp ("Exit...")
      time.sleep(1)
      sp ("Goodbyee :)")
      exit()
      exit()
      os.system("exit")
  else:
    sp("Unknown error!")
    time.sleep(0.5)
    sp("Soft restarting...")
    time.sleep(2)
    menu()
  

# login
def login():
  os.system("clear")
  if os.path.isfile('bangsatkau'):
      sp("\x1b[94mAuto login...")
      time.sleep(2)
      path()
  sp("\033[1;96m       ╔╗   ╔═══╗╔═══╗╔══╗╔═╗ ╔╗")
  sp("       ║║   ║╔═╗║║╔═╗║╚╣─╝║║╚╗║║")
  sp("       ║║   ║║ ║║║║ ╚╝ ║║ ║╔╗╚╝║")
  sp("       ║║ ╔╗║║ ║║║║╔═╗ ║║ ║║╚╗║║")
  sp("       ║╚═╝║║╚═╝║║╚╩═║╔╣─╗║║ ║║║")
  sp("       ╚═══╝╚═══╝╚═══╝╚══╝╚╝ ╚═╝")
  sp("\033[1;96m+\033[1;90m========================================\033[1;96m+")
  sp(" \033[1;97m{\033[1;95m•\033[1;97m} \033[1;93mAuthor   \033[1;91m: \033[1;95mBimz Senpai")
  sp(" \033[1;97m{\033[1;95m•\033[1;97m} \033[1;93mFacebook \033[1;91m: \033[1;95mBimz wibu")
  sp("\033[1;96m+\033[1;90m========================================\033[1;96m+")
  username = input(" \033[1;97m{\033[1;93m+\033[1;97m} \033[1;96mUsername:\033[1;92m ")
  password = getpass.getpass(" \033[1;97m{\033[1;93m+\033[1;97m} \033[1;96mPassword: ")
  if username == x and password == y:
    sp(" \033[1;92mAccess Granted !")
    time.sleep(2)
    simpan()
  else:
    for i in range(ulang):
        sp("\x1b[31m Access Denied !")

#save login
def simpan():
  sim = input("\x1b[93mApakah kamu ingin menyimpan data login,agar tidak memasukkan user dan password kembali? [Y/N]")
  if sim == "Y":
     with open("bangsatkau", "w") as w:
      w. close()
      sp("Berhasil di simpan!")
      time.sleep(3)
      os.system("clear")
      path()

  if sim == "N":
     sp("Data tidak disimpan!")
     os.system("clear")
     path()
  else:
    sp("[!]")
login()
