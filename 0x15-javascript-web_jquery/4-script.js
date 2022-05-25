#!/usr/bin/node
const $ = window.$;
$('#toggle_header').click(function () {
  $('header').toggleClass('green');
  $('header').toggleClass('red');
});
