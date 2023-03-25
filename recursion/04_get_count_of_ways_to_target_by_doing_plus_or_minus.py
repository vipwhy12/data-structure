numbers = [1, 1, 1, 1, 1]
target_number = 3
result = 0


def get_count_of_ways_to_target_by_doing_plus_or_minus(current_index, current_sum ,array, target):
    global result
    if current_index == len(array):
      if target == current_sum :
        result += 1
      return 

    get_count_of_ways_to_target_by_doing_plus_or_minus(current_index + 1, current_sum + array[current_index], array , target)
    get_count_of_ways_to_target_by_doing_plus_or_minus(current_index + 1, current_sum - array[current_index], array , target)
    

get_count_of_ways_to_target_by_doing_plus_or_minus(0, 0, numbers, target_number)
print(result)
