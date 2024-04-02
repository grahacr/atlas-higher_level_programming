#!/usr/bin/node

const request = require('request');
const apiTask = process.argv[2];

request.get(apiTask, (error, response, body) => {
  if (error) {
    console.error(error);
    return;
  }
  const tasks = JSON.parse(body);
  const userCompleted = {};
  tasks.forEach(task => {
    const userId = task.userId;
    const completed = task.completed;
    if (completed && userId) {
      if (userCompleted[task.userId]) {
        userCompleted[task.userId]++;
      } else {
        userCompleted[task.userId] = 1;
      }
    }
  });
  console.log(userCompleted);
});
