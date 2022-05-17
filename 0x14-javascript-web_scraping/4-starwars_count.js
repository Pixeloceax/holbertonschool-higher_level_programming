#!/usr/bin/node

const axios = require('axios').default;


axios.get("https://swapi-api.hbtn.io/api/people/18/")
    .then(function (response) {
        console.log(response.film);
    })
    .catch(function (error) {
        console.log(error);
    })
    .then(function () {
    });
