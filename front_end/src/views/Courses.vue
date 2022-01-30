<template>
  <div class="courses">
    <div class="hero is-primary">
      <div class="hero-body has-text-centered">
        <p class="title">Courses</p>
      </div>
    </div>

    <section class="section">
      <div class="container">
        <div class="columns">
          <div class="column is-2">
            <aside class="menu">
              <p class="menu-label">Categories</p>
              <ul class="menu-list">
                <li @click="setActiveCategory(category)">
                  <a > All Courses </a>
                </li>
                <li
                  v-for="category in categories"
                  :key="category.id"
                  @click="setActiveCategory(category)"
                >
                  <a >{{
                    category.title
                  }}
                  </a>
                </li>
              </ul>
            </aside>
          </div>

          <div class="column is-10">
            <div class="columns is-multiline">
              <div
                class="column is-4"
                v-for="course in courses"
                :key="course.id"
              >
                <CourseItem v-bind:course="course" />
              </div>

              <div class="column is-12">
                <nav class="pagination">
                  <a href="" class="pagination-previous">Previous</a>
                  <a href="" class="pagination-next">Next Page</a>
                  <ul class="pagination-list">
                    <li>
                      <a
                        href="#"
                        class="pagination-link is-current"
                        aria-label="Page 1"
                        aria-current="1"
                        >1</a
                      >
                    </li>
                    <li>
                      <a
                        href="#"
                        class="pagination-link"
                        aria-label="Goto Page 2"
                        >2</a
                      >
                    </li>
                    <li>
                      <a
                        href="#"
                        class="pagination-link"
                        aria-label="Goto Page 3"
                        >3</a
                      >
                    </li>
                  </ul>
                </nav>
              </div>
            </div>
          </div>
        </div>
      </div>
    </section>
  </div>
</template>

<script>
import axios from "axios";
import CourseItem from "@/components/CourseItem.vue";
export default {
  data() {
    return {
      courses: [],
      categories: [],
      activeCategory: null,
    };
  },
  components: {
    CourseItem,
  },
  async mounted() {
    await axios
      .get("/api/v1/courses/get_categories")
      .then((response) => {
        this.categories = response.data;
      })
      .catch((error) => {
        console.log(error);
      });
    this.getCourses()
  },
  methods: {
    setActiveCategory: function (category) {
      console.log(category);
      this.activeCategory = category
      this.getCourses()
    },
    getCourses: function () {
      let url = "/api/v1/courses/";
      if(this.activeCategory){
        url += `?category_id=${this.activeCategory.id}`
      }
      axios
        .get(url)
        .then((response) => {
          this.courses = response.data;
        })
        .catch((error) => {
          console.log(error);
        });
    },
  },
};
</script>