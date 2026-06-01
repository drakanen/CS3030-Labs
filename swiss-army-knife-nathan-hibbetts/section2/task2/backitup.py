import datetime, shutil

today = datetime.datetime.now().strftime("%Y-%m-%d")
shutil.make_archive("section1" + (today), "zip", root_dir="/home/nathan/Desktop/CS3030/CS3030-Labs/swiss-army-knife-nathan-hibbetts/section1")