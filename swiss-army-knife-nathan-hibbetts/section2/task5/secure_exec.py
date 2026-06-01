# An attacker could push a payload like cat /etc/passwd
# because the shell=True does not validate input. This is called
# command injection, which allows attackers to
# append extra commands using shell operators.
# Example: hello; cat /etc/passwd
def unsafe_run(user_input):
    subprocess.run(f"echo {user_input}", shell=True)

# This version is safe because shell operators are treated
# as text instead of commands. The same example above
# would not work on this version, it would simply
# return the entire string.
def safe_run(user_input):
    subprocess.run(["echo", user_input])