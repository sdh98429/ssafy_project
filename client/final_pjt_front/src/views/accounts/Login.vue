<template>
  <div class="container">
    <img src="../../assets/mainlogo.jpg" alt="" width="35%">
    <div>
      <label class="d-flex mx-auto col-6" for="username"><b>아이디</b></label>
      <b-form-input 
        class="d-flex mx-auto col-6"
        type="text"
        rm-input 
        id="username" 
        v-model="credentials.username"
        style="border-style: solid; border-width:2px;"
      ></b-form-input>
      <br>
    </div>
    <div>
      <label class="d-flex mx-auto col-6" for="password"><b>비밀번호</b></label>
      <b-form-input 
        class="d-flex mx-auto col-6"
        type="password" 
        rm-input 
        id="password" 
         v-model="credentials.password"
        style="border-style: solid; border-width:2px;"
        @keyup.enter="login"
      ></b-form-input>
      <br>
    </div>
    
    <button class="btn col-6" style="background-color:rgb(25,206,96); color:white;" @click="login">로그인</button>
  </div>
</template>

<script>
import axios from 'axios'

export default {
  name: 'Login',
  data: function () {
    return {
      credentials: {
        username: null,
        password: null,
      }
    }
  },
  methods: {
    login: function () {
      axios({
        method: 'post',
        url: 'http://127.0.0.1:8000/accounts/api-token-auth/',
        data: this.credentials
      })
        .then(res => {
          console.log(res)
          localStorage.setItem('jwt', res.data.token)
          this.$emit('login')
          this.$router.push({ name: 'ArticleList' })
        })
        .catch(err => {
          console.log(err)
        })
    }
  }
}
</script>

<style scoped>
  label {
    color:white;
  }
</style>