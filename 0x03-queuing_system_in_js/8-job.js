#!/usr/bin/node


function createPushNotificationsJobs(jobs, queue) {
    if(!Array.isArray(jobs)) {
        return new Error('Jobs is not an array')
    }
    for (const i of jobs) {
        const job = queue.create('push_notification_code_3', i);

        job.save((err) => {
            if(!err) {
                console.log(`Notification job created: ${job.id}`)
            }
        })

        job.on('complete', () => {
            console.log(`Notification job ${job.id} completed`)
        })

        .on('failed', (err) => {
            console.log(`Notification job ${job.id} failed: ${err}`)
        })

        .on('progress', (prog, _data) => {
            console.log(`Notification job ${job.id} ${prog}% complete`)
        })
    }
}

export default createPushNotificationsJobs;
