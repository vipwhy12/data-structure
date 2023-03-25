# Q. 60에서 0까지 숫자를 출력하시오


for i in range(60, 0, -1):
  print(i)
  
# 재귀함수와 반복문

def count_down(number):
  if number < 0:
    return
  print(number) 
  count_down(number - 1)

  
count_down(60)