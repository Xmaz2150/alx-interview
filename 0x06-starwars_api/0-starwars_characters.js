#!/usr/bin/node

const request = require('request-promise-native');
const argv = process.argv;

const getMovie = async (fildId) => {
  const response = await request(`https://swapi-api.alx-tools.com/api/films/${fildId}`);

  const movie = await JSON.parse(response);
  return movie;
};

const printCasts = async () => {
  const fildId = argv[2];
  try {
    const movie = await getMovie(fildId);

    for (const [k, v] of Object.entries(movie)) {
      if (k === 'characters') {
        for (const charRoute of v) {
          try {
            const response = await request(charRoute);
            const character = JSON.parse(response);
            console.log(character.name);
          } catch (error) {
            console.log('Character does not exist');
          }
        }
      }
    }
  } catch (error) {
    console.log('Movie not found');
  }
};
printCasts();
