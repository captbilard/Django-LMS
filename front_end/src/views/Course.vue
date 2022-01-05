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
                <a href="#" @click="setActiveLesson(lesson)">{{ lesson.title }}</a>
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
                <hr>
                <article class="media box" v-for="comment in comments" :key="comment.id">
                  <div class="media-content">
                    <div class="content">
                      <p>
                        <strong>{{ comment.name }}</strong> {{ comment.created_at }} <br>
                          {{comment.content}}
                      </p>
                    </div>
                  </div>
                </article>

                <form v-on:submit.prevent="submitForm">
                  <div class="field">
                    <label for="name" class="label">Name</label>
                    <div class="control">
                      <input type="text" name="name" class="input" v-model="comment.name">
                    </div>
                  </div>
                  <div class="field">
                    <label for="comment" class="label">Comment</label>
                    <div class="control">
                      <textarea name="comment" class="textarea" v-model="comment.content"></textarea>
                    </div>
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
const baseUrl = "http://127.0.0.1:8000"
export default {
  data() {
    return {
      course: {},
      lessons: [],
      comments: [],
      activeLesson: null,
      comment: {
        name:'',
        content:'',
      }
    };
  },
  mounted() {
    //const baseUrl = "http://127.0.0.1:8000";
    const slug = this.$route.params.slug;
    axios.get(`${baseUrl}/api/v1/courses/${slug}`).then((response) => {
      this.course = response.data.course;
      this.lessons = response.data.lessons;
    });
  },
  methods:{
    submitForm: function(){
      //const baseUrl = "http://127.0.0.1:8000";
      const formData = this.comment
      axios.post(`${baseUrl}/api/v1/courses/${this.course.slug}/${this.activeLesson.slug}/`, formData)
      .then(response => {
        this.comment.name = ''
        this.comment.content = ''
        alert("This comment was added!")
      })
      .catch(error =>{
        console.log(error);
      })
    },

    setActiveLesson : function(lesson){
      // loads the current lesson and get the comments for that lesson
      this.activeLesson = lesson
      this.getComments()
    },

    getComments:function (){
      axios.get(`${baseUrl}/api/v1/courses/${this.course.slug}/${this.activeLesson.slug}/get-comments/`)
      .then(response =>{
        console.log(response.data)
        this.comments = response.data
      })
      .catch(error => {
        console.log(error);
      })
    }
  }
};
</script>