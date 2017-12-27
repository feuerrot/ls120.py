#!/usr/bin/env python3
# get LS120 values
import json
import time
import requests

configfile = open("config", "r")
config = json.load(configfile)

def getvalue(host):
	g = requests.get(config["url"].format(host), timeout=1)
	if g.status_code != 200:
		raise Exception
	
	return g.json()

def sumhosts():
	rtn = {"power": {}, "energy": {}}
	for host in config["hosts"]:
		j = getvalue(config["hosts"][host])
		print(j)
		rtn["power"][host] = float(j["pwr"])
		rtn["energy"][host] = float(j["cnt"].replace(",", "."))
	
	return rtn

def export():
	data = sumhosts()
	out = open(config["output"], "w")
	for host in config["hosts"]:
		out.write('power_usage_kilowatthours{{location="colo",host="{}"}} {}\n'.format(host, data["energy"][host]))
		out.write('power_current_watt{{location="colo",host="{}"}} {}\n'.format(host, data["power"][host]))
	out.close()

try:
	export()
except Exception as e:
	print(e)
