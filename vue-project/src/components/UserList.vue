<template>
    <ul>
      <li v-for="user in users" :key="user.id">
        {{ user.name }} - {{ user.email }}
        <button @click="$emit('edit', user)">✏️</button>
        <button @click="$emit('delete', user.id)">🗑️</button>
      </li>
    </ul>
  </template>
  
  <script setup>
  defineProps(['users']);
  defineEmits(['edit', 'delete']);
  </script>
  