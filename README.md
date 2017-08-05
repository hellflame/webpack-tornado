# Vue webpack cooperative with python tornado

> A full-featured Webpack setup with hot-reload, lint-on-save, unit testing & css extraction.

> This template is Vue 2.0 compatible. For Vue 1.x take [vuejs-templates/webpack](https://github.com/vuejs-templates/webpack) as referrence

> webpack-tornado is inhreited from [vuejs-templates/webpack](https://github.com/vuejs-templates/webpack) 

## Enables

- SSR (server side render)
- Multiple separate pages in One Site
- One deploy instance, Multiple deveices access (by default)
- Access Control from application level, controled by back end

## Task List

- [x] template base from [vuejs-templates/webpack](https://github.com/vuejs-templates/webpack) 
- [x] support stylus for css
- [x] support pug for html templates (*.vue)
- [x] python tornado frameworks
- [x] document updates

## Documentation

- [For this template](http://vuejs-templates.github.io/webpack): common questions specific to this template are answered and each part is described in greater detail
- [For Vue 2.0](http://vuejs.org/guide/): general information about how to work with Vue, not specific to this template

## Usage

This is a project template for [vue-cli](https://github.com/vuejs/vue-cli). **It is recommended to use npm 3+ for a more efficient dependency tree.**

```bash
$ npm install -g vue-cli
$ vue init hellflame/webpack-tornado my-project
$ cd my-project
$ npm install
$ npm run dev
```

If port 8080 is already in use on your machine you must change the port number in `/config/index.js`. Otherwise `npm run dev` will fail.

Serve the front end page is half way to start the whole project, you still need to start the back end:

```bash
$ python run.py
```

The back end (The whole project entry) will be running at 0.0.0.0:5000 by default

It is ok to give it another usable port numer:

```bash
# run @ http://0.0.0.0:5001
$ python run.py 5001
```

## What's Included

- `npm run dev`: first-in-class development experience.
  - Webpack + `vue-loader` for single file Vue components.
  - State preserving hot-reload
  - State preserving compilation error overlay
  - Lint-on-save with ESLint
  - Source maps
- `npm run build`: Production ready build.
  - JavaScript minified with [UglifyJS](https://github.com/mishoo/UglifyJS2).
  - HTML minified with [html-minifier](https://github.com/kangax/html-minifier).
  - CSS across all components extracted into a single file and minified with [cssnano](https://github.com/ben-eb/cssnano).
  - All static assets compiled with version hashes for efficient long-term caching, and a production `index.html` is auto-generated with proper URLs to these generated assets.
  - Use `npm run build --report`to build with bundle size analytics.
- `npm run unit`: Unit tests run in PhantomJS with [Karma](http://karma-runner.github.io/0.13/index.html) + [Mocha](http://mochajs.org/) + [karma-webpack](https://github.com/webpack/karma-webpack).
  - Supports ES2015+ in test files.
  - Supports all webpack loaders.
  - Easy mock injection.
- `npm run e2e`: End-to-end tests with [Nightwatch](http://nightwatchjs.org/).
  - Run tests in multiple browsers in parallel.
  - Works with one command out of the box:
    - Selenium and chromedriver dependencies automatically handled.
    - Automatically spawns the Selenium server.
- `python run.py`: Tornado Back end of the project.

### Fork It And Make Your Own

You can fork this repo to create your own boilerplate, and use it with `vue-cli`:

```bash
vue init username/repo my-project
```
