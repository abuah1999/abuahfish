# abuahfish

> 'Sblood, you starveling, you elf-skin, you dried neat's tongue, you bull's pizzle, you stock-fish!  
>    **_1 Henry IV (2.4.227-9)_**

Abuahfish is a simple chess engine written in Python and using the python-chess library for move generation and validation. 
It is UCI-compatible and so can work on most standard chess GUIs. It also makes use of the cython language extension for speed as well
as various search-tree pruning methods. 

Play the latest version here: [https://lichess.org/@/abuah2022](https://lichess.org/@/abuah2022)

#### to install on your local machine

1. Switch to your directory of choice and clone the repo

```
mkdir abuahfish
cd abuahfish
git clone <url>
```

2. Use ```pyinstaller``` to generate the executable

```
pyinstaller -F abuahfish.py 

#This will generate an executable file in a folder called `dist`. 
#If you do not have pyinstaller on your system, you can install it like this:

pip install pyinstaller
```

3. Load the executable file into a chess GUI (e.g ArenaGUI, SCID vs PC) and have fun!

#### the name

"Abuahfish" is derived from the name of the most powerful open-source chess engine: Stockfish. One day AF will be strong enough to challenge the 
original fish, but it still has a long way to go...
