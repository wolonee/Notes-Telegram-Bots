
from telebot import types

URL_USEFUL_INFO_1 = "https://lifehacker.ru/special/sleep/"
URL_USEFUL_INFO_2 = "https://lifehacker.ru/10-sposobov-uluchshit-svoj-son/"
URL_USEFUL_INFO_3 = "https://www.youtube.com/watch?v=xfbtIvPRZMY&t=862s"
URL_HARMFUL_INFO  = "https://lifehacker.ru/sleep-loss-consequences/"

        ################################   BUTTONS   ###################################

# markup_Reply_main = types.ReplyKeyboardMarkup(row_width=1, resize_keyboard=True)
# Reply_B1 = types.KeyboardButton(text="Ложусь спать…😴")
# Reply_B2 = types.KeyboardButton(text="Скажу время, в которое лягу…😴")
# # Reply_B3 = types.KeyboardButton(text="🔮 Инструкция использования")
# # Reply_B4 = types.KeyboardButton(text="Всё, что нужно знать о сне💁🏻‍♂️")
# markup_Reply_main.add(Reply_B1,Reply_B2)

# markup_Inline_Info_sleep = types.InlineKeyboardMarkup(row_width=1)
# Info_sleep = types.InlineKeyboardButton(text="Подробнее про сон🛌", callback_data="INFO_SLEEP")
# markup_Inline_Info_sleep.add(Info_sleep)

markup_Inline_Back1 = types.InlineKeyboardMarkup(row_width=1)
Inline_Back1 = types.InlineKeyboardButton(text="Quests for tuday📝", callback_data="MENU_QUESTS_FOR_TODAY")
Inline_Back2 = types.InlineKeyboardButton(text="Remember forever🧠", callback_data="REMEMBER")
Inline_Back3 = types.InlineKeyboardButton(text="Get all finish quests✅", callback_data="ALL_FINISH_TASK")
Inline_Back4 = types.InlineKeyboardButton(text="Post videos", callback_data="REMEMBER_POST_VIDEO")
# Inline_Back3 = types.InlineKeyboardButton(text="Задачи на неделю", callback_data="TRY_ASLEEP")
# Inline_Back4 = types.InlineKeyboardButton(text="Напоминани себе завтрашнему", callback_data="TRY_ASLEEP")
# Inline_Back5 = types.InlineKeyboardButton(text="Закрытый дневник", callback_data="TRY_ASLEEP")
markup_Inline_Back1.add(Inline_Back1, Inline_Back2, Inline_Back3, Inline_Back4)

markup_Inline_Back22 = types.InlineKeyboardMarkup(row_width=1)
Inline_Btn = types.InlineKeyboardButton(text="Stop ⛔️", callback_data="STOP")
markup_Inline_Back22.add(Inline_Btn)

markup_Inline_QUESTS_FOR_TODAY = types.InlineKeyboardMarkup(row_width=1)
Inline_Btn_1 = types.InlineKeyboardButton(text="💚 Add some", callback_data="QUESTS_FOR_TODAY")
Inline_Btn_4 = types.InlineKeyboardButton(text="💸 Сompleted", callback_data="COMPLETE_QUESTS_FOR_TODAY")
Inline_Btn_3 = types.InlineKeyboardButton(text="⛔️ Delete", callback_data="DELETE_QUESTS_FOR_TODAY")
Inline_Btn_2 = types.InlineKeyboardButton(text="📬 Check all", callback_data="CHECK_QUESTS_FOR_TODAY")
Inline_Btn = types.InlineKeyboardButton(text="Back↩️", callback_data="START_MENU")
markup_Inline_QUESTS_FOR_TODAY.add(Inline_Btn_1, Inline_Btn_4, Inline_Btn_3, Inline_Btn_2, Inline_Btn)

markup_Inline_BACK_QUESTS_FOR_TODAY = types.InlineKeyboardMarkup(row_width=1)
Inline_Btn = types.InlineKeyboardButton(text="Back↩️", callback_data="MENU_QUESTS_FOR_TODAY")
markup_Inline_BACK_QUESTS_FOR_TODAY.add(Inline_Btn)

markup_Inline_BACK = types.InlineKeyboardMarkup(row_width=1)
Inline_Btn = types.InlineKeyboardButton(text="Back↩️", callback_data="START_MENU")
markup_Inline_BACK.add(Inline_Btn)

markup_finish_post_video = types.InlineKeyboardMarkup(row_width=1)
Inline_Btn = types.InlineKeyboardButton(text="Я СМОГУ", callback_data="finish_post_video")
markup_finish_post_video.add(Inline_Btn)


# markup_Inline_Back2 = types.InlineKeyboardMarkup(row_width=1)
# Inline_Back_1 = types.InlineKeyboardButton(text="Назад↩️", callback_data="BACK")
# Inline_Back_2 = types.InlineKeyboardButton(text="Да✅", callback_data="TRY_AWAIKENING")
# markup_Inline_Back2.add(Inline_Back_1,Inline_Back_2)

# markup_link_Info_Sleep = types.InlineKeyboardMarkup(row_width=1)
# Inline_link_Info_Sleep1 = types.InlineKeyboardButton(text='СОН - ТОПЛЕС', url=URL_USEFUL_INFO_3)
# Inline_link_Info_Sleep2 = types.InlineKeyboardButton(text='Всё, что нужно знать о сне', url=URL_USEFUL_INFO_1)
# Inline_link_Info_Sleep3 = types.InlineKeyboardButton(text='10 способов улучшить свой сон', url=URL_USEFUL_INFO_2)
# Inline_link_Info_Sleep4 = types.InlineKeyboardButton(text='К чему приводит недостаток сна', url=URL_HARMFUL_INFO)
# markup_link_Info_Sleep.add(Inline_link_Info_Sleep1, Inline_link_Info_Sleep2, Inline_link_Info_Sleep3, Inline_link_Info_Sleep4)

# markup_Inline_Referal_Update = types.InlineKeyboardMarkup(row_width=1)
# Inline_Referal_Update = types.InlineKeyboardButton(text="Обновить🔄", callback_data="REFERAL_UPDATE")
# markup_Inline_Referal_Update.add(Inline_Referal_Update)

# markup_transferred = types.InlineKeyboardMarkup(row_width=1)
# Inline_transferred = types.InlineKeyboardButton(text="Проверить🌟", callback_data="CHECK_TRANSFERRED")
# markup_transferred.add(Inline_transferred)