<template>
  <div class="card">
    <div class="card-image">
      <figure class="image is-4by3">
        <img src="../assets/placeholder.jpg" alt="Learning Image" />
      </figure>
    </div>
    <div class="card-content">
      <div class="media">
        <div class="media-content">
          <p class="title is-5">
            {{ course.title }}
          </p>
        </div>
      </div> 
      <div class="content">
        <p>
          {{ course.short_description }}
        </p>
        <p class="has-text-left">
          <router-link :to="{ name: 'Course', params: { slug: course.slug } }"
            >More</router-link
          >
        </p>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  props: ["course"],
};
</script>