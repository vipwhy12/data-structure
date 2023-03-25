finding_target = 14
finding_numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16]


def is_existing_target_number_sequential(target, array):
    test = len(array) // 2      
    
    for number in range(len(array)):
      if array[test] == target: 
        return True
      
      if array[test] < target :
        test = (len(array) + test) // 2
      elif array[test] > target :
        test = test // 2

    return False


result = is_existing_target_number_sequential(finding_target, finding_numbers)
print(result)  # True