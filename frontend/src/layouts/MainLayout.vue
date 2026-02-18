<template>
  <q-layout view="lHh Lpr lFf">
    <q-header elevated>
      <q-toolbar>
        <q-toolbar-title>My App</q-toolbar-title>
      </q-toolbar>
    </q-header>

    <q-page-container>
      <!-- БЕЗ ЭТОГО ТЕГА БУДЕТ БЕЛЫЙ ЭКРАН -->
      <router-view />
    </q-page-container>
  </q-layout>
</template>

<script setup>
defineOptions({ name: 'MainLayout' })
</script>