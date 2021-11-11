FROM alpine:edge

RUN apk update && apk add --no-cache\
    bash \
    curl \
    tzdata \
    ca-certificates \
    && rm -rf /var/cache/apk/*

COPY BetBotGo /bin/app
# COPY test_config.yaml /etc/BetBot.yaml
COPY config.yaml /etc/BetBot.yaml

CMD ["/bin/app", "--config=/etc/BetBot.yaml"]
