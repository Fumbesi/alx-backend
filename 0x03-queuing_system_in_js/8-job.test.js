import { assert, expect } from "chai";
import sinon from "sinon";
import kue from 'kue';
import createPushNotificationsJobs from './8-job.js';

const queue = kue.createQueue();


describe('createPushNotificationsJobs', function () {

    const jobs = [
        {
          phoneNumber: '4153518780',
          message: 'This is the code 1234 to verify your account'
        },
        {
          phoneNumber: '4153518781',
          message: 'This is the code 4562 to verify your account'
        }            
      ];
      beforeEach(function() {
        sinon.spy(console, 'log');
      })

      before(function() {
        queue.testMode.enter();
      })

      
      afterEach(function() {
        sinon.restore();
        queue.testMode.clear();
      });
      
      after(function() {
        queue.testMode.exit()
      });


    it('display a error message if jobs is not an array', function(done) {
        try{
        assert.fail(createPushNotificationsJobs(1, queue));
        } catch (err) {
            console.log();
        }
        done();
    });

    it('throws if queue is not a valid kue', function() {
        expect(() => createPushNotificationsJobs(jobs, "")).to.throw();
      });

    it('test the creation of jobs', () => {
        createPushNotificationsJobs(jobs, queue);
        expect(queue.testMode.jobs.length).to.equal(2);
        expect(queue.testMode.jobs[0].type).to.equal('push_notification_code_3');
        expect(queue.testMode.jobs[0].data).to.eql(jobs[0]);
        expect(console.log.calledOnceWith(`Notification job created: ${queue.testMode.jobs[0].id}`)).to.be.false;
     });

     it('test job progress event report', (done) => {
        createPushNotificationsJobs(jobs, queue);
        queue.testMode.jobs[0].addListener('progress', () => {
          const id = queue.testMode.jobs[0].id;
          expect(console.log.calledWith(`Notification job ${id} 50% complete`)).to.be.true;
          done();
        });
        queue.testMode.jobs[0].emit('progress', 50, 100);
      });
})
