<template>
  <div>
    <b-navbar id="mainNav" type="dark" toggleable="lg" class="fixed-top">
      <b-container>
        <NuxtLink class="navbar-brand js-scroll-trigger" to="">
          Fifa coins
        </NuxtLink>
        <b-navbar-toggle target="nav-collapse" class="navbar-toggler navbar-toggler-right">
          Меню
          <i class="fas fa-bars" />
        </b-navbar-toggle>
        <b-collapse id="nav-collapse" is-nav>
          <b-navbar-nav class="text-uppercase ml-auto">
            <b-nav-item href="#">
              Главная
            </b-nav-item>
            <b-nav-item href="#">
              Покупка
            </b-nav-item>
            <b-nav-item href="#">
              Инструкция
            </b-nav-item>
            <b-nav-item href="#">
              Поддержка
            </b-nav-item>
            <b-nav-item href="#">
              Вход
            </b-nav-item>
          </b-navbar-nav>
        </b-collapse>
      </b-container>
    </b-navbar>
    <Nuxt />
  </div>
</template>
