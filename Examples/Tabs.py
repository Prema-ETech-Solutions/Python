import random
import site
import time
import webbrowser

while True :
    sites = random.choices(['youtube.com','instagram.com'])
    visit = 'https://{}'.format(sites)
    webbrowser.open(visit)
    time.sleep(2)
    


