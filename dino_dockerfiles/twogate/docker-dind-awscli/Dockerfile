FROM docker:dind

RUN apk --update add python3 \
  && rm -rf /var/cache/apk/* \
  && pip3 install --upgrade pip \
  && pip3 install awscli
