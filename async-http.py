
import asyncio
import requests
import conf

def http(url):
	resp = requests.get(url)
	return resp.text

async def main():
	loop = asyncio.get_event_loop()

	fut = []
	for u in conf.urls:
		r = loop.run_in_executor(None, http, u)
		fut.append(r)

	ret = await asyncio.gather(*fut)
	print( [ len(r) for r in ret ] )

if __name__ == "__main__":
	loop = asyncio.get_event_loop()
	loop.run_until_complete(main())