<template>
  <div class="about">
    <div class="hero is-primary">
      <div class="hero-body has-text-centered">
        <p class="title">Payment Cancelled</p>
      </div>
    </div>
    <section class="section">
      <p>Payment was cancelled</p>
      <hr>
      <router-link to="/">Home</router-link>
    </section>
  </div>
</template>

<script>
export default {
  mounted() {
    document.title = `Cancelled | LMS`;
  },
};
</script>