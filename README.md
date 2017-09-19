# vue webpack-tornado

集成前端 `vue` 以及后端 `tornado` 框架支持的开发框架。vue模版来自于 [vuejs-templates/webpack](https://github.com/vuejs-templates/webpack) .

## 特性

- 服务端渲染 (来自tornado后端)
- 多个独立页面
- 一机开发，多设备同时测试
- 继承式访问权限控制
- 装饰器路由

## 使用

这是一个 [vue-cli](https://github.com/vuejs/vue-cli) 模版框架. **建议使用 npm 3+ 来构建更高效的依赖树**

#### 1. 安装vue-cli

```bash
$ npm install -g vue-cli
```

#### 2. 下载模版

```bash
$ vue init hellflame/webpack-tornado project-name
```

初始化过程中可以自定义所需要的前端属性：

1. Vue-Router
2. Stylus
3. Pug
4. ESLint
5. Unit Test
6. E2E Test

#### 3. npm安装依赖

```bash
$ cd project-name
$ npm install
```

#### 4. pip安装依赖

```bash
$ pip install -r requirements.txt
```

> 如果出现权限问题，加上sudo

#### 5. 启动开发模式

```bash
$ npm run dev # 启动vue开发模式
```

```bash
$ python run.py  # 启动tornado后端
```

#### 6. 测试访问

在浏览器中访问 [http://0.0.0.0:5000](http://0.0.0.0:5000) 

至此，如果能够看到有Vue标志的页面，便说明可以进行自己项目的开发了。

### 注意

前端默认从0.0.0.0:8080端口启动，如果被占用，会尝试0.0.0.0:8081，依此类推，但对后端可见的依然是8080端口，导致无法获取前端实时数据。

后端默认从0.0.0.0:5000端口启动，可以通过CLI指定port参数，运行在其他端口，如:

```bash
$ python run.py --port=5001  # 运行在5001端口
```

由于整个开发过程中前端数据被后端代理，所以只要能访问后端服务器，就可以开始自己的开发。

## 开发应用

项目目录结构如下:

```bash
├── build             # 前端开发配置
├── config            # webpack 配置
├── project           # 项目开发目录
│   ├── model         # 后端model层
│   ├── public          # 静态文件资源目录
│   ├── service         # 后端service层
│   ├── src           # 前端开发目录
│   │   ├── components      # 前端组件
│   │   └── router        # 前端路由(如果开启Vue-Router)
│   ├── static          # 前端发布目录
│   └── templates       # HTML模版
└── test            # 前端测试目录
    ├── e2e           # 前端e2e测试
    │   ├── custom-assertions
    │   └── specs
    └── unit          # 前端unit测试
        └── specs
```

一般应用开发只需要关注 `project` 目录即可

前端开发与一般vue的开发过程一样。

```bash
src/
├── components    # Vue组件
│   └── Hello.vue
├── router      # Vue-Router路由
│   └── index.js  
├── App.vue     # Vue入口
└── main.js     # 入口文件
```

后端开发使用tornado，而且加入了部分定制，让后端开发更顺手

```bash
project/
├── model       # 后端model，主要进行数据操作等
│   ├── __init__.py
│   └── eg_model.py   
├── public        # 无论何时，都可以通过/public/*** 来访问该目录下静态文件
├── service       # 后端service，主要进行路由响应和权限控制等
├── static        # 包含前端打包之后的静态文件，js、css，每次打包都会清空重写
├── templates     # 模版文件目录
│   ├── error.html
│   └── index.html
├── __init__.py
├── config.example.py # 后端配置模版，一般在服务端的配置文件为该配置文件的副本
└── config.py     # 当前在用的配置文件
```

后端service:

```bash
service
├── __init__.py
├── base.py       # 基础响应基类，可分配权限控制
├── s_example.py    # 通用服务处理，文件匹配通配符 s_*.py ，会被自动导入
├── static.py     # 静态文件处理，关联 public/ 和 static/ 
└── templates.py    # 模版响应处理，关联 templates/ 目录
```

#### 定制部分

1. 静态文件手动处理

   由于后端需要在开发过程中实时代理前端数据，又需要在部署时使用已经打包好的前端文件，所以原本只需要一个配置项的地方改为了手动处理，并且静态文件目录变成了两个，`public` 以及 `static`，其中public目录存放不会再变的静态文件，比如用户上传的图片、文件等，static目录专门用来存放前端打包好的文件。静态文件的处理单独放在了 `project/service/static.py` 中，在debug模式下还会额外重定向 `__webpack_hmr`

2. 装饰器路由

   为了方便添加路由，在service中提供了一个 `route` 装饰器，可以在写路由处理类的同时添加路由，可以像下面这样使用：

   ```python
   from . import base, route

   @route(r'/')
   class IndexTemplate(base.NormalBase):
       def get(self):
           return self.render("index.html")
   ```

   额外参数可作为 `route` 装饰器的第二个参数。路由处理类的书写和其他时候没有什么区别。装饰器定义在service下的`__init__.py` 中，十分简单。

3. 自动导入

   由于大多数情况下写在service中的代码都是作为响应路由的必要代码，都会注册到路由中，所以为了进一步偷懒，以 `s_` 开头的python文件都会被自动导入，无路是否有手动import。当然，其他样子的python文件也可以自己手动导入，比如在service下的 `__init__.py`中。 自动导入代码在service下的`__init__.py` 中可以找到。

4. 嵌入日志

   日志的响应级别在 `DEBUG` 模式下为 `DEBUG` ，否则为 `WARNING` ，并且在 `NormalBase` 基类中获取了根日志，可以通过 `self.logger` 访问操作，日志格式也可以在基类中调整。

## 发布应用

在完成前端之后，打包前端代码:

```bash
$ npm run build
```

打包之后的文件位于 `project/static/`

部署后端代码时需要将debug.py覆盖，即 `DEBUG=False` ，此时应用仅运行在本地端口，并且使用static下的静态文件提供服务，剩下的就是 `Supervisor` + `Nginx` 的代理配置了。

### Fork It And Make Your Own

You can fork this repo to create your own boilerplate, and use it with `vue-cli`:

```bash
vue init username/repo my-project
```