// Clear the screen
function clearScreen() {
  document.getElementById("result").value = "";
}

// Show clicked button value
function setScreenValue(value) {
  document.getElementById("result").value += value;
}

// Calculate result
function calculateResult() {
  const resultElement = document.getElementById("result");
  const expression = resultElement.value.trim();

  if (expression === "") {
    resultElement.value = "Enter number";
    return;
  }

  try {
    resultElement.value = eval(expression);
  } catch {
    resultElement.value = "Invalid";
  }
}
