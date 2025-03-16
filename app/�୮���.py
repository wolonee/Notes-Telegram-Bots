
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