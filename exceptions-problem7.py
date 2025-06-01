T = int(input())

for _ in range(T):
    try:
        a_str, b_str = input().split()
        a = int(a_str)
        b = int(b_str)
        print(a // b)
    except ValueError as e:
        print(f"Error Code: {e}")
    except ZeroDivisionError as e:
        print(f"Error Code: {e}")
