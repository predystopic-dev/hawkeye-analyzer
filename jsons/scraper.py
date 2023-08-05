import requests
#import beautifulsoup4
#import selenium
# import time 
import json
"https://polls.iplt20.com/widget/welcome/get_data?path=https://post-feeds.s3.ap-south-1.amazonaws.com/Delivery_1_1_1_13322095374323.json"


def hawkeye_scraper(tld):
    inning = 1
    over = 1
    delivery = 1
    match = "13322787102478"
    data = []

    # website = tld + f"{inning}_{over}_{delivery}_{match}.json"
    # response = requests.get(website)
    while (delivery <= 6):
        website = tld + f"{inning}_{over}_{delivery}_{match}.json"    
        response = requests.get(website)
        if response.text.strip().lower() != "null":
            delivery += 1
            print(f'{inning}_{over}_{delivery}')
            json_data = json.loads(response.text)
            data.append(json_data)
            
            if (delivery == 7):
                delivery = 1
                over += 1
        if (response.text.strip().lower() == "null" and inning == 4):
            break
        if (response.text.strip().lower() == "null" and inning != 4):
            inning += 1
            over = 1
            delivery = 1
    

    with open(f'{match}_hawkeye.json', 'a') as file:
        json.dump(data, file, indent=4)




hawkeye_scraper("https://polls.iplt20.com/widget/welcome/get_data?path=https://post-feeds.s3.ap-south-1.amazonaws.com/Delivery_")
