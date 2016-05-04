#!/usr/bin/env python
#encoding: utf-8

data = open("out","r")
linkStart = "http://steamcommunity.com/market/listings/730/"
tipus = ['', 'StatTrak%E2%84%A2%20']
quality = ["%28Battle-Scarred%29", "%28Well-Worn%29", "%28Field-Tested%29", "%28Minimal%20Wear%29", "%28Factory%20New%29"]

links = open("links","w")

for line in data:
	weapon = line.split(";")[0].replace(" ", "%20")
	skin = line.split(";")[1].strip().replace(" ", "%20")

	for q in quality:
		for t in tipus:
			links.write(linkStart + t + weapon + '%20%7C%20' + skin + '%20' + q +'\n')

links.close()
