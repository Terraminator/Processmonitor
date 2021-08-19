import datetime
import psutil
from tabulate import tabulate
import os
import time


def get_processes():
    procs = []
    ch = []
    for p in psutil.process_iter():
        with p.oneshot():
            pid = p.pid
            if pid == 0:
                continue
            name = p.name()
            status = p.status()
            try:
                child = p.children()
            except psutil.AccessDenied:
                child = "N/A"
            for _ in (child):
                ch.append(str(child[_]))
            try:
                user = p.username()
            except psutil.AccessDenied:
                user = "N/A"
        procs.append({
            "pid": pid,
            "name": name,
            "status": status,
            "user": user,
            "child": ("Länge child: ", len(ch))
        })
    return(procs)


def print_processes(ps):
    print(tabulate(ps, headers="keys", tablefmt='github'))

procs = get_processes()
while True:
    print_processes(procs)
    time.sleep(1)
    procs = get_processes()
    if "nt" in os.name:
        os.system("cls")
    else:
        os.system("clear")