FROM alpine:latest
RUN apk --update add make git wget erlang erlang-ssl erlang-public-key erlang-asn1 erlang-crypto erlang-debugger erlang-dev erlang-dialyzer erlang-edoc erlang-erl-docgen erlang-erl-interface erlang-erts erlang-et erlang-eunit erlang-hipe erlang-ic erlang-inets erlang-runtime-tools erlang-sasl erlang-syntax-tools erlang-tools erlang-wx erlang-mnesia && rm -rf /var/cache/apk/*
RUN cd / && \
    git clone https://github.com/ruanpienaar/crell && \
    cd crell && \
    make release
CMD epmd -daemon && \
    sleep 1 && \
    cd /crell && \
    make console
EXPOSE 9876