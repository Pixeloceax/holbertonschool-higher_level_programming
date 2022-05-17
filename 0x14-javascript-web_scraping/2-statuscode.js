#!/usr/bin/node

const axios = require('axios');

axios({
  method: 'get',
  url: process.argv[2]
})
  .then((response) => {
    console.log('code: ' + response.status);
  }, (error) => {
    console.log('code: ' + error.response.status);
  });
