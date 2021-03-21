HINTS = {
    "#aturan": {
        "key": "#aturan",
        "message": "{query} Silahkan baca Aturan Grup Telegram PythonID di https://pythonid.github.io/aturan.html",
        "default": "Hai.",
        "help": "Kirim peraturan group",
    },
    "#private": {
        "key": "#private",
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
        "key": "#meta",
        "message": """Tidak perlu pertanyaan meta. Tanya saja! 🤗
<i>"Apakah ada yang melakukannya .. sebelumnya?"</i>
Mungkin. <b>Ajukan saja pertanyaan Anda dan seseorang akan membantu!</b> 
        """,
        "help": "Tunjukkan pendirian kami pada pertanyaan meta",
    },
    "#belajar": {
        "key": "#belajar",
        "message": "{query}\nKami sudah mengumpulkan rekomendasi sumber belajar di https://pythonid.github.io/belajar.html",
        "help": "Rekomendasi Anggota Untuk Mulai Belajar Python",
        "default": "Oh, Hei! Rupanya ada yang ingin bergabung dengan komunitas pengembang python ❤️ ",
    },
    "#bertanya": {
        "key": "#bertanya",
        "message": "{query} Agar kami tidak segan menjawab pertanyaan anda silahkan mohon dibaca Bertanya Yang Baik di https://pythonid.github.io/bertanya.html",
        "help": "Bagaimana Bertanya Yang Baik",
        "default": "Hei.",
    },
    "#pastebin": {
        "key": "#pastebin",
        "message": """{query} Harap poskan kode menggunakan pastebin, bukan sebagai teks biasa atau screenshot. https://pastebin.com/ adalah yang paling populer, tetapi ada banyak alternatif di luar sana. Tentu saja, untuk potongan yang sangat pendek, teks sudah cukup. Harap setidaknya memformatnya sebagai monospace. Terimakasih""",
        "help": "Beri tahu pengguna agar tidak mengirim kode sebagai teks atau gambar.",
        "default": "Hei.",
    },
    "#postganda": {
        "key": "#postganda",
        "message": """{query} Please don't double post. Questions usually are on-topic only in one of the two groups anyway.""",
        "help": "Beri tahu pengguna agar tidak mengirim pertanyaan yang sama berkali-kali",
        "default": "Hey.",
    },
    "#xy": {
        "key": "#xy",
        "message": """{query} Masalah XY menanyakan tentang solusi yang Anda coba daripada masalah Anda yang sebenarnya. Hal ini menyebabkan pemborosan waktu dan energi yang sangat besar, baik di pihak orang yang meminta bantuan, maupun di pihak mereka yang memberikan bantuan..""",
        "default": "Hei. Untuk apa sebenarnya Anda menginginkan ini?",
        "help": "Tanyakan kepada pengguna tentang kasus penggunaan yang sebenarnya.",
    },
    "#janganping": {
        "key": "#janganping",
        "message": """{query} Harap hanya sebutkan atau balas pengguna secara langsung jika Anda menindaklanjuti percakapan dengan mereka. Jika tidak, ajukan pertanyaan Anda dan tunggu apakah seseorang memiliki solusi untuk Anda - begitulah cara kerja grup ini 😉 Perhatikan juga bahwa tag <code> @admin </code> hanya digunakan untuk melaporkan spam atau penyalahgunaan!""",
        "default": "Hei.",
        "help": "Beri tahu pengguna untuk tidak melakukan ping secara acak ke Anda.",
    },
}
