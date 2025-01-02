import axios from 'axios';
const axiosInstance = axios.create({
    baseURL: 'http://localhost:5001', //alamat backend
    withCredentials: true, //include cookies
});

// Add CSRF token to every request
axiosInstance.interceptors.request.use(config => {
    const csrfToken = document.cookie.split('; ').find(row =>
    row.startsWith('csrf_access_token='))?.split('=')[1];
    if (csrfToken) {
        config.headers['X-CSRF-TOKEN'] = csrfToken;
    }
    return config;
})

export default axiosInstance;