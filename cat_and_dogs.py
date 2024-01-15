from pathlib import Path

filenames = ["cats.txt", "dogs.txt"]

for filename in filenames:
    path = Path(f"text_files/{filename}")
    try:
        contents = path.read_text()
    except:
        pass
    else:
        print(contents)