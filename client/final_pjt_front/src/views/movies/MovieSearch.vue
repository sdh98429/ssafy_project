<template>
  <div>
    <link rel="stylesheet" href="https://use.fontawesome.com/releases/v5.15.4/css/all.css" integrity="sha384-DyZ88mC6Up2uqS4h/KRgHuoeGwBcD4Ng9SiP4dIRy0EXTlnuz47vAwmeGwVChigm" crossorigin="anonymous">
    <div class="d-flex align-items-center justify-content-center container">
      <div class="w-100">
        <b-form>
          <b-row class="d-flex justify-content-center mt-3">
            <b-col>
                <b-input-group>
                  <b-form-input rm-input id="input-default" placeholder="장르 혹은 영화 제목으로 검색" @keydown.enter.prevent="search" v-model="text" style="border-style: solid; border-color:rgb(25,206,96); border-width:3px;"></b-form-input>
                  <b-button class="submit btn btn-outline-none" @click="search" style="background-color:rgb(25,206,96);"><i class="fas fa-search"></i></b-button>
                </b-input-group>
                <h2 class='d-flex flex-start mx-5'><b>Seach Result..</b></h2>
            </b-col>
          </b-row>
        </b-form>
      </div>
    </div>
    <div class="container">
      <b-card-group deck v-if="movieList.length !== 0" class="mx-2 d-flex justify-content-center">
        <MovieRecommendItem 
          v-for="(movie, idx) in movieList" 
          :key="idx" 
          :movie="movie"
          class="mt-2 col-3"
        />
      </b-card-group>
      <h2 v-if="movieList.length == 0"> 검색 결과가 없습니다...</h2>
      <pre v-if="movieList.length == 0">
                                                                                                                
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
import MovieRecommendItem from '@/components/movie/MovieRecommendItem'
import axios from 'axios'

export default {
  name: 'MovieSearch',
  components: {
    MovieRecommendItem,
  },
  data: function () {
    return {
      searchmovies: null,
      firsttext: this.$route.params.text,
      text: null,
      movieList: [],
    }
  },
  methods: {
    getMovies: function (firsttext) {
      axios({
        method: 'get',
        url: 'http://127.0.0.1:8000/movies/search',
      })
        .then(res => {
          //console.log(res)
          this.searchmovies = res.data
        })
        .then(() => {
          this.text = firsttext
          this.search()
        })
        .catch(err => {
          console.log(err)
        })
      
    },
    search: function () {
      this.movieList = []
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
      if (this.text.trim()) {
        for (let movie of this.searchmovies) {
          // 제목으로 찾기
          if (movie.title.includes(this.text.trim())) {
            this.movieList.push(movie)
          } 
        }
        if (this.text in genre_dict) {
          for (let movie of this.searchmovies) {
            for (let ob of movie.genres) {
              if (this.text.trim() == ob.name) {
                this.movieList.push(movie)
              }
            }
          }
        }
      }
    },
  },
  created: function () {
    this.getMovies(this.firsttext)
  }
}
</script>

<style>
  .header {
    height: 360px;
    background-color: black;
  }
  .submit {
    border-radius: 30px;
  }
</style>