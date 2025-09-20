def sum_n(n):
    if n == 0:      # base case
        return 0
    return n + sum_n(n-1)   # recursive call

# Example usage
print(sum_n(5))
