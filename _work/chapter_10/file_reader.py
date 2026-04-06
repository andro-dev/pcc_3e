from pathlib import Path

path = Path(
    "/home/andrew/projects/python/python_crash_course/_work/chapter_10/pi_million_digits.txt"
)
contents = path.read_text().rstrip()
# print(contents)
print("contents string length:", len(contents))

lines = contents.splitlines()
# [print(i, ":", line.strip()) for i, line in enumerate(lines, 1)]

pi_line = "".join([line.strip() for line in lines])


# for line in lines:
#     pi_line += line

print(f"{pi_line[:52]}")
