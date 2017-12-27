#!/usr/bin/env python3
# get LS120 values
import json
import time
import requests

configfile = open("config", "r")
config = json.load(configfile)

def getvalue(host):
	g = requests.get(config["url"].format(host))
	if g.status_code != 200:
		raise Exception
	
	return g.json()

def sumhosts():
	rtn = {"power": {}, "energy": {}}
	for elem in config["hosts"]:
		j = getvalue(config["hosts"][elem])
		print(j)
		rtn["power"][elem] = float(j["pwr"])
		rtn["energy"][elem] = float(j["cnt"].replace(",", "."))
	
	return rtn

print(sumhosts())
