from collections import Counter

X = int(input())
shoe_sizes = list(map(int, input().split()))
N = int(input())

shoe_counts = Counter(shoe_sizes)

total_earned = 0

for _ in range(N):
    customer_request = list(map(int, input().split()))
    desired_size = customer_request[0]
    price = customer_request[1]

    if shoe_counts[desired_size] > 0:
        total_earned += price
        shoe_counts[desired_size] -= 1

print(total_earned)
