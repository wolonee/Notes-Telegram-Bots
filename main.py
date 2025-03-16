
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
import random
import Crypto
# import queue


import config


bot=telebot.TeleBot(config.BOT_TOKEN)
db = DataBase_Table(config.DataUrl)
# data_queue = queue.Queue()
# file_queue.put(message)


# trial_period = 0
# people = 0
# user_id = ""
# all_users = ""

SUCCESS_EFFECT_IDS = ["5104841245755180586", "5107584321108051014", "5046509860389126442"] #🔥 👍 🎉
FAIL_EFFECT_IDS = ["5104858069142078462", "5046589136895476101"] #👎 💩

Some_methods = Class_of_methods()

    ################################  ФУНКЦИИ  #####################################


def start_db():
    global all_users
    all_users = db.GetUsersAll()
    print(all_users)


def schedule_checker():
    while True:
        schedule.run_pending()
        time.sleep(2)





def Morning_tasks():
    UserId = 324430515
    db.ACTIONS_QUESTS_FOR_TODAY(UserId, "———— 🔆 MORNING ————", action="add")
    db.ACTIONS_QUESTS_FOR_TODAY(UserId, "Я БЛАГОДАРЕН ЗА ВСЕ ❤️", action="add")
    db.ACTIONS_QUESTS_FOR_TODAY(UserId, "ДАЙ МНЕ СИЛЫ ДЛЯ ПРЕОДОЛЕНИЯ ВСЕХ ПРЕГРАД", action="add")
    db.ACTIONS_QUESTS_FOR_TODAY(UserId, "———— 🌙 NIGHT ————", action="add")
    db.ACTIONS_QUESTS_FOR_TODAY(UserId, "Не дрочил", action="add")
    db.ACTIONS_QUESTS_FOR_TODAY(UserId, "Записать квесты на завтра", action="add")

    Some_methods.MORNING_TASKS(action="send", UserId=324430515)

    exam_date = "2025-05-31"
    life_end_date = "2078-12-04"
    life_start_date = "2007-12-04"
    days = Some_methods.weeks_until_exam(exam_date)
    days_life = Some_methods.weeks_until_exam(life_end_date)
    weeks_exam = days//7
    weeks_life = days_life//7

    bot.send_message(UserId, f"До экзамена осталось {weeks_exam} недель ({days} дней)", parse_mode='HTML')

    tz = db.Get_Time_Zone(f"{UserId}")
    cur_time = Some_methods.get_time__with_timezone(tz)

    time_object = dt.datetime.strptime(cur_time, '%d:%H:%M')

    for _ in range(16):
        random_hours = random.randint(1, 16)
        random_minutes = random.randint(1, 60)
        new_time_1 = time_object + dt.timedelta(hours=random_hours) + dt.timedelta(minutes=random_minutes)
        UnicKey_1 = Some_methods.generate_random_string(40)
        db.ACTIONS_FOR_QUEUE(action="add", queue={"UserId":f"{UserId}", "now_date":None, "time_before":new_time_1, "data_type":"i_will_be_success", "msg_text":None, "photo":None, "UnicKey":UnicKey_1})







def Remind_evenng():
    message = None
    try:
        queue_data = db.ACTIONS_FOR_QUEUE(action="get")
        if queue_data:
            message = queue_data
        else:
            print("Очередь пуста. Ожидание новых сообщений...")
    except Exception as e:
        print(f"Ошибка: {e}")

    # data_queue.put({"UserId":message.from_user.id, "now_date":cur_time, "time_before":new_before_time_5, "data_type":"remember", "msg_text":text, "UnicKey":"ADaktnhx"})

    if message is not None:
        for queue in message:
            UserId = queue["UserId"]
            tz = db.Get_Time_Zone(UserId)
            now_date = Some_methods.get_time__with_timezone(tz)
            time_before = queue["time_before"]
            data_type = queue["data_type"]
            text = queue["msg_text"]
            UnicKey = queue["UnicKey"]
            photo = queue["photo"]

            if data_type == "remember":
                now_date_obj = dt.datetime.strptime(now_date, '%d:%H:%M')
                time_before_obj = dt.datetime.strptime(time_before, '%d:%H:%M')
                if now_date_obj > time_before_obj:
                    if photo:
                        bot.send_photo(UserId, photo, caption=f"Одно из твоих напоминаний:<blockquote>{text}</blockquote>", parse_mode='HTML', disable_notification=True)
                    else:
                        bot.send_message(UserId, f"Одно из твоих напоминаний:\n\n<blockquote>{text}</blockquote>", parse_mode='HTML', disable_notification=True)
                    db.ACTIONS_FOR_QUEUE(action="delete", UnicKey_input=UnicKey)


            elif data_type == "finish_evening_tasks":
                evening_time = f"{now_date.split(":")[0]}:21:00"
                if now_date > evening_time:
                    Some_methods.Remind_TODAY_TASKS(action="send", UserId=UserId)
                    db.ACTIONS_FOR_QUEUE(action="delete", UnicKey_input=UnicKey)


            # elif data_type == "post_video":
            #     now_date_obj = dt.datetime.strptime(now_date, '%d:%H:%M')
            #     time_before_obj = dt.datetime.strptime(time_before, '%d:%H:%M')
            #     if now_date_obj > time_before_obj:
            #         if now_date_obj > time_before_obj:
            #             if now_date_obj > time_before_obj:
            #                 if now_date_obj > time_before_obj:
            #                     bot.send_message(UserId, f"Этот должен пробить 100КК💸💸💸", parse_mode='HTML', reply_markup=markup_finish_post_video)
            #                     db.ACTIONS_FOR_QUEUE(action="delete", UnicKey_input=UnicKey)
            #                 else:
            #                     bot.send_message(UserId, f"Нужно больше просмотров💸💸💸", parse_mode='HTML', reply_markup=markup_finish_post_video)
            #                     db.ACTIONS_FOR_QUEUE(action="delete", UnicKey_input=UnicKey)
            #             else:
            #                 bot.send_message(UserId, f"Некст видосы летят💸💸💸", parse_mode='HTML', reply_markup=markup_finish_post_video)
            #                 db.ACTIONS_FOR_QUEUE(action="delete", UnicKey_input=UnicKey)
            #         else:
            #             bot.send_message(UserId, f"Жду первые видосы💸💸💸", parse_mode='HTML', reply_markup=markup_finish_post_video)
            #             db.ACTIONS_FOR_QUEUE(action="delete", UnicKey_input=UnicKey)
            #     else:
            #         pass


            elif data_type == "i_will_be_success":
                now_date_obj = dt.datetime.strptime(now_date, '%d:%H:%M')
                if now_date_obj > time_before:
                    some_dict = {
                        1 : "У МЕНЯ ПОЛУЧИТСЯ",
                        2 : "Я СМОГ БЛЯТЬ",
                        3 : "Я ПОСТУПИЛ В ИННОПОЛИС СУКА",
                        4 : "Я ПОСТУПИЛ В ИННОПОЛИС",
                        5 : "У МЕНЯ ВСЁ ПОЛУЧИЛОСЬ",
                        6 : "I WILLL BE SUCCEESSSS",
                        8 : "Я БЛАГОДАРЕН ЗА ВЕСЬ ПИЗДЕЦ",
                    }
                    rand_num = random.randint(1, 7)
    
                    bot.send_message(UserId, f"<b>{some_dict[rand_num]}</b>", parse_mode='HTML', reply_markup=markup_I_WILL_BE_SUCCESS)
                    db.ACTIONS_FOR_QUEUE(action="delete", UnicKey_input=UnicKey)




def func_start():
    global all_users
    for i in all_users:
        try:
            user_id = i[0]
            bot.send_message(user_id, f"<b>Замечены сбои, работаем над этим</b>", parse_mode='HTML')
            
        except Exception as e:
            print(e)



def time_qualifier(message):
    region = message.text
    timezone = Some_methods.find_timezone(region)
    
    if timezone == False:
        msg = bot.send_message(message.from_user.id, "Неверный регион!\n\nПроверь правильность написания, или укажи регион с таким же часовым поясом")
        bot.register_next_step_handler(msg, time_qualifier)

    reg = timezone[0]
    tz_name = timezone[1]
    cur_time = timezone[2]

    msg = bot.send_message(message.from_user.id, f"Сейчас у вас: {cur_time}\n\nНапоминать о заданиях буду ближе к 21:00")
    db.Add_Time_Zone(str(message.from_user.id), tz_name)
    TODAY_TASKS(message)


def ask_for_quest(call):
    input_text_QUESTS_FOR_TODAY = bot.send_message(call.from_user.id, "Записал ✅", parse_mode='HTML', disable_notification=True)
    bot.register_next_step_handler(input_text_QUESTS_FOR_TODAY, Add_QUESTS_FOR_TODAY)


def Add_QUESTS_FOR_TODAY(call):
    stop_mean=db.ACTIONS_STOP(f"{call.from_user.id}", action="get")
    print(stop_mean)
    if not stop_mean:
        text = call.text
        db.ACTIONS_QUESTS_FOR_TODAY(f"{call.from_user.id}", text, action="add")
        ask_for_quest(call)


def TODAY_TASKS(call):
    db.ACTIONS_STOP(f"{call.from_user.id}", action="False")
    bot.edit_message_text(chat_id=call.from_user.id, message_id=call.message.message_id, text="Я буду записывать задачи по одной\n\n<i>Пример:\nДоделать свой проект</i>", parse_mode='HTML', reply_markup=markup_Inline_Back22)
    # bot.register_next_step_handler(input_text_QUESTS_FOR_TODAY, Add_QUESTS_FOR_TODAY)
    @bot.message_handler(content_types=["text"])
    def wait_text(message: types.Message):
        stop_mean=db.ACTIONS_STOP(f"{message.from_user.id}", action="get")
        if not stop_mean:
            text = message.text
            db.ACTIONS_QUESTS_FOR_TODAY(f"{message.from_user.id}", text, action="add")
            ask_for_quest(message)




def ask_for_quest_GOAL(call):
    input_text_QUESTS_FOR_TODAY = bot.send_message(call.from_user.id, "Записал ✅", parse_mode='HTML', disable_notification=True)
    bot.register_next_step_handler(input_text_QUESTS_FOR_TODAY, Add_QUESTS_FOR_TODAY)


def Add_GOAL(call):
    stop_mean=db.ACTIONS_STOP(f"{call.from_user.id}", action="get")
    print(stop_mean)
    if not stop_mean:
        text = call.text
        db.ACTIONS_QUESTS_FOR_TODAY(f"{call.from_user.id}", text, action="add")
        ask_for_quest(call)


def GOALS(call):
    db.ACTIONS_STOP(f"{call.from_user.id}", action="False")
    bot.edit_message_text(chat_id=call.from_user.id, message_id=call.message.message_id, text="Я буду записывать задачи по одной\n\n<i>Пример:\nДоделать свой проект</i>", parse_mode='HTML', reply_markup=markup_Inline_Back22)
    @bot.message_handler(content_types=["text"])
    def wait_text(message: types.Message):
        stop_mean=db.ACTIONS_STOP(f"{message.from_user.id}", action="get")
        if not stop_mean:
            text = message.text
            db.ACTIONS_QUESTS_FOR_TODAY(f"{message.from_user.id}", text, action="add")
            ask_for_quest(message)



def main_menu(message):
    bot.send_message(message.from_user.id, f"📋 <b>Ты находишься в главном меню</b>\n\nВыбери действие:",  reply_markup=markup_Inline_Back1, parse_mode='HTML')







        ###########################      ПРИВЕТСТВИЕ      ##############################

@bot.message_handler(commands=["start"])
def menu(message: types.Message):
    if message.chat.type == 'private':
        if not db.CheckRegistr(f"{message.from_user.id}"):

            start_command = message.text
            referal_id = str(start_command[7:])

            if str(referal_id) != "":
                if str(referal_id) != str(message.from_user.id):
                    db.AddUser(f"{message.from_user.id}", referal_id, message.from_user.username)
                    # time_zone = bot.send_message(message.from_user.id, f"Нужно определить ваш часовой пояс, напишите область, или город в котором вы проживаете. (для скрытности можете написать область с таким же часовым поясом)")
                    # bot.register_next_step_handler(time_zone, time_qualifier)
                    main_menu(message)

                    try:
                        bot.send_message(referal_id, f"По вашей ссылке зарегестрировался новый пользователь❇️")
                    except:
                        pass
                    
                else:
                    main_menu(message)
            else:
                db.AddUser(f"{message.from_user.id}", None, message.from_user.username)
                # time_zone = bot.send_message(message.from_user.id, f"Нужно определить ваш часовой пояс, напишите область, или город в котором вы проживаете. (для скрытности можете написать область с таким же часовым поясом)")
                # bot.register_next_step_handler(time_zone, time_qualifier)
                main_menu(message)
        else:
            main_menu(message)
    else:
        main_menu(message)







 


"""


                P R E - C A L L B A C K  Q U E R Y  H A N D L E R


"""









@bot.callback_query_handler(func=lambda call: call.data.startswith('CONDITION_completed_task_today') or call.data.startswith('CONDITION_delete_task_today') or call.data.startswith('CONDITION_self_do_task_today') or call.data.startswith('CONDITION_uncomp_task_today') or call.data.startswith('CONDITION_morning_comp_task_today'))
def reg(call):
    # try:
    if "CONDITION_completed_task_today" in call.data:
        tz_name = db.Get_Time_Zone(f"{call.from_user.id}")
        tz = timezone(tz_name)
        current_time = dt.datetime.now(tz)
        formatted_date = current_time.strftime('%d %B').lstrip('0')

        index=call.data.split('|')[1]
        text_btn=db.ACTIONS_QUESTS_FOR_TODAY(f"{call.from_user.id}", index=int(index), action="get_by_index")
        db.ACTIONS_QUESTS_FOR_TODAY(f"{call.from_user.id}", index=int(index), action="remove_by_index")
        db.ACTIONS_HISTORY_FINISH_TASKS(f"{call.from_user.id}", text=text_btn, action="add", date=formatted_date)
        res = db.ACTIONS_QUESTS_FOR_TODAY(f"{call.from_user.id}", text=None, action="get")
        markup_InlineToday = types.InlineKeyboardMarkup(row_width=1)
        num = 0

        if len(res) > 0:
            bot.answer_callback_query(call.id, text=f'Сделано ✅', show_alert = False)
            for task_caption in res:
                Inline_TodayTask = types.InlineKeyboardButton(text=f"🔰 {task_caption}", callback_data=f"CONDITION_completed_task_today|{num}")
                markup_InlineToday.add(Inline_TodayTask)
                num += 1
        
            bot.edit_message_reply_markup(call.message.chat.id, call.message.message_id, reply_markup=markup_InlineToday)
        else:
            bot.answer_callback_query(call.id, text=f'Ты стал ближе к своей цели...', show_alert = True)
            bot.delete_message(chat_id=call.message.chat.id, message_id=call.message.message_id)




    elif "CONDITION_morning_comp_task_today" in call.data:
        tz_name = db.Get_Time_Zone(f"{call.from_user.id}")
        tz = timezone(tz_name)
        current_time = dt.datetime.now(tz)
        formatted_date = current_time.strftime('%d %B').lstrip('0')

        index=call.data.split('|')[1]
        tasks_list, relative_index = db.ACTIONS_QUESTS_FOR_TODAY(f"{call.from_user.id}", text=None, action="get_morning_tasks")
        total_index = relative_index + int(index)
        print(total_index, relative_index)

        text_btn = db.ACTIONS_QUESTS_FOR_TODAY(f"{call.from_user.id}", index=total_index, action="get_by_index")

        db.ACTIONS_QUESTS_FOR_TODAY(f"{call.from_user.id}", index=total_index, action="remove_by_index")
        db.ACTIONS_HISTORY_FINISH_TASKS(f"{call.from_user.id}", text=text_btn, action="add", date=formatted_date)

        markup_InlineToday = types.InlineKeyboardMarkup(row_width=1)
        tasks_list.remove(text_btn)
        num = 0

        if len(tasks_list) > 0:
            bot.answer_callback_query(call.id, text=f'Сделано ✅', show_alert = False)
            for task_caption in tasks_list:
                Inline_TodayTask = types.InlineKeyboardButton(text=f"{task_caption}", callback_data=f"CONDITION_morning_comp_task_today|{num}")
                markup_InlineToday.add(Inline_TodayTask)
                num += 1
        
            bot.edit_message_reply_markup(call.message.chat.id, call.message.message_id, reply_markup=markup_InlineToday)
        else:
            bot.answer_callback_query(call.id, text=f'.....................', show_alert = True)
            bot.delete_message(chat_id=call.message.chat.id, message_id=call.message.message_id)
    




    elif "CONDITION_self_do_task_today" in call.data:
        tz_name = db.Get_Time_Zone(f"{call.from_user.id}")
        tz = timezone(tz_name)
        current_time = dt.datetime.now(tz)
        formatted_date = current_time.strftime('%d %B').lstrip('0')

        index=call.data.split('|')[1]
        text_btn=db.ACTIONS_QUESTS_FOR_TODAY(f"{call.from_user.id}", index=int(index), action="get_by_index")


        db.ACTIONS_QUESTS_FOR_TODAY(f"{call.from_user.id}", index=int(index), action="remove_by_index")
        db.ACTIONS_HISTORY_FINISH_TASKS(f"{call.from_user.id}", text=text_btn, action="add", date=formatted_date)
        res = db.ACTIONS_QUESTS_FOR_TODAY(f"{call.from_user.id}", text=None, action="get")
        markup_InlineToday = types.InlineKeyboardMarkup(row_width=1)
        num = 0

        if len(res) > 0:
            bot.answer_callback_query(call.id, text=f'Сделано ✅', show_alert = False)
            for task_caption in res:
                Inline_TodayTask = types.InlineKeyboardButton(text=f"🔰 {task_caption}", callback_data=f"CONDITION_self_do_task_today|{num}")
                markup_InlineToday.add(Inline_TodayTask)
                num += 1
            Inline_Btn = types.InlineKeyboardButton(text="Back↩️", callback_data="MENU_QUESTS_FOR_TODAY")
            markup_InlineToday.add(Inline_Btn)
        
            bot.edit_message_reply_markup(call.message.chat.id, call.message.message_id, reply_markup=markup_InlineToday)
        else:
            bot.answer_callback_query(call.id, text=f'Ты стал ближе к своей цели...', show_alert = True)
            bot.delete_message(chat_id=call.message.chat.id, message_id=call.message.message_id)
        




    elif "CONDITION_delete_task_today" in call.data:
        index=call.data.split('|')[1]
        db.ACTIONS_QUESTS_FOR_TODAY(f"{call.from_user.id}", index=int(index), action="remove_by_index")
        res = db.ACTIONS_QUESTS_FOR_TODAY(f"{call.from_user.id}", text=None, action="get")
        markup_InlineToday = types.InlineKeyboardMarkup(row_width=1)
        num = 0

        if len(res) > 0:
            bot.answer_callback_query(call.id, text=f'Удалил 👌', show_alert = False)
            for task_caption in res:
                Inline_TodayTask = types.InlineKeyboardButton(text=f"🗑️ {task_caption}", callback_data=f"CONDITION_delete_task_today|{num}")
                markup_InlineToday.add(Inline_TodayTask)
                num += 1
            Inline_TodayTask = types.InlineKeyboardButton(text=f"Back↩️", callback_data=f"MENU_QUESTS_FOR_TODAY")
            markup_InlineToday.add(Inline_TodayTask)
        
            bot.edit_message_reply_markup(call.message.chat.id, call.message.message_id, reply_markup=markup_InlineToday)
        else:
            bot.answer_callback_query(call.id, text=f'Задач на сегодня не осталось ☹️\n\nВернись в меню задач, чтобы добавить новые', show_alert = True)
            bot.delete_message(chat_id=call.message.chat.id, message_id=call.message.message_id)





    elif "CONDITION_uncomp_task_today" in call.data:
        tz_name = db.Get_Time_Zone(f"{call.from_user.id}")
        tz = timezone(tz_name)
        current_time = dt.datetime.now(tz)
        formatted_date = current_time.strftime('%d %B').lstrip('0')


        index=call.data.split('|')[1]
        text_btn=db.ACTIONS_QUESTS_FOR_TODAY(f"{call.from_user.id}", index=int(index), action="get_by_index")
        db.ACTIONS_HISTORY_FINISH_TASKS(f"{call.from_user.id}", text=text_btn, action="add_foul", date=formatted_date)
        db.ACTIONS_QUESTS_FOR_TODAY(f"{call.from_user.id}", index=int(index), action="remove_by_index")

        
        res = db.ACTIONS_QUESTS_FOR_TODAY(f"{call.from_user.id}", text=None, action="get")
        markup_InlineToday = types.InlineKeyboardMarkup(row_width=1)
        num = 0

        if len(res) > 0:
            bot.answer_callback_query(call.id, text=f"It's delete", show_alert = False)
            for task_caption in res:
                Inline_TodayTask = types.InlineKeyboardButton(text=f"❌ {task_caption}", callback_data=f"CONDITION_uncomp_task_today|{num}")
                markup_InlineToday.add(Inline_TodayTask)
                num += 1
            Inline_TodayTask = types.InlineKeyboardButton(text=f"Back↩️", callback_data=f"MENU_QUESTS_FOR_TODAY")
            markup_InlineToday.add(Inline_TodayTask)

            bot.edit_message_reply_markup(call.message.chat.id, call.message.message_id, reply_markup=markup_InlineToday)
        else:
            bot.answer_callback_query(call.id, text=f'Bruh 💀', show_alert = True)
            bot.delete_message(chat_id=call.message.chat.id, message_id=call.message.message_id)



    # except Exception as e:
    #     print(repr(e))







"""


                M A I N  C A L L B A C K  Q U E R Y  H A N D L E R


"""







@bot.callback_query_handler(lambda call: True)
def callback_inline(call):
    try:
        if call.message:
            # if call.data=="BACK":
            #     bot.delete_message(call.message.chat.id, call.message.message_id)
            #     Back(call)


            if call.data=="STOP":
                db.ACTIONS_STOP(f"{call.from_user.id}", action="True")
                res = db.ACTIONS_QUESTS_FOR_TODAY(f"{call.from_user.id}", text=None, action="get")
                if res:
                    message_text = "\n\n❇️ ".join(res)
                else:
                    message_text = "Вы не добавили задачи"
                bot.send_message(call.from_user.id, f"®️<i>Эти квесты тебе помогают, но если ты хочешь быть дерьмом не делай их. Выбор всегда твой</i>\n\n<blockquote>📬<b>Your quests for today:\n\n❇️ {message_text}</b></blockquote>", parse_mode='HTML', reply_markup=markup_Inline_BACK_AFTER_STOP)
                bot.delete_message(call.message.chat.id, call.message.message_id)

                queue_list = db.ACTIONS_FOR_QUEUE(action="get")
                bool_mean = False
                for n_list in queue_list:
                    if str(call.from_user.id) == n_list["UserId"] and "finish_evening_tasks" == n_list["data_type"]:
                        bool_mean = True
                
                if not bool_mean:
                    UnicKey = Some_methods.generate_random_string(40)
                    db.ACTIONS_FOR_QUEUE(action="add", queue={"UserId":f"{call.from_user.id}", "now_date":None, "time_before":None, "data_type":"finish_evening_tasks", "msg_text":None, "photo":None, "UnicKey":UnicKey})


            elif call.data=="START_MENU":
                bot.delete_message(call.message.chat.id, call.message.message_id)
                bot.send_message(call.from_user.id, f"📔 <b>Ты находишься в главном меню</b>\n\nВыбери действие:",  reply_markup=markup_Inline_Back1, parse_mode='HTML')


            elif call.data=="MENU_QUESTS_FOR_TODAY":
                bot.edit_message_text(chat_id=call.from_user.id, message_id=call.message.message_id, text=f"👨‍💻 Что ты хочешь сделать?", reply_markup=markup_Inline_QUESTS_FOR_TODAY)


            elif call.data=="COMPLETE_QUESTS_FOR_TODAY":
                Some_methods.Remind_TODAY_TASKS(action="self_completed", UserId=call.from_user.id)


            elif call.data=="UNCOMP_QUESTS_FOR_TODAY":
                Some_methods.Remind_TODAY_TASKS(action="self_uncomp", UserId=call.from_user.id)


            elif call.data=="CHECK_QUESTS_FOR_TODAY":
                res = db.ACTIONS_QUESTS_FOR_TODAY(f"{call.from_user.id}", text=None, action="get")
                if res:
                    message_text = "\n\n ".join(res)
                else:
                    message_text = "Вы не добавили задачи"
                bot.edit_message_text(chat_id=call.from_user.id, message_id=call.message.message_id, text=f"®️<i>Эти квесты тебе помогают, но если ты хочешь быть дерьмом не делай их. Выбор всегда твой</i>\n\n<blockquote>📬<b>Your quests for today:\n\n❇️ {message_text}</b></blockquote>", parse_mode='HTML', reply_markup=markup_Inline_BACK_QUESTS_FOR_TODAY)


            elif call.data=="QUESTS_FOR_TODAY":
                if not db.Get_Time_Zone(f"{call.from_user.id}"):
                    bot.edit_message_text(chat_id=call.from_user.id, message_id=call.message.message_id, text=f"Чтобы напоминать тебе про задания нужно сравниться с твоим часовым поясом\n\n(указать надо только один раз)")
                    time.sleep(0.5)
                    time_zone = bot.send_message(call.from_user.id, f"Нужно определить ваш часовой пояс, напишите область, или город в котором вы проживаете\n\n(для скрытности можете написать область с таким же часовым поясом)")
                    bot.register_next_step_handler(time_zone, time_qualifier)

                else:
                    TODAY_TASKS(call)


            elif call.data=="DELETE_QUESTS_FOR_TODAY":
                Some_methods.Remind_TODAY_TASKS(action="delete", UserId=call.from_user.id, msg=call)


            elif call.data=="REMEMBER":
                if not db.Get_Time_Zone(f"{call.from_user.id}"):
                    time_qualifier(call)
                else: ############################################################################################################################################################
                    res = bot.edit_message_text(chat_id=call.from_user.id, message_id=call.message.message_id, text=f"Что тебе нужно запомнить?")
                    bot.register_next_step_handler(res, Some_methods.remember_task)





            elif call.data=="I_WILL_BE_SUCCESS_remember":
                bot.answer_callback_query(call.id, text=f'🚀🚀🚀', show_alert = True)
                bot.delete_message(call.message.chat.id, call.message.message_id)

                # bot.delete_message(call.message.chat.id, call.message.message_id)


            elif call.data=="ALL_FINISH_TASK":
                data = db.ACTIONS_HISTORY_FINISH_TASKS(UserId="324430515", action="get")
                msg_text = ""

                for date, entries in data.items():
                    num = 0
                    header_text = f"├-- <b>{date}</b>\n"
                    msg_text += header_text
                    for entry in entries:
                        num+=1
                        num_max = len(entries)
                        if num_max == num:
                            msg_text += f"└ {entry}\n\n"
                        else:
                            msg_text += f"├ {entry}\n"

                    msg_text = f"<blockquote>{msg_text}</blockquote>"

                bot.edit_message_text(chat_id=call.from_user.id, message_id=call.message.message_id, text=msg_text.strip(), reply_markup=markup_Inline_BACK, parse_mode='HTML')



            # elif call.data=="MY_GOALS":
            #     bot.edit_message_text(chat_id=call.from_user.id, message_id=call.message.message_id, text=f"Выбери действие:", reply_markup=markup_Inline_MY_GOALS_MENU)

            # elif call.data=="ADD_GOAL":
            #     bot.edit_message_text(chat_id=call.from_user.id, message_id=call.message.message_id, text=f"Выбери действие:", reply_markup=markup_Inline_MY_GOALS_MENU)

            # elif call.data=="COMPLETE_GOAL":
            #     bot.edit_message_text(chat_id=call.from_user.id, message_id=call.message.message_id, text=f"Выбери действие:", reply_markup=markup_Inline_MY_GOALS_MENU)

            # elif call.data=="DELETE_GOAL":
            #     bot.edit_message_text(chat_id=call.from_user.id, message_id=call.message.message_id, text=f"Выбери действие:", reply_markup=markup_Inline_MY_GOALS_MENU)

            # elif call.data=="CHECK_GOAL":
            #     bot.edit_message_text(chat_id=call.from_user.id, message_id=call.message.message_id, text=f"Выбери действие:", reply_markup=markup_Inline_MY_GOALS_MENU)


            # elif call.data=="TRY_AWAIKENING":
            #     bot.delete_message(call.message.chat.id, call.message.message_id)
            #     num_input = bot.send_message(call.from_user.id, "<b>Введите число:💤</b>\n\nПример:\n08:45 или 12:15", parse_mode='HTML')
            #     bot.register_next_step_handler(num_input, Some_methods.calculation_for_awakening)

            # elif call.data=="REFERAL_UPDATE":
            #     bot.delete_message(chat_id=call.message.chat.id, message_id=call.message.message_id)
            #     invite_people(call.message, user_id=call.from_user.id)

            # elif call.data=="CHECK_TRANSFERRED":
            #     invited_people(call.message, user_id=call.from_user.id)

            # elif call.data=="INFO_SLEEP":
            #     Info_for_Sleep(call)

    except Exception as e:
        print(repr(e))



#_________________________________________________#

if __name__ == '__main__':
    # start_db()
    schedule.every(12).seconds.do(Remind_evenng)
    Morning_tasks()
    # schedule.every().day.at("21:00").do(Remind_evenng)
    Thread(target=schedule_checker).start()
    # Spin up a thread to run the schedule check so it doesn't block your bot.
    # This will take the function schedule_checker which will check every second
    # to see if the scheduled job needs to be ran.
    # Morning_tasks()
    bot.infinity_polling()
    #telegram_bot(token)