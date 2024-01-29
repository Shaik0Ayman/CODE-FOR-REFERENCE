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
 /*MOCK PRACTICAL QUESTIONS*/
/* Write a JavaScript code to add an element at the end of the array and delete a first element in the array and find length of an array. */ 
function modifyArray(array, element) {
    // Add the element to the end of the array
    array.push(element);

    // Remove the first element of the array
    array.shift();

    // Return the length of the array
    return array.length;
}
let array = [1, 2, 3, 4, 5];
let element = 6;
let length = modifyArray(array, element);
console.log("Modified array:", array);
console.log("Length of array:", length);


/* WAP to find and display the factors of a given number. */
function findFactors(number) {
    let factors = [];
    for (let i = 1; i <= number; i++) {
        if (number % i === 0) {
            factors.push(i);
        }
    }
    return factors;
}

let number = 12;
let factors = findFactors(number);
console.log("Factors of", number + ":", factors);



/* Write a JavaScript code for the following pattern. 
***** 
***** 
***** 
***** 
***** */
function printPattern(rows, columns) {
    let pattern = '';
    for (let i = 0; i < rows; i++) {
        for (let j = 0; j < columns; j++) {
            pattern += '*';
        }
        pattern += '\n';
    }
    return pattern;
}

let rows = 5;
let columns = 5;
let pattern = printPattern(rows, columns);
console.log(pattern);

/* Write a program to find and display the number of occurrences of a given 
character from a string. */
function countOccurrences(str, char) {
    let count = 0;
    for (let i = 0; i < str.length; i++) {
        if (str[i] === char) {
            count++;
        }
    }
    return count;
}

let string = "Hello, world!";
let character = "o";
let occurrences = countOccurrences(string, character);
console.log("Number of occurrences of", character + ":", occurrences);


/* WAP to convert kilometres to miles and vice versa based on user’s choice. */
function convertDistance(distance, unit) {
    if (unit === "km") {
        return distance * 0.621371; // Convert kilometers to miles
    } else if (unit === "mi") {
        return distance * 1.60934; // Convert miles to kilometers
    } else {
        return "Invalid unit";
    }
}

let distance = 10;
let unit = "km";
let convertedDistance = convertDistance(distance, unit);
console.log(distance + " " + unit + " is equal to " + convertedDistance + " miles");

distance = 5;
unit = "mi";
convertedDistance = convertDistance(distance, unit);
console.log(distance + " " + unit + " is equal to " + convertedDistance + " kilometers");



