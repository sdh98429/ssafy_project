<template>
  <div>
    <link rel="stylesheet" href="https://use.fontawesome.com/releases/v5.15.4/css/all.css" integrity="sha384-DyZ88mC6Up2uqS4h/KRgHuoeGwBcD4Ng9SiP4dIRy0EXTlnuz47vAwmeGwVChigm" crossorigin="anonymous">
    <section>
      <!-- <MovieSearch 
          :searchmovies="searchmovies" 
      /> -->
      <div class="header d-flex align-items-center justify-content-center container mt-5">
        <div class="w-100 col-9">
          <h2 style="color: white;" class='d-flex flex-start'><i class="fab fa-weebly"><b> 와라영화에 오신걸 환영합니다.</b></i></h2>
          <h4 style="color: white;" class='d-flex flex-start'>영화 검색, 영화 추천, 상세정보를 볼 수 있습니다.</h4>
          <br>
          <b-form>
            <b-row class="d-flex justify-content-center mt-3">
              <b-col>
                  <b-input-group>
                    <b-form-input rm-input id="input-default" placeholder="장르 혹은 영화 제목으로 검색" @keydown.enter.prevent="search" v-model="text" style="border-style: solid; border-color:rgb(25,206,96); border-width:3px;"></b-form-input>
                    <b-button class="submit btn btn-outline-none" @click="search" style="background-color:rgb(25,206,96);"><i class="fas fa-search"></i></b-button>
                  </b-input-group>
              </b-col>
            </b-row>
          </b-form>
        </div>
      </div>
    </section>

    <section>
      <div class="container" style="background-color: black;">
        <h2 style="color: white;"><b>What's Popular? <i class="fas fa-fire-alt" style="color:red;"></i></b></h2>
        <div class="scroll container">
          <b-carousel
            id="carousel-1" v-model="slide" :interval="4000" controls
            indicators background="#ababab"
            style="text-shadow: 1px 1px 2px #333;" @sliding-start="onSlideStart"
            @sliding-end="onSlideEnd"
          >
            <!-- Text slides with image -->
            <b-carousel-slide
              v-for="(movie, idx) in popularmovies"
              :key="idx" 
              :caption="movie.title"
              :img-src="movie.poster_path"
              @click="showDetail"
            >
              <h5>평점 : {{ movie.vote_average }}</h5>
              <b-modal v-model="show" :title="movie.title">
                <movie-detail :movie=movie></movie-detail>
              </b-modal>
            </b-carousel-slide>
          </b-carousel>
        </div>
      </div>
    </section>
    
    <section>
      <div class="container mt-3" style="background-color: black;">
        <h2 class='d-flex flex-start mx-5' style="color:white;"><i class="fas fa-film" style="color:#d9f00f;"><b style="color:white;"> Movies</b></i></h2>
        <b-card-group deck class="mx-2 flex-nowrap" style="position:relative; height:485px; overflow-x:scroll; border: none;">
          <MovieListItem 
            v-for="(movie, idx) in movies" 
            :key="idx" 
            :movie="movie"
            class="mt-2 col-3"
          />
        </b-card-group>
      </div>
    </section>
    
    <section>
      <div class="container mt-3" style="background-color: black;">
        <h2 class='d-flex flex-start mx-5'><i class="far fa-play-circle" style="color:#0887f0;"><b style="color:white;"> Now Playing Movies</b></i></h2>
        <b-card-group deck class="mx-2 flex-nowrap" style="border: none; position:relative; height:485px;  overflow-x:scroll;">
          <MovieNowPlaying 
          v-for="(movie, idx) in nowplayingmovies" 
          :key="idx" 
          :movie="movie"
          class="mt-2 col-3"
          />
        </b-card-group>
      </div>
    </section>

  </div>
</template>

<script>
import axios from 'axios'
import MovieListItem from '@/components/movie/MovieListItem'
import MovieNowPlaying from '@/components/movie/MovieNowPlaying'
// import MoviePopular from '@/components/movie/MoviePopular'
import MovieDetail from '@/components/movie/MovieDetail.vue'

export default {
  name: 'MovieList',
  data: function () {
    return {
      movies: null,
      nowplayingmovies: null,
      popularmovies: null,
      slide: 0,
      sliding: null,
      show: false,
      text: null,
    }
  },
  components: {
    MovieListItem,
    MovieDetail,
    MovieNowPlaying,
  },
  props: {
    movie: Object,
  },
  methods: {
    setToken: function () {
      const token = localStorage.getItem('jwt')
      const config = {
            Authorization: `JWT ${token}` 
      }
      return config
    },
    showDetail: function() {
      this.show = true
      console.log('성공')
    },
    getMovies: function () {
      axios({
        method: 'get',
        url: 'http://127.0.0.1:8000/movies/',
      })
        .then(res => {
          //console.log(res)
          this.movies = res.data.slice(0,12)
        })
        .catch(err => {
          console.log(err)
        })
    },
    getNowPlayingMovies() {
      axios({
        method: 'get',
        url: 'http://127.0.0.1:8000/movies/nowplaying/',
      })
        .then(res => {
          this.nowplayingmovies = res.data.slice(0,12)
        })
        .catch(err => {
          console.log(err)
        })
    },
    getPopularMovies() {
      axios({
        method: 'get',
        url: 'http://127.0.0.1:8000/movies/popular/',
      })
        .then(res => {
          this.popularmovies = res.data.slice(0,12)
        })
        .catch(err => {
          console.log(err)
        })
    },
    search() {
      this.$router.push({ name: 'MovieSearch', params: { text: this.text }})
    },
    onSlideStart() {
      this.sliding = true
    },
    onSlideEnd() {
      this.sliding = false
    },

  },

  created: function () {
    this.getMovies()
    this.getNowPlayingMovies()
    this.getPopularMovies()
  }
}
</script>

<style>
  .carousel-item img {
    height: 640px;
    
  }
</style>