# 使用centos官方镜像
FROM centos:centos6.7

MAINTAINER seekplum <1131909224m@sina.cn>

LABEL Description="基于centos6.7镜像搭建ftp服务器" \
	License="Apache License 2.0" \
	Usage="docker run -d -p [HOST PORT NUMBER]:21 -v [HOST FTP HOME]:/home/ftp seekplum/vsftpd" \
	Version="0.1.0"

# 把文件都加入到 /app 中
COPY . /app

# 设置工作路径
WORKDIR /app

# 设置ftp默认用户名、密码和地址
ENV FTP_USER ftp
ENV FTP_PASS ftp
ENV PASV_ADDRESS 127.0.0.1

# 设置传输端口范围，大于 1023即可
ENV PASV_MIN_PORT 47000
ENV PASV_MAX_PORT 47400

# 安装vsftpd/ftp软件
RUN yum -y install \
        vsftpd \
        ftp \
        db4-utils \
        db4 \
        db4-devel && \
        yum clean all

# 拷贝配置文件
COPY vsftpd.sh /usr/local/vsftpd/
COPY vsftpd.conf /etc/vsftpd/
COPY vsftpd /etc/pam.d/

RUN chmod +x /usr/local/vsftpd/vsftpd.sh

# 设置共享文件夹
VOLUME /home/ftp
VOLUME /var/log/vsftpd

EXPOSE 20 21

# 进入容器时默认执行的命令
CMD ["/bin/sh", "/usr/local/vsftpd/vsftpd.sh"]
