#  股票小数据


## 快速上手

#### 构建 docker 镜像（or 本地准备 python 环境）

```bash
git clone git@github.com:JackonYang/dockerfiles.git
cd dockerfiles/apps-pstocky
make docker-build
```


#### 启动 juypter server

```bash
cd pstocky
make start-jupyter
```

#### 浏览器打开代码

url: `127.0.0.1:8899`

如果是在远程服务器上，IP 改为服务器 IP 即可。


⚠️注意⚠️：juypter server 默认不需要密码，且以 root 运行。使用方便，但暴露在公网有很大的安全风险。

## 运行环境

dockerfile: [https://github.com/JackonYang/dockerfiles/tree/master/apps-pstocky](https://github.com/JackonYang/dockerfiles/tree/master/apps-pstocky)
