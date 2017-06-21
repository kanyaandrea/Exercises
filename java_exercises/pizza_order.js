
var orderCount = 0;

function takeOrder(topping, crustType) {
  console.log("Order: " + crustType + " pizza topped with " + topping);
  orderCount++;
}

function getSubTotal(itemCount) {
  return itemCount * 7.5;
}

takeOrder('bacon', 'thin');
takeOrder('bean', 'thick');
takeOrder('garlic', 'normal');
// this 3 calls is the 3 order for the program //
console.log(getSubTotal(orderCount));

function getTax() {
  return getSubTotal(orderCount) * 0.06;
}

function getTotal() {
  return getSubTotal(orderCount) + getTax();
}

console.log(getTotal());
