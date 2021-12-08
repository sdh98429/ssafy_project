<template>
  <div class="detail">
    <link rel="stylesheet" href="https://use.fontawesome.com/releases/v5.15.4/css/all.css" integrity="sha384-DyZ88mC6Up2uqS4h/KRgHuoeGwBcD4Ng9SiP4dIRy0EXTlnuz47vAwmeGwVChigm" crossorigin="anonymous">
    <div class="d-flex">
      <img :src="this.poster_path" alt="포스터가 없는 영화입니다." class="col-3" style="height:100%">
      <div class='d-inline-flex flex-column align-items-start col-9'>
        <h1><b>{{ movie.title }}</b></h1>
        <span>개봉일 : {{movie.release_date}}</span>
        <span>평점 : {{movie.vote_average}}</span>
        <span v-if="movie.overview">개요 : {{movie.overview}}</span>
        <span v-else>줄거리가 없는 영화입니다.</span>
      </div>
    </div>
    <div class="container">
      <h2><i class="fab fa-youtube" style="color:red;"></i><b>YOUTUBE TRAILER</b></h2>
      <section>
        <video-detail 
          :video="selectedVideo"
        ></video-detail>
        <br>
        <video-list :videos="videos" @select-video="onVideoSelect"></video-list>
      </section>
    </div>
    <!-- <h2>{{movie.id}}</h2> -->
    <hr>
    <b-card>
      <h2>영화 리뷰</h2>
      <!-- 별점(평점) -->
      <!-- <h2> 리뷰 작성하기</h2> -->
      <div class="d-flex">
        <div class="star-rating space-x-4 d-flex mx-2">
          <input type="radio" id="5-stars" name="rating" value="5" v-model="rate"/>
          <label for="5-stars" class="star pr-4">★</label>
          <input type="radio" id="4-stars" name="rating" value="4" v-model="rate"/>
          <label for="4-stars" class="star">★</label>
          <input type="radio" id="3-stars" name="rating" value="3" v-model="rate"/>
          <label for="3-stars" class="star">★</label>
          <input type="radio" id="2-stars" name="rating" value="2" v-model="rate"/>
          <label for="2-stars" class="star">★</label>
          <input type="radio" id="1-star" name="rating" value="1" v-model="rate"/>
          <label for="1-star" class="star">★</label>
        </div >
        <!-- 좋아요 -->
        <div>
          <label for="like">
            <input type="checkbox" id="like" checked="false" v-model="like" class="input">
            <div class="icon-box" style="background-color: white;">
              <i class="far fa-thumbs-up" aria-hidden="true"></i>
            </div>
          </label>
        </div>
      </div>

      
      <!-- 리뷰 내용 -->
      <b-card class="container">
        <!-- 리뷰 리스트 -->
        <h2>리뷰 목록</h2>
        <div class="d-flex flex-column align-items-center" v-if="reviewList.length == 0">
            <h2>∠( ᐛ 」∠)＿</h2>
            <div>아직 작성된 리뷰가 없어요!</div>
        </div>
        <div class='d-flex flex-column' v-for="(review, idx) in reviewList" :key="idx">
          <p>평점 : {{ review.rate }}</p>
          <div class="d-flex">
            <p @click="loadReview(review)">내용 : {{ review.content }}</p>
            <b-button class="ml-auto mx-2" variant="outline-info" @click="updateReviewLoad(review)"><i class="fas fa-edit"></i></b-button>
            <b-button variant="outline-danger" @click="deleteReview(review, movie)"><i class="fas fa-trash-alt"></i></b-button>
          </div>
          <br>
        </div>
        <div>
          <textarea id="content" style="width:100%;" v-model.trim="content" placeholder="내용을 적어주세요"></textarea>
          <button v-if="!update" @click="addReview(movie)" class="btn d-flex ml-auto" style="color: #009f47; background: rgba(3,119,90,0.12);">등록</button>
          <b-button class="btn d-flex ml-auto" variant="outline-info" v-if="update" @click="updateReview(review, movie)" style="background: rgba(1, 78, 122, 0.12);">수정</b-button>
        </div>
      </b-card>
    </b-card>
  </div>
</template>

<script>
import axios from 'axios'
import _ from 'lodash'
import VideoList from '@/components/movie/VideoList'
import VideoDetail from '@/components/movie/VideoDetail'

const API_KEY = 'AIzaSyCw247AiYlIqASl18FXL48xmlIQLSs-kBA'
const API_URL = 'https://www.googleapis.com/youtube/v3/search'

export default {
  name : 'MovieDetail',
  props: {
    movie: Object
  },
  data: function () {
    return {
      update: false,
      review : null,
      like: false,
      rate: null,
      rate_options: _.range(0,6),
      content: null,
      up_user: null,
      poster_path: null,
      reviewList: [],
      inputValue: null,
      videos: [],
      selectedVideo: null,
    }
  },
  components: {
    VideoList,
    VideoDetail,
  },
  methods: {
    setToken: function () {
      const token = localStorage.getItem('jwt')
      const config = {
        headers: {
            Authorization: `JWT ${token}` 
        }
      }
      return config
    },
    getMovie: function (movie) {
      axios({
        method: 'get',
        url: `http://127.0.0.1:8000/movies/${movie.id}`,
      })
        .then(res => {
          console.log(res)
          this.movie = res.data
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
        movie: movie.id,
        user: this.up_user,
      }
      axios.put(`http://127.0.0.1:8000/movies/${movie.id}/reviews/${review.id}/`, reviewInfo, config)
                .then((res) => {
                  console.log(res)
                  this.getReview(movie)
                })
                .catch((err) => {
                    console.log(reviewInfo)
                    console.log('실패')
                    console.log(err)
                })
      this.update = false
      this.content = null
      this.rate = null
      this.like = false
    },
    updateReviewLoad: function (review) {
      this.review = review
      this.like = review.like
      this.content = review.content
      this.rate = review.rate
      this.update = true
      this.up_user = review.user

      this.update = true

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
    getPoster: function(movie) {
      if (movie.poster_path.includes('https')) {
        this.poster_path = movie.poster_path
      } else {
        const posterId = this.movie.poster_path
        this.poster_path = `https://image.tmdb.org/t/p/w200/${posterId}`
      }
    },
    onInputChange: function (movie) {
      this.inputValue = movie.title + '예고편'
      const params = {
        key: API_KEY,
        part: 'snippet',
        q: this.inputValue,
      }
      axios({
        method: 'get',
        url: API_URL,
        params,
      })
        .then(res => {
          this.videos = res.data.items
        })
        .catch(err => {
          console.log(err)
        })
    },
    onVideoSelect: function (video) {
      this.selectedVideo = video
    },
  },
  created: function () {
    const movie = this.movie
    this.getPoster(movie)
    this.getReview(movie)
    this.onInputChange(movie)
  },
}
</script>

<style>
@import url('https://fonts.googleapis.com/css2?family=Nanum+Myeongjo&display=swap');
  .detail {
    font-family: 'Nanum Myeongjo', serif;
  }
  .input[type="checkbox"]{
    position: absolute;
    opacity: 0;
    cursor: pointer;
  }
  .icon-box{
    width: 45px;
    height: 45px;
    background-color: #101010;
    display: flex;
    justify-content: center;
    align-items: center;
    border: 3px solid #000;
    border-radius: 10px;
    transition: 0.5s;
  }

  .icon-box .fa{
    font-size: 30px;
    color: #222;
    transition: 0.5s;
  }
  .input[type="checkbox"]:checked ~ .icon-box{
    background-color: #000;
    border: 3px solid #fff;
    box-shadow: 0 0 10px rgba(33,156,243,.5),
          0 0 20px rgba(33,156,243,.5),
          0 0 30px rgba(33,156,243,.5);
    
  }
  .input[type="checkbox"]:checked ~ .icon-box .fa{
    color: #fff;
    text-shadow: 0 0 10px rgba(33,156,243,.8),
          0 0 10px rgba(33,156,243,1);
  }
  .star-rating {
    display: flex;
    flex-direction: row-reverse;
    font-size: 2.25rem;
    line-height: 2.5rem;
    justify-content: space-around;
    padding: 0 0.2em;
    text-align: center;
    width: 5em;
  }
  
  .star-rating input {
    display: none;
  }
  
  .star-rating label {
    -webkit-text-fill-color: transparent; /* Will override color (regardless of order) */
    -webkit-text-stroke-width: 2.3px;
    -webkit-text-stroke-color: #2b2a29;
    cursor: pointer;
  }
  
  .star-rating :checked ~ label {
    -webkit-text-fill-color: gold;
  }
  
  .star-rating label:hover,
  .star-rating label:hover ~ label {
    -webkit-text-fill-color: #fff58c;
  }
</style>