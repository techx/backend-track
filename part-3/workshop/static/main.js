$(document).ready(function () {
    // login handlers
    $('#submit').click(function () {
        const message = $('#message').val();
        $.post('/message', {
            message: message,
        }).done(function () {
            document.location.reload();
        });
    });
});
