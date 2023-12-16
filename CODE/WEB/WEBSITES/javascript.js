var n = 6;
var oddSum = 0;
var evenSum = 0;
var i = 1; 
for (let i = 1 ; i <= n; i++)
  if(i % 2 == 0){
    evenSum += i;
  } else {
    oddSum += i;
  }
  i++; 
console.log(oddSum, evenSum);