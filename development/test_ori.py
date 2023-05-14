import sys, requests, bs4, urllib3

'''
C:\Python3\Lib\site-packages\bs4\builder\__init__.py:545: XMLParsedAsHTMLWarning: It looks like you're parsing an XML document using an HTML parser. If this really is an HTML document (maybe it's XHTML?), you can ignore or filter this warning. If it's XML, you should know that using an XML parser will be more reliable. To parse this document as XML, make sure you have the lxml package installed, and pass the keyword argument `features="xml"` into the BeautifulSoup constructor.
  warnings.warn(
'''

''' Main menu '''
def MainMenu():
	print(banner)
	# Input Target
	target = input("Starting Point : ")
	if target[0:7] != "http://" and target[0:8] != "https://":
		MainMenu()
	print("[+] Target Locked..")
	domain = input("Domain : ")
	print("[+] Domain Locked..")
	# Checking Response
	req = requests.get(target, verify=False)
	if req.status_code != 200:
		sys.exit()
	print("[+] Target is active..")
	# URL Gathering
	global urls, all_checked, all_skipped
	urls = []
	all_checked = []
	all_skipped = []
	# Parsing HTMl
	soup = bs4.BeautifulSoup(req.text, 'html.parser')
	print("[+] HTML parsed..")
	# HREF
	tag_a = soup.find_all('a')
	tag_area = soup.find_all('area')
	tag_base = soup.find_all('base')
	tag_link = soup.find_all('link')
	# SRC
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
	all_href = tag_a + tag_area + tag_base + tag_link
	print(f"[+] Href : {len(all_href)}")
	all_src = tag_audio + tag_embed + tag_iframe + tag_img + tag_input + tag_script + tag_source + tag_track + tag_video
	print(f"[+] Src : {len(all_src)}")
	# Separating
	for link in all_href:
		url = link.get('href')
		#print(f"{type(url)} <---> {url}")
		if url != None and url != "" and url != " " and url[0] != "#" and url[0:6] != "mailto":
			if url[0] == "/" or url[0:2] == "./" or url[0:3] == "../":
				url = target.strip("/") + url
			if url[0:7] != "http://" and url[0:8] != "https://":
				url = target.strip("/") + "/" + url
			if url not in urls:
				urls.append(url)
			else:
				pass
	for link in all_src:
		url = link.get('src')
		#print(f"{type(url)} <---> {url}")
		if url != None and url != "" and url != " " and url[0] != "#" and url[0:6] != "mailto":
			if url[0] == "/" or url[0:2] == "./" or url[0:3] == "../":
				url = target.strip("/") + url
			if url[0:7] != "http://" and url[0:8] != "https://":
				url = target.strip("/") + "/" + url
			if url not in urls:
				urls.append(url)
			else:
				pass
	urls.sort()
	print(f"[+] Total : {len(urls)} urls found in starting point!")
	repetisi = True
	# Repetisi
	while repetisi:
		repetisi_urls = []
		try:
			counter = 1
			for target in urls:
				print(f"[{counter}/{len(urls)}] Checking {target}")
				if domain in target.split("://")[1].split("/")[0]:
					if target not in all_checked:
						# New URL to check
						# Checking Response
						try:
							req = requests.get(target, verify=False)
						except KeyboardInterrupt:
							break
						except requests.exceptions.RequestException as Err:
							print(f"\t[*] Passing target due to exception : {target}")
							counter += 1
							continue
						if req.status_code != 200:
							print(f"\t[*] Passing target due to status code : {target}")
							counter += 1
							continue
						#print("[+] Target is active..")
						# Parsing HTMl
						soup = bs4.BeautifulSoup(req.text, 'html.parser')
						#print("[+] HTML parsed..")
						# HREF
						tag_a = soup.find_all('a')
						tag_area = soup.find_all('area')
						tag_base = soup.find_all('base')
						tag_link = soup.find_all('link')
						# SRC
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
						all_href = tag_a + tag_area + tag_base + tag_link
						#print(f"[+] Href : {len(all_href)}")
						all_src = tag_audio + tag_embed + tag_iframe + tag_img + tag_input + tag_script + tag_source + tag_track + tag_video
						#print(f"[+] Src : {len(all_src)}")
						# Separating
						for link in all_href:
							url = link.get('href')
							#print(f"{type(url)} <---> {url}")
							if url != None and url != "" and url != " " and url[0] != "#" and url[0:6] != "mailto":
								
						for link in all_src:
							url = link.get('src')
							#print(f"{type(url)} <---> {url}")
							if url != None and url != "" and url != " " and url[0] != "#" and url[0:6] != "mailto":
								if url[0] == "/" or url[0:2] == "./" or url[0:3] == "../":
									url = target.strip("/") + url
								if url[0:7] != "http://" and url[0:8] != "https://":
									url = target.strip("/") + "/" + url
								if url not in repetisi_urls:
									repetisi_urls.append(url)
								else:
									pass
						all_checked.append(target)
						print(f"\t[+] Total in repetition : {len(repetisi_urls)} urls after {target}")
						print(f"\t |---> Total checked : {len(all_checked)} ---> Total skipped : {len(all_skipped)}")
				else:
					print(f"\t[*] Skipping target due to domain irrelation : {target}")
					counter += 1
					all_skipped.append(target)
				counter += 1
			repetisi_urls.sort()
			input("[CTRL + C to stop / ENTER to new repetition]")
		except KeyboardInterrupt:
			break
	all_urls = urls + list(set(repetisi_urls) - set(urls))
	print(f"\n\n[+] All URL collected : {len(all_urls)}")
	print(f"[>] Total checked : {len(all_checked)} // [>] Total skipped : {len(all_skipped)}")
	input("[ENTER]")
	for url in all_urls:
		print(url)


''' Main Apps '''
if __name__ == '__main__':
	MainMenu()