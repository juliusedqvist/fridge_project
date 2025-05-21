// backend/index.js
const express = require('express');
const cors = require('cors');
const mysql = require('mysql2');


const app = express();
const PORT = 4000;

require('dotenv').config();

app.use(cors());
app.use(express.json());

const db = mysql.createConnection({
  host: process.env.DB_HOST,
  user: process.env.DB_USER,
  password: process.env.DB_PASSWORD,
  database: process.env.DB_NAME,
});

db.connect((err) => {
  if (err) throw err;
  console.log('Connected to MySQL database');
});

app.get('/api/hello', (req, res) => {
  res.json({ message: 'Hello from Express!' });
});

app.post('/api/scan', (req, res) => {
  const { code } = req.body;
  console.log('Fick streckkod:', code);
  // Gör vad du vill med koden här (spara i DB etc)
  res.json({ status: 'ok' });
});

app.listen(PORT, () => {
  console.log(`Backend running at http://localhost:${PORT}`);
});


