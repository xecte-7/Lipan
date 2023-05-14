#!/usr/bin/env python3
# -*- coding: utf-8 -*-

''' Importing Modules '''
import sys, platform, os, urllib3, argparse, datetime
import requests, bs4

# Disabling Requests Warning
urllib3.disable_warnings(urllib3.exceptions.SSLError)
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

# Variables
banner = r'''
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣠⡴⠞⠋⠉
⠀⠀⠀⠀⠀⠀⠀⠀⠀⢠⣴⠋⠁⣀⣠⣤⠴⠖⠲
⠀⠀⠀⠀⠀⠀⡤⣤⣶⡿⠛⢻⡏⠉⠀⠀⠀⠀⠀  █    ▄█ █ ▄▄  ██      ▄
⠀⠀⠀⢀⣔⣻⣶⣟⠛⢷⣾⡛⠂⠀⠀⠀⠀⠀⠀  █    ██ █   █ █ █      █
⠀⠀⠘⣁⣩⣿⣏⠙⣲⣾⢅⠈⠁⠀⠀⠀⠀⠀⠀  █    ██ █▀▀▀  █▄▄█ ██   █
⠠⠞⠉⠙⣿⣯⡉⠻⣿⠗⢄⠀⠀⠀⠀⠀⠀⠀⠀  ███▄ ▐█ █     █  █ █ █  █
⢀⣤⠤⠴⣿⣿⡟⠛⢻⣶⠲⢄⠀⠀⠀⠀⠀⠀⠀      ▀ ▐  █       █ █  █ █
⠏⠀⠀⠀⢹⣿⣧⠶⠿⣿⣤⠤⠤⠀⠀⠀⠀⠀⠀⠀⠀          ▀     █  █   ██
⢀⣠⡴⠶⠿⣿⣧⣀⡴⠛⢛⣷⣴⡖⠒⠂⣀⣀⣀⠀⠀               ▀
⠟⠁⠀⣀⣤⣿⣿⣿⣥⢴⡾⠋⠉⢻⣷⢿⣯⡀⠀⣁⡴⠒⠆⣀⡤⠤⠀⢀⡴⠂⢀⡤⠂⠀⣀⡀
⠀⣰⠛⠉⠀⠀⢉⣿⣿⣿⣄⣀⣴⠋⢀⣤⡿⠿⠿⣟⣷⡶⠾⢿⡷⣤⣶⣿⣦⣴⣿⣷⣤⣼⣏⡁⣠⡴⠒
⠀⠁⠀⠀⢠⡾⠋⠉⠙⠷⣿⣿⣿⣶⣾⡟⣀⠀⣠⡿⠋⢀⡤⠊⢾⡟⠁⣴⠟⠁⢀⣾⠏⢈⣽⠟⠛⢷⣦⣤⣤⣤⠦⣄
⠀⠀⠀⠀⠈⠀⠀⠀⣠⠶⠛⠙⠛⢿⣿⣷⣇⣿⣿⣆⣴⣾⣷⣼⣿⣀⣤⣿⢠⡀⣸⢃⣤⡟⠁⠀⢀⡾⠛⠁⠀⣙⣧⣨⡤⠶⣤⡀
⠀⠀⠀⠀⠀⠀⠀⠀⠃⠀⠀⠀⠀⣀⡼⠿⠿⣿⣿⣿⣿⣿⣿⣷⣿⣽⣻⣿⣿⣿⣿⣾⣿⣧⣤⣤⣿⠀⠀⣠⠾⠛⠁⢹⣿⣄⠀⠁⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⠋⠀⠀⠀⣠⠟⠁⠁⣿⠁⠀⣹⠛⠛⢹⠟⠋⠻⡿⠻⣿⣿⡿⢿⣷⣾⣷⣰⠞⠛⠚⠻⣿⡷⢦⣄
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠏⠀⠀⠀⢣⠀⠀⠹⡄⠀⢸⡄⠀⢰⠇⢠⠟⢁⣤⠾⢿⣿⣿⣧⣤⡴⠶⠾⣿⣷⠀⠉⠲
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠑⠀⠈⠂⠘⠀⠎⢠⠞⢻⣿⣿⣏⣡⣴⡶⣶⣾⣿⣷⣄
 Lipan is a nested url crawler⠀⠀⠀⠀⠀⠀⣡⠔⠛⣿⣿⡿⡅⠀⠀⠀⠙⣿⡃⠈⠳
 to help you gather sensitive⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣽⣿⠻⢤⣀⠀⠀⢀⣾⣿
 url related to the target   ⠀⠀⠀⢀⣠⡴⠶⠚⠓⠾⣿⣿⠆⠀⠈⢣⣸⣿⣿⠛⣧⠀
                           ⠀⠀⢀⡴⠋⠁⠀⠀⠀⠀⠀⠙⢿⣿⣄⣄⣠⣿⠟⠁⠀⢸⠊
 Coded by XECTE-7         ⠀⠀⠛⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢉⣿⠛⠉⠁⠀⠀⠀⠈
 version 1.1                ⠀⠀⠀⠀⣀⣀⣀⣀⣠⣤⠶⠋
'''
global all_urls, all_checked, all_skipped
all_urls = []
all_checked = []
all_skipped = []

print(banner)

# Argument Parser
parser = argparse.ArgumentParser()
parser.add_argument("-v", "--verbose", action="store_true",
	help="increase verbosity for detailed information")
parser.add_argument("-u", metavar="url", type=str,
	help="url starting point for crawling")
parser.add_argument("-i", metavar="iteration", type=int, default=1,
	help="crawling iteration (default: 1)")
parser.add_argument("-d", metavar="domain", type=str, default=None,
	help="filter result to specific domain")
parser.add_argument("-o", metavar="output", type=str, default=None,
	help="save crawling result to output file")
args = parser.parse_args()


''' Class for URL Crawler '''
class Crawler:
	def __init__(self, soup_data):
		# Tag containing href attribute
		tag_a = soup.find_all('a')
		tag_area = soup.find_all('area')
		tag_base = soup.find_all('base')
		tag_link = soup.find_all('link')
		# Tag containing src attribute
		tag_audio = soup.find_all('audio')
		tag_embed = soup.find_all('embed')
		tag_iframe = soup.find_all('iframe')
		tag_img = soup.find_all('img')
		tag_input = soup.find_all('input')
		tag_script = soup.find_all('script')
		tag_source = soup.find_all('source')
		tag_track = soup.find_all('track')
		tag_video = soup.find_all('video')
		# Combining
		self.all_href = tag_a + tag_area + tag_base + tag_link
		self.all_src = tag_audio + tag_embed + tag_iframe + tag_img + tag_input + tag_script + tag_source + tag_track + tag_video


''' Running Lipan '''
if args.u != None and args.i > 0:
	main_spu = args.u
	main_spd = main_spu.split("/")[2]
	main_spd_proto = requests.get(f"http://{main_spd}").url
	main_iteration = args.i
	if args.d == None:
		main_domain = main_spu.split("/")[2]
	else:
		main_domain = args.d
	main_output = args.o
	iter_count = 1
	# Basic Info
	if args.verbose:
		print(f"[i] Starting Lipan on {main_spu} with filtered domain {main_domain}")
		print(f"    Total iteration : {main_iteration}\n")
	# First Iteration
	print(f"[*] Iteration {iter_count}")
	if args.verbose:
		print(f"    ➨ start crawling at {main_spu}")
	# Make Request
	try:
		req = requests.get(main_spu, verify=False)
	except requests.exceptions.Timeout:
		print(f"[!] Err: Request timeout to {main_spu}")
		sys.exit(0)
	except requests.exceptions.RequestException as err:
		print(f"[!] Err: {err}")
		sys.exit(0)
	soup = bs4.BeautifulSoup(req.text, 'html.parser')
	crawler = Crawler(soup)
	# Checking for href attribute
	if args.verbose:
		print(f"      ➨ found {len(crawler.all_href)} from href")
		print(f"      ➨ found {len(crawler.all_src)} from src")
	for link in crawler.all_href:
		url = link.get('href')
		# If valid url
		if url != None and url != "" and url != " " and url[0] != "#" and url[0:6] != "mailto":
			# If the url look like this : /site/file or ./site/file or ../site/file
			if url[0] == "/" or url[0:2] == "./" or url[0:3] == "../":
				url = main_spd_proto.strip("/") + url
			# If the url doesnt contain any http:// or https://
			if url[0:7] != "http://" and url[0:8] != "https://":
				url = main_spd_proto.strip("/") + "/" + url
			# If not in container
			url_dom = url.split("/")[2]
			if url not in all_urls and main_domain in url_dom:
				all_urls.append(url)
	# Checking for src attribute
	for link in crawler.all_src:
		url = link.get('src')
		# If valid url
		if url != None and url != "" and url != " " and url[0] != "#" and url[0:6] != "mailto":
			# If the url look like this : /site/file or ./site/file or ../site/file
			if url[0] == "/" or url[0:2] == "./" or url[0:3] == "../":
				url = main_spd_proto.strip("/") + url
			# If the url doesnt contain any http:// or https://
			if url[0:7] != "http://" and url[0:8] != "https://":
				url = main_spd_proto.strip("/") + "/" + url
			# If not in container
			url_dom = url.split("/")[2]
			if url not in all_urls and main_domain in url_dom:
				all_urls.append(url)
	print(f"[+] Found {len(all_urls)} urls after {iter_count} iteration")
	# If more than 1 iteration
	if main_iteration > 1:
		for i in range(2, main_iteration + 1):
			temp_urls = []
			print(f"[*] Iteration {i}")
			for target in all_urls:
				# Checking for valid checked
				if target not in all_checked:
					if args.verbose:
						print(f"    ➨ checking {target}")
					# Make Request
					try:
						req = requests.get(target, verify=False)
					except requests.exceptions.Timeout:
						print(f"[!] Err: Request timeout to {target}")
						sys.exit(0)
					except requests.exceptions.RequestException as err:
						print(f"[!] Err: {err}")
						sys.exit(0)
					soup = bs4.BeautifulSoup(req.text, 'html.parser')
					crawler = Crawler(soup)
					if args.verbose:
						print(f"      ➨ found {len(crawler.all_href)} from href")
						print(f"      ➨ found {len(crawler.all_src)} from src")
					# Checking for href attribute
					for link in crawler.all_href:
						url = link.get('href')
						# If valid url
						if url != None and url != "" and url != " " and url[0] != "#" and url[0:6] != "mailto":
							# If the url look like this : /site/file or ./site/file or ../site/file
							if url[0] == "/" or url[0:2] == "./" or url[0:3] == "../":
								url = main_spd_proto.strip("/") + url
							# If the url doesnt contain any http:// or https://
							if url[0:7] != "http://" and url[0:8] != "https://":
								url = main_spd_proto.strip("/") + "/" + url
							# If not in container
							target_dom = target.split("/")[2]
							if url not in temp_urls and main_domain in target_dom:
								temp_urls.append(url)
					# Checking for src attribute
					for link in crawler.all_src:
						url = link.get('src')
						# If valid url
						if url != None and url != "" and url != " " and url[0] != "#" and url[0:6] != "mailto":
							# If the url look like this : /site/file or ./site/file or ../site/file
							if url[0] == "/" or url[0:2] == "./" or url[0:3] == "../":
								url = main_spd_proto.strip("/") + url
							# If the url doesnt contain any http:// or https://
							if url[0:7] != "http://" and url[0:8] != "https://":
								url = main_spd_proto.strip("/") + "/" + url
							# If not in container
							target_dom = target.split("/")[2]
							if url not in temp_urls and main_domain in target_dom:
								temp_urls.append(url)
					all_checked.append(target)
			print(f"[+] Found {len(temp_urls)} more urls after {iter_count} iteration")
			all_urls += temp_urls
			all_urls.sort()
			iter_count = i
	# Printing Output
	all_urls.sort()
	print(f"[+] Found {len(all_urls)} urls at the end")
	print()
	print(f"[i] Choose your final action: (S)ave // (P)rint // (B)oth")
	save_option = input("    > ")
	if save_option.lower() in ["s", "b"]:
		if main_output == None:
			time_obj = datetime.datetime.now()
			time_format = time_obj.strftime("%Y-%m-%d_%H-%M-%S")
			filename = time_format + ".txt"
		else:
			filename = main_output
		# Opening output file
		output_file = open(filename, 'w')
		for url in all_urls:
			if save_option.lower() == "b":
				print(url)
				output_file.write(url + "\n")
			elif save_option.lower() == "s":
				output_file.write(url + "\n")
		print()
		print(f"[+] Output saved as {filename}")
		output_file.close()
	elif save_option.lower() == "p":
		for url in all_urls:
			print(url)
else:
	if args.u == None:
		print("[!] Err: Specify url for starting point !")
	if args.i < 1:
		print("[!] Err: Minimum iteration value is 1 !")
	sys.exit()