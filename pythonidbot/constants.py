HINTS = {
    "#welcome": {
        "key": "#welcome",
        "message": """{query}\nSilahkan baca Aturan Group PythonID di https://pythonid.github.io/aturan.html\nRekomendasi sumber belajar di https://pythonid.github.io/belajar.html\nPanduan Bertanya Yang Baik di https://pythonid.github.io/bertanya.html""",
        "default": "Selamat datang.",
        "help": "Sambut anggota baru",
    },
    "#aturan": {
        "key": "#aturan",
        "message": "{query}\nSilahkan baca Aturan Group PythonID di https://pythonid.github.io/aturan.html",
        "default": "Halo.",
        "help": "Kirim peraturan group",
    },
    "#private": {
        "key": "#private",
        "message": """Tolong jangan spam group dengan {query}, dan sebaiknya chat pribadi dengan saya. Terimakasih, anggota lain akan menghargainya 😊""",
        "default": "pencarian atau perintah",
        "buttons": [
            {
                "text": "🤖 Ke chat pribadi",
                "url": "https://t.me/pitonidbot",
            }
        ],
        "help": "Beri tahu untuk berhenti mengirim spam dan beralih ke chat pribadi",
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
        "default": "Oh, hai! Rupanya ada yang ingin bergabung dengan komunitas pengembang python ❤️ ",
    },
    "#bertanya": {
        "key": "#bertanya",
        "message": "{query}\nAgar kami tidak segan menjawab pertanyaan anda, silahkan dibaca Bertanya Yang Baik di https://pythonid.github.io/bertanya.html",
        "help": "Bagaimana Bertanya Yang Baik",
        "default": "Halo",
    },
    "#pastebin": {
        "key": "#pastebin",
        "message": """{query}\nSebaiknya kirimkan kode menggunakan pastebin. https://pastebin.com/ adalah yang paling populer, tetapi ada banyak alternatif di luar sana. Tentu saja, untuk potongan kode yang sangat pendek, teks sudah cukup. Atau setidaknya format teks sebagai monospace. Terimakasih""",
        "help": "Beri tahu pengguna agar tidak mengirim kode sebagai teks atau gambar.",
        "default": "Halo",
    },
    "#postganda": {
        "key": "#postganda",
        "message": """{query}\nTolong untuk tidak mengirim pesan ganda.""",
        "help": "Beri tahu pengguna agar tidak mengirim pertanyaan yang sama berkali-kali",
        "default": "Halo",
    },
    "#xy": {
        "key": "#xy",
        "message": """{query}\nMasalah XY menanyakan tentang solusi yang Anda coba daripada masalah Anda yang sebenarnya. Hal ini menyebabkan pemborosan waktu dan energi yang sangat besar, baik di pihak orang yang meminta bantuan, maupun di pihak mereka yang memberikan bantuan..""",
        "default": "Halo. Untuk apa sebenarnya Anda menginginkan ini?",
        "help": "Tanyakan kepada pengguna tentang kasus penggunaan yang sebenarnya.",
    },
    "#janganping": {
        "key": "#janganping",
        "message": """{query}\nHarap hanya sebutkan atau balas pengguna secara langsung jika Anda menindaklanjuti percakapan dengan mereka. Jika tidak, ajukan pertanyaan Anda dan tunggu apakah seseorang memiliki solusi untuk Anda - begitulah cara kerja grup ini 😉\nPerhatikan juga bahwa tag <code> @admin </code> hanya digunakan untuk melaporkan spam atau penyalahgunaan!""",
        "default": "Halo.",
        "help": "Beri tahu pengguna untuk tidak melakukan ping secara acak ke Anda.",
    },
    "#screenshot": {
        "key": "#screenshot",
        "message": """{query}\nUntuk screenshot ke telegram, di laptop/pc tekan Prt Scr di layar yang ingin discreenshot, kemudian buka aplikasi telegram (https://web.telegram.org/) dan paste (ctrl + v) ke chat yang dituju.""",
        "default": "Halo.",
        "help": "Beri tahu cara screenshot yang benar.",
    },
}
