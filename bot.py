import logging
import asyncio
from aiogram import Bot, Dispatcher, types, F
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, ReplyKeyboardRemove
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from aiogram.types import Message
from aiogram.filters import Command
from yt_dlp import YoutubeDL
from aiogram.types import CallbackQuery
from keep_alive import keep_alive


TOKEN =  "7863509418:AAGCvD9MMb-5dL9cg-ShRkHhfReyb3Jw3Y8"  # BotFather-ден алған токеніңді қой

# Логтарды қосу
logging.basicConfig(level=logging.INFO)

# Бот пен диспетчерді іске қосу
bot = Bot(token=TOKEN)
dp = Dispatcher()
keep_alive()
#Menu
menu = ReplyKeyboardMarkup(
    keyboard=[
[KeyboardButton(text="Ән іздеу ☺️"), KeyboardButton(text="Көңіл күй 🥺")],
        [KeyboardButton(text="📢 Достарыңды шақыр"), KeyboardButton(text="ADMIN 💘")]
    ],
    resize_keyboard=True
)
after_Search_menu = ReplyKeyboardMarkup(
      keyboard=[
          [KeyboardButton( text= "Ия 🙃")],
          [KeyboardButton( text= "Көңіл күй 🥺")]
      ],
      resize_keyboard=True
  )


#Start
@dp.message(Command("start"))
async def start_command(message: types.Message):
    await bot.delete_message(chat_id=message.chat.id, message_id=message.message_id)
    await message.answer("Қалайсың Балапан таңда? 🐣", reply_markup=menu)

# 🎵 Ән іздеу батырмасы басылған кезде
@dp.message (F.text.in_(["Ән іздеу ☺️", "Ия 🙃"]))
async def ask_for_song(message: types.Message):
    await bot.delete_message(chat_id=message.chat.id, message_id=message.message_id)  # Пайдаланушының хабарламасын жою
    await message.answer("Атауын жаз..", reply_markup=ReplyKeyboardRemove())  # Боттың жаңа хабарламасы

@dp.message(F.text == "📢 Достарыңды шақыр")
async def forward(message: types.Message):
    share_text = "🔥 Көңіл-күйге сай музыка таңдауға көмектесетін бот! 🎵 Қосыл: https://t.me/FTMusicc_bot"
    await message.answer(share_text)

# Музыка жүктеу функциясы
def download_audio(query):
    ydl_opts = {
        "format": "bestaudio/best",
        "extractaudio": True,
        "audioformat": "mp3",
        "outtmpl": "music/%(title)s.%(ext)s",
    }

    with YoutubeDL(ydl_opts) as ydl:
        info = ydl.extract_info(f"ytsearch:{query}", download=True)
        filename = ydl.prepare_filename(info["entries"][0])
    return filename

@dp.message(F.text.in_ (["Көңіл күй 😌", "Көңіл күй 🥺"]))
async def for_game(message: types.Message):
    await bot.delete_message(chat_id=message.chat.id, message_id=message.message_id)
    await message.answer("Біреуін таңда Балапан 🫶: ", reply_markup= confirm_keyboard)

confirm_keyboard = InlineKeyboardMarkup(
    inline_keyboard=[
        [InlineKeyboardButton(text="😊", callback_data="happy")],
        [InlineKeyboardButton(text="😢", callback_data="sad")],
        [InlineKeyboardButton(text="⚡", callback_data="energy")],
        [InlineKeyboardButton(text="❤️", callback_data="romantic")],
        [InlineKeyboardButton(text="🧘", callback_data="relax")],
    ]
)

# 🎵 Ән тізімдері
@dp.callback_query(lambda c: c.data in ["happy", "sad", "energy", "romantic", "relax"])
async def process_choose_music(callback: CallbackQuery):
    mood = callback.data
    mood_responses = {
       "happy": "🔥 Көңіл-күйің көтерілсін \n The Limba – Камин \n 2. Qanay – Шапағат \n 3. M’Dee – Қалай қарайсың? \n 4. RaiM & Artur – Самая вышка \n 5. Bayge & Ochooou – CHICA \n 6. IMANGALI – Асықпа \n 7. Ерке Есмахан – 100% \n 8. Qanay – Сенің жанарың \n 9. GITTI – Барлық жолдар \n 10. Kalifarniya – Оп, майне \n 11. Aikyn – Кеш you \n 12. Rada – Жаным \n 13. Miras Zhugunussov – Жүрегіңнен бір орын \n 14. Dequine – Balenciaga \n 15. INDIGO – La La La \n 16. Dinaya – Естеліктер \n 17. Ziruza – Айт енді \n 18. Ерке Есмахан – Қайда? (Remix) \n 19. Qanay – Шоколад \n 20. MARXAL – Lollipop \n 21. ADAM – Сүйемін \n 22. Miras Zhugunussov – Жаным, Hello! \n 23. Aikyn – Алтыным \n 24. Taspay – Достар \n 25. Нұржан Керменбаев – Жаным сол \n 26. Ерболат Құдайберген – Сары қыз \n 27. Айдана Меденова – Қызықты күндер \n 28. MAD MEN – Биле \n 29. Natan & Айқын – Алматы түні \n 30. Big Som – Керемет күн \n 31. Raim – Oh My Love \n 32. Kalifarniya – Базар жоқ \n 33. Dequine – Жаным сол \n 34. Almas – Бәрібір \n 35. Say Mo – Қызық қыз \n 36. GITTI – Сен және мен \n 37. INDIGO – Бірге болайық \n 38. Qanay – Сені сүйем \n 39. Aikyn – Арман \n 40. M’Dee – Кел биле \n 41. Baiqa – Аққуым \n 42. Kalifarniya – Жаным сол \n 43. Lido – Бірге \n 44. IMANGALI – Happy End \n 45. Natan – Қуанышым \n 46. Alina Sarin – Бәрі жақсы болады \n 47. Arsen Shuakbay – Көтер көңіл \n 48. Ziruza – Ләззат \n 49. INDIGO – Қыздар-ай \n 50. Miras Zhugunussov – Әдемі қыз",
    "sad": "😢 Жаныңа жақын әндер...\n Adele – Someone Like You \n 2. Lana Del Rey – Born to Die \n 3. Billie Eilish – When the Party's Over \n 4. Radiohead – Creep \n 5. Lewis Capaldi – Someone You Loved \n 6. James Arthur – Say You Won't Let Go \n 7. Christina Perri – Jar of Hearts \n 8. Damien Rice – The Blower’s Daughter \n 9. Coldplay – Fix You \n 10. Sam Smith – Too Good at Goodbyes \n 11. Olivia Rodrigo – drivers license \n 12. The Fray – How to Save a Life \n 13. Ed Sheeran – Photograph \n 14. Birdy – Skinny Love \n 15. Kodaline – All I Want \n 16. Sia – Breathe Me \n 17. Evanescence – My Immortal \n 18. Jeff Buckley – Hallelujah \n 19. Labrinth – Jealous \n 20. Bon Iver – I Can't Make You Love Me \n 21. Linkin Park – One More Light \n 22. XXXTentacion – SAD! \n 23. Celine Dion – My Heart Will Go On \n 24. Whitney Houston – I Will Always Love You \n 25. Taylor Swift – All Too Well (10 Minute Version) \n 26. Guns N’ Roses – November Rain \n 27. Nirvana – Something in the Way \n 28. Keane – Somewhere Only We Know \n 29. Passenger – Let Her Go \n 30. R.E.M. – Everybody Hurts \n 31. Adele – Hello \n 32. Әділхан Макин – Кешір мені \n 33. Ғалымжан Молданазар – Өзің ғана \n 34. МузАРТ – Өмір өткелдері \n 35. Төреғали Төреәлі – Алло \n 36. Қуандық Рахым – Сен емес \n 37. Ерке Есмахан – Қайда? \n 38. Raim – Сәуле \n 39. Нұрболат Абдуллин – Сүйген жүрек \n 40. Әлішер Кәрімов – Сені сағындым \n 41. Айқын – Кешір мені \n 42. Димаш Құдайберген – Ұмытылмас күн \n 43. Нұржан Керменбаев – Жаным \n 44. Али Оқапов – Алыстама \n 45. Серік Ибрагимов – Кім кінәлі? \n 46. Нұрлан Еспанов – Сағындым сені \n 47. Ернар Айдар – Күт мені \n 48. Заман – Сен үшін \n 49. Айдана Меденова – Көзіңнің мөлдірін-ай \n 50. Мархаба Сәби – Менімен биле",
    "energy": "⚡ Қуаттандыратын әндер!\n1. RaiM – Oh My Love \n 2. Qanay – Шапағат \n 3. The Limba – Камин \n 4. IMANGALI – Асықпа \n 5. Kalifarniya – Оп, майне \n 6. MAD MEN – Биле \n 7. GITTI – Барлық жолдар \n 8. Aikyn – Кеш You \n 9. M’Dee – Қалай қарайсың? \n 10. INDIGO – La La La \n 11. Say Mo – Қызық қыз \n 12. Dequine – Balenciaga \n 13. Qanay – Шоколад \n 14. MARXAL – Lollipop \n 15. Kalifarniya – Базар жоқ \n 16. Baiqa – Аққуым \n 17. Almas – Бәрібір \n 18. Big Som – Керемет күн \n 19. Rada – Жаным \n 20. Natan & Айқын – Алматы түні \n 21. Lido – Бірге \n 22. IMANGALI – Happy End \n 23. Ziruza – Айт енді \n 24. Alina Sarin – Бәрі жақсы болады \n 25. Aikyn – Арман \n 26. Kalifarniya – Жаным сол \n 27. Taspay – Достар \n 28. Arsen Shuakbay – Көтер көңіл \n 29. Natan – Қуанышым \n 30. INDIGO – Бірге болайық \n 31. GITTI – Сен және мен \n 32. Dequine – Жаным сол \n 33. Aikyn – Алтыным \n 34. Miras Zhugunussov – Жүрегіңнен бір орын \n 35. Ziruza – Ләззат \n 36. MAD MEN – Қалайсың? \n 37. Qanay – Сенің жанарың \n 38. RaiM & Artur – Самая вышка \n 39. Miras Zhugunussov – Әдемі қыз \n 40. M’Dee – Кел биле \n 41. Kalifarniya – Биле-биле \n 42. Ерке Есмахан – 100% \n 43. Айдана Меденова – Қызықты күндер \n 44. INDIGO – Қыздар-ай \n 45. ADAM – Сүйемін \n 46. Qanay – Сені сүйем \n 47. Серік Ибрагимов – Ойбай, жаным! \n 48. Big Som – Party Time \n 49. Жанар Дұғалова – Айта бер \n 50. Miras Zhugunussov – Жаным, Hello!",
    "romantic": "❤️ Романтикалық әуендер!\n1 Қуандық Рахым – Көзімнің қарасы \n 2. Әділхан Макин – Кешір мені \n 3. Raim – Сәуле \n 4. Нұрболат Абдуллин – Сүйген жүрек \n 5. Ғалымжан Молданазар – Өзің ғана \n 6. МузАРТ – Өмір өткелдері \n 7. Төреғали Төреәлі – Сағынба \n 8. Нұржан Керменбаев – Жаным \n 9. Димаш Құдайберген – Ұмытылмас күн \n 10. Ерке Есмахан – Қайда? \n 11. Али Оқапов – Алыстама \n 12. Серік Ибрагимов – Кім кінәлі? \n 13. Ернар Айдар – Күт мені \n 14. Айқын – Кешір мені \n 15. Заман – Сен үшін \n 16. Айдана Меденова – Көзіңнің мөлдірін-ай \n 17. Marhaba Sabi – Менімен биле \n 18. ADAM – Сүйемін \n 19. Natan – Сағындым \n 20. Kalifarniya – Жаным сол \n 21. Big Som – Сенсіз өмір жоқ \n 22. GITTI – Сен және мен \n 23. Almas – Бәрібір \n 24. INDIGO – Бірге болайық \n 25. Qanay – Сенің жанарың \n 26. IMANGALI – Happy End \n 27. Miras Zhugunussov – Жүрегіңнен бір орын \n 28. Ziruza – Айт енді \n 29. Dequine – Жаным сол \n 30. Aikyn – Алтыным \n 31. Baiqa – Аққуым \n 32. Arsen Shuakbay – Көтер көңіл \n 33. Айқын & Кәмшат Жолдыбаева – Күндер өтуде \n 34. Raim & Artur – Сүйем \n 35. Kalifarniya – Махаббат \n 36. Natan & Айқын – Алматы түні \n 37. Lido – Бірге \n 38. Ziruza – Ләззат \n 39. Qanay – Сені сүйем \n 40. M’Dee – Саған \n 41. Ерке Есмахан – Арман \n 42. Әлішер Кәрімов – Сені сағындым \n 43. Айдана Меденова – Қызықты күндер \n 44. INDIGO – Қыздар-ай \n 45. ADAM – Көзімнің қарасы \n 46. Aikyn – Жүрегім \n 47. MARXAL – Саған ғана \n 48. Серік Ибрагимов – Айым \n 49. Big Som – Сен менің жүрегімде \n 50. Miras Zhugunussov – Әдемі қыз",
    "relax": "🧘 Жайлы, тыныш музыка..\n1 Ludovico Einaudi – Nuvole Bianche \n 2. Yiruma – River Flows in You \n 3. Enya – Only Time \n 4. Hans Zimmer – Time (Inception OST) \n 5. Ólafur Arnalds – Saman \n 6. Max Richter – On the Nature of Daylight \n 7. Sade – By Your Side \n 8. Norah Jones – Come Away With Me \n 9. Air – La Femme d'Argent \n 10. Sigur Rós – Hoppípolla \n 11. Moby – Porcelain \n 12. Einaudi – Experience \n 13. Bon Iver – Holocene \n 14. Massive Attack – Teardrop \n 15. FKA Twigs – Cellophane \n 16. Portishead – Roads \n 17. José González – Heartbeats \n 18. Zero 7 – Destiny \n 19. Agnes Obel – Riverside \n 20. The Cinematic Orchestra – To Build a Home \n 21. Patrick Watson – Je Te Laisserai Des Mots \n 22. Billie Eilish – i love you \n 23. Lana Del Rey – Video Games \n 24. Aurora – Runaway \n 25. Cigarettes After Sex – Apocalypse \n 26. Beach House – Space Song \n 27. Khruangbin – White Gloves \n 28. Rhye – Open \n 29. Alexandre Desplat – The Meadow (Twilight OST) \n 30. Explosions in the Sky – Your Hand in Mine \n 31. Hammock – Turning Into Tiny Particles \n 32. Boards of Canada – Dayvan Cowboy \n 33. Tycho – A Walk \n 34. Coldplay – Sparks \n 35. Kings of Convenience – Misread \n 36. Gregory Alan Isakov – San Luis \n 37. Nick Drake – Pink Moon \n 38. Iron & Wine – Naked as We Came \n 39. Angus & Julia Stone – Big Jet Plane \n 40. Sleeping At Last – Saturn \n 41. Roo Panes – Open Road \n 42. Novo Amor – Anchor \n 43. Ray LaMontagne – Let It Be Me \n 44. Beirut – Postcards from Italy \n 45. Michael Kiwanuka – Cold Little Heart \n 46. Xavier Rudd – Follow the Sun \n 47. Jose Feliciano – Rain \n 48. Damien Rice – Delicate \n 49. James Vincent McMorrow – Higher Love \n 50. Roo Panes – Know Me Well"
    }
    await callback.message.answer(mood_responses[mood], reply_markup=menu)
    await callback.answer()  # Батырма басылғанын көрсету


@dp.message(F.text == "ADMIN 💘")
async def asc_for_Me (message: types.Message):
     await bot.delete_message(chat_id=message.chat.id, message_id=message.message_id)
     await message.answer( "Балапан егер жалоб болса немесе өтініш болса жазағой..😉\n Боқтап жазу жоғынан, Барлығыңды жақсы көремін \n @FTbekzat")

# Қолданушы әннің атын жазғанда ғана іздеу
@dp.message()
async def search_music(message: types.Message):
    if message.text in ["Қандай Әнді Іздегің келеді Балапан 🥰", "Ойын ойнайсың ба? Балапан 🙃", "⚙️ Баптаулар", "Менімен Байланыс жасайсын ба? Балапан ☺️","Тағы Музыка Керекпе?😁", "Әлде ойын?🤪", "Әлде Көңіл күйіңе байланысты музыка таңдайсың ба?😅", "Көңіл күй арқылы керекпа әлде?", "Ән іздеу ☺️", "Көңіл күй😏", "📢 Достарыңды шақыр","ADMIN 💘", "Көңіл күй 🥺"]:
        return  # Егер бұл батырма болса, ештеңе жасамаймыз

    await message.answer(" Әнің іздестірілуде Балапан...🤓")

    try:
        audio_file = download_audio(message.text)
        await message.answer_audio(types.FSInputFile(audio_file), caption="🎧 Enjoy Балапан 😫")
        await message.answer("Балапан тағы Музыка іздейсің бе?\n Әлде..? ☺️ ", reply_markup=after_Search_menu)
    except Exception as e:
        await message.answer("Балапан точна Ән енгіздің ба өзі? 🧐 ")


# Ботты іске қосу
async def main():
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())
