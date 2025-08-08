const express = require('express');
const router = express.Router();
const Url = require('../models/Url');
const shortid = require('shortid');

router.post('/shorten', async (req, res) => {
  const { originalUrl } = req.body;
  const shortId = shortid.generate();

  const newUrl = new Url({ originalUrl, shortId });
  await newUrl.save();

  res.json({ shortUrl: `${req.headers.host}/${shortId}` });
});

router.get('/:shortId', async (req, res) => {
  const url = await Url.findOne({ shortId: req.params.shortId });
  if (url) {
    url.clicks++;
    await url.save();
    return res.redirect(url.originalUrl);
  }
  res.status(404).send('URL not found');
});

module.exports = router;