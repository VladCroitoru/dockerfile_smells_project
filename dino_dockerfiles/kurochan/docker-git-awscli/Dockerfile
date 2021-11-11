FROM docker:stable-git

RUN \
  apk -Uuv add groff less python py-pip && \
  pip install awscli docker-compose && \
  apk --purge -v del py-pip && \
  rm /var/cache/apk/*
