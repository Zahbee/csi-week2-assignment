def average(array):
    
    distinct_heights = set(array)
    
    #  the sum of the distinct heights.
    sum_of_distinct_heights = sum(distinct_heights)
    
    #  the total number of distinct heights.
    total_number_of_distinct_heights = len(distinct_heights)
    
    #  the average. Ensure division results in a float.
    # check if total_number_of_distinct_heights is not zero
    # to avoid ZeroDivisionError, though problem constraints (0 < N <= 100)
    # suggest N will always be at least 1, so distinct_heights won't be empty.
    if total_number_of_distinct_heights == 0:
        return 0.0 # Or handle as per problem's specific edge case if N could be 0
    
    avg = sum_of_distinct_heights / total_number_of_distinct_heights
    
    # Round the result to 3 decimal places.
    # The f-string formatting will handle the rounding for printing.
    return avg


if __name__ == '__main__':
    n = int(input())
    arr = list(map(int, input().split()))
    result = average(arr)
    print(result)
