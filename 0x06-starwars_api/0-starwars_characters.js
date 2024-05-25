#!/usr/bin/node
// Import the 'request' module to make HTTP requests
const request = require('request');

if (process.argv.length < 3) {
  console.error('Please provide a movie ID as an argument');
  process.exit(1);
}

const movieId = process.argv[2];
const url = `https://swapi-api.hbtn.io/api/films/${movieId}/`;

// Function to make an HTTP GET request and return a promise
function fetch(url) {
  return new Promise((resolve, reject) => {
    request(url, (error, response, body) => {
      if (error) reject(error);
      else if (response.statusCode !== 200) {
        reject(new Error(`Failed to fetch URL ${url}`));
      }
      else resolve(body);
    });
  });
}

// Main function to get movie data and then character names in order
async function main() {
  try {
    const movieData = await fetch(url);
    const characters = JSON.parse(movieData).characters;
    for (const characterUrl of characters) {
      const characterData = await fetch(characterUrl);
      console.log(JSON.parse(characterData).name);
    }
  } catch (error) {
    console.error(error.message);
  }
}

main();
