<template>
  <div class="signup">
    <div class="hero is-primary">
      <div class="hero-body has-text-centered">
        <p class="title">Sign Up</p>
      </div>
    </div>

    <section class="section">
      <div class="container">
        <div class="columns">
          <div class="column is-4 is-offset-4">
            <form v-on:submit.prevent="checkForm">
              <!-- <div class="field">
                <label for="username" class="label">Username</label>
                <div class="control has-icons-left">
                  <input
                    type="text"
                    name="username"
                    class="input"
                    v-model="username"
                  />
                  <span class="icon is-small is-left">
                    <i class="fas fa-user"></i>
                  </span>
                </div>
              </div> -->

              <div class="field">
                <label for="email" class="label">Email</label>
                <div class="control has-icons-left">
                  <input
                    type="email"
                    name="email"
                    class="input"
                    v-model="email"
                  />
                  <span class="icon is-small is-left">
                    <i class="fas fa-envelope"></i>
                  </span>
                </div>
              </div>

              <div class="field">
                <label for="password1" class="label">Password</label>
                <div class="control has-icons-left">
                  <input
                    type="password"
                    name="password1"
                    class="input"
                    v-model="password"
                  />
                  <span class="icon is-small is-left">
                    <i class="fas fa-key"></i>
                  </span>
                </div>
              </div>

              <div class="field">
                <label for="password2" class="label"
                  >Confirm Your Password</label
                >
                <div class="control has-icons-left">
                  <input
                    type="password"
                    name="password2"
                    class="input"
                    v-model="password2"
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
                  <button type="submit" class="button is-primary">
                    Submit
                  </button>
                </div>
              </div>
            </form>
            <hr />
            <router-link to="/login">Click here</router-link> to login
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
      errors: [],
      // username: null,
      email: null,
      password: null,
      password2: null,
    };
  },
  mounted() {
    document.title = `SignUp | LMS`;
  },
  methods: {
    checkForm: function () {
      this.errors = [];

      if (!this.email) {
        this.errors.push("Email is required");
      } else if (!this.validEmail(this.email)) {
        this.errors.push("Valid email is required");
      }

      if (!this.password) {
        this.errors.push("Password is required");
      } else if (!this.validPassword(this.password)) {
        this.errors.push("Password doesn't meet the minimum requirements");
      }

      if (!this.password2 && this.password !== this.password2) {
        this.errors.push("Passwords don't match");
      }

      if (!this.errors.length) {
        let formData = {
          username: this.email,
          email: this.email,
          password: this.password,
        };

        axios
          .post(`/api/v1/users/`, formData)
          .then((response) => {
            this.$router.push("/login");
          })
          .catch((error) => {
            // if(error.response){
            //   for (const property in error.response.data ){
            //     this.errors.push(`${property}: ${error.response.data[property]}`)
            //   }
            //   console.log(JSON.stringify(error.response.data));
            // } else if(error.message){
            //   this.errors.push('Something went wrong. Please try again')

            //   console.log(JSON.stringify(error));
            // }
            console.log(error);
          });
      }
    },

    validEmail: function (email) {
      let re =
        /^(([^<>()[\]\\.,;:\s@"]+(\.[^<>()[\]\\.,;:\s@"]+)*)|(".+"))@((\[[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\])|(([a-zA-Z\-0-9]+\.)+[a-zA-Z]{2,}))$/;
      return re.test(email);
    },

    validPassword: function (password) {
      let re = /^(?=.*[a-z])(?=.*[A-Z])(?=.*[0-9])(?=.*[!@#\$%\^&\*])(?=.{8,})/;
      return re.test(password);
    },

    clearError: function () {
      const notification = document.querySelector(".notification");
      notification.parentNode.removeChild(notification);
      console.log("This should be deleted");
    },
  },
};
</script>