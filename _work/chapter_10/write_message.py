from pathlib import Path

path = Path("programming.txt")
path.write_text("I love programming")
path.write_text(" ".join(list(map(str, [10, 20, 30])))) # string_array = list(map(str, numeric_array))
