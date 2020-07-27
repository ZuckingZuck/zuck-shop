const express = require('express');
const app = express();

const bodyParser = require('body-parser');

app.set('view engine', 'pug');

const adminRoutes = require('./routes/admin');
const userRoutes = require('./routes/user');

const path = require('path');


app.use(bodyParser.urlencoded({ extended: false }));
app.use('/admin', adminRoutes);
app.use(userRoutes);



app.use(express.static(path.join(__dirname, 'public')));

app.use((req, res) => {
    res.status(404).render('404', { title: 'Error' });
});

app.listen(3000, () => {
    console.log('listenin on port 3000');
});