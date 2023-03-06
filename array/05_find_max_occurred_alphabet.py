def find_max_occurred_alphabet(string):
    alphabet_array = [0] * 26
    alphabet_a = ord('a')
    
    string_lower = string.lower()
    
    # 배열을 돌아 count     
    for char in string :
        if char != " " :
            index = ord(char) - alphabet_a
            alphabet_array[index] += 1  
            
    # count 된 배열에서 가장 큰 값의 인덱스 번호 찾기 
    max_index = 0
    max_alphabet = 0
    
    for index in range(len(alphabet_array)) :
        if alphabet_array[index] > max_alphabet:
            max_index = index
            max_alphabet = alphabet_array[index]

    max_index = max_index + ord('a')

    return chr(max_index)


result = find_max_occurred_alphabet
print("정답 = a 현재 풀이 값 =", result("Hello my name is sparta"))
print("정답 = a 현재 풀이 값 =", result("Sparta coding club"))
print("정답 = s 현재 풀이 값 =", result("best of best sparta"))