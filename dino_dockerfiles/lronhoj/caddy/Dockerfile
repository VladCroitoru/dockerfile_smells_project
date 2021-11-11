FROM abiosoft/caddy:builder

ENV PLUGINS=prometheus

RUN /bin/sh /usr/bin/builder.sh

FROM abiosoft/caddy:latest
COPY --from=0 /install/caddy /usr/bin/