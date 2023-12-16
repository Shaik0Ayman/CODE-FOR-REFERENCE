
var userInput = prompt("Enter a number:");

var numberString = userInput.toString();

function isPalindrome(str) {

    var reversedStr = str.split('').reverse().join('');

    return str === reversedStr;
}


if (isPalindrome(numberString)) {
    console.log(userInput + " is a palindrome.");
} else {
    console.log(userInput + " is not a palindrome.");
}
