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

// Routes
const apiRoutes = require('./routes/api');
app.use('/api', apiRoutes); // Prefix all API routes with /api


app.listen(PORT, () => {
  console.log(`Backend running at http://localhost:${PORT}`);
});

module.exports = db
