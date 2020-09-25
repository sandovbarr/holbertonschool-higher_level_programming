document.addEventListener('DOMContentLoaded', function () {
  $('#btn_translate').on('keypress click', function (event) {
    var inputVar = $('#language_code').val();
    if (event.which === 13 || event.type === 'click') {
      $.get('https://fourtonfish.com/hellosalut/?lang=' + inputVar, function (data) {
        $('#hello').text(data.hello);
      });
    }
    event.preventDefault();
  });
});
