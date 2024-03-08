#!/usr/bin/node

import express from 'express';
import { createClient } from 'redis';
import { promisify } from 'util';


const app = express();
const client = createClient();
app.use(express.json());

const listProducts = [
    {id: 1, name: 'Suitcase 250', price: 50, initialAvailableQuantity: 4},
    {id: 2, name: 'Suitcase 450', price: 100, initialAvailableQuantity: 10},
    {id: 3, name: 'Suitcase 650', price: 350, initialAvailableQuantity: 2},
    {id: 4, name: 'Suitcase 1050', price: 550, initialAvailableQuantity: 5}
];

function getItemById(id){
    for (const i of listProducts){
        if (i.id === id) {
            return i
        }
    }
    return 0;
}

function reserveStockById(itemId, stock){
    const set = promisify(client.SET).bind(client);
    return set(`item.${itemId}`, stock)
}

async function getCurrentReservedStockById(itemId) {
    const key = `item.${itemId}`;

    const get = promisify(client.GET).bind(client);
    const res = await get(key);
    if (res === null) return 0;
    return res;
}

app.get('/list_products', (req, res) => {
    res.json(listProducts);
})

app.get('/list_products/:itemId', async (req, res) => {
    const itemId = Number(req.params.itemId);
    const obj = getItemById(itemId);
    if (Object.values(obj).length > 0) {
        const stock = await getCurrentReservedStockById(itemId);
        obj.currentQuantity = obj.initialAvailableQuantity - Number(stock);
        res.json(obj);
        return
    }
    res.json({"status":"Product not found"});
});

app.get('/reserve_product/:itemId', async (req, res) => {
    const itemId = Number(req.params.itemId);
    const item = getItemById(itemId);
    if (!getItemById(itemId)){
        res.json({"status":"Product not found"});
        return
    }
    const stock = await getCurrentReservedStockById(itemId);
    if (getItemById(itemId).initialAvailableQuantity - stock <= 0) {
        res.json({"status":"Not enough stock available", itemId});
        return
    }
    await reserveStockById(itemId, Number(stock) + 1);
    res.json({"status":"Reservation confirmed",itemId});
})


app.listen(1245, () => {
    console.log('API available on localhost via port 1245');
});
