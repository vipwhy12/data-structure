finding_target = 14
finding_numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16]


def is_existing_target_number_binary(target, array):
    current_min = 0
    current_max = len(array)
    current_index = (current_max + current_min) // 2

    print(current_max)
    print(current_index)
    
    while current_min <= current_max:
      if array[current_index] == target:
        return True
      elif array[current_index] < target:
        current_min = current_index
      elif array[current_index] > target:
        current_max = current_index
        
      current_index = (current_max + current_min) // 2
      print(current_index)

    return False


result = is_existing_target_number_binary(finding_target, finding_numbers)
print(result)