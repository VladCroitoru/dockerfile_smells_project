FROM abiosoft/caddy

ENV CONFIG "0.0.0.0\n\
browse\n\
log stdout\n\
errors stdout"

WORKDIR /caddy

ADD entrypoint.sh /caddy/entrypoint.sh

RUN chmod +x /caddy/entrypoint.sh

ENTRYPOINT ["/caddy/entrypoint.sh"]
