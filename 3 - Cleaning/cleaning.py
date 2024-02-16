import pandas as pd
from re import findall
import csv

csv_file = pd.read_csv("info.csv", encoding='utf8')
df = pd.DataFrame(csv_file)


df = df.drop_duplicates(subset='token', keep='first')
df = df.reset_index(drop=True)

motor = []
chassis = []
bodys = []
insurance = []
gearbox = []
price = []
fuel = []
distance = []
color = []
brand_type = []
age = []


for data in df["distance"]:
    data = int(data.replace("٬", ""))
    distance.append(data)

for data in df["year"]:
    data = int(data)

    if data > 1600:
        age.append(2023 - data)
    else:
        age.append(1402 - data)

for data in df["color"]:
    color.append(data)

for data in df["price"]:
    if "تومان" in data:
        data = data.split("تومان")[0]
    if "٬" in data:
        data = int(data.replace("٬", ""))
    price.append(data)

for data in df["info"]:

    brand_type_ = findall(r"'برند و تیپ', 'value': '(.+?)'", data)

    brand_type_ = brand_type_[0].replace(r"\u200c", ' ')

    brand_type.append(brand_type_)

    motor_ = findall(r"'وضعیت موتور', 'value': '(.+?)'", data)

    if len(motor_) == 0:
        motor_ = None
    
    else:
        motor_ = motor_[0]

    motor.append(motor_)


    chassis_ = findall(r"'وضعیت شاسی......ها', 'value': '(.+?)'", data)
    if len(chassis_) == 0:
        chassis_ = None
    else:
        chassis_ = chassis_[0]

    chassis.append(chassis_)


    insurance_ = findall(r"'مهلت بیمهٔ شخص ثالث', 'value': '(.+?)'", data)
    if len(insurance_) == 0:
        insurance_ = None

    else:
        insurance_ = insurance_[0]
        insurance_ = int(insurance_.split("ماه")[0])


    insurance.append(insurance_)


    body_ = findall(r"'وضعیت بدنه', 'value': '(.+?)'", data)

    if len(body_) == 0:
        body_ = None

    else:
        body_ = body_[0].replace(r"\u200c", ' ')

    bodys.append(body_)

    gearbox_ = findall(r"'گیربکس', 'value': '(.+?)'", data)
    if len(gearbox_) == 0:
        gearbox_ = None

    else:
        gearbox_ = gearbox_[0]

    gearbox.append(gearbox_)


    fuel_ = findall(r"'نوع سوخت', 'value': '(.+?)'", data)
    if len(fuel_) == 0:
        fuel_ = None

    else:
        fuel_ = fuel_[0]

    fuel.append(fuel_)


df = df.drop('token', axis=1)
df = df.drop('info', axis=1)
df = df.drop('distance', axis=1)
df = df.drop('year', axis=1)
df = df.drop('color', axis=1)
df = df.drop('price', axis=1)

df['MotorState'] = motor
df['ChassisState'] = chassis
df['BodyState'] = bodys
df['Insurance'] = insurance
df['Gearbox'] = gearbox
df['Price'] = price
df['Usage'] = distance
df['Age'] = age
df['Color'] = color
df['FuelType'] = fuel
df["BrandType"] = brand_type

df['BrandType'] = df['BrandType'].str.replace(r"\\u200c", ' ')
df['Gearbox'] = df['Gearbox'].str.replace(r"\\u200c", ' ')
df['FuelType'] = df['FuelType'].str.replace(r"\\u200c", ' ')

print(df)
print(df.info())

df.to_csv("cleaned.csv", encoding = "utf-8-sig", index = False)