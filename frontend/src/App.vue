<template>
  <!-- router-view — это место, куда Quasar будет подставлять ваши страницы -->
  <router-view />
</template>

<script setup>
// Здесь можно инициализировать глобальные настройки, если нужно
defineOptions({
  name: 'App'
});
</script>