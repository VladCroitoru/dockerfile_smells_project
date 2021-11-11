FROM alpine:3.7

WORKDIR /tmp/vault-unsealer

ENV vault_unsealer_version 0.2.1
ENV vault_unsealer_sum 8ef9b05e7be751a3f6ae5dd3886a0ee14c956e0075c94324c6ebfcaae474789a

RUN set -ex && apk add --update ca-certificates curl
RUN set -ex && curl -L -o vault-unsealer https://github.com/jetstack/vault-unsealer/releases/download/${vault_unsealer_version}/vault-unsealer_${vault_unsealer_version}_linux_amd64 \
  && echo "$vault_unsealer_sum  vault-unsealer" | sha256sum -c - \
  && mkdir -p /usr/local/bin/ \
  && mv vault-unsealer /usr/local/bin \
  && chmod a+x /usr/local/bin/vault-unsealer

USER 65534

ENTRYPOINT ["/usr/local/bin/vault-unsealer"]
