"8090273898:AAHxLys5P_VdpvtWcLHPsSH3vUoJMcld7k8"

from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import Application, CommandHandler, CallbackQueryHandler, ContextTypes
import random

TOKEN = "8090273898:AAHxLys5P_VdpvtWcLHPsSH3vUoJMcld7k8"  # Замените на реальный токен

# Вопросы викторины
QUIZ = [
    {
        "question": "Какой национальный парк Алтая самый большой?",
        "options": [
            ["Сайлюгемский", "1_a"],
            ["Катунский заповедник", "1_b"],
            ["Алтайский заповедник", "1_c"]
        ],
        "correct": "1_c",
        "correct_text": "Алтайский заповедник"
    },
    {
        "question": "Что изображено на гербе Республики Алтай?",
        "options": [
            ["Гора Белуха", "2_a"],
            ["Олень", "2_b"],
            ["Грифон", "2_c"]
        ],
        "correct": "2_a",
        "correct_text": "Гора Белуха"
    },
    {
        "question": "Какая река является главной водной артерией Алтая?",
        "options": [
            ["Катунь", "3_a"],
            ["Бия", "3_b"],
            ["Обь", "3_c"]
        ],
        "correct": "3_a",
        "correct_text": "Катунь"
    },
    {
        "question": "Какой народ является коренным для Алтая?",
        "options": [
            ["Алтайцы", "4_a"],
            ["Буряты", "4_b"],
            ["Тувинцы", "4_c"]
        ],
        "correct": "4_a",
        "correct_text": "Алтайцы"
    },
    {
        "question": "Как называется знаменитая алтайская мумия?",
        "options": [
            ["Принцесса Укока", "5_a"],
            ["Царица Алтая", "5_b"],
            ["Снежная дева", "5_c"]
        ],
        "correct": "5_a",
        "correct_text": "Принцесса Укока"
    },
    {
        "question": "Какой высоты гора Белуха?",
        "options": [
            ["4509 м", "6_a"],
            ["3200 м", "6_b"],
            ["5642 м", "6_c"]
        ],
        "correct": "6_a",
        "correct_text": "4509 м"
    },
    {
        "question": "Какой объект на Алтае включен в список Всемирного наследия ЮНЕСКО?",
        "options": [
            ["Золотые горы Алтая", "7_a"],
            ["Плато Укок", "7_b"],
            ["Телецкое озеро", "7_c"]
        ],
        "correct": "7_a",
        "correct_text": "Золотые горы Алтая"
    },
    {
        "question": "Какое озеро называют 'младшим братом Байкала'?",
        "options": [
            ["Телецкое", "8_a"],
            ["Ая", "8_b"],
            ["Манжерок", "8_c"]
        ],
        "correct": "8_a",
        "correct_text": "Телецкое"
    },
    {
        "question": "Какой город является столицей Республики Алтай?",
        "options": [
            ["Горно-Алтайск", "9_a"],
            ["Бийск", "9_b"],
            ["Барнаул", "9_c"]
        ],
        "correct": "9_a",
        "correct_text": "Горно-Алтайск"
    },
    {
        "question": "Какой перевал на Алтае самый высокий?",
        "options": [
            ["Перевал Кату-Ярык", "10_a"],
            ["Семинский перевал", "10_b"],
            ["Перевал Дурбэт-Даба", "10_c"]
        ],
        "correct": "10_b",
        "correct_text": "Семинский перевал (1894 м)"
    },
    {
        "question": "Какое животное изображено на флаге Республики Алтай?",
        "options": [
            ["Снежный барс", "11_a"],
            ["Олень", "11_b"],
            ["Горный козел", "11_c"]
        ],
        "correct": "11_a",
        "correct_text": "Снежный барс (ирбис)"
    },
    {
        "question": "Какой водопад на Алтае самый высокий?",
        "options": [
            ["Водопад Учар", "12_a"],
            ["Камышлинский водопад", "12_b"],
            ["Водопад Корбу", "12_c"]
        ],
        "correct": "12_a",
        "correct_text": "Водопад Учар (160 м)"
    },
    {
        "question": "Какое растение называют 'золотым корнем'?",
        "options": [
            ["Родиола розовая", "13_a"],
            ["Маралий корень", "13_b"],
            ["Женьшень", "13_c"]
        ],
        "correct": "13_a",
        "correct_text": "Родиола розовая"
    },
    {
        "question": "Какой пещерный комплекс Алтая самый известный?",
        "options": [
            ["Денисова пещера", "14_a"],
            ["Тавдинские пещеры", "14_b"],
            ["Каминная пещера", "14_c"]
        ],
        "correct": "14_a",
        "correct_text": "Денисова пещера"
    },
    {
        "question": "Какой праздник является главным у алтайцев?",
        "options": [
            ["Эл-Ойын", "15_a"],
            ["Шагаа", "15_b"],
            ["Масленица", "15_c"]
        ],
        "correct": "15_a",
        "correct_text": "Эл-Ойын"
    },
    {
        "question": "Какой минерал добывают на Алтае?",
        "options": [
            ["Яшма", "16_a"],
            ["Алмаз", "16_b"],
            ["Нефрит", "16_c"]
        ],
        "correct": "16_a",
        "correct_text": "Яшма (Ревневская и Гольцовская)"
    },
    {
        "question": "Какой русский художник прославил Алтай в своих картинах?",
        "options": [
            ["Николай Рерих", "17_a"],
            ["Иван Шишкин", "17_b"],
            ["Исаак Левитан", "17_c"]
        ],
        "correct": "17_a",
        "correct_text": "Николай Рерих"
    },
    {
        "question": "Какой заповедник был создан первым на Алтае?",
        "options": [
            ["Алтайский", "18_a"],
            ["Катунский", "18_b"],
            ["Тигирекский", "18_c"]
        ],
        "correct": "18_a",
        "correct_text": "Алтайский (1932 г.)"
    },
    {
        "question": "Какой археологический памятник Алтая самый древний?",
        "options": [
            ["Каракол", "19_a"],
            ["Пазырыкские курганы", "19_b"],
            ["Улалинская стоянка", "19_c"]
        ],
        "correct": "19_c",
        "correct_text": "Улалинская стоянка (1.5 млн лет)"
    },
    {
        "question": "Какой перевал связывает Алтай с Монголией?",
        "options": [
            ["Перевал Улан-Даба", "20_a"],
            ["Чике-Таман", "20_b"],
            ["Кату-Ярык", "20_c"]
        ],
        "correct": "20_a",
        "correct_text": "Перевал Улан-Даба"
    },
    {
        "question": "Какой ледник на Алтае самый крупный?",
        "options": [
            ["Ледник Аккем", "21_a"],
            ["Ледник Большой Талдуринский", "21_b"],
            ["Ледник Софийский", "21_c"]
        ],
        "correct": "21_b",
        "correct_text": "Ледник Большой Талдуринский (35 км²)"
    },
    {
        "question": "Какой город Алтая называют 'воротами в горы'?",
        "options": [
            ["Бийск", "22_a"],
            ["Горно-Алтайск", "22_b"],
            ["Чемал", "22_c"]
        ],
        "correct": "22_a",
        "correct_text": "Бийск"
    },
    {
        "question": "Какой вид туризма наиболее развит на Алтае?",
        "options": [
            ["Активный", "23_a"],
            ["Пляжный", "23_b"],
            ["Гастрономический", "23_c"]
        ],
        "correct": "23_a",
        "correct_text": "Активный (пеший, водный, альпинизм)"
    },
    {
        "question": "Какой музыкальный инструмент традиционный у алтайцев?",
        "options": [
            ["Топшур", "24_a"],
            ["Хомус", "24_b"],
            ["Домбра", "24_c"]
        ],
        "correct": "24_a",
        "correct_text": "Топшур"
    },
    {
        "question": "Какой природный парк находится рядом с Чемалом?",
        "options": [
            ["'Остров Патмос'", "25_a"],
            ["'Манжерок'", "25_b"],
            ["'Уч-Энмек'", "25_c"]
        ],
        "correct": "25_a",
        "correct_text": "'Остров Патмос'"
    },
    {
        "question": "Какой древний народ оставил Пазырыкские курганы?",
        "options": [
            ["Скифы", "26_a"],
            ["Гунны", "26_b"],
            ["Тюрки", "26_c"]
        ],
        "correct": "26_a",
        "correct_text": "Скифы"
    },
    {
        "question": "Какой продукт Алтая самый известный?",
        "options": [
            ["Мед", "27_a"],
            ["Сыр", "27_b"],
            ["Орехи", "27_c"]
        ],
        "correct": "27_a",
        "correct_text": "Мед (горно-таежный)"
    },
    {
        "question": "Какой климатический пояс преобладает на Алтае?",
        "options": [
            ["Резко континентальный", "28_a"],
            ["Умеренный", "28_b"],
            ["Субарктический", "28_c"]
        ],
        "correct": "28_a",
        "correct_text": "Резко континентальный"
    },
    {
        "question": "Какой район Алтая называют 'Сибирской Швейцарией'?",
        "options": [
            ["Усть-Коксинский", "29_a"],
            ["Чемальский", "29_b"],
            ["Онгудайский", "29_c"]
        ],
        "correct": "29_b",
        "correct_text": "Чемальский"
    },
    {
        "question": "Какой вид спорта популярен среди алтайцев?",
        "options": [
            ["Кок-бору", "30_a"],
            ["Хоккей", "30_b"],
            ["Горные лыжи", "30_c"]
        ],
        "correct": "30_a",
        "correct_text": "Кок-бору (конная игра)"
    },
    {
        "question": "Какой древний торговый путь проходил через Алтай?",
        "options": [
            ["Великий шелковый путь", "31_a"],
            ["Чайный путь", "31_b"],
            ["Меховой путь", "31_c"]
        ],
        "correct": "31_a",
        "correct_text": "Великий шелковый путь"
    },
    {
        "question": "Какой вид дерева преобладает в алтайской тайге?",
        "options": [
            ["Кедр", "32_a"],
            ["Сосна", "32_b"],
            ["Лиственница", "32_c"]
        ],
        "correct": "32_c",
        "correct_text": "Лиственница"
    },
    {
        "question": "Какой заповедник охраняет снежного барса?",
        "options": [
            ["Сайлюгемский", "33_a"],
            ["Катунский", "33_b"],
            ["Тигирекский", "33_c"]
        ],
        "correct": "33_a",
        "correct_text": "Сайлюгемский"
    },
    {
        "question": "Какой алтайский курорт самый известный?",
        "options": [
            ["Белокуриха", "34_a"],
            ["Чемал", "34_b"],
            ["Артыбаш", "34_c"]
        ],
        "correct": "34_a",
        "correct_text": "Белокуриха"
    },
    {
        "question": "Какой древний город был центром Уйгурского каганата?",
        "options": [
            ["Пор-Бажын", "35_a"],
            ["Аркаим", "35_b"],
            ["Катон-Карагай", "35_c"]
        ],
        "correct": "35_a",
        "correct_text": "Пор-Бажын (на озере Тере-Холь)"
    },
    {
        "question": "Какой вид рыбы водится в Телецком озере?",
        "options": [
            ["Телецкий сиг", "36_a"],
            ["Байкальский омуль", "36_b"],
            ["Амурский сазан", "36_c"]
        ],
        "correct": "36_a",
        "correct_text": "Телецкий сиг (эндемик)"
    },
    {
        "question": "Какой водопад называют 'каскадным'?",
        "options": [
            ["Корбу", "37_a"],
            ["Киште", "37_b"],
            ["Девичьи плесы", "37_c"]
        ],
        "correct": "37_b",
        "correct_text": "Киште"
    },
    {
        "question": "Какой природный феномен наблюдается на Алтае?",
        "options": [
            ["Белуха светится на рассвете", "38_a"],
            ["Озера меняют цвет", "38_b"],
            ["Горы 'поют'", "38_c"]
        ],
        "correct": "38_a",
        "correct_text": "Белуха светится на рассвете ('розовые горы')"
    },
    {
        "question": "Какой алтайский продукт имеет ПГИ?",
        "options": [
            ["Алтайский сыр", "39_a"],
            ["Горный мед", "39_b"],
            ["Орехи кедра", "39_c"]
        ],
        "correct": "39_b",
        "correct_text": "Горный мед (защищенное географическое указание)"
    },
    {
        "question": "Какой праздник отмечают в июне на Алтае?",
        "options": [
            ["Тюрюк Байрам", "40_a"],
            ["Масленица", "40_b"],
            ["Сагаалган", "40_c"]
        ],
        "correct": "40_a",
        "correct_text": "Тюрюк Байрам (праздник кедра)"
    },
    {
        "question": "Какой перевал называют 'алтайским Стоунхенджем'?",
        "options": [
            ["Улаганский", "41_a"],
            ["Чике-Таман", "41_b"],
            ["Семинский", "41_c"]
        ],
        "correct": "41_a",
        "correct_text": "Улаганский (каменные стелы)"
    },
    {
        "question": "Какой минерал называют 'алтайской бабочкой'?",
        "options": [
            ["Родонит", "42_a"],
            ["Яшма", "42_b"],
            ["Азурит", "42_c"]
        ],
        "correct": "42_a",
        "correct_text": "Родонит (розовый узорчатый камень)"
    },
    {
        "question": "Какой древний человек был обнаружен в Денисовой пещере?",
        "options": [
            ["Денисовец", "43_a"],
            ["Неандерталец", "43_b"],
            ["Кроманьонец", "43_c"]
        ],
        "correct": "43_a",
        "correct_text": "Денисовец (новый подвид человека)"
    },
    {
        "question": "Какой район Алтая самый высокогорный?",
        "options": [
            ["Кош-Агачский", "44_a"],
            ["Усть-Коксинский", "44_b"],
            ["Онгудайский", "44_c"]
        ],
        "correct": "44_b",
        "correct_text": "Усть-Коксинский (здесь Белуха)"
    },
    {
        "question": "Какой напиток традиционный у алтайцев?",
        "options": [
            ["Чай с талканом", "45_a"],
            ["Кумыс", "45_b"],
            ["Айран", "45_c"]
        ],
        "correct": "45_a",
        "correct_text": "Чай с талканом"
    },
    {
        "question": "Какой вид тумана характерен для алтайских долин?",
        "options": [
            ["Дымка", "46_a"],
            ["Белый туман", "46_b"],
            ["Молочный туман", "46_c"]
        ],
        "correct": "46_c",
        "correct_text": "Молочный туман (особенно осенью)"
    },
    {
        "question": "Какой камень называют 'алтайским чудом'?",
        "options": [
            ["Ревневская яшма", "47_a"],
            ["Белорецкий кварцит", "47_b"],
            ["Коргонский порфир", "47_c"]
        ],
        "correct": "47_a",
        "correct_text": "Ревневская яшма (использована в Эрмитаже)"
    },
    {
        "question": "Какой алтайский продукт входил в космическое питание?",
        "options": [
            ["Маралий корень", "48_a"],
            ["Кедровый орех", "48_b"],
            ["Золотой корень", "48_c"]
        ],
        "correct": "48_a",
        "correct_text": "Маралий корень (адаптоген)"
    },
    {
        "question": "Какой древний зверь изображен на петроглифах Алтая?",
        "options": [
            ["Шерстистый носорог", "49_a"],
            ["Мамонт", "49_b"],
            ["Пещерный лев", "49_c"]
        ],
        "correct": "49_b",
        "correct_text": "Мамонт (в Калбак-Таше)"
    },
    {
        "question": "Какой природный объект называют 'алтайской жемчужиной'?",
        "options": [
            ["Озеро Ая", "50_a"],
            ["Гора Белуха", "50_b"],
            ["Катунский биосферный заповедник", "50_c"]
        ],
        "correct": "50_a",
        "correct_text": "Озеро Ая"
    }
]

FACTS = [
    {
        "text": "Гора Белуха — самая высокая точка Сибири (4509 м).",
        "image": "https://ru.wikipedia.org/wiki/Белуха_%28гора%29#/media/Файл:GoraBeluha.jpg"
    },
{
        "text": "Телецкое озеро входит в список объектов Всемирного наследия ЮНЕСКО.",
        "image": "https://ru.wikipedia.org/wiki/Телецкое#/media/Файл:Телецкое_озеро_с_севера.jpg"
    },
{
        "text": "На Алтае насчитывается более 17 000 озёр.",
        "image": "https://ru.wikipedia.org/wiki/Кучерлинское#/media/Файл:Sunset_at_Kucherla_lake.jpg"
    },
{
        "text": "Алтай — один из самых экологически чистых регионов России.",
        "image": "https://ru.wikipedia.org/wiki/Алтайский_край#/media/Файл:The_Resort_Of_Belokurikha._Early_autumn_in_the_vicinity_of_the_resort_area.jpg"
    },
{
        "text": "В Денисовой пещере был найден новый вид человека — денисовец.",
        "image": "https://ru.wikipedia.org/wiki/Денисова_пещера#/media/Файл:Известная_на_весь_Мир_Денисова_пещера._01.jpg"
    },
{
        "text": "Пазырыкские курганы — выдающийся археологический памятник скифской эпохи.",
        "image": "https://upload.wikimedia.org/wikipedia/commons/b/b9/Пазырыкские_курганы_02.jpg"
    },
{
        "text": "На плато Укок нашли мумию 'Принцессы Укока'.",
        "image": "https://ru.wikipedia.org/wiki/Принцесса_Укока#/media/Файл:Mummy_of_the_Ukok_Princess.jpg"
    },
{
        "text": "Гора Белуха считается священной у местных народов.",
        "image": "https://ru.wikipedia.org/wiki/Белуха_%28гора%29#/media/Файл:GoraBeluha.jpg"
    },
{
        "text": "На гербе Республики Алтай изображён Грифон.",
        "image": "https://ru.wikipedia.org/wiki/Герб_Республики_Алтай#/media/Файл:Coat_of_Arms_of_Altai_Republic.svg"
    },
{
        "text": "Озеро Ая называют 'жемчужиной Алтая'.",
        "image": "https://ru.wikipedia.org/wiki/Ая_%28озеро%29#/media/Файл:Aya.jpg"
    },
{
        "text": "Катунь — главная река Горного Алтая.",
        "image": "https://upload.wikimedia.org/wikipedia/commons/b/b2/Katun.jpg"
    },
{
        "text": "На Алтае водятся снежные барсы — один из самых редких хищников в мире.",
        "image": "https://ru.wikipedia.org/wiki/Ирбис#/media/Файл:Snow_leopard_Zurich_zoo_01.jpg"
    },
{
        "text": "В Алтайском крае много природных минеральных источников.",
        "image": "https://ru.wikipedia.org/wiki/Минеральные_воды_%28курорты%29#/media/Файл:'Narzan'_natural_water_spring_in_the_woods_near_Kislavodsk,_North_Caucasus,_Russian_Federation.JPG"
    },
{
        "text": "Барнаул основали как центр сереброплавильного производства в 1730 году.",
        "image": "https://ru.wikipedia.org/wiki/История_Барнаула#/media/Файл:Altai-old2.jpg"
    },
{
        "text": "Барнаул в XVIII веке производил до 90% серебра Российской империи.",
        "image": "https://ru.wikipedia.org/wiki/Слиток#/media/Файл:Lingot_aluminium.jpg"
    },
{
        "text": "Император Александр I называл Барнаул 'Сибирским Петербургом'.",
        "image": "https://ru.wikipedia.org/wiki/Александр_I#/media/Файл:Alexander_I_by_Stepan_Shchukin.jpg"
    },
{
        "text": "Денисова пещера хранит следы людей возрастом более 50 000 лет.",
        "image": "https://ru.wikipedia.org/wiki/Неандерталец#/media/Файл:Neanderthaler_Fund.png"
    },
{
        "text": "На плато Укок обнаружены загадочные каменные круги.",
        "image": "https://ru.wikipedia.org/wiki/Каменные_круги#/media/Файл:Swinside_(p4160146).jpg"
    },
{
        "text": "Петроглифы Калбак-Таша изображают древних зверей, включая мамонтов.",
        "image": "https://upload.wikimedia.org/wikipedia/commons/1/1b/Калбак-Таш._Колесница.jpg"
    },
{
        "text": "Алтайский мёд считается одним из лучших в мире.",
        "image": "https://upload.wikimedia.org/wikipedia/commons/c/cc/Runny_hunny.jpg"
    },
{
        "text": "Золотые горы Алтая включены в список ЮНЕСКО.",
        "image": "https://ru.wikipedia.org/wiki/Белуха_%28гора%29#/media/Файл:GoraBeluha.jpg"
    },
{
        "text": "На Алтае растёт редкое растение — родиола розовая ('золотой корень').",
        "image": "https://ru.wikipedia.org/wiki/Родиола"
    },
{
        "text": "Белокуриха — известный алтайский курорт с тёплым микроклиматом.",
        "image": "https://ru.wikipedia.org/wiki/Белокуриха#/media/Файл:Белокуриха,_Алтайский_край._Вид_на_город_03.jpg"
    },
{
        "text": "Чике-Таман — живописный горный перевал, часть Чуйского тракта.",
        "image": "https://ru.wikipedia.org/wiki/Чике-Таман#/media/Файл:Chike-Taman_Pass.jpg"
    },
{
        "text": "Бийск — ворота в Горный Алтай, важный исторический город.",
        "image": "https://ru.wikipedia.org/wiki/Бийск#/media/Файл:Biysk225.jpg"
    },
{
        "text": "Культура алтайцев включает горловое пение и шаманизм.",
        "image": "https://ru.wikipedia.org/wiki/Алтайский_шаманизм#/media/Файл:SB_-_Altay_shaman_with_drum.jpg"
    },
{
        "text": "На Алтае есть 'поющие горы' — акустические аномалии на Чуйском тракте.",
        "image": "https://ru.wikipedia.org/wiki/Чуйский_тракт#/media/Файл:Вид_на_Южно-Чуйский_Хребет.jpg"
    },
{
        "text": "Молочный туман — характерное природное явление в осенних долинах Алтая.",
        "image": "https://ru.wikipedia.org/wiki/Туман#/media/Файл:Горы_0095.JPG"
    },
{
        "text": "Камень родонит называют 'алтайской бабочкой'.",
        "image": "https://ru.wikipedia.org/wiki/Родонит#/media/Файл:Rodonita2EZ.jpg"
    },
{
        "text": "Праздник Эл-Ойын — главный у алтайцев, отмечается летом.",
        "image": "https://ru.wikipedia.org/wiki/Праздники_России#/media/Файл:Russia_day_2009_at_St._Petersburg.jpg"
    },
{
        "text": "Маралий корень применялся в составе космического питания.",
        "image": "https://ru.wikipedia.org/wiki/Рапонтикум_сафлоровидный#/media/Файл:Rhaponticum_carthamoides_001.JPG"
    },
{
        "text": "Ревневская яшма использована в отделке Эрмитажа.",
        "image": "https://ru.wikipedia.org/wiki/Эрмитаж#/media/Файл:Hermitage_night.jpg"
    },
{
        "text": "Остров Патмос в Чемале — популярное паломническое место.",
        "image": "https://ru.wikipedia.org/wiki/Патмос_%28остров_на_реке_Катунь%29#/media/Файл:PatmosIsland_014_2701.jpg"
    },
{
        "text": "Чемальский район часто называют 'Сибирской Швейцарией'.",
        "image": "https://ru.wikipedia.org/wiki/Города_Швейцарии#/media/Файл:Lucerne_city,_lake_and_mountains.jpg"
    },
{
        "text":  "Телецкий сиг — редкая рыба-эндемик.",
        "image": "https://ru.wikipedia.org/wiki/Сиги#/media/Файл:Sik,_Iduns_kokbok.jpg"
    },
{
        "text": "На Алтае до сих пор практикуется шаманизм.",
        "image": "https://ru.wikipedia.org/wiki/Шаман#/media/Файл:Witsen's_Shaman.JPG"
    },
{
        "text": "Николай Рерих вдохновлялся Алтаем в своих картинах.",
        "image": "https://ru.wikipedia.org/wiki/Заморские_гости#/media/Файл:Nicholas_Roerich,_Guests_from_Overseas.jpg"
    },
{
        "text": "Алтайцы пьют чай с талканом — напиток с древней историей.",
        "image": "https://ru.wikipedia.org/wiki/Толокно#/media/Файл:Ложка_с_толокном.jpg"
    },
{
        "text":  "Улаганский перевал известен каменными стелами — 'алтайский Стоунхендж'.",
        "image": "https://ru.wikipedia.org/wiki/Оленный_камень#/media/Файл:Deer_stones.jpg"
    },
{
        "text": "Барнаул — один из самых зелёных городов Сибири.",
        "image": "https://ru.wikipedia.org/wiki/Барнаул#/media/Файл:Barnaul_letters.JPG"
    },
{
        "text": "Воды Телецкого озера невероятно чисты — прозрачность до 15 метров.",
        "image": "https://visit-altairepublic.ru/putevoditel/nasledie-gornogo-altaya/legendy/teletskoe-ozero/"
    },
{
        "text":  "Кедр — символ тайги, занимает большие площади в алтайских лесах.",
        "image": "https://ru.wikipedia.org/wiki/Кедр#/media/Файл:Cedar_of_Lebanon,_Forty_Hall,_Enfield_-_geograph.org.uk_-_708717.jpg"
    },
{
        "text": "Катунский и Алтайский заповедники — ключевые центры биоразнообразия.",
        "image": "https://ru.wikipedia.org/wiki/Алтайский_заповедник#/media/Файл:Uchar_Waterfalls.jpg"
    },
{
        "text": "Культура юрт и кочевого быта сохраняется в отдалённых районах.",
        "image": "https://ru.wikipedia.org/wiki/Юрта#/media/Файл:Kyrgyzská_jurta,_Song-köl.jpg"
    },
{
        "text": "Алтай был частью Великого шёлкового пути.",
        "image": "https://ru.wikipedia.org/wiki/Алтайский_край#/media/Файл:The_Resort_Of_Belokurikha._Early_autumn_in_the_vicinity_of_the_resort_area.jpg"
    },
{
        "text": "На флаге Алтайского края изображены колос пшеницы жёлтого цвета символа сельского хозяйства",
        "image": "https://ru.wikipedia.org/wiki/Флаг_Алтайского_края#/media/Файл:Flag_of_Altai_Krai.svg"
    },
{
        "text": "Кок-бору — традиционная конная игра у алтайцев.",
        "image": "https://ru.wikipedia.org/wiki/Кок-бору#/media/Файл:Cholpon-Ata,_Kyrgyzstan,_World_Nomad_Games,_Kok-boru.jpg"
    },
{
        "text": "Горный мед с Алтая имеет защищенное географическое указание (ПГИ).",
        "image": "https://ru.wikipedia.org/wiki/Мёд#/media/Файл:MielCristalizada.jpg"
    },
]

async def facts(update: Update, context: ContextTypes.DEFAULT_TYPE):
    fact = random.choice(FACTS)
    await update.message.reply_photo(
        photo=fact["image"],
        caption=(
            f"📌 *Интересный факт!*\n{fact['text']}\n\n"
            "🔁 Еще один факт: /facts\n"
            "🧠 Пройти квиз тест: /quiz"
        ),
        parse_mode="Markdown"
    )

async def quiz(update: Update, context: ContextTypes.DEFAULT_TYPE):
    context.user_data['quiz'] = {
        'current_question': 0,
        'score': 0
    }
    await send_question(update, context)


async def send_question(update: Update, context: ContextTypes.DEFAULT_TYPE):
    quiz_data = context.user_data['quiz']
    question = QUIZ[quiz_data['current_question']]

    keyboard = [
        [InlineKeyboardButton(text, callback_data=data)]
        for text, data in question["options"]
    ]

    await update.message.reply_text(
        f"❓ Вопрос {quiz_data['current_question'] + 1}/{len(QUIZ)}:\n"
        f"{question['question']}",
        reply_markup=InlineKeyboardMarkup(keyboard)
    )


async def handle_answer(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    await query.answer()

    quiz_data = context.user_data['quiz']
    question = QUIZ[quiz_data['current_question']]

    # Находим текст выбранного варианта
    chosen_option = next(
        opt[0] for opt in question["options"]
        if opt[1] == query.data
    )

    if query.data == question["correct"]:
        response = (
            f"{question['question']}\n"
            f"✅ Верно! {chosen_option}\n\n"
            f"Ваш текущий счет: {quiz_data['score'] + 1}/{len(QUIZ)}"
        )
        quiz_data['score'] += 1
    else:
        response = (
            f"{question['question']}\n"
            f"❌ Неверно!\n"
            f"Правильный ответ: {question['correct_text']}\n\n"
            f"Ваш текущий счет: {quiz_data['score']}/{len(QUIZ)}"
        )

    await query.edit_message_text(response)

    # Переход к следующему вопросу
    quiz_data['current_question'] += 1
    if quiz_data['current_question'] < len(QUIZ):
        await send_question_from_handler(update, context)
    else:
        await query.message.reply_text(
            f"🏁 Викторина завершена!\n"
            f"Итоговый счет: {quiz_data['score']}/{len(QUIZ)}"
        )


async def send_question_from_handler(update: Update, context: ContextTypes.DEFAULT_TYPE):
    quiz_data = context.user_data['quiz']
    question = QUIZ[quiz_data['current_question']]

    keyboard = [
        [InlineKeyboardButton(text, callback_data=data)]
        for text, data in question["options"]
    ]

    await update.callback_query.message.reply_text(
        f"❓ Вопрос {quiz_data['current_question'] + 1}/{len(QUIZ)}:\n"
        f"{question['question']}",
        reply_markup=InlineKeyboardMarkup(keyboard)
    )

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "🏔 Алтай-Бот 🏔\n\n"
        "Доступные команды:\n"
        "/facts - Случайные факты\n"
        "/quiz - Викторина с кнопками"
    )
def main():
    app = Application.builder().token(TOKEN).build()

    app.add_handler(CommandHandler("start", start))
    app.add_handler(CommandHandler("facts", facts))
    app.add_handler(CommandHandler("quiz", quiz))
    app.add_handler(CallbackQueryHandler(handle_answer))

    print("🟢 Бот запущен с улучшенным отображением результатов!")
    app.run_polling()


if __name__ == "__main__":
    main()
