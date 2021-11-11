FROM golang:1.8

# 创建服务端运行环境
WORKDIR $GOPATH/src/agenda-api-first/cli 

# 添加文件
ADD . $GOPATH/src/agenda-api-first

# 将8080端口暴露出来
EXPOSE 8080

# 添加GOPATH环境后，容器运行
CMD  agenda-api-first/main

VOLUME ["/data"]
