'use strict';

$('#addToDo').click(function () {
    event.preventDefault();
    $('#toDoInput').toggle('medium');

});

$('#enter').click( function () {
    event.preventDefault();
    var count = $('#toDoList tr').length;
    console.log(count);
    var item = $('#toDoInputText');
    var html = '<tr><td class="row0">' + count + '</td><td id="td_' + count + '" class="row1">' + item.val() + '</td><td class="row2"><a onclick="done(this)" href="#" id="done_' + count + '">Done</a></td></tr>';
    $('#toDoList').append(html);
    item.val('');
    $('#toDoInput').toggle('medium');

});

function done(el) {
    event.preventDefault();
    var id = el.id.replace ( /[^\d.]/g, '' );
    var itemId = '#td_' + id;
    $(itemId).css('text-decoration', 'line-through');
    console.log(itemId);
}



$('.input').keypress(function (e) {
    if (e.which === 13) {
        $(this).blur();
        $('#enter').focus().click();
    }
});