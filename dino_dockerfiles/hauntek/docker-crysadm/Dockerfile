# 这是迅雷云监工的docker程序
# 云监工原作者powergx

FROM tutum/ubuntu:trusty
MAINTAINER hauntek <hauntek@hotmail.com>

RUN rm /bin/sh &&  ln -s /bin/bash /bin/sh

#设置时区为北京时区
RUN cp /usr/share/zoneinfo/Asia/Shanghai /etc/localtime

#更新，安装git，wget，sudo
RUN apt-get update && apt-get install -y sudo git wget vim nginx

#创建工作目录
RUN mkdir /app
WORKDIR /app

#下载云监工源代码
RUN git clone https://github.com/hauntek/crysadm.git

#Redis数据库保存目录
VOLUME ["/var/lib/redis"]

#安装python，redis
RUN apt-get install -y python3.4 python3.4-dev redis-server
RUN wget https://bootstrap.pypa.io/get-pip.py
RUN python3.4 get-pip.py
RUN pip3.4 install redis && pip3.4 install requests && pip3.4 install flask

#复制配置文件
RUN mv /etc/nginx/sites-available/default ./
COPY default /etc/nginx/sites-available/
COPY config.py ./crysadm/
COPY run.sh ./
RUN apt-get clean

#脚本加运行权限
RUN chmod +x ./run.sh

#设置容器端口
#云监工端口
EXPOSE 4000
#SSH端口
EXPOSE 22
#设置反向代理端口
EXPOSE 80

RUN chmod +w /set_root_pw.sh
#添加运行脚本
RUN echo "/app/run.sh" >>/set_root_pw.sh
RUN echo "service nginx start" >>/set_root_pw.sh
RUN echo "service nginx reload" >>/set_root_pw.sh
RUN echo "/bin/bash" >>/set_root_pw.sh
