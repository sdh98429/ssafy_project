<template>
  <div>
    <img :src="movie.poster_path"  alt="" width="250">
    <h2>{{ movie.title }}</h2>
    <!-- 리뷰 넣을 공간 -->
    
  </div>
</template>

<script>
export default {
  name: 'MoviePopular',
  props: {
    movie: Object,
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