<template>
  <div >
    <div class="container" style="background-color: white">
      <b-card>
        <div v-if= "article" class="container">
          <div class="row d-flex">
            <div class="media" style="width: 100%; word-break:break-all;">
              <div class="media-body text-justify">
                <h2 class="mt-0">{{article.title}}</h2>
                <p>작성자: {{article.user.username}}</p>
                <p>작성일: {{$moment(article.created_at).format('YYYY-MM-DD hh:mm:ss')}} | 수정일 : {{$moment(article.updated_at).format('YYYY-MM-DD hh:mm:ss')}}</p>
                <hr>
                <p>{{article.content}}</p>
              </div>
            </div>
          </div>
        </div>

        <!-- <div v-if="article">
          <h2>{{article.title}}</h2>
          <div>{{article.content}}</div>
          <div>{{article.image}}</div>
        </div> -->
        
        <br>
        <b-card>
          <span><h4 class="d-flex">총 {{comments.length}}개의 댓글이 있습니다.</h4></span>
          <!-- <h4 class="d-flex">댓글 목록</h4> -->
          <div v-if="comments.length == 0">
            <h2>∠( ᐛ 」∠)＿</h2>
            <div>아직 작성된 댓글이 없어요!</div>
          </div>
          <div v-for="(comment, idx) in comments" :key="idx">
            <div class="media-body">
              <strong class="d-flex"> {{comment.user.username}}</strong>
              <div class="d-flex" style="width: 100%; text-align: left;">{{comment.content}} <b-button class="btn ml-auto" variant="outline-danger" @click="deleteComment(comment)">X</b-button> </div> 
              <span class="d-flex">{{$moment(comment.created_at).format('YYYY-MM-DD hh:mm:ss')}}</span>
              <hr>
            </div>
          </div>
          <div class="d-flex">
            <textarea class="form-control" :onkeyup="fn_checkByte(this.content)" v-if="isLogin" type="text" style="width:100%;" v-model.trim="content" placeholder="댓글을 작성해주세요!"></textarea>
            <textarea class="form-control" :onkeyup="fn_checkByte(this.content)" v-if="!isLogin" type="text" style="width:100%;" v-model.trim="content" placeholder="로그인 해주세요!"></textarea>
          </div>
          <div class="d-flex justify-content-end">
            <div>(<span id="nowByte">{{ this.content.length }}</span>/300bytes)</div>
            <button @click="createComment" class="btn" style="color: #009f47; background: rgba(3,119,90,0.12);">등록</button>
          </div>
        </b-card>
      </b-card>
      
      <div class="buttons d-flex">
        <b-button class="mx-2 mt-1" variant="outline-info" @click="updateArticle" style="background: rgba(1, 78, 122, 0.12);">글 수정</b-button>
        <b-button class="mx-2 mt-1" variant="outline-danger" @click="deleteArticle" style="background: rgba(126, 8, 8, 0.12);">글 삭제</b-button>
        <button class="btn button ml-auto" @click="goToArticleList" style="color: #009f47; background: rgba(3,119,90,0.12);">글 목록</button>
      </div>
    </div>

  </div>
</template>

<script>
import axios from 'axios'

export default {
  name : 'ArticleDetail',
  data: function (){
    return {
      // articleId: this.$route.params.articleId,
      article: null,
      comments : null,
      content: '',
      isLogin: false,
    }
  },
  methods: {
    setToken: function(){
      const token = localStorage.getItem('jwt')

      const config = {

        Authorization: `JWT ${token}`
      }
      return config
    },

    goToArticleList: function(){
      this.$router.push({name: 'ArticleList'})
    },

    getArticle: function () {
      axios({
        method: 'get',
        url: `http://127.0.0.1:8000/articles/` + this.$route.params.articleId,
        // headers: this.setToken()
      })
        .then(res => {
          console.log(res)
          this.article = res.data
        })
        .catch(err => {
          console.log(err)
        })
    },

    updateArticle: function(){
      if (this.isLogin) {
        axios({
          method: 'put',
          url: `http://127.0.0.1:8000/articles/` + this.$route.params.articleId +`/update_delete/`,
          headers: this.setToken()
        })
          .then(res => {
            console.log(res)
            this.$router.push({name: 'CreateArticle', query:this.article, params: {update : true, articleId: this.$route.params.articleId}})
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

    deleteArticle: function(){
      if (this.isLogin) {
        axios({
          method: 'delete',
          url: `http://127.0.0.1:8000/articles/` + this.$route.params.articleId +`/update_delete/`,
          headers: this.setToken()
        })
          .then(res => {
            console.log(res)
            this.$router.push({name: 'ArticleList'})
          })
          .catch(err => {
            console.log(err)
            alert('본인 게시글만 삭제할 수 있습니다.')
          })
      } else {
        alert('로그인 해주세요!')
        this.$router.push({name: "Login"}) 
      }
    },

    getComments: function () {
      axios({
        method: 'get',
        url: `http://127.0.0.1:8000/articles/` + this.$route.params.articleId +'/comments/',
        // headers: this.setToken()
      })
        .then(res => {
          console.log(res)
          this.comments = res.data
        })
        .catch(err => {
          console.log(err)
        })
    },

    createComment: function(){
      if (this.isLogin) {
        const commentItem = {
          content : this.content
        }
  
        if (commentItem.content){
          axios({
            method: 'post',
            url: `http://127.0.0.1:8000/articles/` + this.$route.params.articleId +'/comments/',
            data: commentItem,
            // config: config,
            headers: this.setToken()
          })
            .then(res => {
              console.log(res)
              this.content = ''
              this.getComments()
            })
            .catch(err => {
              console.log(err)
            })
        }
      } else {
        alert('로그인 후 댓글을 작성하실 수 있습니다!')
        this.$router.push({name: "Login"})
      }
      // const config = this.setToken()
    },

    deleteComment: function(comment){
      if (this.isLogin){
        axios({
          method: 'delete',
          url: `http://127.0.0.1:8000/articles/` + this.$route.params.articleId +'/comments/' + comment.id,
          headers: this.setToken()
        })
          .then(res => {
            console.log(res)
            this.getComments()
            alert('댓글이 삭제되었습니다.')
          })
          .catch(err => {
            console.log(err)
            alert('본인 댓글이 아닙니다.')
          })
      } else {
        alert('로그인 후 댓글을 삭제하실 수 있습니다!')
        this.$router.push({name: "Login"})
      }
    },
    fn_checkByte: function(obj){
      const maxByte = 300; //최대 300바이트
      const text_len = obj.length; //입력한 문자수
      let totalByte=0;
      for(let i=0; i<text_len; i++){
        const each_char = obj.charAt(i);
        const uni_char = escape(each_char) //유니코드 형식으로 변환
          if(uni_char.length>4){
              totalByte += 1;
          }else{
              totalByte += 1;
          }
      } 
      
      if (totalByte>maxByte) {
        this.content = this.content.slice(1,299)
        alert('최대 300Byte까지만 입력가능합니다.');
      }
    },
  },
  created: function(){
    const token = localStorage.getItem('jwt')
    if (token) {
      this.isLogin = true
    }
    this.getArticle()
    this.getComments()
  },

}
</script>

<style>

</style>