from pathlib import Path

filenames = ["romeo_and_juliet.txt", "pride_and_prejudice.txt", "little_women.txt", "moby_dick.txt"]

for filename in filenames:
    path = Path(f"text_files/{filename}")

    try:
        contents = path.read_text("utf-8")
    except:
        pass
    else:
        print(contents.lower().count('cow '))