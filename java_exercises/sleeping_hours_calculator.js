function getSleepHours(day) {
  var sleepingHours = prompt("how many hours do you sleep on " + day + "? ");
  return Number(sleepingHours);
}

function getActualSleepHours() {
  return getSleepHours('Monday') + getSleepHours('Tuesday') + getSleepHours('Wednesday') + getSleepHours('Thursday') + getSleepHours('Friday') + getSleepHours('Saturday')+
getSleepHours('Sunday');
}

function getIdealSleepHours() {
  var idealHours = prompt("how many hours ideal for you per night ? ");
  return Number(idealHours)*7;
}

function calculateSleepDebt() {
  var actualSleepHours = getActualSleepHours();
  var idealSleepHours = getIdealSleepHours();
  var sleptDiff = idealSleepHours - actualSleepHours;
  console.log("you slept "  + actualSleepHours + "hours this week.");
  if (actualSleepHours < idealSleepHours ) {
    console.log("you slept with " + sleptDiff + " hours less than required. go bed earlier!"); 
  }
   else if (actualSleepHours > idealSleepHours) {
    console.log("you slept with " + sleptDiff + " more than required. wake up eralier and do some exercises");    
  } 
   else {
    console.log("you just fine");    
  } 
}

calculateSleepDebt();
