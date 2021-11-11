# CentOSをベースのOSイメージにする
FROM centos

# 作成者
MAINTAINER Soshi Katsuta

# RUN コマンドを使って、yum コマンドを実行してインストールする
RUN yum update -y && yum -y upgrade
RUN yum install -y sudo
RUN yum install -y passwd
RUN yum install -y httpd
RUN yum install -y php php-mysql

# EXPOSE コマンドを使って、ポート80を解放
EXPOSE 80

# ENTORYPOINT コマンドを使って、コンテナ起動時に実行するコマンドを与える
ENTRYPOINT service httpd start && /bin/bash

