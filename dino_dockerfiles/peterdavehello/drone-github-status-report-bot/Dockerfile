FROM alpine:edge
LABEL name="Drone-GitHub-status-report-bot"
LABEL version="latest"
LABEL maintainer="Peter Dave Hello <hsu@peterdavehello.org>"
COPY main.sh /
RUN apk -U upgrade && \
    apk -v add curl openssl && \
    rm -rf /var/cache/apk/*
ENTRYPOINT ["/main.sh"]
