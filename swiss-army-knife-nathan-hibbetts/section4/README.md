How to set up the cronjob
open your preferred command prompt or shell, such as bash or fish
Type in "* * * * * /yourpath/to/.venv/bin/python3 -u /path/to/your/script.py >> /path/to/the/output/file.log"
If you are using vim, remember to use :wq to save. You MUST include the -u argument or you will not receive output. 


Task 3 query
You would modify it by using concurrent.futures.ThreadPoolExecuter to check multiple sites asyncronously. Print each site as you get the return, rather than adding them all to a list and sending everything at once. Using ThreadPoolExecuter to engage in threading allows the program to run in the background without freezing the execution line. 
