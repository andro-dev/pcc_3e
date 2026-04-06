from pathlib import Path

file = "dummy.txt"
path = Path(file)
contents = path.read_text()
print(contents)

print("\nNow line by line")
lines = contents.splitlines()
[print(line) for line in lines]

print("\nNow changing Python to C language")
[print(line.replace("Python", "C Language")) for line in contents.splitlines()]
