FROM alpine:3.6

ENV WAIT_TIMEOUT=10

COPY wait.sh /wait.sh
RUN apk add --no-cache bash curl \
    && chmod +x /wait.sh

CMD /wait.sh
