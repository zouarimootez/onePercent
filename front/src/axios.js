// src/axios.js
import axios from 'axios';

axios.interceptors.request.use(config => {
  const token = localStorage.getItem('accessToken');
  if (token) {
    config.headers.Authorization = `Bearer ${token}`;
  }
  return config;
});

axios.interceptors.response.use(
  response => response,
  error => {
    if (error.response && error.response.status === 401) {
      // Handle token refresh or redirect to login
    }
    return Promise.reject(error);
  }
);

export default axios;
