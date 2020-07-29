const express = require('express');
const router = express.Router();
const adminController = require('../controllers/admin');


router.get('/add-product', adminController.getAddProduct);

router.post('/add-product', adminController.postAddProduct);

router.get('/edit-product/:productid', adminController.getEditProduct);


router.post('/edit-product', adminController.postEditProduct);


router.get('/product-list', adminController.getProducts);


router.get('/products', adminController.getProducts);

module.exports.routes = router;