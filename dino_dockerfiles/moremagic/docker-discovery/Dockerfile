# Pull base image.
FROM ubuntu:14.04
MAINTAINER moremagic <itoumagic@gmail.com>

RUN apt-get update && apt-get upgrade -y && apt-get install -y vim curl && apt-get clean

# ssh install
RUN apt-get update && apt-get install -y openssh-server openssh-client && apt-get clean
RUN mkdir /var/run/sshd
RUN echo 'root:root' | chpasswd
RUN sed -i 's/PermitRootLogin without-password/PermitRootLogin yes/' /etc/ssh/sshd_config

# SSH login fix. Otherwise user is kicked off after login
RUN sed 's@session\s*required\s*pam_loginuid.so@session optional pam_loginuid.so@g' -i /etc/pam.d/sshd

ENV NOTVISIBLE "in users profile"
RUN echo "export VISIBLE=now" >> /etc/profile

# python3 install
RUN apt-get install -y python3 python3-pip && apt-get clean
RUN pip3 install redis
ADD redis/regist.py /usr/sbin/regist.py
RUN chmod +x  /usr/sbin/regist.py

# redis
RUN apt-get update && apt-get install -fy redis-server
ADD redis/redis.conf /etc/redis/redis.conf

# nginx install
RUN apt-get -y install nginx lua-nginx-redis && apt-get clean
ADD nginx/default /etc/nginx/sites-available/
ADD nginx/rewrite.lua /etc/nginx/sites-available/
ADD nginx/cert/ /etc/nginx/cert/

# tools install
ADD hostbyaddress /usr/local/bin/hostbyaddress
RUN chmod +x /usr/local/bin/hostbyaddress

RUN printf '#!/bin/bash \n\
echo echo $NEXT_HOST > /usr/local/bin/nexthost && chmod +x /usr/local/bin/nexthost \n\
/usr/bin/redis-server & \n\
/usr/sbin/regist.py & \n\
/etc/init.d/nginx start \n\
/etc/init.d/nginx reload \n\
/usr/sbin/sshd -D \n\
tail -f /var/null \n\
' >> /etc/service.sh \
    && chmod +x /etc/service.sh

EXPOSE 22 6379 80 443
CMD /etc/service.sh
