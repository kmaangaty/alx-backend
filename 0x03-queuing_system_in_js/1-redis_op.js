#!/usr/bin/yarn dev
import { createClient, print } from 'redis';

const cl = createClient();

cl.on('error', (err) => {
  console.log('Redis client not connected to the server:', err.toString());
});

cl.on('connect', () => {
  console.log('Redis client connected to the server');
});

const setNewSchool = (schoolName, value) => {
  cl.SET(schoolName, value, print);
};

const displaySchoolValue = (schoolName) => {
  cl.GET(schoolName, (_err, reply) => {
    console.log(reply);
  });
};

displaySchoolValue('Holberton');
setNewSchool('HolbertonSanFrancisco', '100');
displaySchoolValue('HolbertonSanFrancisco');
