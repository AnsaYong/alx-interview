#!/usr/bin/node
// Import the 'request-promise' module to make HTTP requests
const rp = require('request-promise');

// Check if the movie ID is provided as a command-line argument
if (process.argv.length < 3) {
  console.error('Please provide a movie ID as an argument');
  process.exit(1);
}

// Get the movie ID from the command-line arguments
const movieId = process.argv[2];
// Construct the URL to the Star Wars API
const url = `https://swapi-api.hbtn.io/api/films/${movieId}/`;

(async () => {
  try {
    // Make a GET request to the Star Wars API
    const response = await rp(url, { json: true });

    // Get list of character urls from the movie
    const characterUrls = response.characters;

    if (characterUrls.length === 0 || !characterUrls) {
      console.log('No characters found');
      return;
    }

    // Iterate over each character URL and make a GET request to fetch the character
    for (const characterUrl of characterUrls) {
      const character = await rp(characterUrl, { json: true });
      console.log(character.name);
    }
  } catch (error) {
    console.error('Error:', error);
  }
})();
