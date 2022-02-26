<template>
  <div class="home">
    <div class="hero is-primary is-medium">
      <div class="hero-body has-text-centered">
        <p class="title">Welcome to L.M.S</p>
        <p class="subtitle">The central location for your child's learning</p>
      </div>
    </div>

    <section class="section">
      <div class="container">
        <div class="columns is-multiline">
          <div class="column is-4">
            <div class="box has-text-centered">
              <span class="icon is-size-2 has-text-success">
                <i class="far fa-clock"></i>
              </span>
              <h2 class="is-size-4 my-4">Learn at your pace</h2>
              <p class="is-size-6">When you want</p>
            </div>
          </div>

          <div class="column is-4">
            <div class="box has-text-centered">
              <span class="icon is-size-2 has-text-success">
                <i class="far fa-comments"></i>
              </span>
              <h2 class="is-size-4 my-4">Learn with others</h2>
              <p class="is-size-6">Interact with others</p>
            </div>
          </div>

          <div class="column is-4">
            <div class="box has-text-centered">
              <span class="icon is-size-2 has-text-success">
                <i class="fas fa-home"></i>
              </span>
              <h2 class="is-size-4 my-4">Learn from home</h2>
              <p class="is-size-6">Wherever you want</p>
            </div>
          </div>

          <div class="column is-12 has-text-centered">
            <template v-if="$store.state.user.isAuthenticated">
              <p class="has-text-weight-bold is-capitalized is-size-4 mt-4">
                Get lifetime access to all courses by going Premium for only
                $100
              </p>
              <a @click="goPremium()" class="button is-primary is-size-3 my-6"
                >Go Premium
              </a>
            </template>
            <template v-else>
              <a
                @click="$router.push('sign-up')"
                class="button is-primary is-size-3 my-6"
                >Click To Get Started</a
              >
            </template>
          </div>

          <hr />

          <div class="column is-3" v-for="course in courses" :key="course.id">
            <CourseItem v-bind:course="course" />
          </div>
        </div>
      </div>
    </section>
  </div>
</template>

<script>
// @ is an alias to /src
import axios from "axios";
import CourseItem from "@/components/CourseItem.vue";

export default {
  name: "Home",
  data() {
    return {
      courses: [],
      stripe: null,
    };
  },
  components: {
    CourseItem,
  },
  async mounted() {
    await axios
      .get(`/api/v1/courses/get_frontpage_courses/`)
      .then((response) => {
        this.courses = response.data;
        // console.log(response.data);
      });

    await this.getPublishableKey();
  },
  methods: {
    getPublishableKey: function () {
      axios
        .get("/api/v1/courses/get_publishable_key/")
        .then((response) => {
          this.stripe = Stripe(response.data.publicKey);
          console.log("Worked");
        })
        .catch((error) => {
          console.log(error);
        });
    },
    goPremium: function () {
      console.log("Go Premium");
    },
  },
};
</script>
