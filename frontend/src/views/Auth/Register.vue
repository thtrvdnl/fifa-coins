<template>
  <header class="masthead">
    <div class="container">
      <div class="intro-text">
        <UserRegisterForm />
      </div>
    </div>
  </header>
</template>

<script>
import UserRegisterForm from '@/components/auth/UserRegisterForm'
export default {
  name: 'Register',
  components: { UserRegisterForm }
}
</script>

<style scoped>

</style>
