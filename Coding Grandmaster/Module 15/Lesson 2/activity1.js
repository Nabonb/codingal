function palindrome(myString) {

  var input = myString.replace(/[^A-Z0-9]/gi, "").toLowerCase();

  // reverse the string
  var reversedInput = input.split("").reverse().join("");

  // check palindrome
  if (input === reversedInput) {
    document.write("<div>" + myString + " is a palindrome</div>");
  } else {
    document.write("<div>" + myString + " is not a palindrome</div>");
  }
}


palindrome("madam");
