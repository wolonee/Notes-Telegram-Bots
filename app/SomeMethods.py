from telebot import types
import telebot
from NotesDB import *
from Buttons import *
from geopy.geocoders import Nominatim
from timezonefinder import TimezoneFinder
from pytz import timezone
import datetime as dt
import config
import random
import string
from datetime import datetime


SUCCESS_EFFECT_IDS = ["5104841245755180586", "5107584321108051014", "5046509860389126442"] #🔥 👍 🎉
FAIL_EFFECT_IDS = ["5104858069142078462", "5046589136895476101"] #👎 💩



class Class_of_methods:

    def __init__(self):
        self.bot = telebot.TeleBot(config.BOT_TOKEN)
        self.db = DataBase_Table(config.DataUrl)
        pass



    def get_time__with_timezone(self, tz_name):
        tz = timezone(tz_name)
        current_time = dt.datetime.now(tz)
        cur_time = current_time.strftime('%d:%H:%M')

        return cur_time
    

    def get_day__with_timezone(self, tz_name):
        tz = timezone(tz_name)
        current_time = dt.datetime.now(tz)
        cur_time = current_time.strftime('%d')

        return cur_time
    


    def find_timezone(self, region):
        geolocator = Nominatim(user_agent="timezone_bot")
        tz_finder = TimezoneFinder()

        try:
            location = geolocator.geocode(region)
            if location is None:
                print(f"Не удалось найти информацию о регионе: {region}. Попробуйте уточнить название.")
                return False
            
            tz_name = tz_finder.timezone_at(lng=location.longitude, lat=location.latitude)
            if tz_name is None:
                print(f"Не удалось определить часовой пояс для региона: {region}.")
                return False
            
            tz = timezone(tz_name)
            current_time = dt.datetime.now(tz)
            cur_time = current_time.strftime('%d:%H:%M')
            
            print(f"Часовой пояс для {region}: {tz_name}\n"
                        f"Текущее время: {current_time.strftime('%d:%H:%M')}")

            return [region, tz_name, cur_time]
        

        except Exception as e:
            print(f"Произошла ошибка: {str(e)}")
            return False



    def get_QUESTS_FOR_TODAY(self, UserId):
        self.db.ACTIONS_QUESTS_FOR_TODAY(UserId, action="get")



    def generate_random_string(self, length):
        characters = string.ascii_letters + string.digits
        random_string = ''.join(random.choice(characters) for _ in range(length))
        return random_string



    def remember_task(self, message):
        if message.content_type == 'text':
            text = message.text
            photo = None
        elif message.content_type == 'photo':
            text = message.caption
            photo_id = message.photo[-1].file_id
            file_info = self.bot.get_file(photo_id)
            photo = self.bot.download_file(file_info.file_path)
        
        tz = db.Get_Time_Zone(f"{message.from_user.id}")
        cur_time = self.get_time__with_timezone(tz)
        print(cur_time)

        time_object = dt.datetime.strptime(cur_time, '%d:%H:%M')
        new_time_1 = time_object + dt.timedelta(minutes=20)
        new_time_2 = time_object + dt.timedelta(hours=12)
        new_time_3 = time_object + dt.timedelta(hours=32)
        new_time_4 = time_object + dt.timedelta(days=4)
        new_time_5 = time_object + dt.timedelta(days=16)

        new_before_time_1 = new_time_1.strftime('%d:%H:%M')
        new_before_time_2 = new_time_2.strftime('%d:%H:%M')
        new_before_time_3 = new_time_3.strftime('%d:%H:%M')
        new_before_time_4 = new_time_4.strftime('%d:%H:%M')
        new_before_time_5 = new_time_5.strftime('%d:%H:%M')

        UnicKey_1 = self.generate_random_string(40)
        UnicKey_2 = self.generate_random_string(40)
        UnicKey_3 = self.generate_random_string(40)
        UnicKey_4 = self.generate_random_string(40)
        UnicKey_5 = self.generate_random_string(40)

        db.ACTIONS_FOR_QUEUE(action="add", queue={"UserId":f"{message.from_user.id}", "now_date":cur_time, "time_before":new_before_time_1, "data_type":"remember", "msg_text":text, "photo":photo, "UnicKey": UnicKey_1})
        db.ACTIONS_FOR_QUEUE(action="add", queue={"UserId":f"{message.from_user.id}", "now_date":cur_time, "time_before":new_before_time_2, "data_type":"remember", "msg_text":text, "photo":photo, "UnicKey": UnicKey_2})
        db.ACTIONS_FOR_QUEUE(action="add", queue={"UserId":f"{message.from_user.id}", "now_date":cur_time, "time_before":new_before_time_3, "data_type":"remember", "msg_text":text, "photo":photo, "UnicKey": UnicKey_3})
        db.ACTIONS_FOR_QUEUE(action="add", queue={"UserId":f"{message.from_user.id}", "now_date":cur_time, "time_before":new_before_time_4, "data_type":"remember", "msg_text":text, "photo":photo, "UnicKey": UnicKey_4})
        db.ACTIONS_FOR_QUEUE(action="add", queue={"UserId":f"{message.from_user.id}", "now_date":cur_time, "time_before":new_before_time_5, "data_type":"remember", "msg_text":text, "photo":photo, "UnicKey": UnicKey_5})


        self.bot.send_message(message.from_user.id, "Записал, теперь я хакну твой мозг и ты запомнтшь эту инфу навсегда", parse_mode='HTML', reply_markup=markup_Inline_BACK)

        # try:
        #     self.bot.delete_message(message.chat.id, message.message_id)
        #     self.bot.delete_message(message.chat.id, message.message_id-1)
        # except:
        #     pass



    def Remind_TODAY_TASKS(self, UserId, action="send", msg=None):
        if action == "send":

            res = db.ACTIONS_QUESTS_FOR_TODAY(UserId, text=None, action="get")
            markup_InlineToday = types.InlineKeyboardMarkup(row_width=1)
            num = 0
            for task_caption in res:
                Inline_TodayTask = types.InlineKeyboardButton(text=f"⭕️ {task_caption}", callback_data=f"COMPLETED_TASK_TODAY|{num}")
                markup_InlineToday.add(Inline_TodayTask)
                num += 1

            self.bot.send_message(UserId, "Вот и очередной день подошёл к концу.\n\nСначала нажми на сделанные задачи", parse_mode='HTML', reply_markup=markup_InlineToday)


        if action == "self_completed":

            res = db.ACTIONS_QUESTS_FOR_TODAY(UserId, text=None, action="get")
            markup_InlineToday = types.InlineKeyboardMarkup(row_width=1)
            num = 0
            for task_caption in res:
                Inline_TodayTask = types.InlineKeyboardButton(text=f"⭕️ {task_caption}", callback_data=f"SELF_DO_TASK_TODAY|{num}")
                markup_InlineToday.add(Inline_TodayTask)
                num += 1
            Inline_Btn = types.InlineKeyboardButton(text="Back↩️", callback_data="MENU_QUESTS_FOR_TODAY")
            markup_InlineToday.add(Inline_Btn)

            self.bot.send_message(UserId, "🥷🏿 Выбери задачи, которые ты уже сделал", parse_mode='HTML', reply_markup=markup_InlineToday)


        if action == "delete":
            res = db.ACTIONS_QUESTS_FOR_TODAY(UserId, text=None, action="get")
            markup_InlineToday = types.InlineKeyboardMarkup(row_width=1)
            num = 0
            for task_caption in res:
                Inline_TodayTask = types.InlineKeyboardButton(text=f"🧷 {task_caption}", callback_data=f"DELETE_TASK_TODAY|{num}")
                markup_InlineToday.add(Inline_TodayTask)
                num += 1
            Inline_TodayTask = types.InlineKeyboardButton(text=f"Back↩️", callback_data=f"MENU_QUESTS_FOR_TODAY")
            markup_InlineToday.add(Inline_TodayTask)

            self.bot.edit_message_text(chat_id=msg.from_user.id, message_id=msg.message.message_id, text="Удали лишние задачи", parse_mode='HTML', reply_markup=markup_InlineToday)




    def MORNING_TASKS(self, UserId, action="send", msg=None):
        if action == "send":

            res = db.ACTIONS_QUESTS_FOR_TODAY(str(UserId), text=None, action="get")
            last_res = res[-8:]
            markup_InlineToday = types.InlineKeyboardMarkup(row_width=1)
            num = 0

            for task_caption in last_res:
                if task_caption[0] != "—":
                    Inline_TodayTask = types.InlineKeyboardButton(text=f"🔰 {task_caption}", callback_data=f"COMPLETED_TASK_TODAY|{num}")
                else:
                    Inline_TodayTask = types.InlineKeyboardButton(text=f"{task_caption}", callback_data=f"COMPLETED_TASK_TODAY|{num}")

                markup_InlineToday.add(Inline_TodayTask)
                num += 1

                
            self.bot.send_message(UserId, "<b>Не проеби свое будущее</b>\n\nДавай блять, не давай мозгу осознать объем работы", parse_mode='HTML', reply_markup=markup_InlineToday)




    def weeks_until_exam(self, exam_date_str):
        today = datetime.today()
        exam_date = datetime.strptime(exam_date_str, "%Y-%m-%d")
        
        if today > exam_date:
            exam_date = exam_date.replace(year=today.year + 1)
        
        time_left = exam_date - today

        return time_left.days
    


# methods_instance = Class_of_methods()
# now_date = methods_instance.get_time__with_timezone("Europe/Samara")
# methods_instance.calculation_for_falling_asleep("01:20")
# methods_instance.find_timezone("Татарстан")
# tm = methods_instance.get_time__with_timezone("Europe/Moscow")

# Дата экзамена
# exam_date = "2025-05-31"

# # Вызываем функцию
# weeks = methods_instance.weeks_until_exam(exam_date)

# print(f"До экзамена осталось {weeks} недель")
