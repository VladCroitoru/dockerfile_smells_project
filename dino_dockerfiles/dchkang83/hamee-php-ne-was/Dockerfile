FROM dchkang83/centos7-php7-nginx1:latest
MAINTAINER Deokjoon Kang <dchkang83@naver.com>

# add nginx, php files

#ENV \
#  PATH=/root/programs/nginx/sbin:/root/programs/php/bin:/root/programs/php/sbin:$PATH

EXPOSE 80 443


# sh copy
COPY entrypoint.sh /
RUN chmod +x /entrypoint.sh

# put customized config and code files to /data
#VOLUME ["/data"]
#WORKDIR /data

# start nginx, php-fpm
#ENTRYPOINT ["/tmp/script/bootstrap.sh"]
#CMD ["/entrypoint.sh"]
ENTRYPOINT ["/entrypoint.sh"]