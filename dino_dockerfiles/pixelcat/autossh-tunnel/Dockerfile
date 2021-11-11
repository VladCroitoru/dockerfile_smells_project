
FROM alpine:3.8

ENV AUTOSSH_REMOTE_PORT=636
ENV AUTOSSH_LOCAL_PORT=636
ENV AUTOSSH_TUNNEL_HOST=localhost
ENV AUTOSSH_TARGET_HOST=localhost
ENV AUTOSSH_TARGET_PORT=22
ENV AUTOSSH_USER=""
ENV AUTOSSH_OPTS=""

RUN apk --update add autossh

COPY docker-entrypoint.sh /

RUN chmod a+x /docker-entrypoint.sh

VOLUME /root/.ssh

EXPOSE 636

ENTRYPOINT [ "/docker-entrypoint.sh" ]


