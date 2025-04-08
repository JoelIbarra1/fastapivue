<template>
  <h1>Gestión de Usuarios</h1>
  <UserForm :userToEdit="userToEdit" @save="handleSave" @cancel="clearEdit" />
  <UserList :users="users" @edit="editUser" @delete="deleteUser" />
</template>

<script setup>
import { ref, onMounted } from 'vue';
import { getUsers, createUser, updateUser, deleteUser as removeUser } from '@/services/api';
import UserForm from '@/components/UserForm.vue';
import UserList from '@/components/UserList.vue';

const users = ref([]);
const userToEdit = ref(null);

const fetchUsers = async () => {
  const response = await getUsers();
  users.value = response.data;
};

onMounted(fetchUsers);

const handleSave = async (user) => {
  if (user.id) {
    await updateUser(user.id, user);
  } else {
    await createUser(user);
  }
  fetchUsers();
  clearEdit();
};

const deleteUser = async (id) => {
  await removeUser(id);
  fetchUsers();
};

const editUser = (user) => {
  userToEdit.value = user;
};

const clearEdit = () => {
  userToEdit.value = null;
};
</script>
