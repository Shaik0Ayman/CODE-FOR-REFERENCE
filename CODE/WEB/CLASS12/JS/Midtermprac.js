//1. program to print prime numbers between the two numbers

lowerNumber = parseInt(prompt('Enter lower number: '))
higherNumber = parseInt(prompt('Enter higher number: '));

for (let i = lowerNumber; i <= higherNumber; i++) {
    let flag = 0;

    for (let j = 2; j < i; j++) {
        if (i % j == 0) {
            flag = 1;
            break;
        }
    }

    if (i > 1 && flag == 0) {
        document.write(i);
    }
}

//2.  program to check an Armstrong number of three digits

let sum = 0;
var number = prompt('Enter a three-digit positive integer: ');
let temp = number;
while (temp > 0) {
    let remainder = temp % 10;
    sum += remainder * remainder * remainder;
    temp = parseInt(temp / 10); 
}
if (sum == number) {
    document.write(`${number} is an Armstrong number`);
}
else {
    document.write(`${number} is not an Armstrong number.`);
}

//3.  program to find the factorial of a number

const number = parseInt(prompt('Enter a positive integer: '));
if (number < 0) {
    document.write('Error! Factorial for negative number does not exist.');
}
else if (number === 0) {
    document.write(`The factorial of ${number} is 1.`);
}
else {
    let fact = 1;
    for (i = 1; i <= number; i++) 
    {
        fact *= i;
    }
    document.write(`The factorial of ${number} is ${fact}.`);
}

// program to generate fibonacci series up to n terms
const number = parseInt(prompt('Enter the number of terms: '));
let n1 = 0, n2 = 1, nextTerm;
document.write('Fibonacci Series:');
for (let i = 1; i <= number; i++) {
    document.write(n1);
    nextTerm = n1 + n2;
    n1 = n2;
    n2 = nextTerm;
}


// program to find the factors of an integer

const num = prompt('Enter a positive number: ');
document.write(`The factors of ${num} is:`);
for(let i = 1; i <= num; i++) {
    if(num % i == 0) {
        document.write(i);
    }
}



// program to check the number of occurrence of a character

function countString(str, letter) {
    let count = 0;
    for (let i = 0; i < str.length; i++) 
  {
       if (str.charAt(i) == letter) {
            count += 1;
        }
    }
    return count;
}

const string = prompt('Enter a string: ');
const letterToCheck = prompt('Enter a letter to check: ');
const result = countString(string, letterToCheck);
document.write(result);