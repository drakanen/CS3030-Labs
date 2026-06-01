import subprocess

df = subprocess.run(['df', '-h'], capture_output=True, text=True)
for mainDrive in df.stdout.splitlines():
    if mainDrive.endswith("/"):
        print(mainDrive)