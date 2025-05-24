const express = require('express');
const fs = require('fs');
const path = require('path');

const router = express.Router();

router.get('/weight', (req, res) => {
  const filePath = path.join(__dirname, '../scale-out.txt');

  fs.readFile(filePath, 'utf8', (err, data) => {
    if (err) {
      console.error('Error reading weight file:', err);
      return res.status(500).json({ error: 'Failed to read weight file' });
    }
    res.json({ weight: data.trim() });
  });
});

router.post('/add_product', (req, res) => {
  console.log(req.body);
  db.query('SELECT * FROM products', (err, results) => {
    if (err) {
      console.error('Query error:', err);
      return res.status(500).json({ error: 'Database query failed' });
    }
    res.json(results);
  });
});

module.exports = router;
