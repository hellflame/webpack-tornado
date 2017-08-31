{{#pug}}
<template lang="pug">
  #app
    img(src="/public/logo.png")
    {{#router}}
    router-view
    {{else}}
    hello
    {{/router}}
</template>
{{else}}
<template>
  <div id="app">
    <img src="/public/logo.png">
    {{#router}}
    <router-view></router-view>
    {{else}}
    <hello></hello>
    {{/router}}
  </div>
</template>
{{/pug}}

<script>
{{#unless router}}
import Hello from './components/Hello'{{#if_eq lintConfig "airbnb"}};{{/if_eq}}

{{/unless}}
export default {
  name: 'app'{{#router}}{{#if_eq lintConfig "airbnb"}},{{/if_eq}}{{else}},
  components: {
    Hello{{#if_eq lintConfig "airbnb"}},{{/if_eq}}
  }{{#if_eq lintConfig "airbnb"}},{{/if_eq}}{{/router}}
}{{#if_eq lintConfig "airbnb"}};{{/if_eq}}
</script>

{{#stylus}}
<style lang="stylus">
@keyframes shake
  0%
    transform rotate(0deg)
  50%
    transform rotate(-5deg)
  100%
    transform: rotate(5deg)

#app
  font-family 'Avenir', Helvetica, Arial, sans-serif
  -webkit-font-smoothing antialiased
  -moz-osx-font-smoothing grayscale
  text-align center
  color #2c3e50
  margin-top 60px

  img:hover
    animation shake .2s ease infinite

</style>
{{else}}
<style>
#app {
  font-family: 'Avenir', Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
  margin-top: 60px;
}
@keyframes shake{
  0%{
    transform: rotate(0deg);
  }
  50%{
    transform: rotate(-5deg);
  }
  100%{
    transform: rotate(5deg);
  }
}
#app img:hover{
  animation: shake .2s ease infinite;
}
</style>
{{/stylus}}
