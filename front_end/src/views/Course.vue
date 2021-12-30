<template>
    <div class="course">
        <div class="hero is-primary">
            <div class="hero-body has-text-centered">
                <p class="title">The title of the course</p>
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
                        <h3>Introduction</h3>
                        <p class="has-text-justified">
                            Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Sit amet justo donec enim diam vulputate ut pharetra sit. At volutpat diam ut venenatis tellus in. Vestibulum morbi blandit cursus risus. Lectus mauris ultrices eros in cursus turpis. Arcu ac tortor dignissim convallis aenean et tortor at risus. Aliquet risus feugiat in ante metus dictum at. Tortor dignissim convallis aenean et. Turpis nunc eget lorem dolor sed. At in tellus integer feugiat scelerisque varius morbi. 
                        </p>
                        <p class="has-text-justified">
                            Nec dui nunc mattis enim. Amet consectetur adipiscing elit duis. Consectetur a erat nam at lectus urna duis. Dictum at tempor commodo ullamcorper a lacus vestibulum. Volutpat ac tincidunt vitae semper quis. Ut venenatis tellus in metus vulputate eu scelerisque felis. Elit scelerisque mauris pellentesque pulvinar pellentesque habitant. Massa vitae tortor condimentum lacinia quis vel eros donec.
                        </p>

                        <h3>Getting Started</h3>
                        <p class="has-text-justified">
                            Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Sit amet justo donec enim diam vulputate ut pharetra sit. At volutpat diam ut venenatis tellus in. Vestibulum morbi blandit cursus risus. Lectus mauris ultrices eros in cursus turpis. Arcu ac tortor dignissim convallis aenean et tortor at risus. Aliquet risus feugiat in ante metus dictum at. Tortor dignissim convallis aenean et. Turpis nunc eget lorem dolor sed. At in tellus integer feugiat scelerisque varius morbi.
                        </p>
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