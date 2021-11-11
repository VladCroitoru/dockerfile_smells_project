ARG ALPINEVERSION=3.14

FROM alpine:$ALPINEVERSION
LABEL maintainer "Unified Streaming <support@unified-streaming.com>"

# ARGs declared before FROM are in a different scope, so need to be stated again
# https://docs.docker.com/engine/reference/builder/#understand-how-arg-and-from-interact
ARG ALPINEVERSION
ARG BETA_REPO=https://beta.apk.unified-streaming.com/alpine/
ARG STABLE_REPO=https://stable.apk.unified-streaming.com/alpine/
ARG VERSION=1.11.3

# Get USP public key
RUN wget -q -O /etc/apk/keys/alpine@unified-streaming.com.rsa.pub \
    https://stable.apk.unified-streaming.com/alpine@unified-streaming.com.rsa.pub

# Install Origin
RUN apk \
    --update \
    --repository $BETA_REPO/v$ALPINEVERSION \
    --repository $STABLE_REPO/v$ALPINEVERSION \
    add \
        mp4split~$VERSION \
&&  rm -f /var/cache/apk/*

COPY entrypoint.sh /usr/local/bin/entrypoint.sh

RUN chmod +x /usr/local/bin/entrypoint.sh

ENTRYPOINT ["/usr/local/bin/entrypoint.sh"]

CMD ["--help"]
