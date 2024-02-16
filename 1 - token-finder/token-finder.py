import requests
from time import sleep

# input
number_of_requests = 1000

# constants
page = 1
last_post_date = -1
headers = {"Content-Type": "application/json"}

with open("TOKENS.txt", 'a', newline='', encoding='utf-8') as text_file:
    
    for page in range(1, number_of_requests + 1):    
        try:
            response = requests.post(api_url, json=post_body,  headers=headers)
            response.raise_for_status()

            data = response.json()

            for idx in range(len(post_list)):
                text_file.write(str(item_data) + "\n")

            # Pause for a short time to avoid rate limits
            sleep(1.5)

        except requests.exceptions.RequestException as err:
            print("Error:", err)
            sleep(10)  # Sleep and try again
        # progress
        progress = page / number_of_requests * 100
        print("Page: {} => {:.2f}%".format(page, round(progress, 2)))
        page += 1