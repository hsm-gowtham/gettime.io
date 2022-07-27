$(document).ready(function () {
    get_mins();

});

function get_mins() {
    $(document).on('click', '.getMins-btn', function () {
        var text = $('textarea').val();
        $.post('/getMins', { 'text': text }).done(function (data) {
           $('.showTime span').text(data);

        }).fail(function () {
            console.log("failed");
            $('.success-msg').html('Posting data Failed');
        });
    })
}