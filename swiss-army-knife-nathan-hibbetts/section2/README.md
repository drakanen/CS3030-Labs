### Brief 3-sentence security report

    Developers should never use shell=True with unvalidated user input because an attacker could inject commands, known as command injection, to insert extra shell commands into the argument. This can give attackers administrator level access, or lead to data exfiltration, destruction, or full system compromise. Developers should always pass commands as a list to subprocess.run() instead of using shell=True.
