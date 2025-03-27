def remove_duplicates(input_list):
    return list(dict.fromkeys(input_list))

# Example usage
if __name__ == "__main__":
    sample_list = [1, 2, 2, 8, 8, 3, 3, 4, 4, 5, 6, 6, 7]
    print("Original list:", sample_list)
    print("List after removing duplicates:", remove_duplicates(sample_list))