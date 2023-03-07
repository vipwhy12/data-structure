#Q. 정수를 입력 했을 때, 그 정수 이하의 소수를 모두 반환하시오. 
# 소수는 자신보다 작은 두 개의 자연수를 곱하여 만들 수 없는 1보다 큰 자연수이다.


input = 20


def find_prime_list_under_number(number):
    temp = number
    result = []
    
    for num in range(2, number) :
      if num == 2: 
        result.append(num)
      elif num % 2 != 0 and num % 3 != 0:
        result.append(num)
      
      
    return result


result = find_prime_list_under_number(input)
print(result)