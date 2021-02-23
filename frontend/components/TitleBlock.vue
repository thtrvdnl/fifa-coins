<template>
  <b-row>
    <b-col cols="12" class="text-center">
      <h2 v-if="title" class="section-heading text-uppercase">
        {{ title }}
      </h2>
      <h3 v-if="subtitle" class="section-subheading text-muted">
        {{ subtitle }}
      </h3>
    </b-col>
  </b-row>
</template>

<script>
export default {
  name: 'TitleBlock',
  props: {
    title: { default: '' },
    subtitle: { default: '' }
  }
}
</script>

<style scoped>

</style>
