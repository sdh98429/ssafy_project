<template>
  <b-card
      no-body
      style="max-width: 20rem; border: none; height:400px;"
      :img-src="video.snippet.thumbnails.default.url"
      img-alt=""
      img-top
      img-height="240"
      @click="selectVideo"
  >
    <b-card-body>
      <b-card-title class="d-flex"><h5><b>{{ video.snippet.title }}</b></h5></b-card-title>
    </b-card-body>
  </b-card>
</template>

<script>
export default {
  name: 'VideoListItem',
  props: {
    video: {
      type: Object,
      required: true,
    }
  },
  methods: {
    selectVideo: function () {
      this.$emit('select-video', this.video)
    }
  },
}
</script>

<style>

</style>