//https://school.programmers.co.kr/learn/courses/30/lessons/181950?language=javascript

const readline = require("readline");
const rl = readline.createInterface({
  input: process.stdin,
  output: process.stdout,
});

let input = [];

rl.on("line", function (line) {
  input = line.split(" ");
}).on("close", function () {
  answer = "";
  str = input[0];
  n = Number(input[1]);
  for (i = 0; i < n; i++) {
    answer = str + answer;
  }
  console.log(answer);
});
