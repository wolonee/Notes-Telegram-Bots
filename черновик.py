
from Buttons import *
from threading import Thread
from telebot import types
from datetime import datetime
from SomeMethods import *
from NotesDB import *
from PIL import Image
import schedule
import telebot
import time
import os
import subprocess
import queue


import config

# current_time = dt.datetime.now()
# cur_time = current_time.strftime('%d:%H:%M')

# evening_time = f"{cur_time.split(":")[0]}:17:37"
# # print(cur_time.split(":")[0])
# evening_time = dt.datetime.strptime(evening_time, '%d:%H:%M')
# time_object = dt.datetime.strptime(cur_time, '%d:%H:%M')
# new_time_1 = time_object + dt.timedelta(minutes=20)

# tz = db.Get_Time_Zone(f"{message.from_user.id}")
# cur_time = self.get_time__with_timezone(tz)

# time_object = dt.datetime.strptime(cur_time, '%d:%H:%M')



# now_date_obj = dt.datetime.strptime(cur_time, '%d:%H:%M')
# # if new_time_1 > now_date_obj:
# print(new_time_1)
# print(evening_time)
# print(evening_time-new_time_1)
# if new_time_1 > evening_time:
#     print(1414)

# tz = timezone("Europe/Samara")

# print(tz)

# current_time = dt.datetime.now()
# formatted_date = current_time.strftime('%d %B').lstrip('0')
# print(formatted_date)


# rand_num = random.randint(1, 7)
# print(some_dict[rand_num])


# elif call.data=="REMEMBER_POST_VIDEO":
#     bot.answer_callback_query(call.id, text=f'Напомню', show_alert = True)
#     tz = db.Get_Time_Zone(f"{call.from_user.id}")
#     cur_time = Some_methods.get_time__with_timezone(tz)

#     time_object = dt.datetime.strptime(cur_time, '%d:%H:%M')

#     new_time_1 = time_object.replace(hour=13, minute=00)
#     new_time_2 = time_object.replace(hour=15, minute=00)
#     new_time_3 = time_object.replace(hour=18, minute=00)
#     new_time_4 = time_object.replace(hour=21, minute=00)

#     new_before_time_1 = new_time_1.strftime('%d:%H:%M')
#     new_before_time_2 = new_time_2.strftime('%d:%H:%M')
#     new_before_time_3 = new_time_3.strftime('%d:%H:%M')
#     new_before_time_4 = new_time_4.strftime('%d:%H:%M')

#     UnicKey_1 = Some_methods.generate_random_string(40)
#     UnicKey_2 = Some_methods.generate_random_string(40)
#     UnicKey_3 = Some_methods.generate_random_string(40)
#     UnicKey_4 = Some_methods.generate_random_string(40)
#     db.ACTIONS_FOR_QUEUE(action="add", queue={"UserId":f"{call.from_user.id}", "now_date":None, "time_before":new_before_time_1, "data_type":"post_video", "msg_text":None, "photo":None, "UnicKey":UnicKey_1})
#     db.ACTIONS_FOR_QUEUE(action="add", queue={"UserId":f"{call.from_user.id}", "now_date":None, "time_before":new_before_time_2, "data_type":"post_video", "msg_text":None, "photo":None, "UnicKey":UnicKey_2})
#     db.ACTIONS_FOR_QUEUE(action="add", queue={"UserId":f"{call.from_user.id}", "now_date":None, "time_before":new_before_time_3, "data_type":"post_video", "msg_text":None, "photo":None, "UnicKey":UnicKey_3})
#     db.ACTIONS_FOR_QUEUE(action="add", queue={"UserId":f"{call.from_user.id}", "now_date":None, "time_before":new_before_time_4, "data_type":"post_video", "msg_text":None, "photo":None, "UnicKey":UnicKey_4})


# import csv

# words = [("apple", "яблоко"), ("run", "бежать")]

# with open('words.csv', 'w', newline='', encoding='utf-8') as file:
#     writer = csv.writer(file)
#     writer.writerow(["Term", "Definition"])  # Заголовки для Quizlet
#     for word, translation in words:
#         writer.writerow([word, translation])

# aa = ["65345", "7456", "673", "234"]
# aa.remove("65345")
# print(aa)

import requests
from datetime import datetime, timedelta

# Ваш API-ключ OpenWeatherMap
API_KEY = input("Введите ваш API-ключ OpenWeatherMap: ")
CITY = input("Введите название города: ")

# Получаем прогноз погоды
url = f"http://api.openweathermap.org/data/2.5/forecast?q={CITY}&units=metric&appid={API_KEY}"
response = requests.get(url)

if response.status_code != 200:
    print("Ошибка при запросе погоды. Проверьте корректность API-ключа и названия города.")
    exit()

data = response.json()

# Разделяем прогнозы на сегодня и завтра
current_date = datetime.now().date()
tomorrow_date = current_date + timedelta(days=1)

today_forecasts = []
tomorrow_forecasts = []

for forecast in data['list']:
    dt = datetime.fromtimestamp(forecast['dt'])
    if dt.date() == current_date:
        today_forecasts.append(forecast)
    elif dt.date() == tomorrow_date:
        tomorrow_forecasts.append(forecast)

# Выводим прогноз для сегодня
print(f"\nПрогноз погоды в {CITY} на сегодня ({current_date}):")
for forecast in today_forecasts:
    time = datetime.fromtimestamp(forecast['dt']).strftime("%H:%M")
    temp = forecast['main']['temp']
    description = forecast['weather'][0]['description']
    wind_speed = forecast['wind']['speed']
    pressure = forecast['main']['pressure']
    print(f"{time}:")
    print(f"  Температура: {temp}°C")
    print(f"  Описание: {description}")
    print(f"  Ветер: {wind_speed} м/с")
    print(f"  Давление: {pressure} мм рт. ст.")
    print()

# Выводим прогноз для завтра
print(f"\nПрогноз погоды в {CITY} на завтра ({tomorrow_date}):")
for forecast in tomorrow_forecasts:
    time = datetime.fromtimestamp(forecast['dt']).strftime("%H:%M")
    temp = forecast['main']['temp']
    description = forecast['weather'][0]['description']
    wind_speed = forecast['wind']['speed']
    pressure = forecast['main']['pressure']
    print(f"{time}:")
    print(f"  Температура: {temp}°C")
    print(f"  Описание: {description}")
    print(f"  Ветер: {wind_speed} м/с")
    print(f"  Давление: {pressure} мм рт. ст.")
    print()
