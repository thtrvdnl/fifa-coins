<template>
  <section class="page-section" :class="{'bg-light': light}">
    <b-container>
      <slot />
    </b-container>
  </section>
</template>

<script>
export default {
  name: 'BlockWrap',
  props: {
    light: { default: false }
  }
}
</script>
