#!/usr/bin/yarn dev
import { createQueue, Job } from 'kue';

const BLN = ['4153518780', '4153518781'];
const q = createQueue();

const sendNotification = (phoneNumber, message, job, done) => {
  let ttl = 2, pnd = 2;
  let sendInterval = setInterval(() => {
    if (ttl - pnd <= ttl / 2) {
      job.progress(ttl - pnd, ttl);
    }
    if (BLN.includes(phoneNumber)) {
      done(new Error(`Phone number ${phoneNumber} is blacklisted`));
      clearInterval(sendInterval);
      return;
    }
    if (ttl === pnd) {
      console.log(
        `Sending notification to ${phoneNumber},`,
        `with message: ${message}`,
      );
    }
    --pnd || done();
    pnd || clearInterval(sendInterval);
  }, 1000);
};

q.process('push_notification_code_2', 2, (job, done) => {
  sendNotification(job.data.phoneNumber, job.data.message, job, done);
});
