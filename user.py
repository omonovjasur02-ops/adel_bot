
import asyncio
import logging,sys,os
from aiogram import Dispatcher,Bot,F
from aiogram.filters import Command
from aiogram.types import Message, ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardMarkup, InlineKeyboardButton, \
    FSInputFile
from dotenv import load_dotenv
load_dotenv()
API=os.getenv("API")
dp=Dispatcher()

@dp.message(Command('start'))
async def start_handler(msg:Message):
    await msg.answer("salom hush kelibsiz",reply_markup=Menu)

menu=[
    'It live haqida🏫',
    'Kurslar📚',
    'Mentorlar🧑‍🏫',

    "Biz bilan bog`lanish📞",
    "Loktsiaya🚩"
]

Menu=ReplyKeyboardMarkup(
    keyboard=[[KeyboardButton(text=item)]for item in menu
    ],resize_keyboard=True
)
@dp.message(F.text.in_(menu))
async def Menu_handler(msg:Message):
    T=msg.text
    if menu[0]==T:
        await msg.answer("""
IT Live haqida ma’lumot 💻
IT Live — bu axborot texnologiyalari (IT) sohasiga oid jonli (live) tarzda o‘tkaziladigan darslar, seminarlar yoki treninglardir. Bunday tadbirlarda mutaxassislar yoki o‘qituvchilar internet orqali yoki auditoriyada real vaqt rejimida bilim berishadi.

IT Live tadbirlarida odatda quyidagi mavzular bo‘ladi:
    Dasturlash (Python, JavaScript va boshqalar)
    Web dasturlash (veb sayt yaratish)
    Grafik dizayn
    Kompyuter savodxonligi
    Sun’iy intellekt va yangi texnologiyalar

IT Live’ning afzalliklari:
    O‘qituvchi bilan jonli muloqot qilish mumkin
    Savollar berib, darhol javob olish mumkin
    Amaliy mashg‘ulotlar ko‘p bo‘ladi
    Zamonaviy kasbni o‘rganishga yordam beradi        
        """)
    elif menu[1]==T:
        await msg.answer('Kurs tanlang',reply_markup=Kurslar)
    elif menu[2]==T:
        await msg.answer('Mentor tanlang')
    elif menu[3]==T:
        button=InlineKeyboardMarkup(
            inline_keyboard=[
                [InlineKeyboardButton(text='Telegram uchun',url='https://t.me/+998915093298')]
            ]
        )
        await msg.answer("""
📞 Biz bilan bog‘lanish
Agar siz kurslar haqida batafsil ma’lumot olishni istasangiz yoki ro‘yxatdan o‘tmoqchi bo‘lsangiz, biz bilan bog‘lanishingiz mumkin:
    📞 Telefon: +998 99 721 20 17
    📱 Telegram: @itlive
    📧 Email: info@itlive.uz
Biz sizning savollaringizga mamnuniyat bilan javob beramiz.
        """,reply_markup=button)
    elif menu[4]==T:
        photo=FSInputFile('./img/itlive.jpg')
        await msg.answer_photo(photo=photo,cation="""
📍 Loktsiya
Bizning markazimizga tez yetib borish uchun xaritaga qarang:

⏰ Ish vaqti: 09:00 – 18:00
📍 Manzil: Toshkent sh., Masalan ko‘chasi 123
📌 Xarita orqali yo‘naltirish
        """)
        await msg.answer_location(latitude=40.502724,longitude=68.764829)

kurslar = [
    "Mobil dasturlash",      #0
    "Foundation Dasturlash", #1
    "Frontend Dasturlash",   #2
    "Backend Dasturlash",    #3
    "Full Stack Dasturlash", #4
    "Suniy inteleg",         #5
    "Kibir hafsizlik",       #6
    "Robotexnika",           #7
    "Buga`lteriya",          #8
    "SMM",                   #9
    "DevOps",                #10
    "Ardunio",               #11
    "⬅️ Orqaga"              #12
]
Kurslar=ReplyKeyboardMarkup(
    keyboard=[[KeyboardButton(text=item )]for item in kurslar],resize_keyboard=True
)
@dp.message(F.text.in_(kurslar))
async def Kurs_handler(msg:Message):
    T=msg.text
    if kurslar[0]==T:
        await msg.answer('1')
    elif kurslar[12]==T:
        await msg.answer('Bosh menu',reply_markup=Menu)
@dp.message()
async def message_handler(msg:Message):
    T=msg.text
    if T.lower()=='seni kim yaratgan'or T.lower()=='seni kim yasagan':
        await msg.answer('Asadbek')
    else:
        await msg.answer('Salom')


async def main():
    bot=Bot(token=API)
    await dp.start_polling(bot)

if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO, stream=sys.stdout)
    asyncio.run(main())
