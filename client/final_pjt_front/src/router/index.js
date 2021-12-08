import Vue from 'vue'
import VueRouter from 'vue-router'
import Signup from '@/views/accounts/Signup'
import Login from '@/views/accounts/Login'
import ArticleList from '@/views/articles/ArticleList'
import CreateArticle from '@/views/articles/CreateArticle'

import ArticleDetail from '@/components/ArticleDetail'

import MovieList from '@/views/movies/MovieList'
import MovieRecommend from '@/views/movies/MovieRecommend'
import MovieSearch from '@/views/movies/MovieSearch'
import MovieDetail from '@/components/movie/MovieDetail'
//import MovieNowPlaying from '@/components/movie/MovieNowPlaying'
// import MoviePopular from '@/components/movie/MoviePopular'


Vue.use(VueRouter)

const routes = [
  {
    path: '/articles',
    name: 'ArticleList',
    component: ArticleList,
  },
  {
    path: '/articles/create',
    name: 'CreateArticle',
    component: CreateArticle,
  },
  {
    path: '/articles/:articleId',
    name: 'ArticleDetail',
    component: ArticleDetail,
  },
  {
    path: '/accounts/signup',
    name: 'Signup',
    component: Signup,
  },
  {
    path: '/accounts/login',
    name: 'Login',
    component: Login,
  },
  {
    path: '/movies/:movieId',
    name: 'MovieDetail',
    component: MovieDetail,
  },
  {
    path: '/movies',
    name: 'MovieList',
    component: MovieList,
  },
//  {
//    path: '/movies/nowplaying',
//    name: 'MovieNowPlaying',
//  component: MovieNowPlaying,
//  },
//  {
//    path: '/movies/popular',
//    name: 'MoviePopular',
//    component: MoviePopular,
//  },
  {
    path: '/movies/recommend',
    name: 'MovieRecommend',
    component: MovieRecommend,
  },
  {
    path: '/movies/search',
    name: 'MovieSearch',
    component: MovieSearch,
  },
  
]

const router = new VueRouter({
  mode: 'history',
  base: process.env.BASE_URL,
  routes
})

export default router
