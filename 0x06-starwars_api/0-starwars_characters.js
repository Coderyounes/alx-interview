#!/usr/bin/node

const request = require('request');

function getStarWarsCharacters (movieId) {
  const filmUrl = `https://swapi.dev/api/films/${movieId}/`;

  request(filmUrl, { json: true }, (err, res, body) => {
    if (err) {
      return console.error('Error fetching film data:', err);
    }

    if (body.characters) {
      body.characters.forEach((characterUrl) => {
        request(characterUrl, { json: true }, (err, res, character) => {
          if (err) {
            return console.error('Error fetching character data:', err);
          }
          console.log(character.name);
        });
      });
    } else {
      console.error('Invalid movie ID or no characters found.');
    }
  });
}

const movieId = process.argv[2];

if (!movieId) {
  console.error('Please provide a movie ID');
  process.exit(1);
}

getStarWarsCharacters(movieId);
