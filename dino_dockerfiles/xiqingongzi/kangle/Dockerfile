FROM centos 
MAINTAINER xiqingongzi<best.tony@foxmail.com>
WORKDIR /
RUN yum -y update && yum -y install wget make automake gcc gcc-c++ pcre-devel zlib-devel sqlite-devel openssl-devel
RUN wget http://download.kanglesoft.com/zcore.php?os=src && tar -zxvf  zcore.php?os=src 
WORKDIR /kangle-3.4.8
RUN ./configure --prefix=/vhs/kangle --enable-disk-cache --enable-ipv6 --enable-ssl --enable-vh-limit 
RUN make && make install
ENV KANGLEPASS kangle
COPY start.sh /start.sh
RUN chmod a+x /start.sh
ENTRYPOINT ["/start.sh"]