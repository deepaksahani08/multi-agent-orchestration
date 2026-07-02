import axios from "axios";
import { config } from "./config";

export const api = axios.create({
  baseURL: config.apiUrl,
  timeout: 60000,
  headers: {
    "Content-Type": "application/json",
  },
});

api.interceptors.response.use(
  (response) => response,
  (error) => {
    const message =
      error.response?.data?.detail ??
      error.message ??
      "Something went wrong";

    return Promise.reject(new Error(message));
  }
);