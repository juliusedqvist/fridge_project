const express = require('express')
const fs = require('fs')
const path = require('path')
const router = express.Router()

router.post('/scan', (req, res) => {
  const { code } = req.body
  console.log('Fick streckkod:', code)
  // Här kan du spara i databasen eller annan logik

  res.json({ status: 'ok' })
})

module.exports = router
