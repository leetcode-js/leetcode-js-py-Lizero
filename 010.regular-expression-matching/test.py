memo = []
console.log(memo)
for (i = 1; i < 4; i++) {
  for (j = 1; j < 3; j++) {
    memo[i, j] = i * j
    console.log(memo)
  }
}