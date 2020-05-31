import Vue from 'vue'
import Vuex from 'vuex'
import axios from 'axios'

Vue.use(Vuex)

export default new Vuex.Store({
  state: {
    videosData: []
  },
  getters: {
    videosDataGetter: state => state.videosData
  },
  actions: {
    getAllVideos ({commit}) {
      return new Promise((resolve, reject) => {
        axios.get('http://localhost:8000/api/getallvideos/').then(res => {
          console.log(res.data)
          resolve(res.data)
          commit('videosDataRecieved', res.data)
        })
        .catch(err => {
          reject(err)
        })
      })
    }
  },
  mutations: {
    videosDataRecieved (state, data) {
      state.videosData = data
    }
  }
})
