FROM mogria/3source-phpcli:latest

MAINTAINER "Mogria" <m0gr14@gmail.com>

RUN mkdir -p /data/www
VOLUME ["/data"]
WORKDIR /data/www

ENTRYPOINT ["umask-wrapper.sh", "container-user.sh", "php", "artisan"]
