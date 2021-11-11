FROM    centos
MAINTAINER  eugene@taranov.me

RUN   yum install -y epel-release https://mirror.webtatic.com/yum/el7/webtatic-release.rpm && \
      yum clean all
RUN   yum install -y \
      php70w-xml.x86_64 \
      php70w.x86_64 \
      php70w-bcmath.x86_64 \
      php70w-common.x86_64 \
      php70w-gd.x86_64 \
      php70w-mbstring.x86_64 \
      php70w-mcrypt.x86_64 \
      php70w-mysql.x86_64 \
      php70w-opcache.x86_64 \
      httpd
COPY    entrypoint.sh /
RUN     chmod +x /entrypoint.sh
WORKDIR /var/www/html
EXPOSE  80
CMD   /entrypoint.sh
