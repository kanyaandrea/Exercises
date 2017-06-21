function getUserChoice () {
  var userInput = prompt('What is you choice?');
  userInput = userInput.toLowerCase();
  if (userInput === 'rock' || userInput === 'scissors' || userInput === 'paper' || userInput === 'bomb' ) {
    return userInput;
  }   
  else {
    console.log("Error: there is no such an option");
  }    
}

function getComputerChoice() {
  var computerInput = Math.floor(Math.random()*2);
  if (computerInput === 0) {
    return 'rock';
  }
  else if (computerInput === 1) {
    return 'paper';
  }
  else if (computerInput === 2) {
    return 'scissors';
  }
}

function determineWinner (userChoice, computerChoice) {
  if (userChoice === computerChoice) {
    return "This is a tie.";
  }
  if (userChoice === 'rock') {
  	if (computerChoice === 'paper') {
    	return 'The computer won!'; 
    } 
    else {
    	return 'You won!';
  	}
	}
  if (userChoice === 'scissor') {
  	if (computerChoice === 'rock') {
    	return 'The computer won!'; 
    } 
    else {
    	return 'You won!';
  	}
	}
  if (userChoice === 'paper') {
  	if (computerChoice === 'scissor') {
    	return 'The computer won!'; 
    } 
    else {
    	return 'You won!';
  	}
	}
  if (userChoice === 'bomb') {
  	return 'You won!';
      }
}

function playGame() {
  var userChoice = getUserChoice();
  var computerChoice = getComputerChoice();
  console.log(userChoice);
  console.log(computerChoice);
  console.log(determineWinner(userChoice, computerChoice));
}

playGame();
