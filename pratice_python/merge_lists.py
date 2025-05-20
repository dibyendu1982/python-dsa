# Merge two lists by alternating elements from each.

first_list = [1,3,5,9, 11, 13]

second_list = [2,4,6,8,10]

result = []

def merge_list(merge1:list, merge2: list):
    result = []  # Create a new list for each call
    smaller_length = len(merge1) if len(merge1) < len(merge2) else len(merge2)
    
    # Merge elements up to the length of the smaller list
    for i in range(0, smaller_length):       
        result.append(merge1[i])
        result.append(merge2[i])
    
    # Add remaining elements from the longer list
    if len(merge1) > smaller_length:
        result.extend(merge1[smaller_length:])
    elif len(merge2) > smaller_length:
        result.extend(merge2[smaller_length:])
       
    print(result)
    return result  # Return the result for potential further use
    
    
merge_list(first_list, second_list)