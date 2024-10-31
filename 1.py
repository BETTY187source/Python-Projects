def string_to_length(strings):
    use_dict = {}
    for string in strings:
        use_dict[string] = len(string)
    return use_dict


strings = ["apple", "banana", "orange"]
print(string_to_length(strings)) 
