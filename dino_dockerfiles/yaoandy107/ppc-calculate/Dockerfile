FROM ubuntu
MAINTAINER yaoandy107

# update列表
RUN apt-get update

# 安装必備程式
RUN apt-get install -y socat python3 sudo

# copy源文件
COPY ./ /tmp/

## 創建低權限使用者
RUN useradd -U -m pwn

## 配置權限
RUN chown root:pwn /tmp/*
RUN chmod  750 /tmp/*

CMD sudo -u pwn socat -T 100 tcp-l:4444,fork exec:'python3 /tmp/caculate.py'

EXPOSE 4444