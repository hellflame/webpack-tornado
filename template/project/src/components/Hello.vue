{{#pug}}
<template lang="pug">
  .hello
    h1 \{{ msg }}
    h2 Essential Links
    ul
      li
        a(href="https://gitter.im/vuejs/vue", target="_blank") Gitter Chat
      li
        a(href="https://twitter.com/vuejs", target="_blank") Twitter
      br
      li
        a(href="http://vuejs-templates.github.io/webpack/",target="_blank") Docs for This Template
    h2 Ecosystem
    ul
      li
        a(href="http://router.vuejs.org/", target="_blank") vue-router
      li
        a(href="http://vuex.vuejs.org/", target="_blank") vuex
      li
        a(href="http://vue-loader.vuejs.org/", target="_blank") vue-loader
      li
        a(href="https://github.com/vuejs/awesome-vue", target="_blank") awesome-vue
    h2 Config Options
    ul#config
      li Project Name:
        b {{ name }}
      li Project Desc:
        b {{ description }}
      li Author:
        b \{{ author }}
      li Vue Build:
        b {{ build }}
      li Using Router:
        b {{ router }}
      li Using Stylus:
        b {{ stylus }}
      li Using Pug:
        b {{ pug }}
      li Using Lint:
        b {{ lint }}
      {{#lint}}
      li Lint Config:
        b {{ lintConfig }}
      {{/lint}}
      {{#unit}}
      li unit tests with Karma + Mocha
      {{/unit}}
      {{#e2e}}
      li e2e tests with Nightwatch
      {{/e2e}}
</template>
{{else}}
<template>
  <div class="hello">
    <h1>\{{ msg }}</h1>
    <h2>Essential Links</h2>
    <ul>
      <li><a href="https://vuejs.org" target="_blank">Core Docs</a></li>
      <li><a href="https://forum.vuejs.org" target="_blank">Forum</a></li>
      <li><a href="https://gitter.im/vuejs/vue" target="_blank">Gitter Chat</a></li>
      <li><a href="https://twitter.com/vuejs" target="_blank">Twitter</a></li>
      <br>
      <li><a href="http://vuejs-templates.github.io/webpack/" target="_blank">Docs for This Template</a></li>
    </ul>
    <h2>Ecosystem</h2>
    <ul>
      <li><a href="http://router.vuejs.org/" target="_blank">vue-router</a></li>
      <li><a href="http://vuex.vuejs.org/" target="_blank">vuex</a></li>
      <li><a href="http://vue-loader.vuejs.org/" target="_blank">vue-loader</a></li>
      <li><a href="https://github.com/vuejs/awesome-vue" target="_blank">awesome-vue</a></li>
    </ul>
    <h2>Config Options</h2>
    <ul id="options">
      <li>Project Name: <b>{{ name }}</b></li>
      <li>Project Desc: <b>{{ description }}</b></li>
      <li>Author: <b>\{{ author }}</b></li>
      <li>Vue Build: <b>{{ build }}</b></li>
      <li>Using Router: <b>{{ router }}</b></li>
      <li>Using Stylus: <b>{{ stylus }}</b></li>
      <li>Using Pug: <b>{{ pug }}</b></li>
      <li>Using Lint: <b>{{ lint }}</b></li>
      {{#lint}}
      <li>Lint Config: <b>{{ lintConfig }}</b></li>
      {{/lint}}
      {{#unit}}
      <li>unit tests with Karma + Mocha</li>
      {{/unit}}
      {{#e2e}}
      <li>e2e tests with Nightwatch</li>
      {{/e2e}}
      </ul>
  </div>
</template>
{{/pug}}

<script>
export default {
  name: 'hello',
  data{{#unless_eq lintConfig "airbnb"}} {{/unless_eq}}() {
    return {
      author: '{{ author }}',
      msg: 'Welcome to Your Vue.js with Tornado App'{{#if_eq lintConfig "airbnb"}},{{/if_eq}}
    }{{#if_eq lintConfig "airbnb"}};{{/if_eq}}
  }{{#if_eq lintConfig "airbnb"}},{{/if_eq}}
}{{#if_eq lintConfig "airbnb"}};{{/if_eq}}
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
{{#stylus}}
<style lang="stylus" scoped>
h1, h2
  font-weight normal

ul
  list-style-type none
  padding 0
  li
    display inline-block
    margin 0 10px
    a
      color #42b983

ul#options
  width 30%
  margin auto
  text-align left
  li
    border-bottom 1px dashed silver
    display block
    b
      float right

</style>
{{else}}
<style scoped>
h1, h2 {
  font-weight: normal;
}

ul {
  list-style-type: none;
  padding: 0;
}

li {
  display: inline-block;
  margin: 0 10px;
}

a {
  color: #42b983;
}

ul#options{
  width: 30%;
  margin: auto;
  text-align: left;
}

ul#options li{
  display: block;
  border-bottom: 1px dashed silver;
}

ul#options li b{
  float:right;
}
</style>
{{/stylus}}
