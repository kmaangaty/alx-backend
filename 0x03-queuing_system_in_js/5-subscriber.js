#!/usr/bin/yarn dev
import { createClient } from 'redis';

const cl = createClient();
const EM = 'KILL_SERVER';

cl.on('error', (err) => {
  console.log('Redis client not connected to the server:', err.toString());
});

cl.on('connect', () => {
  console.log('Redis client connected to the server');
});

cl.subscribe('holberton school channel');

cl.on('message', (_err, msg) => {
  console.log(msg);
  if (msg === EM) {
    cl.unsubscribe();
    cl.quit();
  }
});
