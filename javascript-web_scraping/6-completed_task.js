#!/usr/bin/node

const request = require('request');
const apiTask = process.argv[2];

request.get(apiTask, (error, response, body) => {
  if (error) {
    console.error(error);
    return;
  }
  const tasks = JSON.parse(body);
  const userCompleted = new Map();
  tasks.forEach(task => {
    const userId = task.userId;
    const completed = task.completed;
    if (completed) {
      if (userCompleted.has(userId)) {
        userCompleted.set(userId, userCompleted.get(userId) + 1);
      } else {
        userCompleted.set(userId, 1);
      }
    }
  });
  console.log(userCompleted);
});
