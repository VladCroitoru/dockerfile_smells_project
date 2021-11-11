FROM alpine:3.5

ENV INTERVAL=-1

COPY run.sh /usr/local/bin/run.sh

RUN apk add --no-cache \
      git \
      py2-pip \
      python \
      tini \
 && pip install --no-cache-dir \
      awscli \
      docker-compose \
 && git config --global credential.helper '!aws codecommit credential-helper $@' \
 && git config --global credential.UseHttpPath true \
 && git --version \
 && aws --version \
 && docker-compose --version

WORKDIR /var/compose

ENTRYPOINT ["/sbin/tini", "--"]

CMD ["run.sh"]
