<template>
  <div class="container" style="background-color : white;">
    <h2 v-if="!update" class="mt-3 d-flex justify-content-center"><b>게시글 작성하기</b></h2>
    <h2 v-else class="my-3"><b>게시글 수정하기</b></h2>
    <hr>
    <div class="container">
      <div class="justify-content-center">
          <!-- <label for="title" class="col-2">제목: </label> -->
          <div class="d-flex justify-content-center mx-5">
            <b-form-input 
            rm-input id="input-default" 
            placeholder="제목을 적어주세요."
            v-model.trim="title"
            >
            </b-form-input>
          </div>
        <br>
        <b-card class="d-flex justify-content-center mx-5">
          <p>❣와라무비 회원이 함께하는 공간입니다❣</p>
          <p>① 광고 및 음란성 게시글 작성 금지</p>
          <p>② 타 회원을 비방하는 글 작성 금지</p>
          <p>③ 논란 조장 글 작성 금지(ex. 정치, 성차별 이슈 등)</p>
          <p>④ 게시판 목적에 맞는 글 작성</p>
          <p>※ 위 사항에 해당하는 게시글은 예고없이 삭제됩니다.</p>
        </b-card>
        <br>
        <div class="d-flex justify-content-center mx-5">
          <b-form-textarea
            id="textarea"
            v-model.trim="content"
            placeholder="내용을 적어주세요."
            rows="4"
            max-rows="4"
          ></b-form-textarea>
        </div>
        
        <br>
        <!-- <div class="row">
          <label for="image" class="col-2">이미지: </label>
          <div class="">
            <input 
              type="text" 
              v-model.trim="image" 
              id="image"
            >
          </div>
        </div> -->

      </div>
      <button class="btn button" v-if="!update" @click="createArticle">등록</button>
      <button class="btn button" v-if="update" @click="updateArticle">수정</button>
    </div>
  </div>
</template>

<script>
import axios from'axios'

export default {
  name: 'CreateArticle',
  data: function () {
    const update = this.$route.params.update
    return {
      update: update,
      title: update ? this.$route.query.title : null,
      content: update ? this.$route.query.content : null,
      // image: update ? this.$route.query.image : null,
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
    createArticle: function () {
      const articleItem = {
        title: this.title,
        content: this.content,
        // image: this.image,
      }
      console.log('user', this.user)
      if (articleItem.title) {
        axios({
          method: 'post',
          url: 'http://127.0.0.1:8000/articles/',
          data: articleItem,
          headers: this.setToken()
        })
          .then(() => {
            this.$router.push({ name: 'ArticleList' })
          })
          .catch(err => {
            console.log(err)
          })
      }
    },
    updateArticle: function () {
      const articleItem = {
        title: this.title,
        content: this.content,
        // image: this.image,
      }
      console.log('user', this.user)
      console.log('aritcleId', this.$route.params.articleId)
      if (articleItem.title) {
        axios({
          method: 'put',
          url: 'http://127.0.0.1:8000/articles/' + this.$route.params.articleId + '/update_delete/',
          data: articleItem,
          headers: this.setToken()
        })
          .then(() => {
            this.$router.push({ name: 'ArticleList' })
          })
          .catch(err => {
            console.log(err)
          })
      }
    }
  }
}
</script>

<style scoped>
  .button {
    background: rgba(3,119,90,0.12);
    color: #009f47;
  }
</style>
