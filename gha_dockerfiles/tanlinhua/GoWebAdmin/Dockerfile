# 打包镜像
# $ docker build -t gowebadmin .
# 运行
# $ docker run -p 1991:1991 -p 2014:2014 gowebadmin

# 方式一: 源码编译
FROM golang:1.16.6-alpine
LABEL maintainer="go_web_admin"
ENV GOPROXY=https://goproxy.io,direct
WORKDIR /gowebadmin
COPY . .
RUN go env && go build -o main .
EXPOSE 1991 2014
ENTRYPOINT ./main

# 方式二: 二进制
# FROM loads/alpine:3.8
# LABEL maintainer="go_web_admin"
# ENV WORKDIR /var/www/gf-empty
# ADD ./main   $WORKDIR/main
# RUN chmod +x $WORKDIR/main
# EXPOSE 1991 2014
# WORKDIR $WORKDIR
# CMD ./main