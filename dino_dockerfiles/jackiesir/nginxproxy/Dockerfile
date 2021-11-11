#Version 0.1
#基础镜像
FROM ubuntu:16.04
#维护者信息
MAINTAINER  30690564@qq.com
#镜像更新操作
RUN apt update && apt upgrade -y && apt install nginx -y && apt install python3 -y
#对外暴露端口
EXPOSE 80
#向镜像中添加文件
COPY tailtest.py /home
#指定容器启动后的工作目录
WORKDIR /home

#容器启动命令
#CMD ["/etc/init.d/nginx","start"]
CMD ["nginx", "-g", "daemon off;"]
RUN python3 /home/tailtest.py



