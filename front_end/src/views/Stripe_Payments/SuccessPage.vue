<template>
  <div class="about">
    <div class="hero is-primary">
      <div class="hero-body has-text-centered">
        <p class="title">Payment Successful</p>
      </div>
    </div>
    <section class="section">
      <p>Welcome to the Premium side</p>
      <hr />
      <router-link to="/courses">Click here</router-link> to view all courses!
    </section>
  </div>
</template>

<script>
export default {
  async mounted() {
    await axios.get("/create_premium_users/").then((response) => {
      console.log(response.data);
    });
    document.title = `Successful | LMS`;
  },
};
</script>