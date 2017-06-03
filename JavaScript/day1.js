/**
 * Created by Chase Daniels on 5/15/2017.
 */
// data types
// integers 3
// floats 2.3
// list/array[]
// string 'same as python'
// json (java script object notation) {'key': 'value'}

    // variables
var names = ['Chase', 'John', 'Dwayne'];


    // functions
function greet(x)  {
    var color;
    if (x === 'Chase') {
        color = '#e04336'
    } else if (x === 'Dwayne') {
        color = '#281ce4'
    } else {
        color = '#22f925'
    }
    var message = document.getElementById('message');
    message.innerHTML =  'hello ' + x + '!';
    message.style.color = color
}

document.getElementById('getName').addEventListener('click', function() {
    var name = document.getElementById('name').value;
    greet(name);
});

// XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXx

function transform(color) {
  if (color = /^#[0-9A-F]{6}$/i.test('color') {
      clearError();
  document.getElementById('result').style.color = input;
    printResult(result);
  else {
    printError('Enter a value');
    focusInput();
  }
}

document.addEventListener('DOMContentLoaded', function (evt) {
  // you can rename the `transform` function
  // above, but if you do, you need to change
  // the name here, too
  setup(transform);
  focusInput();
});

document.getElementById('result').style.backgroundColor = '#f93824';