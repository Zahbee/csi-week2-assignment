def merge_the_tools(string, k):
    n = len(string)
    num_substrings = n // k

    for i in range(num_substrings):
        substring = string[i * k : (i + 1) * k]
        
        seen_chars = ""
        for char in substring:
            if char not in seen_chars:
                seen_chars += char
        print(seen_chars)

if __name__ == '__main__':
    string, k = input(), int(input())
    merge_the_tools(string, k)
