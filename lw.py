import os,sys,requests,re

def note():
	print('''-pembuat arvel ry ganteng slemek slebew Sebelum Menggunakan Tools Ini Taro Tools Ini Dengan
folder Bersamaan Dengan Sc Kalian\n''')

def menu():
	note()
	print('1. File Token .token.txt & .cok.txt')
	print('2. File Token t.txt & c.txt')
	print('3. File Token token.txt & cok.txt')
	menu = input('\npilih : ')
	if menu in ['1']:
		os.system('rm -rf .token.txt')
		os.system('rm -rf .cok.txt')
		token1()
	elif menu in ['2']:
		os.system('rm -rf t.txt')
		os.system('rm -rf c.txt')
		token2()
	elif menu in ['3']:
		os.system('rm -rf token.txt')
		os.system('rm -rf cok.txt')
		token3()
	else:
		exit()

def token1():
	try:
		ses = requests.Session()
		cookie = input('\nMasukan Cookie : ')
		cookies = {'cookie':cookie}
		url = 'https://www.facebook.com/adsmanager/manage/campaigns'
		req = ses.get(url,cookies=cookies)
		set = re.search('act=(.*?)&nav_source',str(req.content)).group(1)
		nek = '%s?act=%s&nav_source=no_referrer'%(url,set)
		roq = ses.get(nek,cookies=cookies)
		tok = re.search('accessToken="(.*?)"',str(roq.content)).group(1)
		tokenw = open(".token.txt", "w").write(tok)
		cokiew = open(".cok.txt", "w").write(cookie)
		print('\nLogin Berhasil , file tersimpan di .token.txt & .cok.txt')
	except Exception as e:
		os.system('rm -rf .cok.txt && rm -rf .token.txt')
		print(e)
		exit()


def token2():
	try:
		ses = requests.Session()
		print('Login Menggunakan Cookie')
		print('Pastikan Jangan Menggunakan Akun Utama !')
		cookie = input('\nMasukan Cookie : ')
		cookies = {'cookie':cookie}
		url = 'https://www.facebook.com/adsmanager/manage/campaigns'
		req = ses.get(url,cookies=cookies)
		set = re.search('act=(.*?)&nav_source',str(req.content)).group(1)
		nek = '%s?act=%s&nav_source=no_referrer'%(url,set)
		roq = ses.get(nek,cookies=cookies)
		tok = re.search('accessToken="(.*?)"',str(roq.content)).group(1)
		tokenw = open("t.txt", "w").write(tok)
		cokiew = open("c.txt", "w").write(cookie)
		print('\nLogin Berhasil , file tersimpan di t.txt & c.txt')
	except Exception as e:
		os.system('rm -rf c.txt && rm -rf t.txt')
		print(e)
		exit()

def token3():
	try:
		ses = requests.Session()
		print('Login Menggunakan Cookie')
		print('Pastikan Jangan Menggunakan Akun Utama !')
		cookie = input('\nMasukan Cookie : ')
		cookies = {'cookie':cookie}
		url = 'https://www.facebook.com/adsmanager/manage/campaigns'
		req = ses.get(url,cookies=cookies)
		set = re.search('act=(.*?)&nav_source',str(req.content)).group(1)
		nek = '%s?act=%s&nav_source=no_referrer'%(url,set)
		roq = ses.get(nek,cookies=cookies)
		tok = re.search('accessToken="(.*?)"',str(roq.content)).group(1)
		tokenw = open("token.txt", "w").write(tok)
		cokiew = open("cok.txt", "w").write(cookie)
		print('\nLogin Berhasil , file tersimpan di token.txt & cok.txt')
	except Exception as e:
		os.system('rm -rf cok.txt && rm -rf token.txt')
		print(e)
		exit()

if __name__=='__main__':
	try:os.mkdir('OK')
	except:pass
	try:os.mkdir('CP')
	except:pass
	os.system('clear')
	menu()
