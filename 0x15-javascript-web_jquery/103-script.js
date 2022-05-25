#!/usr/bin/node
const $ = window.$;
$('#language_code').keyup(function (event) {
  if (event.keyCode === 13) {
    $('#btn_translate').click();
  }
});
