#基础镜像
FROM centos:latest

#作者
MAINTAINER freedoms1988 zzt328697768@gmail.com

#用户
USER root

#更新yum
RUN yum update -y

#安装vim wget openssh-server openssh-clients
RUN yum install -y vim wget openssh-server openssh-clients

#修改ssh配置
RUN sed -i 's/UsePAM yes/UsePAM no/g' /etc/ssh/sshd_config
RUN sed -i '/^#Host_Key/'d /etc/ssh/sshd_config
RUN sed -i '/^Host_Key/'d /etc/ssh/sshd_config
RUN echo 'HostKey /etc/ssh/ssh_host_rsa_key'>/etc/ssh/sshd_config

#生成ssh-key与配置ssh-key
RUN ssh-keygen -t rsa -b 2048 -f /etc/ssh/ssh_host_rsa_key
RUN mkdir -p /root/.ssh
RUN echo 'ssh-rsa AAAAB3NzaC1yc2EAAAADAQABAAABAQDNYXyDd8RLahbcgW7uLzoJgg9LHxNbl9EO82jdCh2VTOKl4ky/oK94wNeifdX8dpty9yjvV/47JU84CQWxUPm5d4xuV9zraq0G0COOMFZ0bNPQHYKaJGyDIVKbi0eWXBRxy+Doq7GCYAP1zKJSpsmHKkInJ0JOvzzcxbAFmzfgTV+2AKTv8W6o8fKFr8uA81XHbHSnUCHiiZbbQxpMaBlOPufZI1RB0E9TflGsBmjuLmVUhoDHKessZ65Mk47SSLL6B23hRWNgLdfkS6N2zAKpBUBubO4MUYwhmWLRzrvMjI7PtuhypoyKCGvd53gOzeRbtsq+q7PaGVpoRa4I0xlF freedoms@Freedoms.local'>/root/.ssh/authorized_keys

#修改root用户登录密码
RUN echo 'root:zztXXXXzzt'|chpasswd

#开放22端口
EXPOSE 22

#镜像运行时，启动sshd
CMD ["/usr/sbin/sshd start"]
