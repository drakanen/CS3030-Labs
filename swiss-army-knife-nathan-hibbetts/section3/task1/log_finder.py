import re

with open("./sample.log", "r") as log:
    for line in log:
        matches = re.findall(r"(\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}) \s*(\[\d{4}-\d{2}-\d{2} \d{2}:\d{2}\])", line)
        if matches:
            ip, date = matches[0]
            print(f"{ip},{date}")