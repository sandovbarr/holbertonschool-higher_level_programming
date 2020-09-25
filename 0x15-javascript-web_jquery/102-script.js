document.addEventListener('DOMContentLoaded', function () {
  $('#btn_translate').click(function (event) {
    var inputVar = $('#language_code').val();
    $.get('https://fourtonfish.com/hellosalut/?lang=' + inputVar, function (data) {
      $('#hello').text(data.hello);
    });
    event.preventDefault();
  });
});
