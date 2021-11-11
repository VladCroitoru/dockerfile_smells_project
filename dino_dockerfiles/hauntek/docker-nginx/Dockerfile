FROM tutum/ubuntu:trusty
MAINTAINER hauntek <hauntek@hotmail.com>

RUN rm /bin/sh &&  ln -s /bin/bash /bin/sh

#设置时区为北京时区
RUN cp /usr/share/zoneinfo/Asia/Shanghai /etc/localtime

#更新，安装git，wget，sudo
RUN apt-get update && apt-get install -y git wget sudo vim nginx

#创建工作目录
RUN mkdir /app 
WORKDIR /app

#复制配置文件
RUN mv /etc/nginx/sites-available/default ./
COPY default /etc/nginx/sites-available/
RUN apt-get clean 

#设置容器端口
#ssh端口
EXPOSE 22
#设置正向代理端口
EXPOSE 3128

RUN chmod +w /set_root_pw.sh
#添加运行脚本
RUN echo "service nginx start" >>/set_root_pw.sh
RUN echo "service nginx reload" >>/set_root_pw.sh
RUN echo "/bin/bash" >>/set_root_pw.sh