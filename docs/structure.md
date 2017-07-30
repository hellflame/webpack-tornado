# Project Structure

```bash
.
├── README.md                   # README
├── build                       # webpack config files
│   └── ...
├── config                      # main project config
│   └── test.env.js
├── package.json                # build scripts and dependencies
├── project                     # primary project with back and front end
│   ├── __init__.py
│   ├── config.example.py       # config example
│   ├── config.py               # current config in use
│   ├── model                   # backend model
│   │   ├── __init__.py
│   │   └── eg_model.py
│   ├── public                  # pure static assets
│   │   └── ...
│   ├── service                 # backend service
│   │   └── __init__.py
│   ├── src
│   │   ├── App.vue             # main app component
│   │   ├── components          # ui components
│   │   │   └── ...
│   │   ├── main.js             # app entry file
│   │   └── router
│   │       └── index.js
│   ├── static                  # built js & css
│   └── templates               # backend templates
│       └── index.html
├── run.py                      # backend start point
└── test
    ├── e2e                     # e2e tests
    │   ├── custom-assertions   # custom assertions for e2e tests
    │   │   └── elementCount.js
    │   ├── nightwatch.conf.js  # test runner config file
    │   ├── runner.js           # test runner script
    │   └── specs               # test spec files
    │       └── test.js
    └── unit                    # unit tests
        ├── index.js
        ├── karma.conf.js
        └── specs               # test spec files
            └── Hello.spec.js   # test runner config file
```

### `build/`

This directory holds the actual configurations for both the development server and the production webpack build. Normally you don't need to touch these files unless you want to customize Webpack loaders, in which case you should probably look at `build/webpack.base.conf.js`.

### `config/index.js`

This is the main configuration file that exposes some of the most common configuration options for the build setup. See [API Proxying During Development](proxy.md) and [Integrating with Backend Framework](backend.md) for more details.

### `project/src/`

This is where most of your application code will live in. How to structure everything inside this directory is largely up to you; if you are using Vuex, you can consult the [recommendations for Vuex applications](http://vuex.vuejs.org/en/structure.html).

### `project/public/`

This directory is an escape hatch for static assets that you do not want to process with Webpack. They will serve under [http://localhost:[port]/public/](http://localhost:5000/public/)

### `test/unit`

Contains unit test related files. See [Unit Testing](unit.md) for more details.

### `test/e2e`

Contains e2e test related files. See [End-to-end Testing](e2e.md) for more details.

### `package.json`

The NPM package meta file that contains all the build dependencies and [build commands](commands.md).
