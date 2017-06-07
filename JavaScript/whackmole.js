'use strict';

var timer;
var counter = 3000;
var score = 0;
// var interval = setInterval(gametime, counter);

$('img').click(function () {
    var img = $(this);
    if (img.attr('class') === 'mole') {
        img.attr('src', 'hole.jpg').toggleClass('mole').toggleClass('hole');
        score += 1;
        $('.score').html(score);

    }
});

$('.begin').click(function () {
    timer = setInterval(gametime, counter)
});

function gametime() {
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
    }
    ;

    currentHole.attr('src', 'mole.jpg').toggleClass('mole').toggleClass('hole');
    clearInterval(timer);
    counter -= counter * (.03);
    timer = setInterval(gametime, counter);
    console.log(counter);

}

// function gametime () {
//     var moleCount = $('.whack-grid').children('.hole');
//     var currentHoleVal = Math.floor((Math.random() * moleCount.length) + 1);
//     var currentHole = $('#' + moleCount[currentHoleVal].id);
//     console.log(currentHole);
//     currentHole.attr('src', 'mole.jpg').toggleClass('mole').toggleClass('hole');
//     clearInterval(timer);
//     counter -= counter * (.05);
//     timer = setInterval(gametime, counter);
//     console.log(counter);
// }