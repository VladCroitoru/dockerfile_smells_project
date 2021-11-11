FROM ubuntu:xenial

RUN apt-get update && apt-get install -y wget && wget https://download.opensuse.org/repositories/home:/rtCamp:/EasyEngine/xUbuntu_16.04/Release.key && apt-key add Release.key && rm Release.key

RUN sh -c "echo 'deb http://download.opensuse.org/repositories/home:/rtCamp:/EasyEngine/xUbuntu_16.04/ /' >> /etc/apt/sources.list.d/nginx.list"

RUN apt-get update && apt-get install -y patch nginx-custom nginx-ee && rm /etc/nginx/sites-enabled/default

COPY nginx-build.sh ./
RUN ./nginx-build.sh

COPY nginx.conf /etc/nginx/nginx.conf

COPY default.conf /etc/nginx/conf.d/default.conf
COPY redislog.conf /etc/nginx/conf.d/redislog.conf
COPY upstream.conf /etc/nginx/conf.d/upstream.conf
COPY fastcgi.conf /etc/nginx/conf.d/fastcgi.conf

COPY locations.conf /etc/nginx/common/locations.conf
COPY wpcommon.conf /etc/nginx/common/wpcommon.conf
COPY proxy.conf /etc/nginx/common/proxy.conf

COPY redis.conf /etc/nginx/common/redis.conf

COPY wpfc.conf /etc/nginx/common/wpfc.conf

COPY wordpress.conf /etc/nginx/common/wordpress.conf

ADD entrypoint.sh entrypoint.sh

RUN mkdir -p /var/lib/nginx/body

ENTRYPOINT ["/entrypoint.sh"]
CMD ["nginx", "-g", "daemon off;"]
