const express = require('express');
const fs = require('fs');

const app = express();

function getStudents(path) {
  return new Promise((resolve, reject) => {
    fs.readFile(path, 'utf8', (error, data) => {
      if (error) {
        reject(new Error('Cannot load the database'));
        return;
      }

      const lines = data
        .trim()
        .split('\n')
        .filter((line) => line.trim() !== '');

      const students = lines.slice(1);
      const output = [`Number of students: ${students.length}`];

      const fields = {};

      students.forEach((student) => {
        const studentData = student.split(',');
        const firstname = studentData[0];
        const field = studentData[3];

        if (!fields[field]) {
          fields[field] = [];
        }

        fields[field].push(firstname);
      });

      Object.keys(fields).forEach((field) => {
        output.push(
          `Number of students in ${field}: ${fields[field].length}. List: ${fields[field].join(', ')}`,
        );
      });

      resolve(output.join('\n'));
    });
  });
}

app.get('/', (request, response) => {
  response.send('Hello Holberton School!');
});

app.get('/students', (request, response) => {
  const database = process.argv[2];

  getStudents(database)
    .then((students) => {
      response.send(`This is the list of our students\n${students}`);
    })
    .catch((error) => {
      response.send(`This is the list of our students\n${error.message}`);
    });
});

app.listen(1245);

module.exports = app;