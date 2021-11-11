FROM gargron/mastodon:v2.0.0
MAINTAINER Moritz Heiber <hello@heiber.im>

ENV ENVCONSUL_VERSION="0.7.2" \
  CONSUL_TEMPLATE_VERSION="0.19.3" \
  ENVCONSUL_SHA256="6a0323b2467ff91be94394291b0326d2fc852315b9a8c6c41c2340ae2eeafd40" \
  CONSUL_TEMPLATE_SHA256="47b3f134144b3f2c6c1d4c498124af3c4f1a4767986d71edfda694f822eb7680"

RUN apk --no-cache add curl ca-certificates && \
  curl -o /tmp/envconsul.zip -L https://releases.hashicorp.com/envconsul/${ENVCONSUL_VERSION}/envconsul_${ENVCONSUL_VERSION}_linux_amd64.zip && \
  echo "${ENVCONSUL_SHA256}  /tmp/envconsul.zip" | sha256sum -c && \
  unzip /tmp/envconsul.zip -d /usr/bin/ && \
  curl -o /tmp/consul-template.zip -L https://releases.hashicorp.com/consul-template/${CONSUL_TEMPLATE_VERSION}/consul-template_${CONSUL_TEMPLATE_VERSION}_linux_amd64.zip && \
  echo "${CONSUL_TEMPLATE_SHA256}  /tmp/consul-template.zip" | sha256sum -c && \
  unzip /tmp/consul-template.zip -d /usr/bin/ && \
  rm -f /tmp/envconsul.zip /tmp/consul-template.zip && \
  apk del --purge curl && \
  adduser -h /mastodon -s /bin/sh -DHS mastodon && \
  rm -rf /tmp/* /var/cache/apk/* && \
  find /mastodon -path /mastodon/public/system -prune -o -not -user mastodon -print0 | xargs -0 chown -f mastodon

USER mastodon
ENTRYPOINT []
