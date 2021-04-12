<template>
  <div>
    <b-form @submit.prevent="login">
      <b-form-group
        id="input-group-1"
        label="Адрес электронной почты:"
        label-for="input-1"
      >
        <b-form-input
          id="input-1"
          v-model="email"
          type="email"
          placeholder="Enter email"
          required
        />
      </b-form-group>

      <b-form-group
        id="input-group-2"
        label="Пароль:"
        label-for="input-2"
        :state="passwordState"
        :invalid-feedback="invalidPasswordFeedback"
        description="Ваш пароль должен состоять из 6-20 символов, содержать буквы и цифры и не должен содержать пробелов, специальных символов или эмодзи."
      >
        <b-form-input
          id="input-2"
          v-model.trim="password"
          type="password"
          placeholder="Enter password"
          :state="passwordState"
          required
        />
      </b-form-group>

      <b-alert v-if="errorMessage" show variant="danger">{{ errorMessage }}</b-alert>

      <b-button type="submit" variant="success">
        Войти
      </b-button>
      <router-link class="btn btn-info" to="/register">
        Зарегистрироваться
      </router-link>
    </b-form>
  </div>
</template>

<script>
export default {
  data () {
    this.$store.commit('setError', null)
    return {
      email: '',
      password: ''
    }
  },
  methods: {
    login () {
      const email = this.email
      const password = this.password
      this.$store.dispatch('login', { email, password })
        .then(() => this.$router.push('/'))
        .catch(() => {})
    }
  },
  computed: {
    errorMessage () {
      return this.$store.getters.error
    },
    passwordState () {
      if (this.password.length === 0) {
        return null
      }
      return this.password.length > 5 && this.password.length < 21
    },
    invalidPasswordFeedback () {
      if (this.password.length < 6 && this.password.length < 21) {
        return 'Ваш пароль должен состоять минимум из 6 символов.'
      }
      return 'Ваш пароль должен состоять максимум из 20 символов.'
    }
  }
}

</script>
