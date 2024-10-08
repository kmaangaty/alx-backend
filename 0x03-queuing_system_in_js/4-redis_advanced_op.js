#!/usr/bin/yarn dev
import { createClient, print } from 'redis';

const cl = createClient();

cl.on('error', (err) => {
  console.log('Redis client not connected to the server:', err.toString());
});

const updateHash = (hashName, fieldName, fieldValue) => {
  cl.HSET(hashName, fieldName, fieldValue, print);
};

const printHash = (hashName) => {
  cl.HGETALL(hashName, (_err, reply) => console.log(reply));
};

function main() {
  const hashObj = {
    Portland: 50,
    Seattle: 80,
    'New York': 20,
    Bogota: 20,
    Cali: 40,
    Paris: 2,
  };
  for (const [field, value] of Object.entries(hashObj)) {
    updateHash('HolbertonSchools', field, value);
  }
  printHash('HolbertonSchools');
}

cl.on('connect', () => {
  console.log('Redis client connected to the server');
  main();
});
