FROM nginx:alpine

ENV HTPASSWD='foo:$apr1$odHl5EJN$KbxMfo86Qdve2FH4owePn.' \
    FORWARD_HOST=web \
    FORWARD_PORT=80 \
    CLIENT_MAX_BODY_SIZE=1M

WORKDIR /opt

RUN apk add --no-cache gettext

COPY auth.conf auth.htpasswd launch.sh ./

CMD ["./launch.sh"]
