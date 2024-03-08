#!/usr/bin/node
import { createClient, print } from "redis";


const client = createClient();
client.on('error', (err) => {
    console.log(`${err}`)
})

client.on('connect', () => {
    console.log('Redis client connected to the server')
})

// client.HMSET('HolbertonSchools',
//                                 {
//                                     'Portland': 50,
//                                     'Seattle': 80,
//                                     'New York': 20,
//                                     'Bogota': 20,
//                                     'Cali': 40,
//                                     'Paris': 2,
//                                 }, print
//                                 );
const myKey = "HolbertonSchools";
client
.MULTI()
.HSET(myKey, 'Portland', 50, print)
.HSET(myKey, 'Seattle', 80, print)
.HSET(myKey, 'New York', 20, print)
.HSET(myKey, 'Bogota', 20, print)
.HSET(myKey, 'Cali', 40, print)
.HSET(myKey, 'Paris', 2, print)
.EXEC();

client.HGETALL('HolbertonSchools', (_err, val) => {
    console.log(val);
});
