# Simple example with rump-nginx-lua

FROM justincormack/rump-nginx

MAINTAINER Justin Cormack

COPY . /usr/src/rump-nginx-test

WORKDIR /usr/src/rump-nginx-test

ENV SUDO_UID=1000

RUN ./build.sh

ENV RUMP_VERBOSE=1

EXPOSE 80

CMD rexec nginx -nx -ro fs.img -rw docker:eth0 -- -c /data/conf/nginx.conf
