import psutil, time

cpuUsage = psutil.cpu_percent(interval=1)
ramUsage= psutil.virtual_memory()
diskUsage = psutil.disk_usage('/')

YELLOW = "\033[93m"
RESET = "\033[0m"

print(time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()))
if cpuUsage > 80:
    print(f"{YELLOW}Warning: CPU Usage at {cpuUsage}%{RESET}")
else:
    print(f"CPU Usage at {cpuUsage}%")

if ramUsage.percent > 10:
    print(f"{YELLOW}Warning: RAM Usage at {ramUsage.percent}%{RESET}")
else:
    print(f"RAM Usage at {ramUsage.percent}%")

if diskUsage.percent > 80:
    print(f"{YELLOW}Warning: Disk Usage at {diskUsage.percent}%{RESET}")
else:
    print(f"Disk Usage at {diskUsage.percent}%")

print("\n")
