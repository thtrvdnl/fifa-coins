<template>
  <div>
    <span class="fa-stack fa-4x">
      <i class="fas fa-circle fa-stack-2x text-primary" />
      <i class="fas fa-shopping-cart fa-stack-1x fa-inverse" v-bind:class="{icon}"/>
    </span>
    <h4 class="service-heading">
      {{ title }}
    </h4>
    <p class="text-muted" v-html="text"></p>
  </div>
</template>

<script>
export default {
  name: 'ItemListIcon',
  props: {
    icon: { default: 'fa-shopping-cart'},
    title: { default: ''},
    text: { default: ''},
  }
}
</script>

<style scoped>

</style>
