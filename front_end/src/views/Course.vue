<template>
    <div class="course">
        <div class="hero is-primary">
            <div class="hero-body has-text-centered">
                <p class="title"> {{course.title}} </p>
            </div>
        </div>

        <section class="section">
            <div class="container">
                <div class="columns content">
                    <div class="column is-2">
                        <h3>Table of Contents</h3>
                        <ul>
                            <li><a href="#">Introduction</a></li>
                            <li><a href="#">Getting Started</a></li>
                            <li><a href="#">Part 1</a></li>
                            <li><a href="#">Part 2</a></li>
                            <li><a href="#">Part 3</a></li>
                            <li><a href="#">Summary</a></li> 

                        </ul>
                    </div>

                    <div class="column is-10">
                        <template v-if="$store.state.user.isAuthenticated">
                            <h3>Introduction</h3>
                            <p class="has-text-justified">
                                {{ course.long_description }}
                            </p>
                        </template>
                        <template v-else>
                            <h2>Restricted Access</h2>
                            <p>
                                Kindly Sign Up or Login to access course content
                            </p>
                        </template>
                    </div>
                </div>
            </div>
        </section>
    </div>
    
</template>

<script>
import axios from 'axios'
export default {
  data(){
    return{
      course: []
    }
  },
  mounted(){
    const baseUrl = "http://127.0.0.1:8000"
    const slug = this.$route.params.slug
    axios.get(`${baseUrl}/api/v1/courses/${slug}`)
    .then(response =>{
      this.course = response.data
      console.log(response.data);
    })
  }
}
</script>