def filter_and_modify(data_list, **kwargs):
    filtered_data = []
    
    for item in data_list:
        match = True
        for key, value in kwargs.items():
            if key in item:
                if item[key] != value:
                    match = False
                    break
        if match:
            modified_item = item.copy()
            for key, value in kwargs.items():
                modified_item[key] = value
            filtered_data.append(modified_item)
    
    return filtered_data

# Test data
data = [
    {"name": "Alice", "age": 30, "city": "New York"},
    {"name": "Bob", "age": 25, "city": "Los Angeles"},
    {"name": "Charlie", "age": 35, "city": "New York"},
    {"name": "Diana", "age": 30, "city": "Chicago"}
]

# Example call
filtered_data = filter_and_modify(data, age=30, city="New York", occupation="Engineer")

# Expected output
print(filtered_data)
# Output: [{'name': 'Alice', 'age': 30, 'city': 'New York', 'occupation': 'Engineer'}]
