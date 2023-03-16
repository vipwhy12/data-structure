#정수형 배열  

def int_array(array):

  if len(array) < 2 :
    return "정수형 배열의 크기가 올바르지 않습니다."
  
  else :
    array = sorted(array)
    
    if (array[0] * array[1] >  array[-1] * array[-2]):
      return array[0], array[1]
    else :
      return array[-1] , array[-2]
        


print("정답 = -6, -7 / 현재 풀이 값 = ", int_array([4, -6, 3, 2, -7]))
print("정답 = -6, -7 / 현재 풀이 값 = ", int_array([3, 8, -2, -4, 7, -9]))