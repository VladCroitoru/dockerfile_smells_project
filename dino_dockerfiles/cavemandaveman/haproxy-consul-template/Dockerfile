FROM alpine:3.4

MAINTAINER cavemandaveman <cavemandaveman@protonmail.com>

ENV S6_VERSION="v1.18.0.0" \
    CONSUL_TEMPLATE_VERSION="0.15.0" \
    CONSUL_TEMPLATE_SHA256="b7561158d2074c3c68ff62ae6fc1eafe8db250894043382fb31f0c78150c513a"

RUN set -x \
    && apk --no-cache add haproxy \
    && apk --no-cache add --virtual .install-deps \
      openssl \
      gnupg \
    && export GNUPGHOME="$(mktemp -d)" WGETHOME="$(mktemp -d)" \
    && wget -q "https://github.com/just-containers/s6-overlay/releases/download/${S6_VERSION}/s6-overlay-amd64.tar.gz.sig" \
      "https://github.com/just-containers/s6-overlay/releases/download/${S6_VERSION}/s6-overlay-amd64.tar.gz" \
      "https://releases.hashicorp.com/consul-template/${CONSUL_TEMPLATE_VERSION}/consul-template_${CONSUL_TEMPLATE_VERSION}_linux_amd64.zip" -P "${WGETHOME}" \
    && gpg --keyserver pgp.mit.edu --recv-key 0x337EE704693C17EF \
    && gpg --verify "${WGETHOME}/s6-overlay-amd64.tar.gz.sig" "${WGETHOME}/s6-overlay-amd64.tar.gz" \
    && tar -zxf "${WGETHOME}/s6-overlay-amd64.tar.gz" -C / \
    && echo "${CONSUL_TEMPLATE_SHA256}  ${WGETHOME}/consul-template_${CONSUL_TEMPLATE_VERSION}_linux_amd64.zip" | sha256sum -c \
    && unzip -qd "/bin/" "${WGETHOME}/consul-template_${CONSUL_TEMPLATE_VERSION}_linux_amd64.zip" \
    && rm -rf "${GNUPGHOME}" "${WGETHOME}" \
    && apk del .install-deps

COPY etc/ /etc/
COPY bin/ /bin/

ENTRYPOINT ["/init"]
