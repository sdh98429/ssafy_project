<template>
  <div>
    <b-card
      no-body
      style="max-width: 20rem; border: none;"
      :img-src="movie.poster_path"
      img-alt=""
      img-top
      img-height="240"
      @click="showDetail"
    >
      <b-card-body style="background-color: black; color:white; height:200px;">
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
    </div>
  </div>
</template>

<script>
import MovieDetail from '@/components/movie/MovieDetail.vue'

export default {
  name: 'MovieRecommendItem',
  props: {
    movie: Object,
  },
  components: {
    MovieDetail,
  },
  data: function () {
      return {
        show: false,
      }
  },
  methods: {
      showDetail: function(){
        this.show = true
      },
  }
}
</script>

<style>

</style>