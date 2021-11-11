#this dockerfile use the centos image
#version 7.3.1611
#Author: jun.peng@youbiai.com

#指定基础镜像
FROM centos:7.3.1611

#维护者信息
MAINTAINER jun.peng jun.peng@youbiai.com

#ssh登录密码
ENV PASSWD 123456

#安装openssh服务
RUN {\
 yum install -y openssh-server openssh-clients;\
 ssh-keygen -t rsa -P "" -f ~/.ssh/id_rsa && cat ~/.ssh/id_rsa.pub >> ~/.ssh/authorized_keys;\
 ssh-keygen -t rsa -P "" -f /etc/ssh/ssh_host_rsa_key;\
 ssh-keygen -t ecdsa -P "" -f /etc/ssh/ssh_host_ecdsa_key;\
 ssh-keygen -t ed25519 -P "" -f /etc/ssh/ssh_host_ed25519_key;\
 touch /var/log/messages;\
}

#修改root登录密码
RUN echo "root:${PASSWD}" | chpasswd

#对外开放端口号
EXPOSE 22

#镜像启动时执行指令，如果指令较多使用脚本，否则只执行最后一条
CMD "/usr/sbin/sshd" && tail -f /var/log/messages
