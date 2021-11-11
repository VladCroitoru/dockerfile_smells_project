FROM alpine:latest

LABEL maintainer="https://github.com/fjakop"

ENTRYPOINT ["/entrypoint.sh"]

ENV CLEAN_PERIOD=1800 \
    LOOP=true \
    DEBUG=0

# run.sh script uses some bash specific syntax
RUN apk add --update bash docker grep

# Install cleanup script
ADD entrypoint.sh /entrypoint.sh
RUN chmod +x /entrypoint.sh
