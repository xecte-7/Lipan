#!/usr/bin/env python3
# -*- coding: utf-8 -*-


''' Importing Modules '''
import sys, urllib3, urllib.parse, argparse, datetime, threading
import requests, bs4


''' Disabling Requests Warning '''
urllib3.disable_warnings(urllib3.exceptions.SSLError)
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)


''' Global Variables '''
all_urls = []
all_checked = []
temp_urls = []
headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/111.0.0.0 Safari/537.36"}
banner = r'''
 ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣠⡴⠞⠋⠉
 ⠀⠀⠀⠀⠀⠀⠀⠀⠀⢠⣴⠋⠁⣀⣠⣤⠴⠖⠲
 ⠀⠀⠀⠀⠀⠀⡤⣤⣶⡿⠛⢻⡏⠉⠀⠀⠀⠀⠀  █    ▄█ █ ▄▄  ██      ▄
 ⠀⠀⠀⢀⣔⣻⣶⣟⠛⢷⣾⡛⠂⠀⠀⠀⠀⠀⠀  █    ██ █   █ █ █      █
 ⠀⠀⠘⣁⣩⣿⣏⠙⣲⣾⢅⠈⠁⠀⠀⠀⠀⠀⠀  █    ██ █▀▀▀  █▄▄█ ██   █
 ⠠⠞⠉⠙⣿⣯⡉⠻⣿⠗⢄⠀⠀⠀⠀⠀⠀⠀⠀  ███▄ ▐█ █     █  █ █ █  █
 ⢀⣤⠤⠴⣿⣿⡟⠛⢻⣶⠲⢄⠀⠀⠀⠀⠀⠀⠀      ▀ ▐  █       █ █  █ █
 ⠏⠀⠀⠀⢹⣿⣧⠶⠿⣿⣤⠤⠤⠀⠀⠀⠀⠀⠀⠀ver 1.2    ▀     █  █   ██
 ⢀⣠⡴⠶⠿⣿⣧⣀⡴⠛⢛⣷⣴⡖⠒⠂⣀⣀⣀⠀⠀               ▀
 ⠟⠁⠀⣀⣤⣿⣿⣿⣥⢴⡾⠋⠉⢻⣷⢿⣯⡀⠀⣁⡴⠒⠆⣀⡤⠤⠀⢀⡴⠂⢀⡤⠂⠀⣀⡀
 ⠀⣰⠛⠉⠀⠀⢉⣿⣿⣿⣄⣀⣴⠋⢀⣤⡿⠿⠿⣟⣷⡶⠾⢿⡷⣤⣶⣿⣦⣴⣿⣷⣤⣼⣏⡁⣠⡴⠒
 ⠀⠁⠀⠀⢠⡾⠋⠉⠙⠷⣿⣿⣿⣶⣾⡟⣀⠀⣠⡿⠋⢀⡤⠊⢾⡟⠁⣴⠟⠁⢀⣾⠏⢈⣽⠟⠛⢷⣦⣤⣤⣤⠦⣄
 ⠀⠀⠀⠀⠈⠀⠀⠀⣠⠶⠛⠙⠛⢿⣿⣷⣇⣿⣿⣆⣴⣾⣷⣼⣿⣀⣤⣿⢠⡀⣸⢃⣤⡟⠁⠀⢀⡾⠛⠁⠀⣙⣧⣨⡤⠶⣤⡀
 ⠀⠀⠀⠀⠀⠀⠀⠀⠃⠀⠀⠀⠀⣀⡼⠿⠿⣿⣿⣿⣿⣿⣿⣷⣿⣽⣻⣿⣿⣿⣿⣾⣿⣧⣤⣤⣿⠀⠀⣠⠾⠛⠁⢹⣿⣄⠀⠁⠀⠀
 ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⠋⠀⠀⠀⣠⠟⠁⠁⣿⠁⠀⣹⠛⠛⢹⠟⠋⠻⡿⠻⣿⣿⡿⢿⣷⣾⣷⣰⠞⠛⠚⠻⣿⡷⢦⣄
 ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠏⠀⠀⠀⢣⠀⠀⠹⡄⠀⢸⡄⠀⢰⠇⢠⠟⢁⣤⠾⢿⣿⣿⣧⣤⡴⠶⠾⣿⣷⠀⠉⠲
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀ ⠀⠀⠀⠀⠑⠀⠈⠂⠘⠀⠎⢠⠞⢻⣿⣿⣏⣡⣴⡶⣶⣾⣿⣷⣄
  Lipan is a nested url crawler   ⠀ ⠀⠀  ⠀⠀⠀⣡⠔⠛⣿⣿⡿⡅⠀⠀⠀⠙⣿⡃⠈⠳
  to help you gather every    ⠀⠀⠀      ⠀⠀⠀⠀⠀⠀⢀⣽⣿⠻⢤⣀⠀⠀⢀⣾⣿
  url related from the target    ⠀   ⠀⠀⢀⣠⡴⠶⠚⠓⠾⣿⣿⠆⠀⠈⢣⣸⣿⣿⠛⣧⠀
                                  ⠀⠀⢀⡴⠋⠁⠀⠀⠀⠀⠀⠙⢿⣿⣄⣄⣠⣿⠟⠁⠀⢸⠊
  Coded by Muhammad Rizky        ⠀⠀⠛⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢉⣿⠛⠉⠁⠀⠀⠀⠈
  {aka XECTE-7 // @xecte-7}            ⠀ ⣀⣀⣀⣀⣠⣤⠶⠋
  #XECTE_7 #Portal_IT_ID
  #DariTeknikUntukDunia #HMTK_FT_UBT
 '''
print(banner)


''' Argument Parser '''
parser = argparse.ArgumentParser()
parser.add_argument("-u", metavar="url", type=str,
	help="url starting point for crawling")
parser.add_argument("-d", metavar="domain", type=str, default=None,
	help="filter result to specific domain (default: from -u)")
parser.add_argument("-i", metavar="iteration", type=int, default=1,
	help="crawling iteration (default: 1)")
parser.add_argument("-t", metavar="thread", type=int, default=10,
	help="threading use to perform action (default: 10)")
parser.add_argument("-o", metavar="output", type=str, default="<default>",
	help="save crawling result to output file")
parser.add_argument("-v", "--verbose", action="store_true",
	help="increase verbosity for detailed information")
args = parser.parse_args()


''' Class for URL Crawler '''
class Lipan_Crawler:
	def __init__(self, soup_data):
		# Tag containing href attribute
		tag_a = soup_data.find_all('a')
		tag_area = soup_data.find_all('area')
		tag_base = soup_data.find_all('base')
		tag_link = soup_data.find_all('link')
		# Tag containing src attribute
		tag_audio = soup_data.find_all('audio')
		tag_embed = soup_data.find_all('embed')
		tag_iframe = soup_data.find_all('iframe')
		tag_img = soup_data.find_all('img')
		tag_input = soup_data.find_all('input')
		tag_script = soup_data.find_all('script')
		tag_source = soup_data.find_all('source')
		tag_track = soup_data.find_all('track')
		tag_video = soup_data.find_all('video')
		# Combining
		self.all_href = tag_a + tag_area + tag_base + tag_link
		self.all_src = tag_audio + tag_embed + tag_iframe + tag_img + tag_input + tag_script + tag_source + tag_track + tag_video


''' Function for Thread Worker '''
def Lipan_Worker(target, verbose):
	global main_spu, main_spd, main_spd_proto, main_iteration, main_thread, main_domain, main_output
	global temp_urls, all_urls, all_checked, iter_count
	# Checking for valid checked
	if target not in all_checked:
		if verbose:
			print(f"    ➨ checking {target}")
		# Make Request
		try:
			req = requests.get(target, verify=False, headers=headers)
		except requests.exceptions.Timeout:
			print(f"    ➨ [!] Err: Request timeout to {target}")
			sys.exit(0)
		except requests.exceptions.RequestException as err:
			print(f"    ➨ [!] Err: Error has occured when crawling at {target}")
			sys.exit(0)
		soup = bs4.BeautifulSoup(req.text, 'html.parser')
		crawler = Lipan_Crawler(soup)
		# if verbose:
		# 	print(f"      ➨ found {len(crawler.all_href)} from href")
		# 	print(f"      ➨ found {len(crawler.all_src)} from src")
		# Checking for href attribute
		for link in crawler.all_href:
			url = link.get('href')
			parsed_url = urllib.parse.urlparse(url)
			parsed_dom = str(parsed_url.netloc)
			# URL have scheme, DOMAIN in scope, and URL not in temp_urls
			if (parsed_url.scheme != '') and (parsed_url.netloc != ''):
				if (main_domain in parsed_dom) and (url not in temp_urls):
					temp_urls.append(url)
			# URL doesn't have scheme and doesn't have DOMAIN
			if (parsed_url.scheme == '') and (parsed_url.netloc == '') and (len(url) > 2):
				if (url[0] == '.') or (url[0:2] == './') or (url[0:3] == '../'):
					url = f"{target.strip('/')}/{url}"
				if (url[0] == '/' and url[1] != '/') or (url[0] == '?'):
				 	url = f"{main_spd_proto.strip('/')}{url}"
				# If not in container
				parsed_url = urllib.parse.urlparse(url)
				parsed_dom = str(parsed_url.netloc)
				if (parsed_url.scheme != '') and (main_domain in parsed_dom) and (url not in temp_urls):
					temp_urls.append(url)
		# Checking for src attribute
		for link in crawler.all_src:
			url = link.get('src')
			parsed_url = urllib.parse.urlparse(url)
			parsed_dom = str(parsed_url.netloc)
			# URL have scheme, DOMAIN in scope, and URL not in temp_urls
			if (parsed_url.scheme != '') and (parsed_url.netloc != ''):
				if (main_domain in parsed_dom) and (url not in temp_urls):
					temp_urls.append(url)
			# URL doesn't have scheme and doesn't have DOMAIN
			if (parsed_url.scheme == '') and (parsed_url.netloc == '') and (len(url) > 2):
				if (url[0] == '.') or (url[0:2] == './') or (url[0:3] == '../'):
					url = f"{target.strip('/')}/{url}"
				if (url[0] == '/' and url[1] != '/') or (url[0] == '?'):
				 	url = f"{main_spd_proto.strip('/')}{url}"
				# If not in container
				parsed_url = urllib.parse.urlparse(url)
				parsed_dom = str(parsed_url.netloc)
				if (parsed_url.scheme != '') and (main_domain in parsed_dom) and (url not in temp_urls):
					temp_urls.append(url)
		all_checked.append(target)


''' Lipan Main App '''
def Lipan_Main():
	# Importing global variables and configure
	global main_spu, main_spd, main_spd_proto, main_iteration, main_thread, main_domain, main_output
	global temp_urls, all_urls, all_checked, iter_count
	main_spu = args.u
	main_parsed = urllib.parse.urlparse(main_spu)
	main_spd = main_parsed.netloc
	main_spd_proto = f"{main_parsed.scheme}://{main_parsed.netloc}"
	main_iteration = args.i
	main_thread = args.t
	if args.d == None:
		main_domain = main_parsed.netloc
	else:
		main_domain = args.d
	main_output = args.o
	iter_count = 1
	# Basic Information
	if args.verbose:
		print(f"[i] Starting point : {main_spu}")
		print(f"    Domain Scope   : {main_domain}")
		print(f"    Iteration      : {main_iteration}")
		print(f"    Threads        : {main_thread}")
		print(f"    Output File    : {main_output}")
	if main_iteration > 3:
		print(f"[*] Warning: using more than 3 iteration may take more time")
		print(f"             consider using on range 1-3")
	# First Iteration
	print(f"[*] Iteration {iter_count}")
	if args.verbose:
		print(f"    ➨ start crawling at {main_spu}")
	# Make Request
	try:
		req = requests.get(main_spu, verify=False, headers=headers)
	except requests.exceptions.Timeout:
		print(f"    ➨ [!] Err: Request timeout to {main_spu}")
		sys.exit(0)
	except requests.exceptions.SSLError:
		print(f"    ➨ [!] Err: SSL certificate failed to {main_spu}")
		sys.exit(0)
	except requests.exceptions.RequestException as err:
		print(f"[!] Err: Error has occured when crawling at {main_spu}")
		sys.exit(0)
	soup = bs4.BeautifulSoup(req.text, 'html.parser')
	crawler = Lipan_Crawler(soup)
	# Checking for href attribute
	if args.verbose:
		print(f"      ➨ found {len(crawler.all_href)} from href")
		print(f"      ➨ found {len(crawler.all_src)} from src")
	for link in crawler.all_href:
		url = link.get('href')
		parsed_url = urllib.parse.urlparse(url)
		parsed_dom = str(parsed_url.netloc)
		# URL have scheme, DOMAIN in scope, and URL not in all_urls
		if (parsed_url.scheme != '') and (parsed_url.netloc != ''):
			if main_domain in parsed_dom and (url not in all_urls):
				all_urls.append(url)
		# URL doesn't have scheme and doesn't have DOMAIN
		if (parsed_url.scheme == '') and (parsed_url.netloc == '') and (len(url) > 2):
			if (url[0] == '.') or (url[0:2] == './') or (url[0:3] == '../'):
				url = f"{main_spd_proto.strip('/')}/{url}"
			if (url[0] == '/' and url[1] != '/') or (url[0] == '?'):
			 	url = f"{main_spd_proto.strip('/')}{url}"
			# If not in container
			parsed_url = urllib.parse.urlparse(url)
			if (parsed_url.scheme != '') and (main_domain in parsed_dom) and (url not in all_urls):
				all_urls.append(url)
	# Checking for src attribute
	for link in crawler.all_src:
		url = link.get('src')
		parsed_url = urllib.parse.urlparse(url)
		parsed_dom = str(parsed_url.netloc)
		# URL have scheme, DOMAIN in scope, and URL not in all_urls
		if (parsed_url.scheme != '') and (parsed_url.netloc != ''):
			if (main_domain in parsed_dom) and (url not in all_urls):
				all_urls.append(url)
		# URL doesn't have scheme and doesn't have DOMAIN
		if (parsed_url.scheme == '') and (parsed_url.netloc == '') and (len(url) > 2):
			if (url[0] == '.') or (url[0:2] == './') or (url[0:3] == '../'):
				url = f"{main_spd_proto.strip('/')}/{url}"
			if (url[0] == '/' and url[1] != '/') or (url[0] == '?'):
			 	url = f"{main_spd_proto.strip('/')}{url}"
			# If not in container
			parsed_url = urllib.parse.urlparse(url)
			if (parsed_url.scheme != '') and (main_domain in parsed_dom) and (url not in all_urls):
				all_urls.append(url)
	print(f"[+] Found {len(all_urls)} urls after {iter_count} iteration")
	# If more than 1 iteration
	if main_iteration > 1:
		for i in range(2, main_iteration + 1):
			print(f"[*] Iteration {i}")
			index_counter = 0
			while index_counter < len(all_urls):
				# Running thread workers here
				threads = list()
				try:
					for j in range(1, main_thread+1):
						if index_counter == len(all_urls):
							break
						worker = threading.Thread(target=Lipan_Worker, args=(all_urls[index_counter], args.verbose, ))
						threads.append(worker)
						worker.start()
						index_counter += 1
					for worker_index, worker_thread in enumerate(threads):
						worker_thread.join()
				# If keyboad interrupted
				except KeyboardInterrupt:
					print("[*] Warning: Keyboard interrupt detected, waiting for all thread to finish on this iteration..")
					for worker_index, worker_thread in enumerate(threads):
						worker_thread.join()
					break
			iter_count += 1
			print(f"[+] Found {len(temp_urls)} more urls after {iter_count} iteration")
			all_urls += temp_urls
			temp_urls.clear()
			all_urls.sort()
	# Final filtering
	print("[*] Filtering domain for final result..")
	filtered_urls = []
	for url in all_urls:
		parsed_url = urllib.parse.urlparse(url)
		parsed_dom = str(parsed_url.netloc)
		if (url not in filtered_urls) and (main_domain in parsed_dom) and (parsed_url.scheme != ""):
			filtered_urls.append(url.replace("///","/"))
	filtered_urls.sort()
	print(f"[+] Found {len(filtered_urls)} urls at the end")
	print()
	print(f"[i] Final action: (S)ave // (P)rint // (B)oth")
	save_option = input("    ➨ ")
	if save_option.lower() in ["s", "b", "", " "]:
		if main_output == "<default>":
			time_obj = datetime.datetime.now()
			time_format = time_obj.strftime("%Y-%m-%d_%H-%M-%S")
			filename = time_format + ".txt"
		else:
			filename = main_output
		# Writing output file
		output_file = open(f"./output/{filename}", 'w')
		for url in filtered_urls:
			if save_option.lower() == "b":
				print(url)
			output_file.write(url + "\n")
		print()
		print(f"[+] Output saved to ./output/{filename}")
		output_file.close()
	elif save_option.lower() == "p":
		for url in filtered_urls:
			print(url)


''' Running Lipan '''
if args.u != None and args.i > 0 and (args.t > 0 and args.t <= 50):
	Lipan_Main()
else:
	if args.u == None:
		print("[!] Err: Specify url for starting point !")
	if args.i < 1:
		print("[!] Err: Minimum iteration value is 1 !")
	if args.t < 1 or args.t > 50:
		print("[!] Err: Thread value is 1 to 50")
	sys.exit()