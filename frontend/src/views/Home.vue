<template>
  <div class="player-container">
    <video width="450" controls :src="src"></video>
    <h3 style="display: block;">Videos List</h3>
    <hr />
    <div v-for="(video, i) in videosData" @click="onClickVideo(video)" :key="i">
      {{video.video_title}}
      <hr />
    </div>
  </div>
</template>

<script>
import {mapGetters} from 'vuex'
export default {
  name: 'Home',
  data: function() {
    return {
      uri: '',
      src: ''
    }
  },
  computed: {
    ...mapGetters({
      videosData: 'videosDataGetter'
    })
  },
  methods: {
    onClickVideo (video) {
      this.src = 'http://localhost:8000' + video.videos
    }
  },
  created () {
    this.$store.dispatch('getAllVideos').then(res => {
      this.src = 'http://localhost:8000'+res[0].videos
    })
  }
}
</script>
