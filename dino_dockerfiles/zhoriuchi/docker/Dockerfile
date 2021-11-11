# Dockerイメージの作成
FROM ubuntu:latest

#作成者
MAINTAINER 0.3 horiuchi@zlab.co.jp

#httpdのインストール
RUN apt-get install -y \
            apache2 \
            curl


#RUN echo "ServerName localhost" >> /etc/apache2/apache2.conf
RUN mkdir /var/lock/apache2
RUN mkdir /var/run/apache2

# httpdの実行
CMD . /etc/apache2/envvars && /usr/sbin/apache2 -D FOREGROUND
