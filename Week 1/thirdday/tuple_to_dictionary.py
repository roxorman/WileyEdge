def list_of_tuples_to_dict(tuple_list):
    result_dict = {}
    for item in tuple_list:
        key, value = item
        result_dict[key] = value
    return result_dict

# Example usage
tuple_list = [("apple", 3), ("banana", 5), ("cherry", 2)]
result_dict = list_of_tuples_to_dict(tuple_list)
print(result_dict)





