# Q. 다음과 같이 영어로 되어 있는 문자열이 있을 때, 
#    이 문자열에서 반복되지 않는 첫번째 문자를 반환하시오. 
#    만약 그런 문자가 없다면 _ 를 반환하시오.

input = "abadabac"

def find_not_repeating_first_character(string):
    test = []

    for i in range(len(string)):
        check_word = string[i]
        count = 0
        if check_word not in test :
            for j in range(i+1, len(string)):
                if check_word == string[j]:
                    count += 1
            if count == 0 :
                return check_word
            else :
                test.append(check_word)
        
    return "_"

result = find_not_repeating_first_character
print("정답 = d 현재 풀이 값 =", result("abadabac"))
print("정답 = c 현재 풀이 값 =", result("aabbcddd"))
print("정답 =_ 현재 풀이 값 =", result("aaaaaaaa"))