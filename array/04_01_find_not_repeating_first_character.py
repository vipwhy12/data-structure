# Q. 다음과 같이 영어로 되어 있는 문자열이 있을 때, 이 문자열에서 반복되지 않는 첫번째 문자를 반환하시오. 만약 그런 문자가 없다면 _ 를 반환하시오.

def find_not_repeating_first_character(string):
  alphabet_array = [0] * 26
  alphabet_a = ord('a')
  
  #string 모든 숫자를 카운트
  for char in string:
    index = ord(char) - alphabet_a
    alphabet_array[index] += 1
  
  not_repeating_array = []
  
  for index in range(len(alphabet_array)):
    if alphabet_array[index] == 1 :
      temp = chr(index + alphabet_a)
      not_repeating_array.append(temp)
  
  for char in string:
    if char in not_repeating_array : 
      return char
  
  return "_"
  
  # if len(not_repeating_array) == 0:
  #   return "_"
  # else :
  #   index_array = []
  #   for i in range(len(not_repeating_array)):
  #     for j in range(len(string)): 
  #       if not_repeating_array[i] == string[j] : 
  #         index_array.append(j)

  #   index = min(index_array)
  #   return string[index]


result = find_not_repeating_first_character
print("정답 = d 현재 풀이 값 =", result("abadabac"))
print("정답 = c 현재 풀이 값 =", result("aabbcddd"))
print("정답 =_ 현재 풀이 값 =", result("aaaaaaaa"))