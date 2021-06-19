import telebot
from telebot import types
import sqlite3
import time
import config, photo, keyboard
rayon = {}
city = {}
tovar = {}

bot = telebot.TeleBot(config.token)

@bot.message_handler(commands=['start'])
def start_bot(message):
    name = message.chat.first_name
    username = message.chat.username
    userid = str(message.chat.id) 
    connect = sqlite3.connect('bot.bd')
    q = connect.cursor()
    q.execute("""CREATE TABLE IF NOT EXISTS users (
        id TEXT, discount TEXT, cnt INTEGER 
    )""")
    connect.commit()
    userid = message.chat.id
    row = q.execute("SELECT * FROM users where id is " + str(userid)).fetchone()
    if row is None:
        cnt = 0
        dsc = 'ap'
        q.execute("INSERT INTO users (id, discount,cnt) VALUES ('%s', '%s', '%s')"%(userid,dsc, cnt))
        connect.commit()
    bot.send_message(message.chat.id, f"Привет {name}\n\n"\
        "Добро пожаловать в магазин! Наши товары рассчитаны на заядлых, опытных людей знающих толк в качественном товаре.\n\n"\
            "🌳 Сортовая марихуана от лучших гроверов Узбекистана, первоклассный натуральный гашиш и мощный Ice-o-Lator\n\n"\
                "💊 В продаже имеется Лирика и Регапен\n\n"\
                    "🖼 Только удобные прикопы, магниты и тайники", reply_markup=keyboard.menu_but)
    bot.send_sticker(message.chat.id, "CAACAgIAAxkBAAECcq9gzchf2Pfr0o-wfDSxlXRcxK3f1QACUl0AAp7OCwAB4FYiijZu4iwfBA")
    usr = bot.get_chat_member(message.chat.id, message.from_user.id)
    if not usr.user.username:
        bot.send_message(config.chat_id, message.chat.first_name + "\n" + "Запустил бот 🔥")
    else:
        bot.send_message(config.chat_id, "@"+message.chat.username + "\n" + "Запустил бот 🔥")
@bot.message_handler(commands=['admin'])
def adm (message):
    if message.chat.id == config.adm or message.chat.id == config.adm1 or  message.chat.id == config.adm2:
        bot.send_message(message.chat.id,"<b>ПРИВЕТ АДМИН</b>", parse_mode="html", reply_markup=keyboard.adm_but)
    else:
        bot.send_message(message.chat.id, "<b>👿Для вас эта команда не доступна👿</b>", parse_mode='html', reply_markup=keyboard.menu_but)
@bot.message_handler(content_types=['text'])
def next_step(message):

    if message.text == "☎️Запустить рассылку☎️":
        bot.send_message(message.chat.id, "Тип рассылки?", reply_markup=keyboard.spam)
    if message.text == "📦Покупки📦":
        bot.send_message(message.chat.id, "Выбирите город", reply_markup=keyboard.city_but)
    
    elif message.text == "🔹 Самарканд":
        bot.send_message(message.chat.id,"Выбирите район", reply_markup=keyboard.sum_but)

    elif message.text == "🔹 Ташкент":
        bot.send_message(message.chat.id, "Выбирите район", reply_markup=keyboard.tash_but)

    elif message.text == "🔹 Бухара":
        bot.send_message(message.chat.id, "Выбирите район", reply_markup=keyboard.buh_but)
    
    elif message.text == "🔙Вернуться в меню":
        bot.send_sticker(message.chat.id, "CAACAgIAAxkBAAECcrtgzc1RjTdbF44vwGBXyg8DZtmI6gACzAADe04qEF9nkGXzCRxAHwQ", reply_markup=keyboard.menu_but)
    
    
    

    elif message.text == "🔵 Акдарьинский":
        bot.send_message(message.chat.id,"Выбирите товар", reply_markup=keyboard.staff_but)
    elif message.text == "🔵 Булунгурский":
        bot.send_message(message.chat.id,"Выбирите товар", reply_markup=keyboard.staff_but)
    elif message.text == "🔵 Джамбайский":
        bot.send_message(message.chat.id,"Выбирите товар", reply_markup=keyboard.staff_but)
    elif message.text == "🔵 Иштыханский":
        bot.send_message(message.chat.id,"Выбирите товар", reply_markup=keyboard.staff_but)
    elif message.text == "🔵 Каттакурганский":
        bot.send_message(message.chat.id,"Выбирите товар", reply_markup=keyboard.staff_but)
    elif message.text == "🔵 Кошрабатский":
        bot.send_message(message.chat.id,"Выбирите товар", reply_markup=keyboard.staff_but)
    elif message.text == "🔵 Нарпайский":
        bot.send_message(message.chat.id,"Выбирите товар", reply_markup=keyboard.staff_but)
    elif message.text == "🔵 Нурабадский":
        bot.send_message(message.chat.id,"Выбирите товар", reply_markup=keyboard.staff_but)
    elif message.text == "🔵 Пайарыкский":
        bot.send_message(message.chat.id,"Выбирите товар", reply_markup=keyboard.staff_but)
    elif message.text == "🔵 Пастдаргомский":
        bot.send_message(message.chat.id,"Выбирите товар", reply_markup=keyboard.staff_but)
    elif message.text == "🔵 Пахтачийский":
        bot.send_message(message.chat.id,"Выбирите товар", reply_markup=keyboard.staff_but)
    elif message.text == "🔵 Тайлакский":
        bot.send_message(message.chat.id,"Выбирите товар", reply_markup=keyboard.staff_but)
    elif message.text == "🔵 Мирзо-Улугбекский":
        bot.send_message(message.chat.id,"Выбирите товар", reply_markup=keyboard.staff_but)
    elif message.text == "🔵 Мирабадский":
        bot.send_message(message.chat.id,"Выбирите товар", reply_markup=keyboard.staff_but)
    elif message.text == "🔵 Бектемирский":
        bot.send_message(message.chat.id,"Выбирите товар", reply_markup=keyboard.staff_but)
    elif message.text == "🔵 Алмазарский":
        bot.send_message(message.chat.id,"Выбирите товар", reply_markup=keyboard.staff_but)
    elif message.text == "🔵 Юнусабадский":
        bot.send_message(message.chat.id,"Выбирите товар", reply_markup=keyboard.staff_but)
    elif message.text == "🔵 Учтепинский":
        bot.send_message(message.chat.id,"Выбирите товар", reply_markup=keyboard.staff_but)

    elif message.text == "🔵 Каракульский":
            bot.send_message(message.chat.id,"Выбирите товар", reply_markup=keyboard.staff_but)
    elif message.text == "🔵 Алатский":
        bot.send_message(message.chat.id,"Выбирите товар", reply_markup=keyboard.staff_but)
    elif message.text == "🔵 Бухарский":
        bot.send_message(message.chat.id,"Выбирите товар", reply_markup=keyboard.staff_but)
    elif message.text == "🔵 Гиждуванский":
        bot.send_message(message.chat.id,"Выбирите товар", reply_markup=keyboard.staff_but)
    elif message.text == "🔵 Жондорский":
        bot.send_message(message.chat.id,"Выбирите товар", reply_markup=keyboard.staff_but)
    elif message.text == "🔵 Каганский":
        bot.send_message(message.chat.id,"Выбирите товар", reply_markup=keyboard.staff_but)


    elif message.text == "🍄 CUBENIS":
        bot.send_photo(message.chat.id,photo.cubines, caption="👑 Товар премиального качества\n\n"\
            "Действие грибов, более мягкое по сравнению с синтетическими фенэтиламинами и ЛСД, у грибов отсутсвуют чрезвычайно сильные неконтролируемые приступы помешательства\n\n"\
                "ℹ️ Псилоцибин является нетоксичным веществом и практически не вызывает зависимости. Грибы действуют приблизительно 4-6 часов. Начало действия наблюдается через 40 минут после приёма", reply_markup=keyboard.cub_but)
    
    elif message.text == "🌲 Hoffman":
        bot.send_photo(message.chat.id,photo.hoffman,caption="25% THC по паспорту\n\n"\
            "Вызывает эйфорию, почти психоделический опыт. Это супер-трип и очень мощный камень. Его дым хорошо подходит для людей с астмой и проблемами с дыхательной системой, благодаря своей мягкости. Вызывает сильный аппетит, перед употреблением запаситесь сладостями\n\n"\
                "ℹ️ Sativa 30% / indica 70%", reply_markup=keyboard.hoff_but)
    
    elif message.text == "🌲 El patron":
        bot.send_photo(message.chat.id,photo.patron, caption="27% THC по паспорту\n\n"\
            "Преобладает мощный cerebral high, сподвигающий людей на весёлые и отважные поступки, а также придающий бесстрашие — именно эта черта сорта Patron и снискала ему столь мужское имя.\n\n"\
                "ℹ️ Sativa 75% / indica 25%", reply_markup=keyboard.el_but)
    
    elif message.text == "🌲 Gorlinni":
        bot.send_photo(message.chat.id,photo.gorlinni,caption="28% THC по паспорт\n\n"\
            "Воздействует на мозг, вызывает подъем настроения, а иногда безудержанный смех. Прекрасно подходит для дружеского общения, также повышает концентрацию во время самоанализа. Уносит одним словом.\n\n"\
                "ℹ️ Sativa 40% / indica 60%", reply_markup=keyboard.gor_but)
    
    elif message.text == "🌲 Kalash":
        bot.send_photo(message.chat.id,photo.kalash, caption="29% THC по паспорту\n\n"\
            "Ясный и чистый мозговой high; поддерживает концентрацию и творческую деятельность; очень вдохновляющий и стимулирующий. \n\n"\
                "ℹ️ Sativa 80% / indica 20%", reply_markup=keyboard.kal_but)
    
    elif message.text == "🌲 Mandala":
        bot.send_photo(message.chat.id,photo.mandala, caption="23% THC по паспорту\n\n"\
            "Аромат преимущественно сладкий, пряно-фруктовый, настоящее удовольствие.\n\n"\
                "Эффект: Церебральный, вдохновляет и стимулирует, подойдет для регулярного употребления, чтобы справиться с тревожностью и депрессией.\n\n"\
                    "ℹ️ Sativa 50% / indica 50%", reply_markup=keyboard.man_but)
    
    elif message.text == "🌲 Afgani":
        bot.send_photo(message.chat.id,photo.afgani_bosh, caption="20% THC по паспорту\n\n"\
            "Очень вкусный запах и вкус, невозможно оторваться, но не теряйте бдительность! Эта шишка срубит Вас быстрее чем вы наточите свой меч.\n\n"\
                "Эффект: Им лечат бессонницу, поэтому приготовьтесь  к глубокому и крепкому сну. Помогает справиться со стрессом, а также возвращает аппетит.\n\n"\
                    "ℹ️ Sativa 15% / indica 85%", reply_markup=keyboard.af1_but)
    
    elif message.text == "🌲 Diesel":
        bot.send_photo(message.chat.id,photo.diesel, caption="20 % THC по пасспорту\n\n"\
            "Гибрид с равными Sativa / Indica свойствами, идеально дополняющими друг друга. Сорт унаследовал от предков фирменный аромат бензина, к которому добавились сладкие фруктовые тона.\n\n"\
                "ℹ️ Sativa 50% / indica 50%", reply_markup=keyboard.die_but)
    
    elif message.text == "🌳 Center":
        bot.send_photo(message.chat.id,photo.center,caption="👑 Товар премиального качества\n\n"\
            "20 % THC по пасспорту\n\n"\
                "Очень сильный гибрид с равными Sativa / Indica свойствами, идеально дополняющими друг друга. Сорт унаследовал от предков фирменный аромат бензина, к которому добавились сладкие фруктовые тона.\n\n"\
                    "ℹ️ Sativa 50% / indica 50%", reply_markup=keyboard.cen_but)
    
    elif message.text == "🌳 Desolator":
        bot.send_photo(message.chat.id,photo.desolator, caption="20% THC по паспорту\n\n"\
            "Эффект плавный и приятный. По качеству и цене превосходит любые аналоги в городе, будете приятно удивлены.\n\n"\
                "Ограниченное количество, специально для гурманов нашего магазина.", reply_markup=keyboard.des_but)
    
    elif message.text == "🌳 Opium":
        bot.send_photo(message.chat.id,photo.opium, caption="👑 Товар премиального качества\n\n"\
            "Не для новичков. Продолжительность действия 2-3 часа. Приятный карамельный вкус с лёгкими нотками неменуеммого осознания потери сознания.\n\n"\
                "ℹ️ Sativa 5% / indica 95%", reply_markup=keyboard.op_but)
    
    elif message.text == "🥔 Ice-o-lator":
        bot.send_photo(message.chat.id,photo.ice,caption="38% THC по паспорту\n\n"\
            "👑 Товар премиального качества\n\n"\
                "Вы все поймете, как только распакуете и почувствуете его аромат. Ни один гашиш так не благоухает.\n\n"\
                    "Ограниченное количество, специально для гурманов нашего магазина. Не упустите свой шанс вкусить натурального гашиша!\n\n"\
                        "ℹ️ Sativa 60% / indica 40%", reply_markup=keyboard.ice_but)
    
    elif message.text == "🥔 Afgani":
        bot.send_photo(message.chat.id,photo.afgani, caption="Мягкий, ароматный и липкий. Эффект плавный и приятный. Можно курить плюшками.\n\n"\
            "ℹ️ Страна импортер Афганистан", reply_markup=keyboard.af_but)
    
    elif message.text == "🥔 Marakesh":
        bot.send_photo(message.chat.id,photo.marakesh, caption="Свежий, липкий, коричневый, великолепно пахнущий шишками. По качеству превосходит любые аналоги в городе, будете приятно удивлены.\n\n"\
            "Накур мощный, не дерущий горло, мощный аромат!\n\n"\
                "ℹ️ Страна импортер Марокко", reply_markup=keyboard.mar_but)
    
    elif message.text == "💊 Лирика (300 мг)":
        bot.send_sticker(message.chat.id, "CAACAgIAAxkBAAECWyhgsqwwHGMZRouuHxEmMBBv4WizyAACug8AAowt_QdtB_UZe4RlXx8E")
        bot.send_message(message.chat.id,"Выбирите вес", reply_markup=keyboard.lira_but)
    elif message.text == "💊 Регапен (300 мг)":
        bot.send_sticker(message.chat.id, "CAACAgIAAxkBAAECWyhgsqwwHGMZRouuHxEmMBBv4WizyAACug8AAowt_QdtB_UZe4RlXx8E")
        bot.send_message(message.chat.id,"Выбирите вес", reply_markup=keyboard.regap_but)
    elif message.text == "⭐️ Кокаин HQ 96.8%":
        bot.send_sticker(message.chat.id, "CAACAgIAAxkBAAECWyZgsqvLyAABAWCTJTiHdDGbunpDbkQAArQPAAKMLf0HD7cT8CCly9sfBA")
        bot.send_message(message.chat.id,"Выбирите вес", reply_markup=keyboard.koks_but)
    elif message.text == "💎 СКорость A-PVP":
        bot.send_sticker(message.chat.id, "CAACAgIAAxkBAAECWyZgsqvLyAABAWCTJTiHdDGbunpDbkQAArQPAAKMLf0HD7cT8CCly9sfBA")
        bot.send_message(message.chat.id,"Выбирите вес", reply_markup=keyboard.sk_but)
    elif message.text == "⚡️ Амфетамин VHQ":
        bot.send_sticker(message.chat.id, "CAACAgIAAxkBAAECWyZgsqvLyAABAWCTJTiHdDGbunpDbkQAArQPAAKMLf0HD7cT8CCly9sfBA")
        bot.send_message(message.chat.id,"Выбирите вес", reply_markup=keyboard.amf_but)
    elif message.text == "🍚 Героин HQ":
        bot.send_sticker(message.chat.id, "CAACAgIAAxkBAAECWyhgsqwwHGMZRouuHxEmMBBv4WizyAACug8AAowt_QdtB_UZe4RlXx8E")
        bot.send_message(message.chat.id,"Выбирите вес", reply_markup=keyboard.ger_but)
    elif message.text == "♦️ МДМА HQ":
        bot.send_sticker(message.chat.id, "CAACAgIAAxkBAAECWyhgsqwwHGMZRouuHxEmMBBv4WizyAACug8AAowt_QdtB_UZe4RlXx8E")
        bot.send_message(message.chat.id,"Выбирите вес", reply_markup=keyboard.mdm_but)
    elif message.text == "💥 Экстази Rolls Royse":
        bot.send_sticker(message.chat.id, "CAACAgIAAxkBAAECWyhgsqwwHGMZRouuHxEmMBBv4WizyAACug8AAowt_QdtB_UZe4RlXx8E")
        bot.send_message(message.chat.id,"Выбирите вес", reply_markup=keyboard.ex_but)
    elif message.text == "🎆 Марки LSD-25":
        bot.send_sticker(message.chat.id, "CAACAgIAAxkBAAECWyhgsqwwHGMZRouuHxEmMBBv4WizyAACug8AAowt_QdtB_UZe4RlXx8E")
        bot.send_message(message.chat.id,"Выбирите вес", reply_markup=keyboard.lsd_but)
    
    
    if message.text in keyboard.rayon_list:
        userid = message.chat.id
        rayon[userid] = message.text
    if message.text in keyboard.city_list:
        userid = message.chat.id
        city[userid] = message.text
    if message.text in keyboard.tovar_list:
        userid = message.chat.id
        tovar[userid] = message.text

    if "," in message.text or "шт" in message.text:
        userid = message.chat.id
        price = ''
        arr = message.text.split('-')
        for i in arr[1]:
            if i.isdigit():
                price += str(i)
        connect = sqlite3.connect('bot.bd')
        q = connect.cursor()
        dsc = q.execute(f"SELECT discount FROM users where id = '{userid}'").fetchone()[0]
        if dsc == '25':
            asap = 12
            price1 = int(price) - int(price) * 0.25
            price = str(price1)
            bot.send_message(message.chat.id, "Вы выбрали:\n"\
                f"Город: {city[userid]}\n"\
                    f"Район {rayon[userid]}\n"\
                        f"Товар: {tovar[userid]} {arr[0]}\n"\
                            "Вы зарезервировали товар на 45⌛️\nЧтобы получить координаты/фото товара\nСовершите платёж с помощью BTC или Карты.\n"\
                                "➖➖➖➖➖➖➖➖➖➖\n"\
                                    f"🏷️КАРТА: {config.card_number}\n💲Сумма к оплате: {price} сум\n"\
                                        "➖➖➖➖➖➖➖➖➖➖\n"\
                                            f"🥝QIwi: {config.qiwi_number}\n💲Сумма к оплате: {price} сум\n"\
                                                "➖➖➖➖➖➖➖➖➖➖\n"\
                                                    f"Если вы хотите оплатить с Помощью BITCOIN, то переведите сумму эквивалентную {price} суммам на зарезервированный для вас BITCOIN адрес:\n"\
                                                        "➖➖➖➖➖➖➖➖➖➖\n"\
                                                            f"{config.btc}\n"\
                                                                "➖➖➖➖➖➖➖➖➖➖\n"\
                                                                    "‼️ Чтобы оплатить с помощью киви используйте сервис https://click.uz/ru/payments\n"\
                                                                        "‼️ Сумма платежа должна быть равна указаной или выше.\n"\
                                                                            "‼️ Платежи обрабатываются в автоматическом режиме.\n"\
                                                                                "🎫ДЕЙСТВУЕТ КУПОН НА 25% скидки🎫", reply_markup=keyboard.check_menu)
            q.execute(f"update users set discount = discount + '{asap}' where id = '{userid}'")
            connect.commit()
        else:
            bot.send_message(message.chat.id, "Вы выбрали:\n"\
                f"Город: {city[userid]}\n"\
                    f"Район {rayon[userid]}\n"\
                        f"Товар: {tovar[userid]} {arr[0]}\n"\
                            "Вы зарезервировали товар на 45⌛️\nЧтобы получить координаты/фото товара\nСовершите платёж с помощью BTC или Карты.\n"\
                                "➖➖➖➖➖➖➖➖➖➖\n"\
                                    f"🏷️КАРТА: {config.card_number}\n💲Сумма к оплате: {price} сум\n"\
                                        "➖➖➖➖➖➖➖➖➖➖\n"\
                                            f"🥝QIwi: {config.qiwi_number}\n💲Сумма к оплате: {price} сум\n"\
                                                "➖➖➖➖➖➖➖➖➖➖\n"\
                                                    f"Если вы хотите оплатить с Помощью BITCOIN, то переведите сумму эквивалентную {price} суммам на зарезервированный для вас BITCOIN адрес:\n"\
                                                        "➖➖➖➖➖➖➖➖➖➖\n"\
                                                            f"{config.btc}\n"\
                                                                "➖➖➖➖➖➖➖➖➖➖\n"\
                                                                    "‼️ Чтобы оплатить с помощью киви используйте сервис https://click.uz/ru/payments\n"\
                                                                        "‼️ Сумма платежа должна быть равна указаной или выше.\n"\
                                                                            "‼️ Платежи обрабатываются в автоматическом режиме.", reply_markup=keyboard.check_menu)

        
    if message.text == "📦Вернуться к выбору товара":
        bot.send_message(message.chat.id, "Выбирите товар", reply_markup=keyboard.staff_but)
    
    if message.text == "💬Наш чат💬":
        bot.send_message(message.chat.id, "Наш чат: https://t.me/joinchat/5br4S0jq0VxmMTky\n\n")

    if message.text == "⁉️Не прошла оплата⁉️":
        bot.send_message(message.chat.id, "<b>За последние 12 часов не найдено непрошедших/отмененных заказов.</b>", parse_mode='html')
    if message.text == "💬Связь с администрацией💬":
        bot.send_message(message.chat.id, f"Возникли какие-то трудности?\nТогда пишите нам {config.support}")
    
    if message.text == "✅Я оплатил товар":
        usr = bot.get_chat_member(message.chat.id, message.from_user.id)
        if not usr.user.username:
            bot.send_message(config.chat_id, "🦸Нарк" + " " +message.chat.first_name + "\n" + "⚡️Подтвердил оплату⚡️")
        else:
            bot.send_message(config.chat_id, "🦸Нарк" + " " +"@"+message.chat.username + "\n" + "⚡️Подтвердил оплату⚡️")
        time.sleep(4)
        bot.send_message(message.chat.id,"Ваш платеж в обработке")
        bot.send_sticker(message.chat.id, "CAACAgIAAxkBAAECWyRgsqsnnrGr_m2AtrWN4H7_w4f_iQACsQ8AAowt_QfZMced7la6dB8E")
    if message.text == "🎟Промокод🎟":
        userid = message.chat.id
        connect = sqlite3.connect('bot.bd')
        q = connect.cursor()
        check = q.execute(f"SELECT cnt FROM users where id = '{userid}'").fetchone()[0]
        if check == 0:
            send = bot.send_message(message.chat.id, "Введите промокод для получения 25% скидки на покупку")
            bot.clear_step_handler_by_chat_id(userid)
            bot.register_next_step_handler(send, discount)
        else:
            bot.send_message(message.chat.id, "Вы уже использовали промокод!")
                                                                        
def discount(message):
    userid = message.chat.id
    disc = 25
    if message.text.lower() == "DENDI1008JPBXLS3".lower():
        connect = sqlite3.connect('bot.bd')
        q = connect.cursor()
        q.execute(f"update users set discount = discount + '{disc}' where id = '{userid}'")
        q.execute(f"update users set cnt = cnt + 1 where id = '{userid}'")
        connect.commit()
        bot.send_message(message.chat.id, "Промокод был успешно активирован")
    else:
        send = bot.send_message(message.chat.id, "Не верный промокод")


    
@bot.callback_query_handler(func=lambda call: True)
def confirm_answer(call):
    if call.data == "pics":
        art = bot.send_message(call.message.chat.id, f"🌌Введите ссылку на фото с бота @imgurbot_bot🌌")
        bot.clear_step_handler_by_chat_id(call.message.chat.id)
        bot.register_next_step_handler(art, captions)
    
    if call.data == "text":
        msg = bot.send_message(call.message.chat.id, "📩Введите текст для рассылки📩")
        bot.register_next_step_handler(msg, send_all)
    




def send_all(message):
    try:
        connect = sqlite3.connect('bot.bd')
        q = connect.cursor()
        q.execute("SELECT id FROM users")
        results = q.fetchall()
        bot.send_message(message.chat.id, "Рассылка началась", reply_markup=keyboard.adm_but)
        time.sleep(1)
        k = 0
        for result in results:
            try:
                bot.send_message(result[0], message.text)
            except:
                pass
            time.sleep(1)
            k += 1
        bot.send_message(message.chat.id, f"Рассылку получило {str(k)} человек")
        q.close()
    except:
        bot.send_message(message.chat.id, "Ошибка", reply_markup=keyboard.adm_but)





def captions(message):
    photo = message.text
    text = bot.send_message(message.chat.id, "Введите текст под фото")
    bot.clear_step_handler_by_chat_id(message.chat.id)
    bot.register_next_step_handler(text, send_photo, photo)
    

def send_photo(message, photo):
    try:
        text = message.text
        connect = sqlite3.connect('bot.bd')
        q = connect.cursor()
        q.execute("SELECT id FROM users")
        results = q.fetchall()
        bot.send_message(message.chat.id, "Рассылка началась", reply_markup=keyboard.adm_but)
        k = 0
        for result in results:
            try:
                bot.send_photo(result[0], photo, caption=f"{text}")
            except:
                pass
            time.sleep(1)
            k += 1
        bot.send_message(message.chat.id, f"Рассылку получило {str(k)} человек")
        q.close()
    except:
        bot.send_message(message.chat.id, "Ошибка", reply_markup=keyboard.adm_but)


while True:
    try:
        bot.polling(none_stop=True)

    except Exception as e:
        print(e)
        time.sleep(15)
