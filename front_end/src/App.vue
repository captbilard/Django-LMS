<template>
  <div>
    <Nav />
    <router-view />

    <Footer />
  </div>
</template>


<script>
import axios from "axios";
import Nav from "@/components/Nav";
import Footer from "@/components/Footer";

export default {
  name: "App",
  components: {
    Nav,
    Footer,
  },
  // Initialise the vuex before loading the site
  beforeCreate() {
    this.$store.commit("initializeStore");
    const token = this.$store.state.user.token;
    if (token) {
      axios.defaults.headers.common["Authorization"] = token;
    } else {
      axios.defaults.headers.common["Authorization"] = "";
    }
  },
};
</script>


<style lang="scss">
// Configuring Bulma
@import "../node_modules/bulma";
</style>
