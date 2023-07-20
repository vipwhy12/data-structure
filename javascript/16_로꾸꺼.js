const strTest = "거꾸로";

/*
 * split() 메서드는 문자열을 배열로 만들어 반환하고,
 * reverse() 메서드는 배열의 순서를 반전하며,
 * join() 메서드는 원소를 모두 붙여 문자열로 반환합니다.
 */
const answer1 = strTest.split("").reverse().join("");
console.log(answer1);

let answer2 = "";
for (char of strTest) {
  answer2 += char;
}

console.log(answer2);
