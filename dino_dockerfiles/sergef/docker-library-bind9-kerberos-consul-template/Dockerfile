FROM sergef/docker-library-alpine:3.6

ENV DNS_HOST 127.0.0.1
ENV HOST_IP 127.0.0.1

ENV CLUSTER_DC local
ENV CLUSTER_DOMAIN localhost.localdomain

ENV CONSUL_SERVICE consul:8500

ENV KRB_KEYTAB /etc/nsupdate/ddns.keytab
ENV KRB_USER ddns@localhost.localdomain

ENV APKBUILD_PACKAGE bind
ENV APKBUILD_PACKAGE_VERSION 9.11.1_p1-r1
ENV APKBUILD_ORIGIN 3.6-stable

ENV CONSUL_TEMPLATE_VERSION 0.19.2
ENV CONSUL_TEMPLATE_FILENAME consul-template_${CONSUL_TEMPLATE_VERSION}_linux_amd64.tgz
ENV CONSUL_TEMPLATE_SHA256SUM f92f2abbdc034b9797c2ea7561c8fb95234ee97d4d6c5c0a1f96380c036c962c

COPY build.sh /build.sh
COPY APKBUILD.patch /APKBUILD.patch

COPY etc/nsupdate /etc/nsupdate
COPY entrypoint.sh /entrypoint.sh
COPY nsupdate.sh /nsupdate.sh

ADD https://releases.hashicorp.com/consul-template/${CONSUL_TEMPLATE_VERSION}/${CONSUL_TEMPLATE_FILENAME} /tmp/downloads/

RUN echo "${CONSUL_TEMPLATE_SHA256SUM}  /tmp/downloads/${CONSUL_TEMPLATE_FILENAME}" | sha256sum -c - \
  && tar -xvf /tmp/downloads/${CONSUL_TEMPLATE_FILENAME} -C /bin \
  && chmod +x /bin/consul-template \
  && rm -rf /tmp/downloads \
  && apk add \
    --update-cache \
    alpine-sdk \
    coreutils \
    krb5 \
  && adduser -G abuild -g "Alpine Package Builder" -s /bin/ash -D builder \
  && echo "builder ALL=(ALL) NOPASSWD:ALL" >> /etc/sudoers \
  && mkdir -p /aports \
  && chmod +x /build.sh \
  && chown builder:abuild /aports /build.sh \
  && sudo su - builder /build.sh ${APKBUILD_ORIGIN} ${APKBUILD_PACKAGE} \
  && cp /home/builder/packages/main/x86_64/* /var/lib/apk \
  && deluser --remove-home builder \
  && apk add \
    /var/lib/apk/${APKBUILD_PACKAGE}-${APKBUILD_PACKAGE_VERSION}.apk \
  && apk del \
    --no-cache \
    alpine-sdk \
    coreutils \
  && chmod +x /entrypoint.sh \
  && chmod +x /nsupdate.sh \
  && rm -rf \
    /var/cache/apk/* \
    /var/lib/apk/* \
    /aports

ENTRYPOINT ["tini", "--", "/entrypoint.sh"]
