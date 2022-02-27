<template>
  <div class="about">
    <div class="hero is-primary">
      <div class="hero-body has-text-centered">
        <p class="title">Payment Successful</p>
      </div>
    </div>
    <template v-if="$store.state.user.isAuthenticated">
      <section class="section">
        <p>Welcome to the Premium side</p>
        <hr />
        <router-link to="/courses">Click here</router-link> to view all courses!
      </section>
    </template>
    <template v-else>
      <section class="section">
        <p>Oops you need to be logged in to access this page</p>
      </section>
    </template>
  </div>
</template>

<script>
import axios from "axios";
export default {
  async mounted() {
    await axios.get("/api/v1/courses/create_premium_user/").then((response) => {
      console.log(response.data);
    })
    .catch((error) => {
      console.log(error);
    });
    document.title = `Successful | LMS`;
  },
};
</script>