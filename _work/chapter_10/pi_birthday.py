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

birthday = input("Enter your BD in 'mmddyy' format: \n--> ")
print("yor entered:" ,birthday)

idx_found = pi_line.index(birthday
                          )
if birthday in pi_line:
    print(f"\nYour birthday appears at location {idx_found:,} in first million digits of pi ")
else:
    print("\nYour birthday doesn't appear in first million digits of pi ")


# for line in lines:
#     pi_line += line

print(f"PI with 52 decimals precision: {pi_line[:52]}")
