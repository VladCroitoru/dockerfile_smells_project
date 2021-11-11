FROM alpine:3.7

ENV \
  CONSUL_TEMPLATE_VERSION='0.19.4' \
  CONTAINERPILOT_VERSION='3.6.2'

RUN \
  apk --no-cache add certbot curl jq nginx openssl && \
  mkdir -p /code/private && \
  curl -fLsS https://releases.hashicorp.com/consul-template/$CONSUL_TEMPLATE_VERSION/consul-template_${CONSUL_TEMPLATE_VERSION}_linux_amd64.tgz | \
    tar xz -C /usr/local/bin && \
  curl -fLsS https://github.com/joyent/containerpilot/releases/download/$CONTAINERPILOT_VERSION/containerpilot-$CONTAINERPILOT_VERSION.tar.gz | \
    tar xz -C /usr/local/bin

WORKDIR /code

COPY bin bin
COPY etc etc

ENV \
  CONSUL_TAG_PREFIX='consul-lb' \
  CONSUL_SERVICE_NAME='consul-lb' \
  CONSUL_SERVICE_TAGS='' \
  CONSUL_URL='http://consul:8500' \
  CONTAINERPILOT='/code/etc/containerpilot.json5.gotmpl' \
  LETSENCRYPT_EMAIL_ADDRESS='' \
  LETSENCRYPT_TEST_CERT='0' \
  USE_SSL='1'

EXPOSE 80 443

CMD ["containerpilot"]
