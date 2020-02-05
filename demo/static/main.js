$(document).ready(function() {
    $('#submit').click(function() {
        const message = $('#message').val();
        $.post('/message', {
            message: message
        }).done(function() {
            document.location.reload();
        });
    });
});
