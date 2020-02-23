#!/bin/bash

echo sync-http.py
time venv/bin/python3 sync-http.py
echo 

sleep 1

echo async-http.py
time venv/bin/python3 async-http.py
echo 

sleep 1

echo async-aiohttp.py
time venv/bin/python3 async-aiohttp.py
echo 

