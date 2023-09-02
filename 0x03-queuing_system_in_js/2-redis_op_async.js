#!/usr/bin/yarn dev
// This script connects to the Redis server running on the current machine.
// It prints out a message when it's connected and when it's not.
// It then goes on to interact with the server using the redisClient using
// promisify.
import { promisify } from "util";
import { createClient, print } from "redis";

const redisClient = createClient();

redisClient.on("error", (err) => {
  console.log("Redis client not connected to the server:", err.toString());
});

const setNewSchool = (schoolName, value) => {
  redisClient.SET(schoolName, value, print);
};

const displaySchoolValue = async (schoolName) => {
  console.log(await promisify(redisClient.GET).bind(redisClient)(schoolName));
};

async function runProcess() {
  await displaySchoolValue("Holberton");
  setNewSchool("HolbertonSanFransisco", "100");
  await displaySchoolValue("HolbertonSanFransisco");
}

redisClient.on("connect", async () => {
  console.log("Redis client connected to the server");
  await runProcess();
});
