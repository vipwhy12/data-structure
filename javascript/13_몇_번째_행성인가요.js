//13. 몇 번째 행성인가요?

const solarSystem = [
  "수성",
  "금성",
  "지구",
  "화성",
  "목성",
  "토성",
  "천왕성",
  "해왕성",
];
const input = 1;

for (index in solarSystem) {
  if (input == index + 1) {
    console.log(solarSystem[index]);
  }
}
