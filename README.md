# python-asyncio-test

## Getting Started

### Prerequisites
- Python 3.6 over 
	- requests
	- aiohttp
	
### Installing

```bash
$ python3 -m venv venv
$ source venv/bin/activate
$ pip install -r requirements.txt
```

## Running the tests
- [sync-http.py](sync-http.py) : sync http call 
	- http client : requests
	- r = http()
- [async-http.py](async-http.py) : asyncio, sync http call 
	- http client : requests
	- r = loop.run_in_executor(None, http, u)
- [async-aiohttp.py](async-aiohttp.py) : asyncio, async http call 
	- http client : aiohttp
	- r = asyncio.ensure_future(http(u))

```bash
$ ./run.sh 
sync-http.py
[9269, 9269, 9269, 9269, 9269, 64944, 9269, 64950, 9269, 9269, 9269, 9269, 9269, 64266, 9269, 9269, 9269, 9269, 9269, 9269]

real    0m8.372s
user    0m0.606s
sys     0m0.055s

async-http.py
[9269, 9269, 9269, 9269, 9269, 9269, 9269, 9269, 9269, 9269, 9269, 9269, 9269, 9269, 9269, 9269, 9269, 9269, 9269, 9269]

real    0m1.084s
user    0m1.069s
sys     0m0.339s

async-aiohttp.py
[9269, 9269, 9269, 9269, 9269, 9269, 9269, 9269, 9269, 9269, 9269, 9269, 9269, 9269, 9269, 9269, 9269, 9269, 9269, 9269]

real    0m0.898s
user    0m0.563s
sys     0m0.090s
```