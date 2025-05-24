const express = require('express');
const fs = require('fs');
const path = require('path');
const db = require('../db')

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

router.get('/get_products', (req, res) => {
  const query = 'SELECT * FROM Food_Item';

  db.query(query, (err, results) => {
    if (err) {
      console.error('Query error:', err);
      return res.status(500).json({ error: 'Database query failed' });
    }

    res.status(200).json(results);
  });
});

router.post('/add_product', (req, res) => {
  console.log(req.body);
  const { name, weight, kcal, protein, exp_date } = req.body;

  if (
    name === undefined ||
    weight === undefined ||
    kcal === undefined ||
    protein === undefined ||
    exp_date === undefined
  ) {
    return res.status(400).json({ error: 'Missing required fields' });
  }


  const insertQuery = `
    INSERT INTO Food_Item (Name, Weight, KcalPer100g, ProteinPer100g, Exp_Date)
    VALUES (?, ?, ?, ?, ?)
  `;
  console.log(name, weight, kcal, protein, exp_date);

  db.query(insertQuery, [name, weight, kcal, protein, exp_date], (err, result) => {
    if (err) {
      console.error('Insert error:', err);
      return res.status(500).json({ error: 'Failed to insert product' });
    }

    res.status(201).json({
      message: 'Product added successfully',
      productId: result.insertId
    });
  });
});

module.exports = router;
