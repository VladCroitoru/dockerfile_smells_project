FROM alpine:3.11.3
ENV EDITOR vi # For Elastic Beanstalk
RUN apk -v --update add \
  ca-certificates \
  git \
  groff \
  jq \
  less \
  mailcap \
  openssh \
  openssl \
  py-pip \
  python \
  && update-ca-certificates \
  && rm /var/cache/apk/*
RUN pip install --upgrade awscli==1.17.9 --target /usr/local/lib/awscli \
  && printf '#!/bin/sh\nPYTHONPATH=/usr/local/lib/awscli /usr/local/lib/awscli/bin/aws "$@"\n' \
  > /usr/local/bin/aws \
  && chmod +x /usr/local/bin/aws
RUN pip install --upgrade awsebcli==3.17.0 --target /usr/local/lib/awsebcli \
  && printf '#!/bin/sh\nPYTHONPATH=/usr/local/lib/awsebcli /usr/local/lib/awsebcli/bin/eb "$@"\n' \
  > /usr/local/bin/eb \
  && chmod +x /usr/local/bin/eb
RUN pip install --upgrade s3cmd==2.0.2 --target /usr/local/lib/s3cmd \
  && printf '#!/bin/sh\nPYTHONPATH=/usr/local/lib/s3cmd /usr/local/lib/s3cmd/bin/s3cmd "$@"\n' \
  > /usr/local/bin/s3cmd \
  && chmod +x /usr/local/bin/s3cmd
