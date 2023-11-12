## Gilgamesh Bot
![build](https://img.shields.io/appveyor/build/AidenBeresford/gilgamesh-discord)

Gilgamesh Bot is an open-source Python discord bot written using the pycord wrapper.

### How to Run

#### Windows

- Install the latest version of Python 3
- Install pip
  - Run `pip --version` in the command prompt to check if pip is installed.
- Run `pip install py-cord` in the command prompt
- Create a file named "token" in the same folder as main.py and paste your bots token inside
- Open command prompt in the folder with main.py
- Run `python main.py` in the command prompt

#### Linux

- Depending on your distro, python3 may come preinstalled
  - Run `$ python3 --version` in your terminal to check.
  - If python3 is not installed, run `$ sudo apt-get install python3`
  - If you're using a different package manager, replace `apt-get` with whatever you use
- Do the above steps with pip instead of python3
- Run `$ pip install py-cord`
- Navigate to the directory with main.py
  - Run `$ cat > token` in the terminal, and then paste your bots token in the first line
  - Run `$ python3 main.py` in the terminal

### Features

- Command cogs that can be easily disabled and enabled by even the Python illiterate.
- Highly customizable and easily tweaked command cogs.
- Moderation commands for quick server management.
- Multipurpose `/role` command, which offers a more modular way to mute members.
- Miscellaneous functions, i.e. rolling dice.
- Four Job Fiesta job generation (For the few Final Fantasy V fans).

#### Wishlist

- More fun commands.
- More moderation commands.
- Improved Four Job Fiesta cog.
- UI that selects active cogs.

