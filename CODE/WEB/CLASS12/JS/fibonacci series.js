// program to generate fibonacci series up to n terms

// take input from the user
var number = parseInt(prompt('Enter the number of terms: '));
let n1 = 0, n2 = 1, nextTerm;

for (let i = 1; i <= number; i++) {
    cdocument.writeln(n1);
    nextTerm = n1 + n2;
    n1 = n2;
    n2 = nextTerm;
}