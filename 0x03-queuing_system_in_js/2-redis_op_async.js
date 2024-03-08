#!/usr/bin/node
/**
 * connecting to redis using node-redis
 */
import { createClient, print } from "redis";
import  { promisify } from "util";


const client = createClient()

client.on('error', (err) => {
    console.log(`Redis client not connected to the server: ${err}`)
});

client.on('connect', () => {
    console.log('Redis client connected to the server')
})

function setNewSchool(schoolName, value) {
    client.SET(schoolName, value, print)
}


async function displaySchoolValue(schoolName) {
    const g = promisify(client.GET).bind(client);
    try{
        const value = await g(schoolName);
        console.log(value);
    } catch(err) {
        console.log(`${err}`)
    }
}


(async () => {
await displaySchoolValue('Holberton');
setNewSchool('HolbertonSanFrancisco', '100');
await displaySchoolValue('HolbertonSanFrancisco');
})();
