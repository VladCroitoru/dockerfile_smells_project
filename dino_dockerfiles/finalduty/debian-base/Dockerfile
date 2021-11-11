FROM debian
MAINTAINER "FinalDuty" <root@finalduty.me>

RUN apt-get update && apt-get install -y vim curl 

RUN \
  curl -s http://raw.githubusercontent.com/finalduty/configs/master/.bashrc > /root/.bashrc; \
  curl -s http://raw.githubusercontent.com/finalduty/configs/master/.vimrc > /root/.vimrc; \
  curl -s http://raw.githubusercontent.com/finalduty/docker-debian/master/sources.list > /etc/apt/sources.list;
  
