FROM alpine:edge

ENV ELIXIR_VERSION 1.2.6

RUN apk --update add erlang-sasl erlang-crypto erlang-syntax-tools erlang-public-key erlang-ssl erlang-inets erlang-parsetools openssl && \
    apk add elixir=$ELIXIR_VERSION-r0 && \
    rm -rf /etc/ssl && \
    rm -rf /var/cache/apk/*

ENV PATH $PATH:/opt/elixir-${ELIXIR_VERSION}/bin
CMD ["/bin/sh"]
