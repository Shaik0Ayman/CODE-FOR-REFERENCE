let e, x, d = 0;
let b = prompt("Enter a number");
x=b;

while (x > 0) {
  e = x % 10;
  x = parseInt(x/10);
  d = d + (e*e*e);
}

if (b==d)
   document.writeln("given number is an armstrong number");
else
   document.writeln("given number is not an armstrong number")