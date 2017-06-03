'use strict';

var vows = ['a', 'e', 'i', 'o', 'u'];

$('#vowvow').click(function () {
    event.preventDefault();
    var input = $('#vowel').val();
    // console.log(input)
        if (vows.indexOf(input) != -1 ) {
            $('#message').html('Yes ' + input + ' is a vowel')
        } else {
            $('#message').html('No ' + input + ' is not a vowel')
        }

});