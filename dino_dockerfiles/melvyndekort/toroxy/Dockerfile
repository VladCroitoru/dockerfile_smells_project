FROM melvyndekort/docker-base:base-alpine-1.0

RUN apk add --update --no-cache tor privoxy
ADD torrc /etc/tor/torrc
ADD privoxy /etc/privoxy/config

EXPOSE 9050 3128

ENTRYPOINT [ "dockerfy", \
             "--start", "/usr/sbin/privoxy", "--no-daemon", "/etc/privoxy/config", "--" ]

CMD [ "/usr/bin/tor", "-f", "/etc/tor/torrc" ]
