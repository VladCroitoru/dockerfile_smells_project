FROM python:2-alpine

RUN apk add curl && \
    curl -O https://pagekite.net/pk/pagekite.py

ENV LOCAL_HOST=traefik \
    SUBDOMAINS=blimp

COPY start.sh /

CMD start.sh
