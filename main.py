#!/usr/bin/python3
import requests

# main_url = "http://devilishere666.000webhostapp.com/index.html"
url = "http://devilishere666.000webhostapp.com/mailer.php"

headers = {
	'Host': 'devilishere666.000webhostapp.com',
	'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64; rv:78.0) Gecko/20100101 Firefox/78.0',
	'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
	'Accept-Language': 'en,en-US;q=0.5',
	'Accept-Encoding': 'gzip, deflate',
	'Content-Type': 'application/x-www-form-urlencoded',
	'Content-Length': '121',
	'Origin': 'http://devilishere666.000webhostapp.com',
	'Connection': 'close',
	'Referer': 'http://devilishere666.000webhostapp.com/index.html',
	'Cookie': '_ga=GA1.2.1953321504.1637271960',
	'Upgrade-Insecure-Requests': '1',
}


data = {
	's_name': 'admin',
	's_email': 'admin@fetr.ac.in',
	'subject': 'about test',
	'r_email': 'padsalatrushal11@gmail.com',
	'message':'this is test #8',
}


r = requests.post(url, headers=headers, data=data, allow_redirects=True)
res = r.text
print(r.text)
