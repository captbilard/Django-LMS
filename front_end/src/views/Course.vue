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
                <a href="#" @click="setActiveLesson(lesson)">{{
                  lesson.title
                }}</a>
              </li>
            </ul>
          </div>

          <div class="column is-10">
            <template v-if="$store.state.user.isAuthenticated">
              <template v-if="activeLesson">
                <h2>{{ activeLesson.title }}</h2>
                <p class="has-text-justified">
                  {{ activeLesson.long_description }}
                </p>
                <hr />
                <template v-if="activeLesson.lesson_type === 'Quiz'">
                  <h2>{{quiz.question}}</h2>
                  <div class="control">
                    <label class="radio">
                      <input type="radio" name="selectedAnswer" :value="quiz.option1" v-model="selectedAnswer">
                      {{quiz.option1}}
                    </label>
                  </div>
                  <div class="control">
                    <label class="radio">
                      <input type="radio" name="selectedAnswer" :value="quiz.option2" v-model="selectedAnswer">
                        {{quiz.option2}}
                    </label>
                  </div>
                  <div class="control">
                    <label class="radio">
                      <input type="radio" name="selectedAnswer" :value="quiz.option3" v-model="selectedAnswer">
                        {{quiz.option3}}
                    </label>
                  </div>
                  <div class="control mt-4 mb-4">
                    <button class="button is-info">Submit</button>
                  </div>

                </template>

                <article
                  class="media box"
                  v-for="comment in comments"
                  :key="comment.id"
                >
                  <div class="media-content">
                    <div class="content">
                      <p>
                        <strong>{{ comment.name }}</strong>
                        {{ comment.created_at }} <br />
                        {{ comment.content }}
                      </p>
                    </div>
                  </div>
                </article>

                <form v-on:submit.prevent="submitForm">
                  <div class="field">
                    <label for="name" class="label">Name</label>
                    <div class="control">
                      <input
                        type="text"
                        name="name"
                        class="input"
                        v-model="comment.name"
                      />
                    </div>
                  </div>
                  <div class="field">
                    <label for="comment" class="label">Comment</label>
                    <div class="control">
                      <textarea
                        name="comment"
                        class="textarea"
                        v-model="comment.content"
                      ></textarea>
                    </div>
                  </div>
                  <div
                    class="notification is-danger"
                    v-for="error in errors"
                    :key="error"
                  >
                    <p>{{ error }}</p>
                  </div>
                  <div class="field">
                    <div class="control">
                      <button class="button is-link">Submit</button>
                    </div>
                  </div>
                </form>
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
      comments: [],
      errors: [],
      quiz: {},
      selectedAnswer: "",
      activeLesson: null,
      comment: {
        name: "",
        content: "",
      },
    };
  },
  async mounted() {
    const slug = this.$route.params.slug;

    await axios.get(`/api/v1/courses/${slug}`).then((response) => {
      this.course = response.data.course;
      this.lessons = response.data.lessons;
    });

    document.title = `${this.course.title} | LMS`;
  },
  methods: {
    submitForm: function () {
      this.errors = [];
      if (this.comment.name == "") {
        this.errors.push("The name should be filled out");
      }
      if (this.comment.content == "") {
        this.errors.push("The content should be filled out");
      }

      if (!this.errors.length) {
        const formData = this.comment;
        axios
          .post(
            `/api/v1/courses/${this.course.slug}/${this.activeLesson.slug}/`,
            formData
          )
          .then((response) => {
            this.comment.name = "";
            this.comment.content = "";
            this.comments.push(response.data);
          })
          .catch((error) => {
            console.log(error);
          });
      }
    },

    setActiveLesson: function (lesson) {
      // loads the current lesson and get the comments for that lesson
      this.activeLesson = lesson;
      if(this.activeLesson.lesson_type == "Quiz"){
        this.getQuiz()
      }else{
        this.getComments();
      }
    },

    getComments: function () {
      axios
        .get(
          `/api/v1/courses/${this.course.slug}/${this.activeLesson.slug}/get-comments/`
        )
        .then((response) => {
          this.comments = response.data;
        })
        .catch((error) => {
          console.log(error);
        });
    },
    getQuiz : function(){
      axios.get(`/api/v1/courses/${this.course.slug}/${this.activeLesson.slug}/get-quiz/`)
      .then((response) => {
        console.log(response.data);
        this.quiz = response.data

      })
      .catch((error) => {
        console.log(error);
      })
    }
  },
};
</script>