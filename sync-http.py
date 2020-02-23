
import asyncio
import requests

import conf

def http(url):
	resp = requests.get(url)
	return resp.text
	

def main():
	ret = []
	for u in conf.urls:
		r = http(u)
		ret.append(r)

	print( [ len(r) for r in ret ] )

if __name__ == "__main__":
	main()