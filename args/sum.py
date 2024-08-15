def sum_args(*args):
    total = 0
    for num in args:
        total += num
    return total

# Test cases
print(sum_args(1, 2, 3))            # Output: 6
print(sum_args(10, 20, 30, 40))     # Output: 100
print(sum_args())                   # Output: 0
print(sum_args(5.5, 4.5, -10))      # Output: 0