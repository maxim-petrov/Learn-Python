from pathlib import Path

name = input("Please, write your name: ")

path = Path("text_files/guest.txt")
path.write_text(name)