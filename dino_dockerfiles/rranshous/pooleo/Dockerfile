FROM rranshous/openresty-docker

RUN mkdir -p /app/logs
RUN ln -sf /dev/stdout /app/logs/access.log
RUN ln -sf /dev/stderr /app/logs/error.log

ADD ./ /app
EXPOSE 80
