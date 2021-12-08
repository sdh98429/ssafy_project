<template>
  <div>
    <link rel="stylesheet" href="https://use.fontawesome.com/releases/v5.15.4/css/all.css" integrity="sha384-DyZ88mC6Up2uqS4h/KRgHuoeGwBcD4Ng9SiP4dIRy0EXTlnuz47vAwmeGwVChigm" crossorigin="anonymous">
    <div class="container">
      <h1 class="my-3" style="color: white">자유게시판</h1>
      
      <div class="row">
        <table class="table table-hover table-striped" style="width: 100%; table-layout: fixed;">
          <thead class="table-secondary">
            <tr>
              <th>게시글 번호</th>
              <th>제목</th>
              <th>작성자</th>
              <th>게시일</th>
              <th>관리</th>

            </tr>
          </thead>
          <tbody v-for="article in articles" :key="article.id" class="table-light">
            <tr>
              <td>{{article.id}}</td>
              <td @click="goToArticleDetail(article)" style="overflow:hidden;white-space:nowrap;text-overflow:ellipsis;">{{article.title}}</td>
              <td>{{article.user.username}}</td>
              <!-- <th>{{article.created_at}}</th> -->
              <!-- <th>{{article.created_at|date 'D'}}</th> -->
              <td>{{$moment(article.created_at).format('YYYY-MM-DD hh:mm:ss')}}</td>
              <!-- <th>등록일 : {{ board.created_at | moment('YYYY-MM-DD HH:mm:ss') }}</th> -->
              <td>
                <b-button @click="updateArticle(article)" class="article-btn" variant="outline-info"><i class="fas fa-edit"></i></b-button>
                <b-button @click="deleteArticle(article)" class="article-btn" variant="outline-danger"><i class="fas fa-trash-alt"></i></b-button>
              </td>
            </tr>
          </tbody>
        </table>
      </div>
      <div class="row">
        <div v-if="isLogin" class="ml-auto">
          <router-link  outer-link :to="{ name: 'CreateArticle'}"><b-button class="font-1-5-em my-2" variant="outline-dark"><i class="fas fa-pen">글 작성</i></b-button></router-link> 
        </div>
      </div>



      <!-- <ul>
        <li v-for="article in articles" :key="article.id">
          <router-link :to="{name: 'ArticleDetail', params: {articleId: article.id }}">{{article.id}}</router-link>
          <div @click="goToArticleDetail(article)">
            <span>
            {{ article.title }}
            </span>
            <span>
            {{ article.content }}
            </span>
            <span>
            {{ article.image }}
            </span>
            <button @click="deleteArticle(article)" class="article-btn">X</button>
          </div>
          <hr>
        </li>
      </ul>
      <button @click="getArticles">Get Articles</button> -->
    </div>
  
  </div>

</template>

<script>
import axios from 'axios'


export default {
  name: 'ArticleList',
  components: {
    
  },
  data: function () {
    return {
      articles: null,
      isLogin: false,
    }
  },
  methods: {
    setToken: function () {
      const token = localStorage.getItem('jwt')
      const config = {
        Authorization: `JWT ${token}` 
      }
      return config
    },
    getArticles: function () {
      axios({
        method: 'get',
        url: 'http://127.0.0.1:8000/articles/',
        // headers: this.setToken()
      })
        .then(res => {
          console.log(res.data)
          this.articles = res.data
        })
        .catch(err => {
          console.log(err)
        })
    },

    deleteArticle: function (article) {
      console.log(article)
      axios({
        method: 'delete',
        url: `http://127.0.0.1:8000/articles/${article.id}/update_delete/`,
        headers: this.setToken()
      })
        .then(res => {
          console.log(res)
          this.getArticles()
        })
        .catch(err => {
          console.log(err)
        })
    },

    updateArticle: function(article){
      if (this.isLogin) {
        axios({
          method: 'put',
          url: `http://127.0.0.1:8000/articles/` + article.id +`/update_delete/`,
          headers: this.setToken()
        })
          .then(res => {
            console.log(res)
            this.$router.push({name: 'CreateArticle', query:article, params: {update : true, articleId: article.id}})
          })
          .catch(err => {
            console.log(err)
            alert('본인 게시글만 수정할 수 있습니다.')
          })
      } else {
        alert('로그인 해주세요!')
        this.$router.push({name: "Login"}) 
      }
    },

    goToArticleDetail(article) {
      this.$router.push({path: `/articles/${article.id}`, article:article})
      // this.$router.push({path: `/articles/${article.id}`, query:article})
    }
  },
  created: function () {
    const token = localStorage.getItem('jwt')
    if (token) {
      this.isLogin = true
    }
    this.getArticles()
  }
}
</script>

<style scoped>
  .article-btn {
    margin-left: 10px;
  }

  .is-completed {
    text-decoration: line-through;
    color: rgb(112, 112, 112);
  }


</style>
