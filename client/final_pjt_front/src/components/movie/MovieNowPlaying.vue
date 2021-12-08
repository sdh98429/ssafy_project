<template>
  <div>
    <b-card
      no-body
      style="max-width: 20rem; border: none; height:400px;"
      :img-src="posterUrl"
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
    <!-- 리뷰 넣을 공간 -->
    <div>
      <div>
        <b-modal size="xl" v-model="show">
          <movie-detail :movie=movie></movie-detail>
        </b-modal>
      </div>
    </div>
  </div>
</template>

<script>
import MovieDetail from '@/components/movie/MovieDetail.vue'

export default {
  name: 'MovieNowPlaying',
  props: {
    movie: Object,
  },
  components: {
      MovieDetail
  },
  data: function () {
      return {
        show: false,
      }
  },
  computed: {
    posterUrl() {
      const posterId = this.movie.poster_path
      return `https://image.tmdb.org/t/p/w200/${posterId}`
    }
  },
  methods: {
      showDetail: function(){
        this.show = true
      },
  },
  // 디테일, 리뷰 데이터 삽입
  // data: function () {
  //   return {
      
  //   }
  // },
  

}
</script>

<style>

</style>