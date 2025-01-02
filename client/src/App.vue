<template>
  <div>
    <RouterLink to="/"></RouterLink>
    <RouterLink to="/login"></RouterLink>
    <!-- <div class="flex flex-col font-Roboto bg-canvas-primary">
      <SiteNavigation />
      <UserManagement />
    </div> -->
      <RouterView /> 
  </div>
</template>

<script setup>
import { RouterView } from "vue-router";

</script>

<style>

</style>