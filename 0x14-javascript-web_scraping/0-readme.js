#!/usr/bin/node

const fs = require('fs');

const writeStringToFile = (filePath, content) => {
  fs.writeFile(filePath, content, { encoding: 'utf-8' }, (err) => {
    if (err) {
      console.error(err);
    }
  });
};

if (process.argv.length !== 4) {
  console.error('Usage: node script.js <file_path> <string_to_write>');
  process.exit(1);
}

const filePath = process.argv[2];
const content = process.argv[3];

writeStringToFile(filePath, content);
