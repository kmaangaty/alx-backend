#!/usr/bin/yarn dev
import { promisify } from 'util';
import { createClient, print } from 'redis';

const cl = createClient();

cl.on('error', (err) => {
  console.log('Redis client not connected to the server:', err.toString());
});

const setNewSchool = (schoolName, value) => {
  cl.SET(schoolName, value, print);
};

const displaySchoolValue = async (schoolName) => {
  console.log(await promisify(cl.GET).bind(cl)(schoolName));
};

async function main() {
  await displaySchoolValue('Holberton');
  setNewSchool('HolbertonSanFrancisco', '100');
  await displaySchoolValue('HolbertonSanFrancisco');
}

cl.on('connect', async () => {
  console.log('Redis client connected to the server');
  await main();
});
