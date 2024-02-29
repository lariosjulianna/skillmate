const express = require('express');
const bodyParser = require('body-parser');
const mysql = require('mysql');

const app = express();
const port = 3000;

app.use(bodyParser.json());

// Your MySQL connection configuration
const db = mysql.createConnection({
  host: 'localhost',
  user: 'root',
  password: 'CPSC408!',
  database: 'Skillmate'
});

// Endpoint for creating a new user
app.post('/createUser', (req, res) => {
  const { email, password, firstname, lastname } = req.body;

  const query = `
    INSERT INTO User (FirstName, LastName, Email, PasswordHash)
    VALUES (?, ?, ?, ?);
  `;

  db.query(query, [firstname, lastname, email, password], (err, result) => {
    if (err) {
      console.error('Error creating user:', err);
      res.status(500).send('Internal Server Error');
    } else {
      res.status(200).send('User created successfully');
    }
  });
});

// Endpoint for logging in
app.post('/login', (req, res) => {
  const { email, password } = req.body;

  const query = `
    SELECT FirstName
    FROM User
    WHERE Email = ? AND PasswordHash = ?;
  `;

  db.query(query, [email, password], (err, result) => {
    if (err) {
      console.error('Error logging in:', err);
      res.status(500).send('Internal Server Error');
    } else {
      if (result.length === 0) {
        res.status(401).send('Invalid credentials');
      } else {
        const firstname = result[0].FirstName;
        res.status(200).json({ firstname });
      }
    }
  });
});

app.listen(port, () => {
  console.log(`Server is running on http://localhost:${port}`);
});