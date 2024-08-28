#!/usr/bin/yarn dev
import { createQueue } from 'kue';

const q = createQueue({name: 'push_notification_code'});

const j = q.create('push_notification_code', {
  phoneNumber: '07045679939',
  message: 'Account registered',
});

j
  .on('enqueue', () => {
    console.log('Notification job created:', j.id);
  })
  .on('complete', () => {
    console.log('Notification job completed');
  })
  .on('failed attempt', () => {
    console.log('Notification job failed');
  });
j.save();
