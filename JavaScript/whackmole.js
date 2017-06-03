'use strict';

var timer;

$('img').click( function () {
    var img = $(this);
    if (img.attr('class') === 'mole') {
        alert('click!');
        console.log(this);
    }
});


$('.begin').click( function() {
    timer = setInterval(gametime, 300)
});


function gametime () {
    var currentHoleVal = Math.floor((Math.random() * $('div img').length) + 1);
    var currentHole = $('.whack-grid img:nth-child(' + currentHoleVal + ')');
    var isTrue = true;
    while (currentHole.attr('src') === 'mole.jpg' && isTrue) {
        var molelist = 0;
        $('.mole').each(function () {
            molelist++;
            console.log(molelist);

        });

            if (molelist < 20) {
                currentHoleVal = Math.floor((Math.random() * $('div img').length) + 1);
                currentHole = $('.whack-grid img:nth-child(' + currentHoleVal + ')');
            } else {
                isTrue = false;
                alert('GAME OVER');
                clearInterval(timer);
            }
        };

        currentHole.attr('src', 'mole.jpg').toggleClass('mole').toggleClass('hole');

    }
