import sys


def push(n):
    stack.append(n)


def pop():
    if not stack:
        print(-1)
    else:
        sys.stdout.write(stack.pop(0) + '\n')


def size():
    print(len(stack))


def empty():
    if not stack:
        print(1)
    else:
        print(0)


def front():
    if not stack:
        print(-1)
    else:
        sys.stdout.write(stack[0] + '\n')


def back():
    if not stack:
        print(-1)
    else:
        sys.stdout.write(stack[-1] + '\n')



stack = []
n = eval(sys.stdin.readline())
for i in range(n):
    cmd = sys.stdin.readline().split()
    if cmd[0] == 'push':
        push(cmd[1])
    elif cmd[0] == 'pop':
        pop()
    elif cmd[0] == 'size':
        size()
    elif cmd[0] == 'empty':
        empty()
    elif cmd[0] == 'front':
        front()
    elif cmd[0] == 'back':
        back()
