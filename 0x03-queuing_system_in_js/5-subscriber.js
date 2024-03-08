#!/usr/bin/node
import { createClient, print } from "redis";


const client = createClient();
client.on('error', (err) => {
    console.log(`Redis client not connected to the server: ${err}`)
})

client.on('connect', () => {
    console.log('Redis client connected to the server')
})

const chan = 'holberton school channel';

client.SUBSCRIBE(chan);

client.on('message', (_channel, message) => {
    console.log(message);
    if (_channel === chan) {
        if (message === 'KILL_SERVER') {
            client.UNSUBSCRIBE('holberton school channel');
            client.quit();
        }
    }
});
