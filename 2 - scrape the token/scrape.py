from requests import get
from json import loads
from pathlib import Path
import csv

tokens = []
dashes = "------------------------------------------------------------------------"


fields = ["distance", "year", "color", "price", "info", "token"]

with open("TOKENS.txt", "r") as txt_file:
    urls = txt_file.read().split("\n")[:-1]

with open("info.csv", 'w', encoding="UTF-8") as csv_file:

    writer = csv.writer(csv_file)

    writer.writerow(fields)
    
    for url in urls:

        info = []
        data = []

        url = main_url + url
        print(url)

        res = get(url).content

        try:
            dyc = res[0]["data"]["items"]

            distance = dyc[0]["value"]
            info.append(distance)

            year = dyc[1]["value"]
            info.append(year)

            color = dyc[2]["value"]
            info.append(color)

            res = res[1:]

            for row in res:
                row = row["data"]

                    if "تومان" in row["value"]:
                        info.append(row["value"])
                    else:
                        continue

                else:
                    data.append(row)

            info.append(data)
            info.append(url)

            print(info)

            writer.writerow(info)

        except:
            continue

        print(dashes)