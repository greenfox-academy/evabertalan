function add(a, b) {
  return a + b;
}

console.log(add(1, 2));

var osszead = add;
console.log(osszead(4, 5));




function multiply(a, b) {
  return a * b;
}

var szoroz = function multiply(a, b){
  return a*b;
}

console.log(szoroz(4, 5));


var car = {
  km: 100,
  type: 'Skoda',
  honk: function() {
    console.log('Duuuuu');
  }
};

car.honk();
