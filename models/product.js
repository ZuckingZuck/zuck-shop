let products = [
    { id: '12345', name: 'Samsung S9', price: 3000, imageUrl: '1.jpg', description: 'Test' },
    { id: '12346', name: 'Samsun S8', price: 2750, imageUrl: '2.jpg', description: 'Güzel Telefon' }
];

module.exports = class Product {
    constructor(name, price, imageUrl, description) {
        this.id = Math.floor(Math.random() * 99999) + 1;
        this.name = name;
        this.price = price;
        this.imageUrl = imageUrl;
        this.description = description;
    }

    saveProduct() {
        products.push(this);
    }

    static getAll() {
        return products;
    }

    static getById(id) {
        const product = products.find(i => i.id === id);
        return product;
    }
}