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
