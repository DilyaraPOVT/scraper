import telebot
from telebot import types

token='1334171364:AAExrt3JYSyVlycZI32fmE_19phTXI7-Sag'

bot=telebot.TeleBot(token)

@bot.message_handler(content_types=['text'])
def inline_key(a):
    if a.text == "/start":
        mainmenu = types.InlineKeyboardMarkup()
        keyStrahovanie = types.InlineKeyboardButton(text='Страхование', callback_data='keyStrahovanie')
        keyCarts = types.InlineKeyboardButton(text='Карты', callback_data='keyCarts')
        keyCredit = types.InlineKeyboardButton(text='Кредит', callback_data='keyCredit')
        keyVklad = types.InlineKeyboardButton(text='Вклад', callback_data='keyVklad')
        keySubsidii = types.InlineKeyboardButton(text='Субсидии', callback_data='key5')
        mainmenu.add(keyStrahovanie, keyCarts, keyCredit, keyVklad, keySubsidii)
        bot.send_message(a.chat.id, 'Привет, это AkBarsBot. Я помогу Вам подобрать услугу. Выбирайте!', reply_markup=mainmenu)

@bot.callback_query_handler(func=lambda call: True)
def callback_inline(call):
    # Главное меню
    if call.data == "mainmenu":
        mainmenu = types.InlineKeyboardMarkup()
        keyStrahovanie = types.InlineKeyboardButton(text='Страхование', callback_data='keyStrahovanie')
        keyCarts = types.InlineKeyboardButton(text='Карты', callback_data='keyCarts')
        keyCredit = types.InlineKeyboardButton(text='Кредит', callback_data='keyCredit')
        keyVklad = types.InlineKeyboardButton(text='Вклад', callback_data='keyVklad')
        keySubsidii = types.InlineKeyboardButton(text='Субсидии', callback_data='keySubsidii')
        mainmenu.add(keyStrahovanie, keyCarts, keyCredit, keyVklad, keySubsidii)
        bot.edit_message_text('Привет, это AkBarsBot. Я помогу Вам подобрать услугу. Выбирайте!', call.message.chat.id, call.message.message_id,
                              reply_markup=mainmenu)
    ## ПодМеню Страхование
    elif call.data == "keyStrahovanie":
        next_menuStrahovanie = types.InlineKeyboardMarkup()
        keyZastahovat = types.InlineKeyboardButton(text='Застраховать', callback_data='keyZastahovat')
        back = types.InlineKeyboardButton(text='Назад', callback_data='mainmenu')
        next_menuStrahovanie.add(keyZastahovat, back)
        bot.edit_message_text('Здесь вы можете застраховать жизнь или имущество!', call.message.chat.id, call.message.message_id,
                              reply_markup=next_menuStrahovanie)
    ### ПодПодМеню Выбрать страхование
    elif call.data == "keyZastahovat":
        next_menuVibratStrahovku = types.InlineKeyboardMarkup()
        keyKV = types.InlineKeyboardButton(text='Квартира', callback_data='keyKV')
        keyNS = types.InlineKeyboardButton(text='Несчастные случаи', callback_data='keyNS')
        keyPU = types.InlineKeyboardButton(text='Путешественники', callback_data='keyPU')
        keyTravels = types.InlineKeyboardButton(text='Путешественники России', callback_data='keyTravels')
        keyAnimals = types.InlineKeyboardButton(text='Животные', callback_data='keyAnimals')
        keyBolezni = types.InlineKeyboardButton(text='Заболевания', callback_data='keyBolezni')
        keyAvarii = types.InlineKeyboardButton(text='ДТП', callback_data='keyAvarii')
        back = types.InlineKeyboardButton(text='Назад', callback_data='keyStrahovanie')
        next_menuVibratStrahovku.add(keyKV, keyNS, keyPU, keyTravels, keyAnimals, keyBolezni, back)
        bot.edit_message_text('Выберите страхование:', call.message.chat.id, call.message.message_id,
                              reply_markup=next_menuVibratStrahovku)
    #### ПодПодПодМеню Оформление страхования
    elif call.data == ("keyKV") or call.data == ("keyNS") or call.data == ("keyPU") or call.data == ("keyTravels") or call.data == ("keyAnimals"):
        next_menuOformlenieStrahovki = types.InlineKeyboardMarkup()
        back = types.InlineKeyboardButton(text='Отмена', callback_data='keyZastahovat')
        next_menuOformlenieStrahovki.add(back)
        bot.edit_message_text("Введите:"
            "\r\nРегион\r\nСумму страхования\r\nСрок страхования\r\n"
            "____________________________________________________"
            "\r\nНапишите цифры, которые относятся к вам:\r\n1-занимаюсь спортом\r\n2-не инвалид\r\n3-есть промокод\r\n"
            "____________________________________________________"
            "\r\nВведите\r\nФИО\r\nДата рождения\r\nАдрес регистрации\r\nНомер телефона\r\nЭлектронную почту", call.message.chat.id, call.message.message_id,
                              reply_markup=next_menuOformlenieStrahovki)

    ## ПодМеню Карты
    elif call.data == "keyCarts":
        next_menuCatrs = types.InlineKeyboardMarkup()
        keyOformit = types.InlineKeyboardButton(text='Оформить карту', callback_data='keyOformit')
        back = types.InlineKeyboardButton(text='Назад', callback_data='mainmenu')
        next_menuCatrs.add(keyOformit, back)
        bot.edit_message_text('Здесь вы можете оформить карту!', call.message.chat.id, call.message.message_id,
                              reply_markup=next_menuCatrs)
    ### ПодПодМеню Оформить карту
    elif call.data == "keyOformit":
        next_menuSpisokCart = types.InlineKeyboardMarkup()
        keyAurum = types.InlineKeyboardButton(text='Ак Барс Aurum', callback_data='keyAurum')
        keyGeneration = types.InlineKeyboardButton(text='Ак Барс Generation', callback_data='keyGeneration')
        keyEvolution = types.InlineKeyboardButton(text='Ак Барс Evolution', callback_data='keyEvolution')
        keyPremium = types.InlineKeyboardButton(text='Ак Барс Premium', callback_data='keyPremium')
        keyMir = types.InlineKeyboardButton(text='Ак Барс "Мир"', callback_data='keyMir')
        back = types.InlineKeyboardButton(text='Назад', callback_data='keyCarts')
        next_menuSpisokCart.add(keyAurum, keyGeneration, keyEvolution, keyPremium, keyMir, back)
        bot.edit_message_text('Выберите тип карты:', call.message.chat.id, call.message.message_id,
                              reply_markup=next_menuSpisokCart)
    #### ПодПодПодМеню Оформление заявки на крату
    elif call.data == ("keyAurum") or call.data == ("keyGeneration") or call.data == ("keyEvolution") or call.data == ("keyPremium") or call.data == ("keyMir"):
        next_menuOformlenie = types.InlineKeyboardMarkup()
        back = types.InlineKeyboardButton(text='Отмена', callback_data='keyOformit')
        next_menuOformlenie.add(back)
        bot.edit_message_text("Введите:"
            "\r\nФИО\r\nДату рождения"
            "\r\nНомер телефона\r\nЭлектронную почту", call.message.chat.id, call.message.message_id,
                              reply_markup=next_menuOformlenie)

    ## ПодМеню Кредит
    elif call.data == "keyCredit":
        next_menuCredit = types.InlineKeyboardMarkup()
        keyPoluchitCredit = types.InlineKeyboardButton(text='Получить кредит', callback_data='keyPoluchitCredit')
        back = types.InlineKeyboardButton(text='Назад', callback_data='mainmenu')
        next_menuCredit.add(keyPoluchitCredit, back)
        bot.edit_message_text('Кредит!', call.message.chat.id, call.message.message_id,
                              reply_markup=next_menuCredit)
    ## ПодМеню Вклад
    elif call.data == "keyVklad":
        next_menuVklad = types.InlineKeyboardMarkup()
        keyOtkritVklad = types.InlineKeyboardButton(text='Открыть вклад', callback_data='keyOtkritVklad')
        back = types.InlineKeyboardButton(text='Назад', callback_data='mainmenu')
        next_menuVklad.add(keyOtkritVklad, back)
        bot.edit_message_text('Вклад!', call.message.chat.id, call.message.message_id,
                              reply_markup=next_menuVklad)
    ## ПодМеню Субсидии
    elif call.data == "keySubsidii":
        next_menuSubsidii = types.InlineKeyboardMarkup()
        keyPoluchitSubsidii = types.InlineKeyboardButton(text='Получить субсидии', callback_data='keyPoluchitSubsidii')
        back = types.InlineKeyboardButton(text='Назад', callback_data='mainmenu')
        next_menuSubsidii.add(keyPoluchitSubsidii, back)
        bot.edit_message_text('Субсидии!', call.message.chat.id, call.message.message_id,
                              reply_markup=next_menuSubsidi)




bot.polling(none_stop=True, interval=0)