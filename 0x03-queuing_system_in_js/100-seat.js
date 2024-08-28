#!/usr/bin/yarn dev
import express from 'express';
import { promisify } from 'util';
import { createQueue } from 'kue';
import { createClient } from 'redis';

const app = express();
const cl = createClient({ name: 'reserve_seat' });
const q = createQueue();
const ISC = 50;
let RES = false;
const PT = 1245;

const reserveSeat = async (number) => {
  return promisify(cl.SET).bind(cl)('available_seats', number);
};

const getCurrentAvailableSeats = async () => {
  return promisify(cl.GET).bind(cl)('available_seats');
};

app.get('/available_seats', (_, res) => {
  getCurrentAvailableSeats()
    // .then(result => Number.parseInt(result || 0))
    .then((numberOfAvailableSeats) => {
      res.json({ numberOfAvailableSeats })
    });
});

app.get('/reserve_seat', (_req, res) => {
  if (!RES) {
    res.json({ status: 'Reservation are blocked' });
    return;
  }
  try {
    const job = q.create('reserve_seat');

    job.on('failed', (err) => {
      console.log(
        'Seat reservation job',
        job.id,
        'failed:',
        err.message || err.toString(),
      );
    });
    job.on('complete', () => {
      console.log(
        'Seat reservation job',
        job.id,
        'completed'
      );
    });
    job.save();
    res.json({ status: 'Reservation in process' });
  } catch {
    res.json({ status: 'Reservation failed' });
  }
});

app.get('/process', (_req, res) => {
  res.json({ status: 'Queue processing' });
  q.process('reserve_seat', (_job, done) => {
    getCurrentAvailableSeats()
      .then((result) => Number.parseInt(result || 0))
      .then((availableSeats) => {
        RES = availableSeats <= 1 ? false : RES;
        if (availableSeats >= 1) {
          reserveSeat(availableSeats - 1)
            .then(() => done());
        } else {
          done(new Error('Not enough seats available'));
        }
      });
  });
});

const resetAvailableSeats = async (initialSeatsCount) => {
  return promisify(cl.SET)
    .bind(cl)('available_seats', Number.parseInt(initialSeatsCount));
};

app.listen(PT, () => {
  resetAvailableSeats(process.env.INITIAL_SEATS_COUNT || ISC)
    .then(() => {
      RES = true;
      console.log(`API available on localhost port ${PT}`);
    });
});

export default app;
