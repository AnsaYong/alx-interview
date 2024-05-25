#!/usr/bin/node
// Import the 'request' module to make HTTP requests
const request = require('request');

if (process.argv.length < 3) {
  console.error('Please provide a movie ID as an argument');
  process.exit(1);
}

const movieId = process.argv[2];
const url = `https://swapi-api.hbtn.io/api/films/${movieId}/`;

// Make a GET request to the Star Wars API
request(url, { json: true }, (error, response, body) => {
  if (error) {
    console.error('Error retreiving movie data:', error);
    return;
  }
  if (response.statusCode !== 200) {
    console.error(`Failed to fetch movie with ID ${movieId}`);
    return;
  }

  const characterUrls = body.characters;

  if (characterUrls.length === 0 || !characterUrls) {
    console.log('No characters found');
    return;
  }

  // Iterate over each character URL and make a GET request to fetch the character
  characterUrls.forEach((characterUrl) => {
    request(characterUrl, { json: true }, (error, response, body) => {
      if (error) {
        console.error('Error fetching character data:', error);
        return;
      }
      if (response.statusCode !== 200) {
        console.error(`Failed to fetch character with URL ${characterUrl}`);
        return;
      }

      // Print the character name
      console.log(body.name);
    });
  });
});
