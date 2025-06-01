n = int(input())
s = set(map(int, input().split()))
N = int(input())

for _ in range(N):
    command_parts = input().split()
    command = command_parts[0]

    if command == "pop":
        if s:
            s.pop()
    elif command == "remove":
        value = int(command_parts[1])
        try:
            s.remove(value)
        except KeyError:
            pass
    elif command == "discard":
        value = int(command_parts[1])
        s.discard(value)

print(sum(s))
