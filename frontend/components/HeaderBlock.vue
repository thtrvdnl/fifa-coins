<template>
  <!-- Header -->
  <header class="masthead">
    <div class="container">
      <div class="intro-text">
        <div class="intro-lead-in">
          {{ title }}
        </div>
        <div class="intro-heading text-uppercase">
          {{ bigTitle }}
        </div>
        <NuxtLink class="btn btn-primary btn-xl text-uppercase js-scroll-trigger" to="">
          {{ buttonText }}
        </NuxtLink>
      </div>
    </div>
  </header>
</template>

<script>
export default {
  name: 'HeaderBlock',
  data () {
    return {
      title: 'Добро пожаловать на FIFA COINS',
      bigTitle: 'It\'s Nice To Meet You',
      buttonText: 'Купить монеты'
    }
  }
}
</script>

<style scoped>

</style>
