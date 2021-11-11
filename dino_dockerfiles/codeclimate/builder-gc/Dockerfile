FROM alpine:latest

RUN wget -O /bin/docker https://get.docker.com/builds/Linux/x86_64/docker-1.6.0
RUN chmod +x /bin/docker

VOLUME /data/builder-gc

COPY files /

RUN crontab /tmp/crontab
RUN rm /tmp/crontab

CMD ["/bin/start_and_log"]
