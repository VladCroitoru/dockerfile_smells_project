FROM certbot/certbot:v0.27.1
MAINTAINER Miguel Gonzalez (migolo10@gmail.com)
RUN apk add --no-cache openssh-client bash curl
ENV NGINXHUP_URL https://github.com/migolo/dockernginxhup/releases/download/v1.1.0/dockernginxhup_alpine
RUN curl -O -L $NGINXHUP_URL && \
    mv dockernginxhup_alpine /usr/local/bin/dockernginxhup && \
    chmod +x /usr/local/bin/dockernginxhup
RUN touch /var/log/cron.log
VOLUME /var/acmechallenge
ENTRYPOINT []
CMD ["certbot"]
