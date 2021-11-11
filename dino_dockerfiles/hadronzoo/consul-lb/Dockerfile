FROM alpine:3.6

ENV \
  CONSUL_VERSION='1.0.0' \
  CONSUL_TEMPLATE_VERSION='0.19.3' \
  CONTAINERPILOT_VERSION='3.4.3'

RUN \
  apk --no-cache add certbot curl jq nginx openssl && \
  curl -o /tmp/consul.zip https://releases.hashicorp.com/consul/$CONSUL_VERSION/consul_${CONSUL_VERSION}_linux_amd64.zip && \
  unzip /tmp/consul.zip -d /usr/bin && \
  rm /tmp/consul.zip && \
  chmod +x /usr/bin/consul && \
  mkdir -p /code/private /code/public /run/nginx /var/lib/consul/data && \
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
  CONSUL_HOST='consul' \
  CONSUL_URL='http://localhost:8500' \
  CONTAINERPILOT='/code/etc/containerpilot.json5.gotmpl' \
  DATACENTER='dc1' \
  LETSENCRYPT_EMAIL_ADDRESS='' \
  LETSENCRYPT_TEST_CERT='0' \
  USE_SSL='1'

EXPOSE 80
EXPOSE 443

CMD ["containerpilot"]
