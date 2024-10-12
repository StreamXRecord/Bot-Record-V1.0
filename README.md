# Livestream Recording Bot

This bot allows you to record livestreams by providing a link. It supports various platforms that work with VLC player, such as MangoLive, BigoLive, PapayaLive, DreamLive, SugarLive, and others.

## Features:
- Records livestreams via link
- Captions host name and ID
- Auto splits video if size exceeds 2 GB
- Displays upload progress
- Supports multiple processing recording
- Stop Recording

## Configuration

Edit `configs.py` and replace it with your Telegram account credentials:

```python
class Config:
    # Required Variables
    BOT_TOKEN = "6974758906:AAFKfPsvOcmwYBxk2ClcGkZV2vTKWXddcbQ" #GET IT FROM @BOTFATHER
    API_ID = "25957266" #GET IT FROM my.telegram.org
    API_HASH = "e25868582faa883861842e3ea85cf60e" #GET IT FROM my.telegram.org
    ADMINISTRATORS = [5401929272] #GET IT FROM @getmyid_bot
    MAX_RECORDINGS = 20 #Maximal processing url for recording 
    SPLIT_DURATION = 1800 #Value duration Video will be splited as a seconds for example 1800 = 30 minutes and 3600 = 1 hour
    # Optional Variables
    CHANNEL_ID = -1001867625473 #GET IT FROM @showjsonbot
```

## Installation on VPS / RDP

1. Install necessary packages:
```sh
sudo apt install python3-pip && sudo apt install git
```

2. Clone the repository:
```sh
git clone https://github.com/IndraBagus0/StreamXRecord.git
```

3. Navigate to the cloned directory:
```sh
cd StreamXRecord
```

```sh
apt-get install zip unzip && apt-get install ffmpeg
```

#####
Make sure you install this in enviroment
```sh
sudo apt install python3-venv
```
```sh
python3 -m venv venv
source venv/bin/activate
pip3 install -r requirements.txt
```


## Running the Bot
### Adjust MAX_RECORDINGS in cofigs.py to suit your VPS capabilities:
- With a VPS of 4 GB RAM, you can run 8 processing url for recordings
```sh
nohup python3 -u main.py &

```


# Happy Recording✌️