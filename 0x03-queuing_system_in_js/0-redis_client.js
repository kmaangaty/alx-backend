#!/usr/bin/yarn dev
import { createClient } from 'redis';

const cl = createClient();

cl.on('error', (err) => {
  console.log('Redis client not connected to the server:', err.toString());
});

cl.on('connect', () => {
  console.log('Redis client connected to the server');
});
