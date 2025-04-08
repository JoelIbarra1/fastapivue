import axios from 'axios';

const api = axios.create({
  baseURL: 'http://127.0.0.1:8000', // Tu backend FastAPI
});

export const getUsers = () => api.get('/users');
export const createUser = (data) => api.post('/users', data);
export const updateUser = (id, data) => api.put(`/users/${id}`, data);
export const deleteUser = (id) => api.delete(`/users/${id}`);
