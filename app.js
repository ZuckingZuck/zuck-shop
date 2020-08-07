const express = require('express');
const app = express();
const errors = require('./controllers/errors');

const bodyParser = require('body-parser');

app.set('view engine', 'pug');

const admin = require('./routes/admin');
const user = require('./routes/shop');

const path = require('path');



app.use(bodyParser.urlencoded({ extended: false }));

app.use(express.static(path.join(__dirname, 'public')));

app.use('/admin', admin.routes);
app.use(user.routes);


const port = process.env.PORT || 3000;

app.use(errors.get404Page);

app.listen(port, () => {
    console.log('listenin on port 3000');
}); 
