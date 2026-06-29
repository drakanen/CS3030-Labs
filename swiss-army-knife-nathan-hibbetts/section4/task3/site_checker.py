import requests

# Ecosia blocks the request so it shows as down
urls = ["https://www.ecosia.org", "https://www.startpage.com", "http://www.awfutmn3a4.gov"]

for each in urls:
    try:
        response = requests.get(each)
        if response.status_code == 200:
            print("SITE UP")
        else:
            print("SITE DOWN")
    except requests.exceptions.ConnectionError:
        print("SITE DOWN")