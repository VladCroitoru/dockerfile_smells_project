FROM alpine:3.5
MAINTAINER Willem willemvd@github

COPY backup.sh /tmp/backup.sh

RUN apk --no-cache add \
      curl \
      less \
      groff \
      jq \
      python \
      py-pip \
      postgresql \
      openssl \
      heirloom-mailx && \
      pip install --upgrade pip awscli && \
      chmod -R 777 /tmp

CMD /tmp/backup.sh