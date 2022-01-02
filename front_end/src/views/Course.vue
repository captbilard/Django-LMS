<template>
  <div class="course">
    <div class="hero is-primary">
      <div class="hero-body has-text-centered">
        <p class="title">{{ course.title }}</p>
      </div>
    </div>

    <section class="section">
      <div class="container">
        <div class="columns content">
          <div class="column is-2">
            <h3>Table of Contents</h3>
            <ul>
              <li v-for="lesson in lessons" :key="lesson.id">
                <a href="#" @click="activeLesson=lesson">{{ lesson.title }}</a>
              </li>
              
            </ul>
          </div>

          <div class="column is-10">
            <template v-if="$store.state.user.isAuthenticated">
              <template v-if="activeLesson">
                <h2>{{activeLesson.title}}</h2>
                <p class="has-text-justified">
                  {{activeLesson.long_description}}
                </p>
              </template>
              <template v-else>
                <!-- <h3>Introduction</h3> -->
                <p class="has-text-justified">
                  {{ course.long_description }}
                </p>
              </template>
            </template>
            <template v-else>
              <h2>Restricted Access</h2>
              <p>Kindly Sign Up or Login to access course content</p>
            </template>
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
      course: {},
      lessons: [],
      activeLesson: null,
    };
  },
  mounted() {
    const baseUrl = "http://127.0.0.1:8000";
    const slug = this.$route.params.slug;
    axios.get(`${baseUrl}/api/v1/courses/${slug}`).then((response) => {
      this.course = response.data.course;
      this.lessons = response.data.lessons;
      console.log(this.course);
      console.log(this.lessons);
    });
  },
};
</script>