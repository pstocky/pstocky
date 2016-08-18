#  股票小数据

# 安装说明

- Python 2.7
- Redis 3.0
- Mysql 5.7 -- 非必选，可用 sqlite3 开发

```bash
$ cd backend
$ pip install -r requirements.txt
$ ./install.sh  # 提示输入并确认 superuser 的密码
$ ./run.sh
```

浏览器打开 `http://127.0.0.1:8000/api`

admin `http://127.0.0.1:8000/admin`

账号／密码：admin/123

# 注意

1. 目前没有 html 文件，所以，首页打不开。
2. 提交代码前执行check.sh进行pep8检查以及isort

# 文档

1. 电子书统一上传至七牛，在单独的 github 仓库里维护一份 阅读 list

大家有想要分享的文档，可以邮件发给我，我人肉上传至七牛并分享。

很快会提供个工具，让大家可以自己上传。

# 贡献者

- [Jackon Yang](http://github.com/jackonyang)
- [bug-wang](https://github.com/linux-wang)
