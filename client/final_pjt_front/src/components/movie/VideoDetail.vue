<template>
  <div v-if="video" class="container">
    <iframe :src="videoUrl" frameborder="0" width="100%" height="1024"></iframe>
    <hr>
  </div>
</template>

<script>
export default {
  name: 'VideoDetail',
  props: {
    video: {
      type: Object,
    }
  },
  computed: {
    videoUrl: function () {
      const videoId = this.video.id.videoId
      return `https://www.youtube.com/embed/${videoId}`
    }
  }
}
</script>

<style>

</style>