FROM alpine:3.6
MAINTAINER Liang Xingchen <liang@maichong.it>
RUN apk upgrade --update && \
    apk add php5-cli php5-dev php5-pear php5-openssl ca-certificates autoconf openssl-dev g++ make && \
    ln -s /usr/bin/php5 /usr/bin/php && \
    pear update-channels && \
    php /usr/share/pear/peclcmd.php install -f mongo && \
    echo "extension=mongo.so" >> /etc/php5/php.ini && \
    apk del --purge php5-dev php5-pear php5-openssl openssl-dev autoconf g++ make ca-certificates
ADD . /rockmongo
WORKDIR /rockmongo
EXPOSE 80
CMD ["php","-d","upload_max_filesize=1024M","-d","post_max_size=1024M","-S","0.0.0.0:80"]

# USEAGE
# docker run -it --rm -p 8080:80 -v /path/to/config.php:/rockmongo/config.php maichong/rockmongo
# docker run -it --rm -p 8080:80 -e "ADMIN_USER=admin" -e "ADMIN_PASS=password" maichong/rockmongo
# docker run -it --rm -p 8080:80 -e "ADMIN_USER=admin" -e "ADMIN_PASS=password" maichong/rockmongo php -d upload_max_filesize=100M -d post_max_size=100M -S 0.0.0.0:80
