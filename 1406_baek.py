import sys


def cursor_left():
    if not sentence1:
        pass
    else:
        sentence2.append(sentence1.pop(-1))


def cursor_right():
    if not sentence2:
        pass
    else:
        sentence1.append(sentence2.pop(-1))


def left_delete():
    if not sentence1:
        pass
    else:
        sentence1.pop(-1)


def include(letter):
    sentence1.append(letter)


letter = sys.stdin.readline().strip()
sentence1 = list(letter)
sentence2 = []

for i in range(int(sys.stdin.readline())):
    cmd = sys.stdin.readline().split()
    if cmd[0] == 'L':
        cursor_left()
        continue
    if cmd[0] == 'D':
        cursor_right()
        continue
    if cmd[0] == 'B':
        left_delete()
        continue
    if cmd[0] == 'P':
        include(cmd[1])
        continue
    else:
        break

print(''.join(sentence1 + list(reversed(sentence2))))
