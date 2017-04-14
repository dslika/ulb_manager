<template>
  <div id="app">
    <b-navbar toggleable type="inverse" variant="success" fixed="top">
      <b-nav-toggle target="nav_collapse"></b-nav-toggle>

      <router-link to="/" class="navbar-brand">
        <span>BootstrapVue</span>
      </router-link>

      <b-collapse is-nav id="nav_collapse">

        <b-nav is-nav-bar>
          <li class="nav-item">
            <router-link to="/" active-class="active" class="nav-link">Home</router-link>
          </li>
          <li class="nav-item">
            <router-link to="/doc" active-class="active" class="nav-link">Docs</router-link>
          </li>
          <li class="nav-item">
            <router-link to="/contact" active-class="active" class="nav-link">Contact Us</router-link>
          </li>
        </b-nav>

      </b-collapse>
    </b-navbar>
    <div class="container">
      <main-page></main-page>
    </div>
  </div>
</template>

<script>
  export default {
    name: 'base'
  }
</script>
