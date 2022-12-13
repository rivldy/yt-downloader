
# YouTube Downloader

Adalah sebuah proyek yang memudahkan pengguna untuk mengunduh video maupun playlist YouTube.

## Instal Python

Hal pertama yang harus anda lakukan adalah menginstal Python di PC anda. Program ini membutuhkan Python versi 3.10.2 keatas.

Pertama, pergi ke [python.org](https://python.org). Setelah itu download sesuai sistem operasi pc anda.

Jalankan file executable seperti menginstal software, jangan lupa aktifkan Add to PATH.

Buka command prompt, dan ketik ```python --version```, jika terdapat tulisan ```Python [versi]``` maka anda sudah berhasil.

## Memulai

[Download](https://github.com/rivldy/yt-downloader/archive/refs/heads/main.zip) file YouTube Downloader terlebih dahulu, setelah itu extract file.

Setelah diekstrak, pergi ke direktori ekstrakan tersebut. Copy path direktorinya, buka command prompt lalu ketik ```cd [paste disini]``` tekan enter.

## Instal Library

Proyek ini dibuat  menggunakan library [Pytube](https://pypi.org/project/pytube/) dan [Click](https://pypi.org/project/click/). Jadi, anda harus menginstal kedua library ini.

Caranya adalah, ketik di cmd ```pip install -r requirements.txt``` tunggu hingga proses selesai.

Setelah memastikan tidak ada error, maka anda dapat memulai program dengan mengetik ```python main.py```

## Dokumentasi

Untuk mendownload sebuah video youtube :

```python main.py video [url]```

contoh : ```python main.py video https://www.youtube.com/watch?v=dQw4w9WgXcQ```

Untuk mendownload playlist youtube :

```python main.py playlist [url]```

contoh : ```python main.py playlist https://www.youtube.com/watch?v=qWoXr30nFu0&list=PLTT-pJu2_vXmRessfYoroUm-wlGwMcgOd```