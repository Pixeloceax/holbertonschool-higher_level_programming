#!/usr/bin/node
const $ = window.$;
$(document).ready(function () {
  $('#update_header').click(function () {
    $('header').text('New Header!!!');
  });
});
