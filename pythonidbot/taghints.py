"""Thank you https://github.com/python-telegram-bot/rules-bot/blob/master/components/taghints.py"""
from collections import namedtuple

from telegram import InlineKeyboardButton, InlineKeyboardMarkup, ParseMode, Update
from telegram.error import BadRequest
from telegram.ext import CommandHandler, Filters, MessageHandler, CallbackContext

from pythonidbot.utils.helpers import build_menu

HINTS = {
    "#aturan": {
        "message": "{query} Silahkan baca Aturan Grup Telegram PythonID di https://pythonid.github.io/aturan.html",
        "default": "Hai.",
        "help": "Kirim peraturan group",
    },
    "#private": {
        "message": "Tolong jangan spam group dengan {query}, dan sebaiknya "
        "obrolan pribadi dengan saya. Terimakasih, anggota lain akan menghargainya 😊",
        "default": "pencarian atau perintah",
        "buttons": [
            {
                "text": "🤖 Ke obrolan pribadi",
                "url": "https://t.me/pitonidbot",
            }
        ],
        "help": "Beri tahu anggota untuk berhenti mengirim spam dan beralih ke obrolan pribadi",
    },
    "#meta": {
        "message": """No need for meta questions. Just ask! 🤗
<i>"Has anyone done .. before?"</i>
Probably. <b>Just ask your question and somebody will help!</b> 
        """,
        "help": "Show our stance on meta-questions",
    },
    "#belajar": {
        "message": "{query}\nKami sudah mengumpulkan rekomendasi sumber belajar di https://pythonid.github.io/belajar.html",
        "help": "Rekomendasi Anggota Untuk Mulai Belajar Python",
        "default": "Oh, Hei! Rupanya ada yang ingin bergabung dengan komunitas pengembang python ❤️ ",
    },
    "#bertanya": {
        "message": "{query} Agar kami tidak segan menjawab pertanyaan anda silahkan mohon dibaca Bertanya Yang Baik di https://pythonid.github.io/bertanya.html",
        "help": "Bagaimana Bertanya Yang Baik",
        "default": "Hei.",
    },
    "#pastebin": {
        "message": """{query} Harap poskan kode menggunakan pastebin, bukan sebagai teks biasa atau screenshot. https://pastebin.com/ adalah yang paling populer, tetapi ada banyak alternatif di luar sana. Tentu saja, untuk potongan yang sangat pendek, teks sudah cukup. Harap setidaknya memformatnya sebagai monospace. Terimakasih""",
        "help": "Beri tahu pengguna agar tidak mengirim kode sebagai teks atau gambar.",
        "default": "Hei.",
    },
    "#postganda": {
        "message": """{query} Please don't double post. Questions usually are on-topic only in one of the two groups anyway.""",
        "help": "Beri tahu pengguna agar tidak mengirim pertanyaan yang sama berkali-kali",
        "default": "Hey.",
    },
    "#xy": {
        "message": """{query} Masalah XY menanyakan tentang solusi yang Anda coba daripada masalah Anda yang sebenarnya. Hal ini menyebabkan pemborosan waktu dan energi yang sangat besar, baik di pihak orang yang meminta bantuan, maupun di pihak mereka yang memberikan bantuan..""",
        "default": "Hei. Untuk apa sebenarnya Anda menginginkan ini?",
        "help": "Tanyakan kepada pengguna tentang kasus penggunaan yang sebenarnya.",
    },
    "#janganping": {
        "message": """{query} Harap hanya sebutkan atau balas pengguna secara langsung jika Anda menindaklanjuti percakapan dengan mereka. Jika tidak, ajukan pertanyaan Anda dan tunggu apakah seseorang memiliki solusi untuk Anda - begitulah cara kerja grup ini 😉 Perhatikan juga bahwa tag <code> @admin </code> hanya digunakan untuk melaporkan spam atau penyalahgunaan!""",
        "default": "Hei.",
        "help": "Beri tahu pengguna untuk tidak melakukan ping secara acak ke Anda.",
    },
}


def list_available_hints(update: Update, context: CallbackContext):
    message = "Anda dapat menggunakan hashtag berikut untuk memandu anggota baru:\n\n"
    message += "\n".join(
        "🗣 {tag} ➖ {help}".format(tag=k, help=v["help"]) for k, v in HINTS.items()
    )
    message += "\n\nPastikan untuk membalas pesan lain, jadi saya tahu siapa yang harus dirujuk."
    update.effective_message.reply_text(
        message, parse_mode=ParseMode.HTML, disable_web_page_preview=True
    )


Hint = namedtuple("Hint", "help, msg, reply_markup")


def get_hints(query):
    results = {}
    hashtag, _, query = query.partition(" ")

    for k, v in sorted(HINTS.items()):
        if k.lower().startswith(hashtag.lower()):
            reply_markup = (
                InlineKeyboardMarkup(
                    build_menu(
                        [
                            InlineKeyboardButton(
                                **{k: v.format(query=query) for k, v in b.items()}
                            )
                            for b in v["buttons"]
                        ],
                        1,
                    )
                )
                if "buttons" in v
                else None
            )

            msg = v["message"].format(query=query if query else v.get("default", ""))

            results[k] = Hint(
                help=v.get("help", ""), msg=msg, reply_markup=reply_markup
            )

    return results


def hint_handler(update: Update, context: CallbackContext):
    reply_to = update.message.reply_to_message

    hint = get_hints(update.message.text).popitem()[1]

    if hint is not None:
        update.effective_message.reply_text(
            hint.msg,
            reply_markup=hint.reply_markup,
            reply_to_message_id=reply_to.message_id if reply_to else None,
            parse_mode=ParseMode.HTML,
            disable_web_page_preview=True,
        )
        try:
            update.effective_message.delete()
        except BadRequest:
            pass


def register(dispatcher):
    dispatcher.add_handler(
        MessageHandler(
            Filters.regex(rf'(?i){"|".join(HINTS.keys())}'),
            hint_handler,
            run_async=True,
        )
    )
    dispatcher.add_handler(
        CommandHandler(("hints", "listhints"), list_available_hints, run_async=True)
    )
