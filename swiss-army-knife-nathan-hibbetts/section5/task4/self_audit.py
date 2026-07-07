import time, psutil, os, logging

logging.basicConfig(filename='usage.log', level=logging.INFO,
                    format='%(asctime)s - %(levelname)s - %(message)s')

process = psutil.Process(os.getpid())
cpu_start = process.cpu_times()
memory_usage_start = psutil.virtual_memory()
print(f"CPU Time Starting: {cpu_start.user:.4f} sec")
print(f"Memory Time Starting: {memory_usage_start.used:.4f} MB")
empty = [x^2 for x in range(10_000_000)]

cpu_end = process.cpu_times()
memory_usage_end = psutil.virtual_memory()
logging.info(f"CPU time used: {cpu_end.user - cpu_start.user:.4f} sec")
logging.info(f"Memory used: {memory_usage_end.used - memory_usage_start.used:.4f} MB")

# The memory peak is the point where the script used the highest amount
# of memory on the device. This would be near the end of this particular
# script when it starts getting into large numbers.