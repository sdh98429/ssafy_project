<template>
  <b-card-group deck class="mx-2 flex-nowrap" style="position:relative; height:440px; overflow-x:scroll; border: none;">
    <video-list-item
      v-for="video in videos"
      :key="video.id.videoId"
      :video="video"
      @select-video="onSelectVideo"
      class="mt-2 col-3"
    >
    </video-list-item>
  </b-card-group>
</template>

<script>
import VideoListItem from '@/components/movie/VideoListItem'
export default {
  name: 'VideoList',
  components: {
    VideoListItem,
  },
  props: {
    videos: {
      type: Array,
      required: true,
    }
  },
  methods: {
    onSelectVideo: function (video) {
      this.$emit('select-video', video)
    }
  }
}
</script>

<style>

</style>