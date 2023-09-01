#!/usr/bin/yarn dev
// This script connects to the Redis server running on the current machine.
// It prints out a message when it's connected and when it's not.
// It then goes on to interact with the server using the redisClient.
import { createClient, print } from "redis";

const redisClient = createClient();

redisClient.on("error", (err) => {
  console.log("Redis client not connected to the server:", err.toString());
});

redisClient.on("connect", () => {
  console.log("Redis client connected to the server");
});

const setNewSchool = (schoolName, value) => {
  redisClient.SET(schoolName, value, print);
};

const displaySchoolValue = (schoolName) => {
  redisClient.GET(schoolName, (_, reply) => console.log(reply));
};

displaySchoolValue("Holberton");
setNewSchool("HolbertonSanFransisco", "100");
displaySchoolValue("HolbertonSanFransisco");
