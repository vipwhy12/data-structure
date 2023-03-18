input = "토마토"

number = 0

def is_palindrome(string):
  # 첫글자와 마지막 글자를 비교한다 
  if len(string) == 1:
    return True
  
  if string[0] == string[-1]:
    n = len(string) - 1 
    string = string[1:n]
    return is_palindrome(string)
  
  else :
    return False
  


print(is_palindrome(input))