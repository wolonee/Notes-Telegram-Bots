
import random
from telebot import types



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

markup_Inline_Back1 = types.InlineKeyboardMarkup(row_width=2)
Inline_Back1 = types.InlineKeyboardButton(text="Quests for tuday📝", callback_data="MENU_QUESTS_FOR_TODAY")
Inline_Back2 = types.InlineKeyboardButton(text="Remember forever🧠", callback_data="REMEMBER")
Inline_Back3 = types.InlineKeyboardButton(text="Get all finish quests✅", callback_data="ALL_FINISH_TASK")
Inline_Back4 = types.InlineKeyboardButton(text="Ma dinary </3📔", callback_data="MY_DINARY")
Inline_Back5 = types.InlineKeyboardButton(text="Bussnes Cases🔒", callback_data="BUSSNES_CASES")
Inline_Back6 = types.InlineKeyboardButton(text="My goals-dreams🚀", callback_data="MY_GOALS-DREAMS")
# Inline_Back6 = types.InlineKeyboardButton(text="Post videos", callback_data="REMEMBER_POST_VIDEO")
# Inline_Back3 = types.InlineKeyboardButton(text="Задачи на неделю", callback_data="TRY_ASLEEP")
# Inline_Back4 = types.InlineKeyboardButton(text="Напоминани себе завтрашнему", callback_data="TRY_ASLEEP")
# Inline_Back5 = types.InlineKeyboardButton(text="Закрытый дневник", callback_data="TRY_ASLEEP")
markup_Inline_Back1.add(Inline_Back1, Inline_Back4, Inline_Back2, Inline_Back5, Inline_Back3, Inline_Back6)

markup_Inline_Back22 = types.InlineKeyboardMarkup(row_width=1)
Inline_Btn = types.InlineKeyboardButton(text="Stop ⛔", callback_data="STOP")
markup_Inline_Back22.add(Inline_Btn)

markup_Inline_QUESTS_FOR_TODAY = types.InlineKeyboardMarkup(row_width=1)
Inline_Btn_1 = types.InlineKeyboardButton(text="💚 Add some", callback_data="QUESTS_FOR_TODAY")
Inline_Btn_2 = types.InlineKeyboardButton(text="💸 Сomplete", callback_data="COMPLETE_QUESTS_FOR_TODAY")
Inline_Btn_3 = types.InlineKeyboardButton(text="❌ Foul some", callback_data="UNCOMP_QUESTS_FOR_TODAY")
Inline_Btn_4 = types.InlineKeyboardButton(text="🗑️ Delete", callback_data="DELETE_QUESTS_FOR_TODAY")
Inline_Btn_5 = types.InlineKeyboardButton(text="📬 Check all", callback_data="CHECK_QUESTS_FOR_TODAY")
Inline_Btn = types.InlineKeyboardButton(text="Back↩️", callback_data="START_MENU")
markup_Inline_QUESTS_FOR_TODAY.add(Inline_Btn_1, Inline_Btn_2, Inline_Btn_3, Inline_Btn_4, Inline_Btn_5, Inline_Btn)


markup_Inline_BACK_QUESTS_FOR_TODAY = types.InlineKeyboardMarkup(row_width=1)
Inline_Btn = types.InlineKeyboardButton(text="Back↩️", callback_data="MENU_QUESTS_FOR_TODAY")
markup_Inline_BACK_QUESTS_FOR_TODAY.add(Inline_Btn)

markup_Inline_BACK = types.InlineKeyboardMarkup(row_width=1)
Inline_Btn = types.InlineKeyboardButton(text="Back↩️", callback_data="START_MENU")
markup_Inline_BACK.add(Inline_Btn)

markup_Inline_BACK_AFTER_STOP = types.InlineKeyboardMarkup(row_width=1)
Inline_Btn_1 = types.InlineKeyboardButton(text="💸 Сomplete", callback_data="COMPLETE_QUESTS_FOR_TODAY")
Inline_Btn_2 = types.InlineKeyboardButton(text="Back↩️", callback_data="START_MENU")
markup_Inline_BACK_AFTER_STOP.add(Inline_Btn)

####################################################################################################################


markup_I_WILL_BE_SUCCESS = types.InlineKeyboardMarkup(row_width=1)
Inline_Btn = types.InlineKeyboardButton(text="YEAP", callback_data="I_WILL_BE_SUCCESS_remember")
markup_I_WILL_BE_SUCCESS.add(Inline_Btn)

####################################################################################################################

