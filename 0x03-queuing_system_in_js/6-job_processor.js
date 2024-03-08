#!/usr/bin/node

import { createQueue } from "kue";

const queue = createQueue();

function sendNotification(phoneNumber, message) {
    console.log(`Sending notification to ${phoneNumber}, with message: ${message}`);
}

queue.process('push_notification_code', (job, done) => {
    // console.log(job.data);
    sendNotification(job.data.phoneNumber, job.data.message)
    done();
});
