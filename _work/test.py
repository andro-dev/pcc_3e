# l1 =['anton',
#                 'julia',
#                 'kate',
#                 'sara',
#                 'nata',
#                 'sergio'
#                 ]

# for person in l1:
#     print(f"hello, {person} 👋 👋 👋")

d = {0: 'polkovniju', 100: 'nikto', 200: 'ne', 2: 'pishet'}

new_d = {i: v for i, (_, v) in enumerate(d.items())}

print(new_d)

d = {i: v for i, (_, v) in enumerate(d.items())}
print(d)
