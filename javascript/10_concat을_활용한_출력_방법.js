//10. 2019/04/26 11:34:27 다음과 같이 출력할 수 있게 하세요.
//concat() 메서드는 매개변수로 전달된 문자열을 메서드를 호출한 문자열에 붙여 새로운 문자열로 반환합니다.

const year = "2019";
const month = "04";
const day = "26";
const hour = "11";
const minute = "34";
const second = "27";

const result = year.concat(
  "/",
  month,
  "/",
  day,
  " ",
  day,
  ":",
  hour,
  ":",
  minute,
  ":",
  second
);

console.log(result);
