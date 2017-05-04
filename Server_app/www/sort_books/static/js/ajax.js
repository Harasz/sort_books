//$(function() {
//	$('button#kick_server').bind('click', function() {
//		$.getJSON('/_action/kick', {
//			clid: $(this).val(),
//		}, function(data) {
//			return true;
//		});
//		return false;
//	});
//});

$(function() {
    $('button#kick_server').click(function() {
        $.ajax({
            type: 'POST',
            url: '/_action/kick',
            contentType: 'application/json;charset=UTF-8',
            data: JSON.stringify({'clid': $(this).val(), 'msg': $('input#msg').val()})
        });
    });
});
