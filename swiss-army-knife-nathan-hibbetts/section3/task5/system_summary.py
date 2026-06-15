import subprocess
import re

result = subprocess.run("last | head -20", capture_output=True, text=True, shell=True)
pattern = r"^(\w+)\s+.*?\s{2,}(\w{3}\s+\w{3} +\d{1,2} +\d{2}:\d{2})"

divider = '-' * 30
print(divider)
for line in result.stdout.splitlines():
    match = re.match(pattern, line)
    if match:
        name, date = match.groups()
        print("User: " + name + "\nLogin Date: " + date)
        print(divider)