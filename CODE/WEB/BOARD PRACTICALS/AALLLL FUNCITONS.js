/*ARMSTRONG NUMBER*/
function isArmstrongNumber(number) {
    // Convert the number to a string
    const numString = number.toString();
    
    // Get the length of the number
    const length = numString.length;
    
    // Calculate the sum of the digits raised to the power of the length
    let sum = 0;
    for (let i = 0; i < length; i++) {
        sum += Math.pow(parseInt(numString[i]), length);
    }
    
    // Check if the sum is equal to the original number
    if (sum === number) {
        return true;
    } else {
        return false;
    }
}

/*FACTORIAL NUMBER*/
function factorial(number) {
    let result = 1;
    for (let i = 1; i <= number; i++) {
        result *= i;
    }
    return result;
}
let number = 5;
let result = factorial(number);
console.log(result);

/*FIBONACCI NUMBER*/
function generateFibonacciSeries(start, end) {
    let series = [];
    let a = 0, b = 1;

    while (a <= end) {
        if (a >= start) {
            series.push(a);
        }
        let temp = a + b;
        a = b;
        b = temp;
    }

    return series;
}

let start = 0;
let end = 100;
let fibonacciSeries = generateFibonacciSeries(start, end);
console.log(fibonacciSeries);

/*PALINDROME NUMBER*/
function isPalindromeNumber(number) {
    let reversed = 0;
    let original = number;
    while (number > 0) {
        let digit = number % 10;
        reversed = reversed * 10 + digit;
        number = Math.floor(number / 10);
    }
    return original === reversed;
}
document.querySelector('form').addEventListener('submit', function(event) {
    // Prevent the form from being submitted
    event.preventDefault();
    // Get the number from the input field
    var number = document.querySelector('input[name="number"]').value;
    // Call the isPalindromeNumber function
    var result = isPalindromeNumber(number);
    // Log the result
    console.log(result);
});

/*PRIME NUMBER*/
function isPrimeNumber(number) {
    // Check if the number is 1
    if (number === 1) {
        return false;
    }
    
    // Check if the number is 2
    if (number === 2) {
        return true;
    }
    
    // Check if the number is even
    if (number % 2 === 0) {
        return false;
    }
    
    // Check if the number is divisible by any odd number
    for (let i = 3; i < number; i += 2) {
        if (number % i === 0) {
            return false;
        }
    }
    
    // If the number is not divisible by any odd number, it is a prime number
    return true;
}
document.querySelector('form').addEventListener('submit', function(event) {
    // Prevent the form from being submitted
    event.preventDefault();

    // Get the number from the input field
    var number = document.querySelector('input[name="number"]').value;

    // Call the isPrimeNumber function
    var result = isPrimeNumber(number);

    // Log the result
    console.log(result);
});

/*PERFECT NUMBER*/
function isPerfectNumber(number) {
    // Calculate the sum of the factors
    let sum = 0;
    for (let i = 1; i < number; i++) {
        if (number % i === 0) {
            sum += i;
        }
    }
    // Check if the sum is equal to the original number
    if (sum === number) {
        return true;
    } else {
        return false;
    }
}
document.querySelector('form').addEventListener('submit', function(event) {
    // Prevent the form from being submitted
    event.preventDefault();
    // Get the number from the input field
    var number = document.querySelector('input[name="number"]').value;
    // Call the isPerfectNumber function
    var result = isPerfectNumber(number);
    // Log the result
    console.log(result);
});

/*SUM ODD EVEN*/
function findSumOfOddAndEven(s, e) {
    let oddSum = 0;
    let evenSum = 0;
    for (let i = start; i <= end; i++) {
        if (i % 2 === 0) {
            evenSum += i;
        } else {
            oddSum += i;
        }
    }
    return [oddSum, evenSum];
}
const s = 1;
const e = 10;
const [oddSum, evenSum] = findSumOfOddAndEven(start, end);
console.log("Sum of odd numbers:", oddSum);
console.log("Sum of even numbers:", evenSum);
