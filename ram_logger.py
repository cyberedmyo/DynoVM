import psutil
import time

while True:
    ram = psutil.virtual_memory().percent
    cpu = psutil.cpu_percent()
    with open("/mnt/shared/usage.txt", "w") as f:
        f.write(f"{ram},{cpu}")
    time.sleep(5)
