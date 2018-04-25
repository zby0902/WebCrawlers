#!/usr/bin/env python
"""
This is a simplest script that will take all html content of a url and
then save them into a text file.
It has one command line parameter which is --url or -u.
If no command line parameter is given, it uses its default url wich is:
'http://www.baidu.com
'
"""
import requests
import argparse	
ap = argparse.ArgumentParser()
ap.add_argument('-u','--url',help="url path of the website")
args = ap.parse_args()

def getHtmlText(url='http://www.baidu.com'):
	try:
		r = requests.get(url, timeout=20)
		r.raise_for_status()
		r.encoding = r.apparent_encoding
		with open('./result.txt','a') as f:
			f.write('\n')			
			f.write(str(r.text))
	except:
		return "Exception encounter!"
if __name__ == '__main__':
	if args.url:
		getHtmlText(url=args.url)
	else:
		getHtmlText()
