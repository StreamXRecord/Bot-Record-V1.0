# Livestream Recording Bot

Bot ini memungkinkan Anda merekam siaran langsung dengan memberikan tautan. Bot ini mendukung berbagai platform yang kompatibel dengan VLC player, seperti MangoLive, BigoLive, PapayaLive, DreamLive, SugarLive, dan lainnya.

## Features:
- Merekam livestream melalui tautan ✅
- Captions host name and ID❌ (Hanya Tersedia di bot v 2.0)
- Memotong video secara otomatis jika ukuran melebihi 2 GB ✅
- Displays upload progress ✅
- Mendukung rekaman multi-proses ✅
- Stop Recording ✅

## Configuration

Edit `configs.py` and replace it with your Telegram account credentials:

```python
class Config:
    # Variabel yang Diperlukan
    BOT_TOKEN = "GANTI_INI" #DAPATKAN DARI @BOTFATHER
    API_ID = "GANTI_INI" #DAPATKAN DARI my.telegram.org
    API_HASH = "GANTI_INI" #DAPATKAN DARI my.telegram.org
    ADMINISTRATORS = [GANTI_INI] #DAPATKAN DARI @getmyid_bot
    MAX_RECORDINGS = 20 #Jumlah maksimal URL yang diproses untuk rekaman
    SPLIT_DURATION = 1800 #Durasi pemotongan video dalam detik, misalnya 1800 = 30 menit dan 3600 = 1 jam
    # Variabel Opsional
    CHANNEL_ID = -1001867625473 #DAPATKAN DARI @showjsonbot
```

## Installation on VPS / RDP

1. Install necessary packages:
```sh
sudo apt install python3-pip && sudo apt install git
```

2. Clone the repository:
```sh
git clone https://github.com/StreamXRecord/Bot-Record-V1.0.git && StreamXRecord/
```

3. Navigate to the cloned directory:
```sh
cd StreamXRecord
```

```sh
apt-get install ffmpeg
```

#####
Pastikan Anda menginstal ini di lingkungan virtual:
```sh
sudo apt install python3-venv
```
```sh
python3 -m venv venv
source venv/bin/activate
pip3 install -r requirements.txt
```


## Running the Bot
### Sesuaikan MAX_RECORDINGS di configs.py dengan kemampuan VPS Anda
- Dengan VPS 4 GB RAM, Anda dapat menjalankan 8 URL untuk rekaman secara bersamaan
```sh
nohup python3 -u main.pyc &

```


# Happy Recording✌️
