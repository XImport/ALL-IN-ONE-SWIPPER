// src/axiosInstance.js
import axios from 'axios';

const axiosInstance = axios.create({
  baseURL: 'https://hamzanwn.pythonanywhere.com/', // Replace with your API's base URL
  timeout: 14000000, // Request timeout in milliseconds
  headers: {
    'Content-Type': 'application/json',
    // Add any additional headers if required
  },
});

export default axiosInstance;
