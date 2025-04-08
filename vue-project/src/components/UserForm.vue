<template>
    <form @submit.prevent="handleSubmit">
      <input v-model="form.name" placeholder="Nombre" required />
      <input v-model="form.email" placeholder="Correo" required />
  
      <button type="submit">{{ isEdit ? 'Actualizar' : 'Agregar' }}</button>
      <button v-if="isEdit" @click="cancelEdit" type="button">Cancelar</button>
    </form>
  </template>
  
  <script setup>
  import { ref, watch } from 'vue';
  
  const props = defineProps(['userToEdit']);
  const emit = defineEmits(['save', 'cancel']);
  
  const form = ref({ name: '', email: '' });
  const isEdit = ref(false);
  
  watch(() => props.userToEdit, (newUser) => {
    if (newUser) {
      form.value = { ...newUser };
      isEdit.value = true;
    }
  });
  
  function handleSubmit() {
    emit('save', form.value);
    form.value = { name: '', email: '' };
    isEdit.value = false;
  }
  
  function cancelEdit() {
    emit('cancel');
    form.value = { name: '', email: '' };
    isEdit.value = false;
  }
  </script>
  