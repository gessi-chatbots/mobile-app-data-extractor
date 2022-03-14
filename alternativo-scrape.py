from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import json

urls = ['https://alternativeto.net/software/osmand/about/',
        'https://alternativeto.net/software/etar-calendar/about/',
        'https://alternativeto.net/software/simple-calendar/about/',
        'https://alternativeto.net/software/organic-maps/about/']

apps = []
count = 0
write_file = open("knowledge_base.json", "w")
for url in urls:
    #initiate chrome driver with viewing options
    chrome_options = Options()
    chrome_options.add_argument("--incognito")
    chrome_options.add_argument("--window-size=1920x1080")
    s = Service(executable_path='./chromedriver')

    #get website started
    driver = webdriver.Chrome(options=chrome_options, service=s)
    driver.get(url)

    # retrieve name
    elem = driver.find_element(By.CLASS_NAME, "Heading_h1__MW2Lp")
    name = elem.get_attribute('innerHTML')
    print(name)

    #retrive features
    features = []
    tags = []

    #elem2 contains features in pos 0 and tags in pos 1
    [fts, tgs] = driver.find_elements(By.CLASS_NAME, "badges.link-color")

    li = fts.find_elements(By.TAG_NAME, "li")
    for l in li:
        ft = l.find_element(By.TAG_NAME, "a")
        features.append(ft.get_attribute('innerHTML'))

    li = tgs.find_elements(By.TAG_NAME, "li")
    for l in li:
        tg = l.find_elements(By.TAG_NAME, "span")
        tags.append(tg[1].get_attribute('innerHTML'))

    obj = {
        "name": name, 
        "features": features,
        "tags": tags,
    }

    json.dump(obj, write_file, indent=4)
    write_file.write('\n')
    

    obj = {
        "id": count,
        "name": name, 
        "features": features + tags,
    }

    apps.append(obj)
    count += 1

write_file.close()

obj = {
    "apps": apps
}

with open("rasa_knowledge_base.json", "w") as wf:
    json.dump(obj, wf, indent=4)
    wf.write('\n')
wf.close()