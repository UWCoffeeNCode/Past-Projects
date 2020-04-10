<template>
  <div id="app">
    <Navbar />
    <router-view/>
  </div>
</template>

<script>
import Navbar from './components/Navbar'

export default {
  name: 'App',
  components: {
    Navbar
  }
}
</script>
<style>
  .content-section {
    margin-top: -3.25rem;
    padding-top: 3.25rem;
  }
</style>
