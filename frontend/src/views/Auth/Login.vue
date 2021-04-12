<template>
  <header class="masthead">
    <div class="container">
      <div class="intro-text">
        <UserAuthForm  />
      </div>
    </div>
  </header>
</template>

<script>
import UserAuthForm from '@/components/auth/UserAuthForm'
export default {
  name: 'Login',
  components: { UserAuthForm }
}
</script>
