# Playing Minecraft Handless

## Description
This project brings a new gaming experience, substituting hand commands with voice and gesture commands. 

## Installation
To install the required Python dependencies, run the following commands:

```bash
sudo apt install python3.10-venv
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt --no-cache-dir
```
The flag '--no-cache-dir' prevents the process to be killed if running out of RAM.

Note that this setup has been tested on Linux Mint 21.3 (which is a Debian based distribution), Windows 10 & 11.

## Usage
Run Minecraft on any world. Once inside the game, run either **main_for_GT.py** to play with gaze-tracking or **main_for_HT.py** to play with head-tracking.

When you are done playing, select the running terminal and `ctrl + c` twice to stop the process.

## Authors
Jiaxin LI, Pierre Masserey & Christian Galley
