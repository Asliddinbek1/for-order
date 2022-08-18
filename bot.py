import logging
from aiogram.types import ReplyKeyboardMarkup, ReplyKeyboardRemove, KeyboardButton, InlineKeyboardButton, InlineKeyboardMarkup
from aiogram import Bot, Dispatcher, executor, types
from models import *

API_TOKEN = '5580348761:AAHB-QvDtKYUyT_fv73112GdVmpFCNFt_MU'
admin = ''


button1 = KeyboardButton("Raqamni yuborish",request_contact=True)
keyboard1 = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True).add(button1)



get_order = False
update_services = {
    'holat': False,
    'qiymat': '',
}

Ishchi = {
    'name': 'ishchi',
    "phone" : " ",
}


user = {
    "id" : {
        "name": "Asliddin",
        "contact": "+998938796066",
    }
}

button3 = KeyboardButton("BOSHLASH")
keyboard3 = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True).add(button3)



logging.basicConfig(level=logging.INFO)

bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)

@dp.message_handler(commands=['start', 'help'])
async def send_welcome(message: types.Message):
    await message.answer(f"Salom ! {message.chat.username} \nMen ertangi buyurtmalarni qabul qiluvchi botman\nBUYUTMA berishni boshlang !", reply_markup=keyboard3)
   


@dp.message_handler(lambda message: message.text == "BOSHLASH")
async def oauth(message: types.Message):
    await message.answer(f"Yaxshi , {message.chat.username} raqamingizni yuboring va /tasdiqlash ni bosing",reply_markup=keyboard1)
 

@dp.message_handler(content_types=['contact'])
async def input_number(message: types.Message):
    # keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
    # keyboard.add("Saqlash")
    # user[int(message.chat.id)]['contact'] = message.contact.phone_number
    # text = f"{user[int(message.chat.id)]['name']} {user[int(message.chat.id)]['contact']}"
    await message.answer(f"malumot tasdiqlandi ✅ \nstolni tanlang !",reply_markup=keyboard4)

# @dp.message_handler(commands=['tasdiqlash'])
# async def contact(message: types.Message):





Button1 = KeyboardButton("09:00")
Button2 = KeyboardButton("10:00")
Button3 = KeyboardButton("11:00")
Button4 = KeyboardButton("12:00")
Button5 = KeyboardButton("13:00")
Button6 = KeyboardButton("14:00")
Button7 = KeyboardButton("15:00")
Button8 = KeyboardButton("16:00")
Button9 = KeyboardButton("17:00")
Button10 = KeyboardButton("18:00")
Button11 = KeyboardButton("19:00")
Button12 = KeyboardButton("20:00")

keyboardAA = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True).add(Button1,Button2,Button3,
                                                                                Button4,Button5,Button6,
                                                                                Button7,Button8,Button9,
                                                                                Button10,Button11,Button12)
button4 = KeyboardButton("1-STOL")
button5 = KeyboardButton("2-STOL")
button6 = KeyboardButton("3-STOL")
button7 = KeyboardButton("4-STOL")
keyboard4 = ReplyKeyboardMarkup(resize_keyboard=True,one_time_keyboard=True).add(button4,
                                                                                 button5,
                                                                                 button6,
                                                                                 button7)

@dp.message_handler(lambda message: message.text == "1-STOL")
async def one(message: types.Message):
    await message.answer("1-STOL bo`yicha vaqtlar",reply_markup=keyboardAA)


@dp.message_handler(lambda message: message.text == "2-STOL")
async def one(message: types.Message):
    await message.answer("1-STOL bo`yicha vaqtlar",reply_markup=keyboardAA)


@dp.message_handler(lambda message: message.text == "3-STOL")
async def one(message: types.Message):
    await message.answer("1-STOL bo`yicha vaqtlar",reply_markup=keyboardAA)


@dp.message_handler(lambda message: message.text == "4-STOL")
async def one(message: types.Message):
    await message.answer("1-STOL bo`yicha vaqtlar",reply_markup=keyboardAA)

@dp.message_handler()
async def ok(message: types.Message):
    await message.answer("Malumotlaringiz qabul qilindi sizga tez orada javob beramiz!")

if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)