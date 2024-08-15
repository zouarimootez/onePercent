// src/auth.js
export function isAuthenticated() {
    return !!localStorage.getItem('access_token');
  }
  