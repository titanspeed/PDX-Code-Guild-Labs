'use strict';
$('[name=protein]').click( function () {
    var proteinValue = $(this).data('value');
    var proteinName = this.id;
    var proval = $(this).data('value');
    var html = '<li id="meat" data-value="' + proval + '">' + proteinName.toUpperCase() + ' ' + '$' + proteinValue + '</li>';
    if ($("[id=meat]").length < 1) {
        $('#ordertotal').append(html);
    } else {
        $('#meat').replaceWith(html);
    }
});
$('[name=inside]').click( function () {
    var sidename = $(this).data('name');
    var sideId = this.id;
    var sideval = $(this).data('value');
    var sidelist = "[id=side_" + sideId + "]";
    var html = '<li id="side_' + sideId +'" data-value="' + sideval + '">' + sidename.toUpperCase() + ' ' + '$' + sideval + '</li>';
    if ($(sidelist).length < 1 ) {
        $('#ordertotal').append(html);
    } else {
        $(sidelist).remove();
    }
});
$('#ordertotal').bind("DOMSubtreeModified", function () {
    var value = 0.0;
    $("#ordertotal li").each(function() {
    value += parseFloat($(this).data('value'));
    });
    var html = '<h3 class="finalprice">' + 'Order Total = $' + value + '</h3>';
    if ($('.finalprice').length < 1) {
        $('.totalprice').append(html);
    } else {
        $('.finalprice').replaceWith(html);
    }
    $('#donedone').click(function () {
        var message = 'Thank You for the order!';
        event.preventDefault();
        alert(message);
    })
});

