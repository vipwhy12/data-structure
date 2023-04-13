//13. 몇 번째 행성인가요?
const planets = [
  "Mercury",
  "Venus",
  "Earth",
  "Mars",
  "Jupiter",
  "Saturn",
  "Uranus",
  "Neptune",
];

const readline = require("readline");

const reader = readline.createInterface({
  input: process.stdin,
});

reader.question("Which planet is it? ", (planet) => {
  console.log(planets[planet - 1]);
});
