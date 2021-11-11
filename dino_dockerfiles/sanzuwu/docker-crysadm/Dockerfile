# 这是迅雷云监工的docker程序
# 云监工原作者powergx

FROM tutum/ubuntu:trusty
MAINTAINER sanzuwu <sanzuwu@gmail.com>

RUN rm /bin/sh &&  ln -s /bin/bash /bin/sh

#设置时区为北京时区
RUN cp /usr/share/zoneinfo/Asia/Shanghai /etc/localtime
#设置时区服务器
#RUN ntpdate  ntp1.aliyun.com

#更新，安装git，wget，sudo
RUN apt-get update && apt-get install -y git wget sudo vim nginx curl

#创建工作目录
RUN mkdir /app 
RUN cd /app
#下载云监工源代码
RUN git clone https://github.com/sanzuwu/crysadm.git
#添加计划任务每小时运行云监工
#RUN echo '0 * * * * root sh /app/crysadm/run.sh' >> /etc/crontab

#安装python，redis
RUN apt-get install -y python3.4 python3.4-dev redis-server
RUN chmod +x ./crysadm/get-pip.py
RUN python3.4 ./crysadm/get-pip.py
RUN pip3.4 install redis && sudo pip3.4 install requests && sudo pip3.4 install flask

#复制配置文件
RUN mv /etc/nginx/sites-available/default ./
COPY default /etc/nginx/sites-available/
RUN apt-get clean 

#脚本加运行权限
RUN chmod +x ./crysadm/run.sh ./crysadm/down.sh ./crysadm/setup.sh  ./crysadm/cron.sh
#redis数据库保存目录
VOLUME ["/var/lib/redis"]

#设置容器端口
#设置反向代理端口
EXPOSE 80
#云监工端口
EXPOSE 4000
#ssh端口
EXPOSE 22

WORKDIR /app

RUN chmod +w /set_root_pw.sh
#添加运行脚本
RUN echo "/app/crysadm/run.sh" >>/set_root_pw.sh
#RUN echo "cron start" >>/set_root_pw.sh
RUN echo "service nginx start" >>/set_root_pw.sh
RUN echo "service nginx reload" >>/set_root_pw.sh
RUN echo "/bin/bash" >>/set_root_pw.sh

