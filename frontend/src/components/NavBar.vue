<template>
  <b-navbar id="mainNav" type="dark" toggleable="lg" class="fixed-top">
    <b-container>
      <router-link no-prefetch class="navbar-brand js-scroll-trigger" to="/">
        Fifa coins
      </router-link>
      <b-navbar-toggle target="nav-collapse" class="navbar-toggler navbar-toggler-right">
        Меню
        <i class="fas fa-bars" />
      </b-navbar-toggle>
      <b-collapse id="nav-collapse" is-nav>
        <b-navbar-nav class="text-uppercase ml-auto">
          <li class="nav-item">
            <router-link no-prefetch active-class="active" class="nav-link" to="/buy">
              Покупка
            </router-link>
          </li>
          <li class="nav-item">
            <router-link no-prefetch active-class="active" class="nav-link" to="/about">
              Инструкция
            </router-link>
          </li>
          <li v-if="isLoggedIn" class="nav-item" @click="logout">
            <router-link no-prefetch active-class="active" class="nav-link" to="#" >
              Выйти
            </router-link>
          </li>
          <li v-else class="nav-item">
            <router-link no-prefetch active-class="active" class="nav-link" to="/login">
              Войти
            </router-link>
          </li>
        </b-navbar-nav>
      </b-collapse>
    </b-container>
  </b-navbar>
</template>

<script>
export default {
  computed: {
    isLoggedIn () {
      return this.$store.getters.isLoggedIn
    }
  },
  methods: {
    logout () {
      this.$store.dispatch('logout')
        .then(() => { this.$router.push('/login') })
    }
  }
}
</script>
