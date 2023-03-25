# Q. 다음과 같이 숫자로 이루어진 배열이 있을 때, 이 배열 내에서 가장 큰 수를 반환하시오.
#  A. 파이썬의 max() 함수를 사용하게 되면 시간복잡도가 log(N)이다.
def find_max_num(array):
    max_num = 0
    for index in range(len(array)):
        if max_num < array[index] :
            max_num = array[index]
    
    return max_num
        


print("정답 = 6 / 현재 풀이 값 = ", find_max_num([3, 5, 6, 1, 2, 4]))
print("정답 = 6 / 현재 풀이 값 = ", find_max_num([6, 6, 6]))
print("정답 = 1888 / 현재 풀이 값 = ", find_max_num([6, 9, 2, 7, 1888]))