#!/usr/bin/node
// Import the 'request' module to make HTTP requests
const request = require('request');

// Check if the movie ID is provided as a command-line argument
if (process.argv.length < 3) {
  console.error('Please provide a movie ID as an argument');
  process.exit(1);
}

// Get the movie ID from the command-line arguments
const movieId = process.argv[2];
// Construct the URL to the Star Wars API
const url = `https://swapi-api.hbtn.io/api/films/${movieId}/`;

// console.log(`url: ${url}`);

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

  // console.log('Status Code:', response && response.statusCode);
  // console.log('Body:', body);

  // Get list of character urls from the movie
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
