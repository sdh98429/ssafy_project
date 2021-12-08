<template>
  <div>
    <b-card
      no-body
      style="max-width: 20rem; border: none; height:400px;"
      :img-src="movie.poster_path"
      img-alt=""
      img-top
      img-height="240"
      @click="showDetail"
      
    >
      <b-card-body style="background-color:black; color:white;">
        <b-card-title><h5><b>{{ movie.title }}</b></h5></b-card-title>
        <b-card-text>
          <p>개봉일 : {{ movie.release_date }}</p>  
          <p>평점 : {{ movie.vote_average }}</p>
        </b-card-text>
      </b-card-body>
    </b-card>

    <!-- 리뷰 -->
    <div>
      <div>
        <b-modal size="xl" v-model="show">
          <movie-detail :movie=movie></movie-detail>
        </b-modal>
      </div>

      <!-- <h2>영화 리뷰</h2> -->
      <!-- 별점(평점) -->
      <!-- <div>
        <label for="rate">별점</label>
        <select v-model="rate" id="rate">
          <option v-for="(num, idx) in rate_options" :key="idx">{{ num }}</option>
        </select>점
      </div>
      <br> -->
      <!-- 좋아요 -->
      <!-- <div>
        <label for="like">추천</label>
        <input type="checkbox" id="like" checked="false" v-model="like">
      </div> -->
      <!-- 리뷰 내용 -->
      <!-- <div>
        <textarea id="content" cols="30" rows="10" v-model.trim="content" placeholder="내용을 적어주세요"></textarea>
        <button @click="addReview(movie)">등록</button>
      </div> -->
      <!-- 리뷰 리스트 -->
      <!-- <div v-for="(review, idx) in reviewList" :key="idx">
        <p @click="loadReview(review)">{{ review.content }}</p>
        <button @click="updateReview(review, movie)">수정</button>
        <button @click="deleteReview(review, movie)">삭제</button>
      </div> -->
    </div>
  </div>
</template>

<script>
  import axios from 'axios'
  import _ from 'lodash'
  import MovieDetail from '@/components/movie/MovieDetail.vue'

  export default {
    name: 'MovieListItem',
    components: {
      MovieDetail
    },
    props: {
      movie: Object,
    },
    data: function () {
      return {
        like: false,
        moviedetail: null,
        rate: null,
        rate_options: _.range(0,11),
        content: null,
        reviewList: [],
        show: false,
      }
    },
    methods: {
      showDetail: function(){
        this.show = true
      },
      
      setToken: function () {
        const token = localStorage.getItem('jwt')
        const config = {
          headers: {
            Authorization: `JWT ${token}` 
          }
        }
        return config
      },

      getMovie: function () {
        axios({
          method: 'get',
          url: `http://127.0.0.1:8000/movies/` + this.$route.params.movieId,
        })
          .then(res => {
            // console.log(res)
            this.moviedetail = res.data
          })
          .catch(err => {
            console.log(err)
          })
      },
      addReview: function (movie) {
        const reviewInfo = {
          content: this.content,
          rate: this.rate,
          like: this.like,
        }
        const config = this.setToken()
        axios.post(`http://127.0.0.1:8000/movies/${movie.id}/reviews/add`, reviewInfo, config)
          .then(() => {
            this.getReview(movie)
            this.content = null
            this.like = false
            this.rate = null
          })
          .catch((err) => {
              console.log(err)
          })
      },
      getReview: function (movie) {
        axios.get(`http://127.0.0.1:8000/movies/${movie.id}/reviews/`)
          .then(res => {
            // console.log(res.data)
            this.reviewList = res.data
          })
          .catch((err) => {
              console.log(err)
          })
      },
      loadReview: function (review) {
        this.content = review.content
        this.rate = review.rate
        this.like = review.like
      },
      updateReview: function (review, movie) {
        const config = this.setToken()
        const reviewInfo = {
          content: this.content,
          rate: this.rate,
          like: this.like,
        }
        axios.put(`http://127.0.0.1:8000/movies/${movie.id}/reviews/${review.id}/`, reviewInfo, config)
          .then((res) => {
            console.log(res)
          })
          .catch((err) => {
              console.log(err)
          })
      },
      deleteReview: function (review, movie) {
        const config = this.setToken()
        const movieId = movie.id
        axios.delete(`http://127.0.0.1:8000/movies/${movieId}/reviews/${review.id}/`, config)
          .then(() => {
            console.log('성공')
            this.getReview(movie)
          })
          .catch((err) => {
              console.log(err)
          })
      },

    },
    created: function () {
      const movie = this.movie
      this.getReview(movie)
    }
    
      
  }
</script>

<style scoped>
</style>