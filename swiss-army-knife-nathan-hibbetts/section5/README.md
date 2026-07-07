# README

## Security & Robustness Checklist

### Secrets

- [ ] .env file is used for all secrets/keys
- [ ] .env is listed in .gitignore
- [ ] Sensitive values are masked

### Error Handling

- [ ] Scripts fail with a clear error message
- [ ] All argparse values have type validation
- [ ] try/except blocks catch specific exceptions
- [ ] File paths are validated and created safely using pathlib

### Process & Resource Handling

- [ ] Loops have exit conditions

### Subprocess Safety

- [ ] subprocess calls avoid shell=True unless necessary
- [ ] User input is never turned into a shell command string
- [ ] subprocess calls have timeouts to prevent hanging
- [ ] return codes are checked and handled

### Logging & Output

- [ ] Logs don't expose sensitive system details
- [ ] Log output is consistent and professional

### Automation

- [ ] Cron/systemd services run with the least privilege necessary
- [ ] Failures are logged

### Testing & Documentation

- [ ] Include a README that explains how the script works and what it does

## Technical  Reflection

I would say the hardest lab for me was lab 4. For task 1, the coloring method I chose for coloring the terminal text did not work when exported to the file. I tried another coloring method, but after that didn't work I decided to leave it as it wasn't very important.

For task 2, I initially had a little bit of trouble starting up crontab as I had never used vim before. I was having issues getting the text to save to crontab. After looking up how to use and navigate vim, this task became much easier.

Task 3 had me a bit confused as one of the websites I was trying to test was a good website, but the result kept coming back as offline. After peforming further research, I learned that some websites detect bots and hand them a fail code in response instead of the good 200 code. This is why it is recommended to use response.ok instead, as it helps bypass those issues. 

Task 4 went pretty smoothly.

Task 5 was a pain because I kept getting rate limited by systemctl due to the script constantly ending and restarting without any waiting time. The service file itself was rather easy to create. I saw someone else had changed their monitor script into a loop to prevent it from constantly restarting itself; while I had added a sleep timer to end of it myself.
