import telebot
from telebot import types


tovar_list = ["🍄 CUBENIS","🌲 Hoffman","🌲 El patron","🌲 Gorlinni","🌲 Kalash","🌲 Mandala","🌲 Afgani","🌲 Diesel","🌳 Center","🌳 Desolator","🌳 Opium","🥔 Ice-o-lator","🥔 Afgani","🥔 Marakesh",
"💊 Лирика (300 мг)","💊 Регапен (300 мг)","⭐️ Кокаин HQ 96.8%","💎 СКорость A-PVP","⚡️ Амфетамин VHQ", "🍚 Героин HQ","♦️ МДМА HQ","💥 Экстази Rolls Royse","🎆 Марки LSD-25"]

rayon_list = ["🔵 Акдарьинский","🔵 Булунгурский","🔵 Джамбайский","🔵 Иштыханский","🔵 Каттакурганский","🔵 Кошрабатский","🔵 Нарпайский","🔵 Нурабадский","🔵 Пайарыкский","🔵 Пастдаргомский",
"🔵 Пахтачийский","🔵 Тайлакский","🔵 Мирзо-Улугбекский","🔵 Мирабадский","🔵 Бектемирский","🔵 Алмазарский","🔵 Юнусабадский","🔵 Учтепинский",
"🔵 Каракульский", "🔵 Алатский", "🔵 Бухарский", "🔵 Гиждуванский", "🔵 Жондорский", "🔵 Каганский"]

city_list = ["🔹 Самарканд", "🔹 Ташкент", "🔹 Бухара"]

menu_but = types.ReplyKeyboardMarkup(True)
menu_but.add("📦Покупки📦", "💬Наш чат💬")
menu_but.add("💬Связь с администрацией💬", "⁉️Не прошла оплата⁉️")
menu_but.add("🎟Промокод🎟")

adm_but = types.ReplyKeyboardMarkup(True)
adm_but.add("📦Покупки📦", "💬Наш чат💬")
adm_but.add("💬Связь с администрацией💬", "⁉️Не прошла оплата⁉️")
adm_but.add("☎️Запустить рассылку☎️", "🎟Промокод🎟")

city_but = types.ReplyKeyboardMarkup(True,row_width=1)
city_but.add("🔹 Самарканд",
"🔹 Ташкент",
"🔹 Бухара",
"🔙Вернуться в меню")

sum_but = types.ReplyKeyboardMarkup(True,row_width=1)
sum_but.add("🔵 Акдарьинский",
"🔵 Булунгурский",
"🔵 Джамбайский",
"🔵 Иштыханский",
"🔵 Каттакурганский",
"🔵 Кошрабатский",
"🔵 Нарпайский",
"🔵 Нурабадский",
"🔵 Пайарыкский",
"🔵 Пастдаргомский",
"🔵 Пахтачийский",
"🔵 Тайлакский",
"🔙Вернуться в меню")



tash_but = types.ReplyKeyboardMarkup(True,row_width=1)
tash_but.add("🔵 Мирзо-Улугбекский",
"🔵 Мирабадский",
"🔵 Бектемирский",
"🔵 Алмазарский",
"🔵 Юнусабадский",
"🔵 Учтепинский",
"🔙Вернуться в меню")

buh_but = types.ReplyKeyboardMarkup(True,row_width=1)
buh_but.add("🔵 Каракульский",
"🔵 Алатский",
"🔵 Бухарский",
"🔵 Гиждуванский",
"🔵 Жондорский",
"🔵 Каганский",
"🔙Вернуться в меню")

staff_but = types.ReplyKeyboardMarkup(True,row_width=1)
staff_but.add("🍄 CUBENIS",
"🌲 Hoffman",
"🌲 El patron",
"🌲 Gorlinni",
"🌲 Kalash",
"🌲 Mandala",
"🌲 Afgani",
"🌲 Diesel",
"🌳 Center",
"🌳 Desolator",
"🌳 Opium",
"🥔 Ice-o-lator",
"🥔 Afgani",
"🥔 Marakesh",
"💊 Лирика (300 мг)",
"💊 Регапен (300 мг)",
"⭐️ Кокаин HQ 96.8%",
"💎 СКорость A-PVP",
"⚡️ Амфетамин VHQ", 
"🍚 Героин HQ",
"♦️ МДМА HQ",
"💥 Экстази Rolls Royse",
"🎆 Марки LSD-25",
"🔙Вернуться в меню")


hoff_but = types.ReplyKeyboardMarkup(True,row_width=1)
hoff_but.add("0,5g - 400000сум",
"1,0g - 690000сум",
"🔙Вернуться в меню")

cub_but = types.ReplyKeyboardMarkup(True,row_width=1)
cub_but.add("1,5g - 280000сум",
"2,0g - 390000сум",
"3,0g - 490000сум",
"5,0g - 850000сум",
"🔙Вернуться в меню")

el_but = types.ReplyKeyboardMarkup(True,row_width=1)
el_but.add("0,5g - 470000сум",
"1,0g - 790000сум",
"🔙Вернуться в меню")

gor_but = types.ReplyKeyboardMarkup(True,row_width=1)
gor_but.add("1,0g - 850000сум",
"🔙Вернуться в меню")

kal_but = types.ReplyKeyboardMarkup(True,row_width=1)
kal_but.add("0,5g - 550000сум",
"1,0g - 850000сум",
"🔙Вернуться в меню")

af1_but = types.ReplyKeyboardMarkup(True,row_width=1)
af1_but.add("1,0g - 550000сум",
"🔙Вернуться в меню")

man_but = types.ReplyKeyboardMarkup(True,row_width=1)
man_but.add("1,0g - 650000сум",
"🔙Вернуться в меню")

af_but = types.ReplyKeyboardMarkup(True,row_width=1)
af_but.add("0,5g - 390000сум",
"1,0g - 590000сум",
"🔙Вернуться в меню")

die_but = types.ReplyKeyboardMarkup(True,row_width=1)
die_but.add("1,0g - 390000сум",
"🔙Вернуться в меню")

cen_but = types.ReplyKeyboardMarkup(True,row_width=1)
cen_but.add("1,0g - 300000сум",
"1,5g - 390000",
"🔙Вернуться в меню")

des_but = types.ReplyKeyboardMarkup(True,row_width=1)
des_but.add("1,0g - 250000сум",
"2,0g - 450000",
"🔙Вернуться в меню")

op_but = types.ReplyKeyboardMarkup(True,row_width=1)
op_but.add("1,0g - 253000сум",
"🔙Вернуться в меню")


mar_but = types.ReplyKeyboardMarkup(True,row_width=1)
mar_but.add("0,15g - 160000сум",
"0,25g - 220000сум",
"0,5g - 330000сум",
"1,0g - 450000сум",
"2,0g - 800000сум",
"5,0g - 2000000сум",
"🔙Вернуться в меню")

ice_but = types.ReplyKeyboardMarkup(True,row_width=1)
ice_but.add("0,25g - 240000сум",
"0,5g - 360000сум",
"1,0g - 560000сум",
"2,0g - 1000000сум",
"🔙Вернуться в меню")

koks_but = types.ReplyKeyboardMarkup(True,row_width=1)
koks_but.add("1,0g - 1400000сум",
"2,0g - 2200000сум",
"3,0g - 3100000сум",
"5,0g - 4800000сум",
"🔙Вернуться в меню")

sk_but = types.ReplyKeyboardMarkup(True,row_width=1)
sk_but.add("0,3g - 290000сум",
"0,5g - 425000сум",
"1,0g - 650000сум",
"🔙Вернуться в меню")

amf_but = types.ReplyKeyboardMarkup(True,row_width=1)
amf_but.add("2,0g - 390000сум",
"3,0g - 510000сум",
"5,0g - 700000сум",
"🔙Вернуться в меню")

ger_but = types.ReplyKeyboardMarkup(True,row_width=1)
ger_but.add("1,0g - 500000сум",
"2,0g - 800000сум",
"🔙Вернуться в меню")

mdm_but = types.ReplyKeyboardMarkup(True,row_width=1)
mdm_but.add("0,5g - 200000сум",
"1,0g - 380000сум",
"2,0g - 590000сум",
"3,0g - 820000сум",
"🔙Вернуться в меню")

ex_but = types.ReplyKeyboardMarkup(True,row_width=1)
ex_but.add("3шт - 300000сум",
"5шт - 500000сум",
"10шт - 900000сум",
"🔙Вернуться в меню")

lsd_but = types.ReplyKeyboardMarkup(True,row_width=1)
lsd_but.add("2шт - 300000сум",
"5шт - 550000сум",
"10шт - 1000000сум",
"🔙Вернуться в меню")

lira_but = types.ReplyKeyboardMarkup(True,row_width=1)
lira_but.add("1шт - 30000сум",
"🔙Вернуться в меню")

regap_but = types.ReplyKeyboardMarkup(True,row_width=1)
regap_but.add("1шт - 25000сум",
"🔙Вернуться в меню")

check_menu = types.ReplyKeyboardMarkup(True)
check_menu.add("✅Я оплатил товар")
check_menu.add("🔙Вернуться в меню", "📦Вернуться к выбору товара")


spam = types.InlineKeyboardMarkup()
spam_text = types.InlineKeyboardButton("💬Спам текстом💬", callback_data="text")
spam_pic = types.InlineKeyboardButton("🖼Спам с картинкой🖼", callback_data="pics")
spam.row(spam_text)
spam.row(spam_pic)











