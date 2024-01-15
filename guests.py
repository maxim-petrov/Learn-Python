from pathlib import Path

names = []
while True:
    text = input("Please, write your name: ")
    if text == 'q':
        break

    names.append(text)

content = ''
for name in names:
    content += f"{name} \n"

path = Path("text_files/guest_book.txt")
path.write_text(content)