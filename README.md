# 说明

XJU本部宿舍区SRUN4k验证py暴力实现

py2.x/3.x

# 依赖

## python
requests time os

## openwrt
python-requests

# 用法

python run.py

# 原README

# pySrun4k
## 简介
pySrun4k是一个模仿Srun4k认证客户端协议，用Python3实现的认证客户端。

实现了登录，检查在线状态，登出当前终端，登出所有终端功能。
## API

### 登录：srun4k.do_login(username,pwd,mbytes=0,minutes=0)

### 检查在线状态 srun4k.check_online()

### 登出当前终端 srun4k.do_logout(username)

### 登出所有终端 srun4k.force_logout(username,password)

