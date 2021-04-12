<template>
  <div id="app">
    <NavBar />
    <router-view />
  </div>
</template>

<style>
@import "assets/css/agency.css";
@import "assets/fontawesome-free/css/all.min.css";

</style>

<script>
import NavBar from './components/NavBar'

export default {
  components: { NavBar }
}
</script>
