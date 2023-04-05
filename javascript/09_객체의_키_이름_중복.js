//객체에서 키이름이 중복되었을 때,
//  마지막으로 선언된 값이 유효한 값으로 출력됩니다.

const d = {
  height: 180,
  weight: 78,
  weight: 84,
  temperature: 36,
  eyesight: 1,
};

console.log(d["weight"]);
