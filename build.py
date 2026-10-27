"""Builds the Bridge Con website into ./public: landing, privacy and support
pages in English (/), Ukrainian (/uk/) and Russian (/ru/).

    python3 -I build.py

Set SUPPORT_EMAIL and APP_STORE_URL below, then rebuild and redeploy.
"""
import html, os, shutil

SUPPORT_EMAIL = "mayevskydv@gmail.com"   # the address users write to
APP_STORE_URL = ""                       # the App Store link, once the app is live
# Where the site sits on its host: "/" on its own domain, "/bridgecon-site/" on GitHub Pages.
BASE = os.environ.get("SITE_BASE", "/")
UPDATED = {"en": "27 October 2026", "uk": "27 жовтня 2026", "ru": "27 октября 2026"}

ROOT = os.path.dirname(os.path.abspath(__file__))
OUT = os.path.join(ROOT, "public")

LANGS = {"en": ("English", ""), "uk": ("Українська", "uk/"), "ru": ("Русский", "ru/")}

T = {
"en": dict(
    tagline="Tools for the officer of the watch",
    lead="Tides for 5,900 ports, bridge checklists, GMDSS distress steps, the vessel identifier and celestial navigation — offline, in plain words.",
    store="Download on the App Store", soon="Coming soon to the App Store",
    nav_home="Home", nav_support="Support", nav_privacy="Privacy",
    features=[
        ("Tides, offline", "High and low water, the curve and the tidal window for 5,900 ports, with alerts before HW and LW. Checked against NOAA: median 0.3 minutes and 1 mm."),
        ("Bridge checklists", "35 checklists and 386 points, each with a short how-to. Swipe right for done, left to postpone."),
        ("GMDSS", "Distress, received alerts and false alerts, one decision at a time, with your ship's MAYDAY ready to read out."),
        ("Vessel identifier", "Tap the lights you see: the vessel, her heading and what to do, with the COLREG rule."),
        ("Celestial and more", "Sky, almanac and sight reduction; ETA; rest hours with an inspection PDF; compass error; true wind; air draft; a private journal."),
        ("Yours, and only yours", "No account, no ads, no tracking. Your data lives on your phone and in your own iCloud, synced across your iPhones. English, Ukrainian and Russian."),
    ],
    pricing="GMDSS, the vessel identifier and ETA are free, and every other tool has a free part. Try everything free for 7 days — no charge, nothing renews — then buy only the tools you use, or all of them once. No subscription.",
    disclaimer="Bridge Con helps the watch. It does not replace the ship's SMS, official charts, tide tables and publications, or the Master's orders.",
    privacy_title="Privacy policy",
    privacy=[
        ("In short", "Bridge Con does not collect, sell or share any data about you. There is no account, no analytics, no advertising and no tracking. What you enter is kept on your iPhone and, if iCloud is on, in your own private iCloud — which we cannot access."),
        ("Where your data is kept", "Your ship's details, tide ports, checklist records, rest hours, compass book, ETA, journal notes and voice recordings are kept on your device. If you're signed in to iCloud with iCloud Drive on for Bridge Con, they are also stored in the app's container in your private iCloud database, so they appear on your other devices. That copy is held by Apple under your Apple Account; only you can read it — we never see it. Turn it off in Settings › [your name] › iCloud. Deleting the app removes the copy on this device; delete the iCloud copy in Settings › [your name] › iCloud › Manage Storage."),
        ("Permissions", "Notifications — only if you turn on tide alerts, reminders or rest-hour warnings; they are scheduled on the phone. Microphone and speech recognition — only when you record a voice note. Most languages are turned into text on the phone. Languages that Apple can't yet transcribe offline, such as Ukrainian, are sent to Apple's speech service when you're online; that is handled by Apple under Apple's privacy policy, and we never receive the audio or the text."),
        ("Purchases", "Purchases and the free trial go through Apple's App Store. Apple handles payment; we receive no card or personal details. The app checks your purchases on the device."),
        ("Ratings", "The app may ask for an App Store rating with Apple's own rating window. Whether you rate is up to you, and the app doesn't learn your answer."),
        ("Children", "Bridge Con is a tool for professional seafarers and is not directed at children. It collects no data from anyone."),
        ("Changes and contact", "If this policy changes, the new version will be published on this page with its date. Questions: "),
    ],
    support_title="Support",
    support_lead="Something not working, a wrong figure, or an idea? Write to us — a deck officer reads every message.",
    faq=[
        ("How do I restore my purchases on a new phone?", "Open any locked item to show the paywall, scroll down and tap Restore purchases. Purchases follow your Apple Account."),
        ("How does the free trial work?", "It's free and opens every tool for 7 days. Nothing is charged and nothing renews. After it ends, the free parts stay and you buy only what you need."),
        ("How do I change the language?", "Tap the gear on the main screen and choose English, Українська or Русский, then close and reopen the app."),
        ("How accurate are the tides?", "They're the astronomical tide from each port's harmonic constants — checked against NOAA to about a minute and a centimetre. Wind, pressure and river flow change the real level. For pilotage and critical under-keel clearance use the official tables and real-time gauges."),
        ("I can't find my port.", "Type the port's name in English or locally, or its UN/LOCODE (for example NL RTM). The app shows the tide stations around it and how far away they are."),
        ("How do I get a refund?", "Refunds are handled by Apple: reportaproblem.apple.com."),
    ],
    write="Write to support", updated="Last updated", footer="Made for the officer of the watch.",
),
"uk": dict(
    tagline="Інструменти вахтового помічника",
    lead="Припливи для 5 900 портів, чеклісти на містку, кроки ГМЗЛБ при лиху, визначення судна за вогнями й астронавігація — офлайн, простими словами.",
    store="Завантажити в App Store", soon="Незабаром в App Store",
    nav_home="Головна", nav_support="Підтримка", nav_privacy="Конфіденційність",
    features=[
        ("Припливи офлайн", "Повна й мала вода, крива та приливне вікно для 5 900 портів, з нагадуваннями перед ПВ і МВ. Звірено з NOAA: медіана 0,3 хв і 1 мм."),
        ("Чеклісти на містку", "35 чеклістів і 386 пунктів, до кожного — коротко, як зробити. Свайп праворуч — виконано, ліворуч — відкласти."),
        ("ГМЗЛБ", "Лихо, отриманий сигнал лиха, хибний сигнал — по одному рішенню, з готовим MAYDAY вашого судна."),
        ("Визначення судна за вогнями", "Позначте вогні, які бачите: судно, його курс і що робити, з правилом МППЗС."),
        ("Астронавігація та інше", "Небо, альманах і обсервація; ETA; години відпочинку з PDF для перевірок; поправка компаса; справжній вітер; надводний габарит; особистий журнал."),
        ("Ваше — і лише ваше", "Без акаунта, реклами й стеження. Дані — на вашому телефоні та у вашому iCloud, синхронізовані між вашими iPhone. Українська, англійська й російська."),
    ],
    pricing="ГМЗЛБ, визначення судна за вогнями та ETA — безкоштовно, і в кожному іншому інструменті є безкоштовна частина. 7 днів усе безкоштовно — без оплати й автопродовження, — далі купуйте лише потрібні інструменти або все разом, один раз. Без підписки.",
    disclaimer="Bridge Con допомагає вахті, але не замінює СУБ судна, офіційні карти, таблиці припливів і посібники чи розпорядження капітана.",
    privacy_title="Політика конфіденційності",
    privacy=[
        ("Коротко", "Bridge Con не збирає, не продає й не передає жодних даних про вас. Немає акаунта, аналітики, реклами й стеження. Те, що ви вводите, зберігається на вашому iPhone і, якщо ввімкнено iCloud, у вашому приватному iCloud, до якого ми не маємо доступу."),
        ("Де зберігаються дані", "Дані судна, порти припливів, записи чеклістів, години відпочинку, журнал поправок, ETA, нотатки й голосові записи зберігаються на пристрої. Якщо ви ввійшли в iCloud і для Bridge Con увімкнено iCloud, вони також зберігаються в контейнері програми у вашій приватній базі iCloud і з'являються на інших ваших пристроях. Цю копію зберігає Apple у вашому Apple Account; прочитати її можете лише ви — ми її ніколи не бачимо. Вимкнути: Параметри › [ваше ім'я] › iCloud. Видалення програми видаляє копію на пристрої; копію в iCloud видаліть у Параметри › [ваше ім'я] › iCloud › Керувати сховищем."),
        ("Дозволи", "Сповіщення — лише якщо ви ввімкнете нагадування про припливи, нагадування чи попередження про відпочинок; їх планує сам телефон. Мікрофон і розпізнавання мовлення — лише коли ви записуєте голосову нотатку. Більшість мов розпізнається на телефоні. Мови, які Apple ще не розпізнає офлайн, як-от українська, надсилаються до служби розпізнавання Apple, коли є зв'язок; це обробляє Apple за своєю політикою конфіденційності, і ми ніколи не отримуємо ні звук, ні текст."),
        ("Покупки", "Покупки й пробний період проходять через App Store. Оплату обробляє Apple; ми не отримуємо даних картки чи особистих даних. Програма перевіряє покупки на пристрої."),
        ("Оцінки", "Програма може запропонувати оцінити її у власному вікні оцінки Apple. Оцінювати чи ні — вирішуєте ви, і програма не дізнається вашої відповіді."),
        ("Діти", "Bridge Con — інструмент для професійних моряків і не призначений для дітей. Програма не збирає даних ні про кого."),
        ("Зміни та контакти", "Якщо політика зміниться, нову версію з датою буде опубліковано на цій сторінці. Питання: "),
    ],
    support_title="Підтримка",
    support_lead="Щось не працює, неправильна цифра чи є ідея? Напишіть нам — кожен лист читає судноводій.",
    faq=[
        ("Як відновити покупки на новому телефоні?", "Відкрийте будь-який закритий пункт, щоб з'явилося вікно покупки, прокрутіть униз і натисніть «Відновити покупки». Покупки прив'язані до вашого Apple Account."),
        ("Як працює безкоштовний пробний період?", "Він безкоштовний і відкриває всі інструменти на 7 днів. Нічого не списується й не продовжується. Після завершення безкоштовні частини лишаються, а купуєте лише потрібне."),
        ("Як змінити мову?", "Натисніть шестерню на головному екрані, виберіть English, Українська або Русский, тоді закрийте й знову відкрийте програму."),
        ("Наскільки точні припливи?", "Це астрономічний приплив за гармонічними сталими порту — звірено з NOAA з точністю близько хвилини й сантиметра. Вітер, тиск і стік річки змінюють реальний рівень. Для лоцманської проводки й критичного запасу під кілем користуйтеся офіційними таблицями та даними мареографів."),
        ("Не можу знайти свій порт.", "Введіть назву порту англійською чи місцевою мовою або його UN/LOCODE (наприклад NL RTM). Програма покаже припливні станції поруч і відстань до них."),
        ("Як повернути гроші?", "Повернення обробляє Apple: reportaproblem.apple.com."),
    ],
    write="Написати в підтримку", updated="Оновлено", footer="Зроблено для вахтового помічника.",
),
"ru": dict(
    tagline="Инструменты вахтенного помощника",
    lead="Приливы для 5 900 портов, чек-листы на мостике, шаги ГМССБ при бедствии, определение судна по огням и астронавигация — офлайн, простыми словами.",
    store="Загрузить в App Store", soon="Скоро в App Store",
    nav_home="Главная", nav_support="Поддержка", nav_privacy="Конфиденциальность",
    features=[
        ("Приливы офлайн", "Полная и малая вода, кривая и приливное окно для 5 900 портов, с напоминаниями перед ПВ и МВ. Сверено с NOAA: медиана 0,3 мин и 1 мм."),
        ("Чек-листы на мостике", "35 чек-листов и 386 пунктов, к каждому — коротко, как сделать. Свайп вправо — выполнено, влево — отложить."),
        ("ГМССБ", "Бедствие, полученный сигнал бедствия, ложный сигнал — по одному решению, с готовым MAYDAY вашего судна."),
        ("Определение судна по огням", "Отметьте огни, которые видите: судно, его курс и что делать, с правилом МППСС."),
        ("Астронавигация и другое", "Небо, альманах и обсервация; ETA; часы отдыха с PDF для проверок; поправка компаса; истинный ветер; надводный габарит; личный журнал."),
        ("Ваше — и только ваше", "Без аккаунта, рекламы и слежки. Данные — на вашем телефоне и в вашем iCloud, синхронизированы между вашими iPhone. Русский, английский и украинский."),
    ],
    pricing="ГМССБ, определение судна по огням и ETA — бесплатно, и в каждом другом инструменте есть бесплатная часть. 7 дней всё бесплатно — без оплаты и автопродления, — дальше покупайте только нужные инструменты или всё сразу, один раз. Без подписки.",
    disclaimer="Bridge Con помогает вахте, но не заменяет СУБ судна, официальные карты, таблицы приливов и пособия или распоряжения капитана.",
    privacy_title="Политика конфиденциальности",
    privacy=[
        ("Коротко", "Bridge Con не собирает, не продаёт и не передаёт никаких данных о вас. Нет аккаунта, аналитики, рекламы и слежки. То, что вы вводите, хранится на вашем iPhone и, если включён iCloud, в вашем личном iCloud, к которому у нас нет доступа."),
        ("Где хранятся данные", "Данные судна, порты приливов, записи чек-листов, часы отдыха, журнал поправок, ETA, заметки и голосовые записи хранятся на устройстве. Если вы вошли в iCloud и для Bridge Con включён iCloud, они также хранятся в контейнере приложения в вашей личной базе iCloud и появляются на других ваших устройствах. Эту копию хранит Apple в вашем Apple Account; прочитать её можете только вы — мы её никогда не видим. Выключить: Настройки › [ваше имя] › iCloud. Удаление приложения удаляет копию на устройстве; копию в iCloud удалите в Настройки › [ваше имя] › iCloud › Управление хранилищем."),
        ("Разрешения", "Уведомления — только если вы включите напоминания о приливах, напоминания или предупреждения об отдыхе; их планирует сам телефон. Микрофон и распознавание речи — только когда вы записываете голосовую заметку. Большинство языков распознаётся на телефоне. Языки, которые Apple пока не распознаёт офлайн, например украинский, отправляются в службу распознавания Apple при наличии связи; это обрабатывает Apple по своей политике конфиденциальности, и мы никогда не получаем ни звук, ни текст."),
        ("Покупки", "Покупки и пробный период проходят через App Store. Оплату обрабатывает Apple; мы не получаем данных карты или личных данных. Приложение проверяет покупки на устройстве."),
        ("Оценки", "Приложение может предложить оценить его в собственном окне оценки Apple. Оценивать или нет — решаете вы, и приложение не узнаёт вашего ответа."),
        ("Дети", "Bridge Con — инструмент для профессиональных моряков и не предназначен для детей. Приложение не собирает данных ни о ком."),
        ("Изменения и контакты", "Если политика изменится, новая версия с датой будет опубликована на этой странице. Вопросы: "),
    ],
    support_title="Поддержка",
    support_lead="Что-то не работает, неверная цифра или есть идея? Напишите нам — каждое письмо читает судоводитель.",
    faq=[
        ("Как восстановить покупки на новом телефоне?", "Откройте любой закрытый пункт, чтобы появилось окно покупки, прокрутите вниз и нажмите «Восстановить покупки». Покупки привязаны к вашему Apple Account."),
        ("Как работает бесплатный пробный период?", "Он бесплатный и открывает все инструменты на 7 дней. Ничего не списывается и не продлевается. После окончания бесплатные части остаются, а покупаете только нужное."),
        ("Как сменить язык?", "Нажмите шестерёнку на главном экране, выберите English, Українська или Русский, затем закройте и снова откройте приложение."),
        ("Насколько точны приливы?", "Это астрономический прилив по гармоническим постоянным порта — сверено с NOAA с точностью около минуты и сантиметра. Ветер, давление и сток реки меняют реальный уровень. Для лоцманской проводки и критичного запаса под килем пользуйтесь официальными таблицами и данными мареографов."),
        ("Не могу найти свой порт.", "Введите название порта по-английски или на местном языке либо его UN/LOCODE (например NL RTM). Приложение покажет приливные станции рядом и расстояние до них."),
        ("Как вернуть деньги?", "Возвраты обрабатывает Apple: reportaproblem.apple.com."),
    ],
    write="Написать в поддержку", updated="Обновлено", footer="Сделано для вахтенного помощника.",
),
}

CSS = """
:root{--bg:#0B1724;--band:#10233A;--card:#172C45;--ink:#E8EEF5;--muted:#9AA8B8;--accent:#C9A55E;--line:rgba(232,238,245,.12)}
*{box-sizing:border-box}html{-webkit-text-size-adjust:100%}
body{margin:0;background:var(--bg);color:var(--ink);font:17px/1.55 -apple-system,BlinkMacSystemFont,"SF Pro Text","Segoe UI",Roboto,sans-serif}
a{color:var(--accent)}
.wrap{max-width:860px;margin:0 auto;padding:0 20px}
header{background:radial-gradient(120% 100% at 50% 0,var(--band),var(--bg));border-bottom:1px solid var(--line)}
nav{display:flex;gap:18px;align-items:center;padding:16px 0;flex-wrap:wrap}
nav .brand{display:flex;gap:10px;align-items:center;color:var(--ink);text-decoration:none;font-weight:700;margin-right:auto}
nav .brand img{width:30px;height:30px;border-radius:8px}
nav a{text-decoration:none;font-weight:600;font-size:15px}
.langs{display:flex;gap:8px;font-size:14px}.langs a{color:var(--muted)}.langs a.on{color:var(--ink)}
.hero{padding:56px 0 64px;position:relative;overflow:hidden}
.hero .mark{position:absolute;right:-60px;top:10px;width:300px;opacity:.16}
.hero img.icon{width:96px;height:96px;border-radius:22px;box-shadow:0 10px 30px rgba(0,0,0,.4)}
h1{font-size:42px;line-height:1.1;margin:18px 0 6px}
.tag{color:var(--accent);font-weight:600;margin:0 0 14px}
.lead{color:var(--muted);font-size:19px;max-width:620px}
.btn{display:inline-block;margin-top:22px;background:var(--accent);color:#14202E;font-weight:700;padding:13px 22px;border-radius:999px;text-decoration:none}
.btn.off{background:var(--card);color:var(--muted)}
main{padding:40px 0 56px}
.grid{display:grid;grid-template-columns:repeat(auto-fit,minmax(240px,1fr));gap:14px}
.card{background:var(--card);border:1px solid var(--line);border-radius:20px;padding:20px}
.card h3{margin:0 0 6px;font-size:18px}.card p{margin:0;color:var(--muted);font-size:15px}
.note{color:var(--muted);font-size:15px;margin-top:26px}
h2{font-size:30px;margin:0 0 6px}
section.text h3{margin:28px 0 6px;font-size:19px}
section.text p{color:#C9D3DE;margin:0}
details{background:var(--card);border:1px solid var(--line);border-radius:16px;padding:14px 18px;margin:10px 0}
summary{cursor:pointer;font-weight:600}details p{color:var(--muted);margin:10px 0 0}
footer{border-top:1px solid var(--line);padding:24px 0 40px;color:var(--muted);font-size:14px}
footer a{color:var(--muted)}
@media (max-width:560px){h1{font-size:32px}.hero .mark{width:200px;right:-70px}}
"""

def page(lang, path, title, body, desc):
    t = T[lang]; prefix = LANGS[lang][1]; depth = "../" if prefix else ""
    langs = " ".join(
        f'<a class="{"on" if l == lang else ""}" href="{"../" if prefix else ""}{LANGS[l][1]}{path}" hreflang="{l}">{LANGS[l][0]}</a>'
        for l in LANGS)
    return f"""<!doctype html>
<html lang="{lang}"><head><meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1">
<title>{html.escape(title)}</title>
<meta name="description" content="{html.escape(desc)}">
<link rel="icon" href="{BASE}img/favicon-64.png"><link rel="apple-touch-icon" href="{BASE}img/apple-touch-icon.png">
<link rel="stylesheet" href="{BASE}style.css">
</head><body>
<header><div class="wrap"><nav>
<a class="brand" href="{BASE}{prefix}"><img src="{BASE}img/icon-256.png" alt="">Bridge Con</a>
<a href="{BASE}{prefix}support">{t["nav_support"]}</a><a href="{BASE}{prefix}privacy">{t["nav_privacy"]}</a>
<span class="langs">{langs}</span>
</nav></div></header>
{body}
<footer><div class="wrap">© 2026 Bridge Con · {t["footer"]} · <a href="{BASE}{prefix}privacy">{t["nav_privacy"]}</a> · <a href="{BASE}{prefix}support">{t["nav_support"]}</a></div></footer>
</body></html>
"""

def home(lang):
    t = T[lang]
    store = (f'<a class="btn" href="{APP_STORE_URL}">{t["store"]}</a>' if APP_STORE_URL
             else f'<span class="btn off">{t["soon"]}</span>')
    cards = "".join(f'<div class="card"><h3>{html.escape(h)}</h3><p>{html.escape(p)}</p></div>' for h, p in t["features"])
    body = f"""<section class="hero"><div class="wrap">
<img class="mark" src="{BASE}img/mark.png" alt="">
<img class="icon" src="{BASE}img/icon-256.png" alt="Bridge Con">
<h1>Bridge Con</h1><p class="tag">{t["tagline"]}</p>
<p class="lead">{html.escape(t["lead"])}</p>{store}
</div></section>
<main><div class="wrap"><div class="grid">{cards}</div>
<p class="note">{html.escape(t["pricing"])}</p><p class="note">{html.escape(t["disclaimer"])}</p></div></main>"""
    return page(lang, "", f"Bridge Con — {t['tagline']}", body, t["lead"])

def privacy(lang):
    t = T[lang]
    secs = ""
    for i, (h, p) in enumerate(t["privacy"]):
        tail = f'<a href="mailto:{SUPPORT_EMAIL}">{SUPPORT_EMAIL}</a>' if i == len(t["privacy"]) - 1 else ""
        secs += f"<h3>{html.escape(h)}</h3><p>{html.escape(p)}{tail}</p>"
    body = f"""<main><div class="wrap"><section class="text">
<h2>{t["privacy_title"]}</h2><p class="note">{t["updated"]}: {UPDATED[lang]}</p>{secs}
</section></div></main>"""
    return page(lang, "privacy", f"{t['privacy_title']} — Bridge Con", body, t["privacy"][0][1])

def support(lang):
    t = T[lang]
    faq = "".join(f"<details><summary>{html.escape(q)}</summary><p>{html.escape(a)}</p></details>" for q, a in t["faq"])
    body = f"""<main><div class="wrap"><section class="text">
<h2>{t["support_title"]}</h2><p class="lead">{html.escape(t["support_lead"])}</p>
<a class="btn" href="mailto:{SUPPORT_EMAIL}?subject=Bridge%20Con">{t["write"]}</a>
<div style="margin-top:28px">{faq}</div>
</section></div></main>"""
    return page(lang, "support", f"{t['support_title']} — Bridge Con", body, t["support_lead"])

if __name__ == "__main__":
    shutil.rmtree(OUT, ignore_errors=True)
    shutil.copytree(os.path.join(ROOT, "src"), OUT)
    open(os.path.join(OUT, "style.css"), "w").write(CSS.strip() + "\n")
    for lang, (_, prefix) in LANGS.items():
        d = os.path.join(OUT, prefix)
        os.makedirs(d, exist_ok=True)
        for name, fn in (("index.html", home), ("privacy.html", privacy), ("support.html", support)):
            open(os.path.join(d, name), "w", encoding="utf-8").write(fn(lang))
    print("built", sum(len(f) for _, _, f in os.walk(OUT)), "files into public/")
