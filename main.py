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
	rtn = {"power": 0, "energy": 0}
	for elem in config["hosts"]:
		j = getvalue(elem)
		print(j)
		rtn["power"] += float(j["pwr"])
		rtn["energy"] += float(j["cnt"].replace(",", "."))
	
	return rtn

print(sumhosts())
