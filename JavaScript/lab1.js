// function transform(input) {
//   if (input <= 3) {
//       clearError();
//       printResult(input);
//   } else {
//     var new_num = num.toLocaleString();
//     printResult(new_num);
//   }

  // function transform(input) {
  //   var x = input
  //   document.getElementById('result').innerHTML = x.toLocaleString();
  // }
  //
  // function transform2(input) {
  //     if (input <= 999){
  //         document.getElementById('result').innerHTML = input
  //     } else if (input >= 1000 || input <= 9999{
  //         var n1 = input.toString();
  //         var n2 = n1.split(' ');
  //         var n3 = n2.splice()
  //         var n4 = input.charAt(0) + ','
  //     }
  // }
// function transform(input) {
//     var x = numberWithCommas(input)
//     document.getElementById('result').innerHTML = x;
//   }
//
// function numberWithCommas(input) {
//     return x.toString().replace(/\B(?=(\d{3})+(?!\d))/g, ",");
// }
//
// document.getElementById('getNumber').addEventListener('clicl', function() {
//     var number = document.getElementById('number').value;
//     var numberComma = parseInt(number).toLocaleString();
//     document.getElementById('message').innerHTML = numberComma
// });
//
// function reverseString(str){
//     var splitString = str.split("");
//     var reverseArray = splitString.reverse();
//     return reverseArray.join("");
// }

document.getElementById('animatebutton').addEventListener('click', function () {
    var icon = document.getElementById('animate');
    var id = setInterval(frame, 5);
    var pos = 0;

    function frame() {
        if (pos === = 100) {
            clearInterval(id);
        } else {
            pos++;
            if (pos % 2 === 0) {
                icon.style.right = '50px';
            } else {
                icon.style.left = '50px'
            }
        }

    }
};