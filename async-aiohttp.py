
import asyncio
import aiohttp
import conf

async def http(url):
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as response:
        	return await response.text()

async def main():
	fut = []
	for u in conf.urls:
		r = asyncio.ensure_future(http(u))
		fut.append(r)

	ret = await asyncio.gather(*fut)
	print( [ len(r) for r in ret ] )

if __name__ == "__main__":
	loop = asyncio.get_event_loop()
	loop.run_until_complete(main())