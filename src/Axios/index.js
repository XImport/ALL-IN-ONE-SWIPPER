// src/axiosInstance.js
import axios from 'axios';

const axiosInstance = axios.create({
  baseURL: 'http://127.0.0.1:5000', // Replace with your API's base URL
  timeout: 1000000, // Request timeout in milliseconds
  headers: {
    'Content-Type': 'application/json',
    // Add any additional headers if required
  },
});

export default axiosInstance;
