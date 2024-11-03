#!/usr/bin/python3

def safe_print_list(my_list=[], x=0):
    """
    Prints x elements of a list safely without using len()
    Returns the real number of elements printed
    """
    count = 0
    try:
        for i in range(x):
            print(my_list[i], end="")
            count += 1
    except IndexError:
        pass
    print()
    return count

def sum_args(*args):
    """
    Sums up all arguments passed to the function
    """
    total = 0
    for arg in args:
        try:
            total += float(arg)
        except (TypeError, ValueError):
            continue
    return total

# Test cases for safe_print_list
if __name__ == "__main__":
    my_list = [1, 2, 3, 4, 5]

    # Test case 1: Print within list bounds
    nb_print = safe_print_list(my_list, 2)
    print("nb_print: {:d}".format(nb_print))

    # Test case 2: Print beyond list bounds
    nb_print = safe_print_list(my_list, 10)
    print("nb_print: {:d}".format(nb_print))

    # Test case 3: Print with mixed types
    mixed_list = [1, "Hello", 3, 4.5, {"key": "value"}, [1, 2]]
    nb_print = safe_print_list(mixed_list, 4)
    print("nb_print: {:d}".format(nb_print))

    # Test case 4: Empty list
    empty_list = []
    nb_print = safe_print_list(empty_list, 2)
    print("nb_print: {:d}".format(nb_print))

    # Test cases for sum_args
    print("\nTesting sum_args function:")
    print("Sum of integers:", sum_args(1, 2, 3, 4, 5))
    print("Sum with mixed types:", sum_args(1, "2", 3.5, "hello", 4))
    print("Sum with empty args:", sum_args())
    print("Sum with invalid numbers:", sum_args("hello", "world", [1, 2], {"a": 1}))