<template>
  <div class="login">
    <div class="hero is-primary">
      <div class="hero-body has-text-centered">
        <p class="title">Login</p>
      </div>
    </div>

    <section class="section">
      <div class="container">
        <div class="columns">
          <div class="column is-4 is-offset-4">
            <form v-on:submit.prevent="checkForm">
              <div class="field">
                <label for="email" class="label">Email</label>
                <div class="control has-icons-left">
                  <input
                    type="email"
                    name="email"
                    class="input"
                    v-model="username"
                  />
                  <span class="icon is-small is-left">
                    <i class="fas fa-envelope"></i>
                  </span>
                </div>
              </div>

              <div class="field">
                <label for="password" class="label">Password</label>
                <div class="control has-icons-left">
                  <input
                    type="password"
                    name="password"
                    v-model="password"
                    class="input"
                  />
                  <span class="icon is-small is-left">
                    <i class="fas fa-key"></i>
                  </span>
                </div>
              </div>

              <div class="notification is-danger" v-if="errors.length">
                <button class="delete" v-on:click="clearError"></button>
                <p v-for="error in errors" v-bind:key="error">
                  {{ error }}
                </p>
              </div>

              <div class="field">
                <div class="control">
                  <button type="submit" class="button is-primary">Login</button>
                </div>
              </div>
            </form>

            <hr />
            <router-link to="/sign-up">Click here</router-link> to sign up!
          </div>
        </div>
      </div>
    </section>
  </div>
</template>

<script>
import axios from "axios";
export default {
  data() {
    return {
      username: null,
      password: null,
      errors: [],
    };
  },

  methods: {
    checkForm: function () {
      this.errors = [];
      // Set the token headers to none
      axios.defaults.headers.common["Authorization"] = "";

      //remove token from previous session
      localStorage.removeItem("token");

      if (!this.username) {
        this.errors.push("Email is required");
      }
      if (!this.password) {
        this.errors.push("Password is required");
      }

      if (!this.errors.length) {
        let formData = {
          username: this.username,
          password: this.password,
        };

        this.loginForm(formData);
      }
    },

    loginForm: function (formData) {
      const baseUrl = "http://127.0.0.1:8000";
      axios
        .post(`${baseUrl}/api/v1/token/login/`, formData)
        .then((response) => {
          //get the token from the sever
          const token = response.data.auth_token;
          console.log(token);
          // update it in the store through mutations
          this.$store.commit("setToken", token);

          //set the token to the header using axios
          axios.defaults.headers.common["Authorization"] = `Token ${token}`;
          console.log(axios.defaults.headers.common["Authorization"])
          // save it in localstorage incase of user refreshes
          localStorage.setItem("token", token);

          this.$router.push("/dashboard/my-account");
        })
        .catch((error) => {
          if (error.response) {
            for (const property in error.response.data) {
              this.errors.push(`${property}: ${error.response.data[property]}`);
            }
            console.log(JSON.stringify(error.response.data));
          } else if (error.message) {
            this.errors.push("Something went wrong. Please try again");

            console.log(JSON.stringify(error));
          }
        });
    },
  },
};
</script>