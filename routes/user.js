const express = require('express');
const router = express.Router();
const path = require('path');

router.get('/', (req, res, next) => {

    let products = [
        { name: 'Samsung S8', price: 3000, image: '1.jpg', description: 'İyi telefon' },
        { name: 'Samsung S7', price: 2500, image: '2.jpg', description: 'Çok İyi telefon' },
        { name: 'Samsung S6', price: 2500, image: '3.jpg', description: 'Mükemmel telefon' },
        { name: 'Iphone X', price: 6000, image: '4.jpg', description: 'Efsane bişey bu' },
    ]


    res.render('index', { title: 'Home Page', products: products });
});

module.exports = router;