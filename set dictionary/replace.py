def search_replace(my_list, search, replace):
    
    new_list = [replace if element == search else element for element in my_list]
    return new_list
if __name__ == "__main__":
    my_list = [1, 2, 3, 4, 5, 4, 2, 1, 1, 4, 89]
    
    new_list = search_replace(my_list, 2, 89)
    
    print(new_list)  # Expected: [1, 89, 3, 4, 5, 4, 89, 1, 1, 4, 89]
    print(my_list)   # Expected: [1, 2, 3, 4, 5, 4, 2, 1, 1, 4, 89]
