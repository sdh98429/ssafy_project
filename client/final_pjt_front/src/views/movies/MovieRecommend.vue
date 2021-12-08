<template>
  <div class="mt-3">
    <link rel="stylesheet" href="https://use.fontawesome.com/releases/v5.15.4/css/all.css" integrity="sha384-DyZ88mC6Up2uqS4h/KRgHuoeGwBcD4Ng9SiP4dIRy0EXTlnuz47vAwmeGwVChigm" crossorigin="anonymous">
    <b-form>
      <b-row class="d-flex justify-content-center mt-3">
        <b-col class="col-9">
            <b-input-group>
              <b-form-input rm-input id="input-default" placeholder="장르 혹은 영화 제목으로 검색" @keydown.enter.prevent="getGenre" v-model="genre" style="border-style: solid; border-color:rgb(25,206,96); border-width:3px;"></b-form-input>
              <b-button class="submit btn btn-outline-none" @click="getGenre" style="background-color:rgb(25,206,96);"><i class="fas fa-search"></i></b-button>
            </b-input-group>
        </b-col>
      </b-row>
    </b-form>
    <button @click="setData(1)" class="mx-2 button btn btn-outline-none"><i class="fas fa-hashtag" style="color:white;"><b style="color:white;"> 좋아</b></i></button>
    <button @click="setData(2)" class="mx-2 button btn btn-outline-none"><i class="fas fa-hashtag" style="color:white;"><b style="color:white;"> 나른나른</b></i></button>
    <button @click="setData(3)" class="mx-2 button btn btn-outline-none"><i class="fas fa-hashtag" style="color:white;"><b style="color:white;"> 슬퍼ㅠ</b></i></button>
    <button @click="setData(4)" class="mx-2 button btn btn-outline-none"><i class="fas fa-hashtag" style="color:white;"><b style="color:white;"> 짜증나!</b></i></button>
    <button @click="setData(5)" class="mx-2 button btn btn-outline-none"><i class="fas fa-hashtag" style="color:white;"><b style="color:white;"> 행복해</b></i></button>
    <br>
    <button @click="getDate(1)" class="mx-2 button btn btn-outline-none"><i class="fas fa-hashtag" style="color:white;"><b style="color:white;"> 1980년대</b></i></button>
    <button @click="getDate(2)" class="mx-2 button btn btn-outline-none"><i class="fas fa-hashtag" style="color:white;"><b style="color:white;"> 1990년대</b></i></button>
    <button @click="getDate(3)" class="mx-2 button btn btn-outline-none"><i class="fas fa-hashtag" style="color:white;"><b style="color:white;"> 2000년대</b></i></button>
    <button @click="getDate(4)" class="mx-2 button btn btn-outline-none"><i class="fas fa-hashtag" style="color:white;"><b style="color:white;"> 2010년대</b></i></button>
    <button @click="getDate(5)" class="mx-2 button btn btn-outline-none"><i class="fas fa-hashtag" style="color:white;"><b style="color:white;"> 2020년대</b></i></button>
    <div v-if="recommend" class="container" >
      <b-card-group deck class="mx-2 d-flex justify-content-center">
        <MovieRecommendItem 
          v-for="(movie, idx) in recommend" 
          :key="idx" 
          :movie="movie"
          class="mt-2 col-3"
        />
      </b-card-group>
    </div>
    <div>
      <!-- <h2 v-if="!search">ㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡ</h2> -->
      <h2 v-if="!search">ƪ( ˘ ⌣˘ )ʃ</h2>
      <h2 v-if="!search">태그를 눌러주세요~♬</h2>

      <h2 v-if="recommend.length == 0 && search"> 검색 결과가 없습니다...</h2>
      <pre v-if="recommend.length == 0 && search">
                                                                                                                
                      .;!:.                                 
                    :;:;;;:*     .$*;*!.                    
                  ,~;:::::::;!--*::::::;,                   
                 -;:::::::::::!;:::::::::                   
                .~::::::;;;;:::!:::::::::=                  
                :::::;;;::::!!;!:;;!!!!;::                  
               .!::::;::::::::;;;;;!!!!;::;,                
               $::::::::::::::;:;;:::::::::;$.              
              ,:::::::::!:!*!;!!!!!;;;;*$$*;;;,             
             -*;:::::::;!!;;!;!!;!$;*;;;;!;:;*;.            
            ;:;:::::;=;;;:::::;::::;:::::;;;;:!,            
           -::::::::;;!;::;;~*#!  .!~-:-~=@*~ :~            
          .::::::::;*=!*!.,*=;@@;  !   :@!@@#  .            
          -;::::::::::;-   =@@;,@:.    ;@@!:@! $            
          ;:::::::::::;!~-~$@#$*$;;:,,-*@*====:.            
          ;:::::::::::;;!!;;!!!!!*;:::;;!;:::;..            
         $:::::::::::::::::;;;;!;::::::::::;;               
         ;:::::::::::::::::::;;*::::;!;;!!;;                
         ;:::::::::::::::::!*;;::::::;;;;;;!.               
         :::::::::::::::::::::::::::::::::::~               
         ::::::::::::::::::::::::::::::::::::,              
         ::::::::::::::::::::::::::::::::::::;              
         :::::::::::;;;;;;;:::::::::::::::::;;.             
         ::::::::::;!:~~~;!;;**;::::::::::!!;!-             
         ;:::::::::*~:;;:~~~~~:~::*$$$$$;:~~~;-             
         ;:::::::::=~~~~~:;!:~~:::~~~~~::::~;~              
         ::::::::!;!!****::~~~~;;::~~::::;;:;               
         ;:::::::;;:;;;;;;;!#;:~~~~~~~~~~~~~=               
         .!:::::::;!::::::::::;;!*===*!;;~;-                
         .**;::::::::::::::::::::::::::!~                   
         ..;;*!::::::::::::::::::::::;!.                    
         .  ,;!;*;:;;!;;:::::::::;!:;,.                     
         .    ,-;*;;;!;;:;;;;;;;;!~~                        
         .         ,~;*=*;;;;;!=:.  :.                      
         .                           ,.                     
         ,                            ,,                    
         ,                            .,.                   
         -,,,,,,,,,,,,,,,,,,,,,,,,,,,,,-.                   

      </pre>
    </div>
  </div>
</template>

<script>
import axios from 'axios'
import MovieRecommendItem from '@/components/movie/MovieRecommendItem'

export default {
  name: 'MovieRecommend',
  components: {
    MovieRecommendItem,
  },
  data: function () {
    return {
      movies: null,
      recommend: [],
      genre: null,
      date: null,
      search: false,
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
    getGenre: function () {
      this.recommend = []
      this.search = true
      const genre_dict = {
        '액션': '28', '모험': '12', 
        '애니메이션': '16', '코미디': '35',
        '범죄': '80', '다큐멘터리': '99', 
        '드라마': '18', '가족': '10751',
        '판타지': '14', '역사': '36', 
        '공포': '27', '음악': '10402',
        '미스터리': '9648', '로맨스': '10749', 
        'SF': '878', 'TV 영화': '10770',
        '스릴러': '53', '전쟁': '10752', 
        '서부': '37',
      }
      if (this.genre in genre_dict) {
        this.getRecommend()
      }
      for (let movie of this.movies) {
        if (movie.title.includes(this.genre)) {
          this.recommend.push(movie)
        }
      }
      this.genre = null
    },
    getRecommend: function () {
      this.recommend = []
      // 영화 중에 장르가 같은 영화데이터 불러오기
      for (let movie of this.movies) {
        for (let ob of movie.genres) {
          if (this.genre == ob.name) {
            this.recommend.push(movie)
          }
        }
      }

    },
    getMovies: function () {
      axios({
        method: 'get',
        url: 'http://127.0.0.1:8000/movies/recommend/',
        // headers: this.setToken()
      })
        .then(res => {
            // 모든 영화 불러오고
            this.movies = res.data
        })
        .catch(err => {
            console.log(err)
        })
    },
    getDate: function (num) {
      if (num === 1) {
        this.date = '198'
      } else if (num === 2) {
        this.date = '199'
      } else if (num === 3) {
        this.date = '200'
      } else if (num === 4) {
        this.date = '201'
      } else {
        this.date = '202'
      }
      this.recommend = []
      // 영화 중에 년도가 같은 영화데이터 불러오기
      for (let movie of this.movies) {
        if (movie.release_date.includes(this.date)) {
          this.recommend.push(movie)
        }
      }
    },
    setData: function (num) {
      if (num === 1) {
        this.genre = '액션'
      } else if (num === 2) {
        this.genre = '모험'
      } else if (num === 3) {
        this.genre = '코미디'
      } else if (num === 4) {
        this.genre = '판타지'
      } else {
        this.genre = '로맨스'
      }
      this.getGenre()
    },

  },
  created: function () {
    this.getMovies()
  }
}
</script>

<style>
  .button {
    opacity: 0.8;
    transition: 0.3s;
    border: none;
    padding: 10px 20px;
    text-align: center;
    text-decoration: none;
    display: inline-block;
    font-size: 12px;
    margin: 4px 2px;
    cursor: pointer;
  }

  .button:hover {opacity: 1}
</style>