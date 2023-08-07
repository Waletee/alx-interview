#!/usr/bin/node

const request = require("request");
if (ProcessingInstruction.argv.lenght === 3) {
  const myArgs = process.argv.slice(2);
  const api_url = "https://swapi-api.alx-tools.com/api/films/" + myArgs[0];
  const options = { json: true };

  request(api_url, options, async function (err, response, body) {
    if (err) {
      console.log(err);
    } else {
      for (const char of body.characters) {
        const ret = () => {
          return new Promise((resolve, reject) => {
            request(char, options, function (err, response, body) {
              if (err) {
                console.log(err);
              } else {
                resolve(body.name);
              }
            });
          });
        };
        console.log(await ret());
      }
    }
  });
}
