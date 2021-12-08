<template>
  <div id="app">
    <link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/bootstrap@4.5.3/dist/css/bootstrap.min.css"
    integrity="sha384-TX8t27EcRE3e/ihU7zmQxVncDAy5uIKz4rEkgIXeMed4M0jlfIDPvg6uqKI2xXr2" crossorigin="anonymous">

    <div id="nav">
      <b-navbar toggleable="lg" type="dark" id="navbar">
        <b-navbar-brand>
          <router-link :to="{ name: 'MovieList'}" >
            <img src="./assets/mainlogo.jpg" alt="" width='100%' height="50px" >
          </router-link>
        </b-navbar-brand>


        <b-collapse id="nav-collapse" is-nav class="d-flex justify-content-between">
          <b-navbar-nav class="d-flex mx-2">
            <router-link :to="{ name: 'ArticleList'}" class="d-flex mx-2">커뮤니티</router-link>
            <router-link :to="{ name: 'MovieRecommend'}" class="d-flex mx-2">추천영화</router-link>
          </b-navbar-nav>

          <!-- Right aligned nav items -->
          <b-navbar-nav>
            <!-- Using 'button-content' slot -->
            <div v-if="isLogin" class="mr-auto">
              <router-link @click.native="logout" :to="{ name: 'MovieList'}" class="nav-margin">Logout</router-link>
            </div>
            <div v-else class="mr-auto">
              <router-link :to="{ name: 'Signup' }" class="mr-auto nav-margin mx-2">Signup</router-link>
              <router-link :to="{ name: 'Login' }" class="mr-auto nav-margin mx-2">Login</router-link>
            </div>
          </b-navbar-nav>
        </b-collapse>
      </b-navbar>
    </div>
    <router-view @login="login = true" />
    <footer>
      <br>
      <p>Copyright © 2021 TEAM ALLBBEME. ALL RIGHTS RESERVED</p>
    </footer>
  </div>

</template>

<script>
export default {
  name: 'App',
  data: function () {
    return {
      isLogin: false,
    }
  },
  created: function () {
    const token = localStorage.getItem('jwt')
    if (token) {
      this.isLogin = true
    }
    this.$router.push({ name : "MovieList"})
  },
  updated: function () {
    const token = localStorage.getItem('jwt')
    if (token) {
      this.isLogin = true
    }
  },

  methods: {
    logout: function () {
      this.isLogin = false
      localStorage.removeItem('jwt')
      this.$router.push({ name: 'Login' })
    },
  },
}
</script>

<style>
@import url('https://fonts.googleapis.com/css2?family=Nanum+Myeongjo&display=swap');
#app {
  font-family: 'Nanum Myeongjo', serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  background-image: url("assets/bg.png");
  text-align: center;
  color: black;
}

#nav {
  background-image: url('assets/bg.png');
}
#nav a {
  font-weight: bold;
  color: white;
}

#nav a.router-link-exact-active {
  color: white;
  
}

</style>
