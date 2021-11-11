FROM gliderlabs/alpine:3.3
RUN apk add --no-cache --update \
      python \
      python-dev \
      py-pip \
      bash \
      openssl \
  && wget -O /tmp/awscli-bundle.zip "https://s3.amazonaws.com/aws-cli/awscli-bundle.zip" \
  && unzip -o -d /tmp /tmp/awscli-bundle.zip \
  && /tmp/awscli-bundle/install -b /usr/local/bin/aws \
  && rm -rf /tmp/*
ADD chaos.sh /usr/sbin/chaos.sh

RUN chmod +x /usr/sbin/chaos.sh
ENTRYPOINT ["/usr/sbin/chaos.sh"]