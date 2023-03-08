

# input = 20


# def find_prime_list_under_number(number):
#     # 이 부분을 채워보세요!
#     prime_number_list = []   
    
#     for i in range(2, number):
#       number_list = []
      
#       for j in range(1, i):
#         if i % j == 0:
#           number_list.append(j) 
          
#       if len(number_list) == 1:
#         prime_number_list.append(i)
    
#     return prime_number_list


# result = find_prime_list_under_number(input)
# print(result)


input = 20


def find_prime_list_under_number(number):
    prime_list = []

    for n in range(2, number + 1):
        for i in prime_list:
            if n % i == 0 and i * i <= n:
                break
        else:
          prime_list.append(n)

    return prime_list


result = find_prime_list_under_number(input)
print(result)