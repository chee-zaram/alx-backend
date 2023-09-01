#!/usr/bin/yarn dev
// This script connects to the Redis server running on the current machine.
// It prints out a message when it's connected and when it's not.
import { createClient } from "redis";

const redisClient = createClient();

redisClient.on("error", (err) => {
  console.log("Redis client not connected to the server:", err.toString());
});

redisClient.on("connect", () => {
  console.log("Redis client connected to the server");
});
