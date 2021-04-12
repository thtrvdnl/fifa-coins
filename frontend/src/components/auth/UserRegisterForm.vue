<template>
  <div>
    <b-form @submit.prevent="register" >
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
        label="Ваше имя:"
        label-for="input-2"
        :state="nameState"
        :invalid-feedback="invalidNameFeedback"
      >
        <b-form-input
          id="input-2"
          v-model="full_name"
          :state="nameState"
          placeholder="Enter name"
          required
        />
      </b-form-group>

      <b-form-group
        id="input-group-3"
        label="Пароль:"
        label-for="input-3"
        :state="passwordState"
        :invalid-feedback="invalidPasswordFeedback"
        description="Ваш пароль должен состоять из 6-20 символов, содержать буквы и цифры и не должен содержать пробелов, специальных символов или эмодзи."
      >
        <b-form-input
          id="input-3"
          v-model.trim="password"
          type="password"
          placeholder="Enter password"
          :state="passwordState"
          required
        />
      </b-form-group>

      <b-alert v-if="errorMessage" show variant="danger">{{ errorMessage }}</b-alert>

      <b-button :disabled="!passwordState || !nameState" type="submit" variant="success">
        Отправить
      </b-button>
      <b-button type="reset" variant="danger">
        Сбросить
      </b-button>
    </b-form>
  </div>
</template>

<script>
export default {
  data () {
    this.$store.commit('setError', null)
    return {
      full_name: '',
      email: '',
      password: ''
    }
  },
  methods: {
    register () {
      const data = {
        full_name: this.full_name,
        email: this.email,
        password: this.password
      }
      this.$store.dispatch('register', data)
        .then(() => this.$router.push('/login'))
        .catch(() => {})
    }
  },
  computed: {
    errorMessage () {
      return this.$store.getters.error
    },
    nameState () {
      if (this.full_name.length === 0) {
        return null
      }
      return this.full_name.length > 4
    },
    invalidNameFeedback () {
      if (this.full_name.length < 5) {
        return 'Введите минимум 5 символа.'
      }
      return null
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
