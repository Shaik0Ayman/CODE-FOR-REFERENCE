var str = prompt("Please enter a string to check for palindrome: ");
var len = str.length;
var mid = Math.floor(len/2);

    for ( var i = 0; i < mid; i++ ) {
        if (str[i] == str[len - 1 - i]) {
            document.writeln("ITS A PALINDROME");
        }
        else{
            document.writeln("ITS A NOT PALINDROME");
        }
    }

    
