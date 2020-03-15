def get_key(val):
    for key, value in old_enc.items():
        if val == key:
            return value

    for key, value in old_enc_capital.items():
        if val == key:
            return value

    for key, value in new_enc.items():
        if val == key:
            return value

    for key, value in new_enc_capital.items():
        if val == key:
            return value

    for key, value in space.items():
        if val == key:
            return value

    for key, value in numbers.items():
        if val == key:
            return value


a = input()

old_enc = dict([(chr(i), chr(i+13)) for i in range(97, 97+13)])
old_enc_capital = dict([(chr(i), chr(i+13)) for i in range(65, 65+13)])

new_enc = dict([(value, key) for key, value in old_enc.items()])
new_enc_capital = dict([(value, key) for key, value in old_enc_capital.items()])

space = {" ": " "}
numbers = {"1": "1", "2": "2", "3": "3", "4": "4", "5": "5", "6": "6", "7": "7", "8": "8", "9": "9", }

for s in a:
    print(get_key(s), end='')
