function AppendForm() {
    var $contents = $('#contents');
    var item = $('<div/>').addClass('focusing').append($('<input/>').addClass('focus-val'));
    $contents.append(item);
}
$(function() {
    AppendForm();
    $(document).on("click", "#run-btn", function () {
        var _this = this;
        var q = $('.focus-val').val();
        console.log(q);
        var data = {'query': q};

        $.ajax({
            url:'/',
            type:"POST",
            data:JSON.stringify(data),
            contentType:"application/json",
            dataType:"json",
            success: function(result) {
                if (result['status'] === 'ok') {
                    $('.focusing').remove();
                    var $result = $('<div/>').append('<p/>').text(q + ' = ' + result['result'].toString())
                    $('#contents').append($result);
                    AppendForm();
                }
            }
        })
    });
});
