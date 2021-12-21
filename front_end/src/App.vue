<template>
<div>
  <nav class="navbar" role="navigation" aria-label="main navigation" style="min-height:5rem;">
    <div class="navbar-brand" >
      <a href="/" class="navbar-item is-size-4">LMS</a>
    </div>

    <div class="navbar-menu" id="navbar-item">
      <div class="navbar-start">
        <a href="/" class="navbar-item">Home</a>
        <a href="/about" class="navbar-item">About</a>
      </div>

      <div class="navbar-end">
        <div class="navbar-item">
          <div class="buttons">
            <a href="#" class="button is-primary"><strong>Sign Up</strong></a>
            <a href="#" class="button is-light">Login</a>
          </div>
        </div>
      </div>
     
    </div>

  </nav>
  <router-view/>

  <footer>
    <div class="content has-text-centered">
      <p>Designed by Bilard. Copyright (c) 2021</p>
    </div>
  </footer>
</div>
</template>

<style lang="scss">
// Configuring Bulma
@import '../node_modules/bulma';
</style>
