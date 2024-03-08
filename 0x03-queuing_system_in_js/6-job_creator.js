#!usr/bin/node

import { createQueue } from "kue";

const queue = createQueue();
const jobData = {phoneNumber: '+251951034116', message: 'test message'};
const job = queue.create('push_notification_code', jobData)
            .save((err) => {
                if(!err) {
                    console.log(`Notification job created: ${job.id}`)
                }
            });
job.on('complete', () => {
    console.log(`Notification job completed`);
});

job.on('failed', (_err) => {
    console.log(`Notification job failed`)
});
