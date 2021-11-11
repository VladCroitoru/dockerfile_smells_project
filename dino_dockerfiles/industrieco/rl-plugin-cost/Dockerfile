
FROM alpine

RUN apk update && \
    apk add --no-cache --upgrade \
      python \
      py2-requests

COPY . /usr/local/rl-overage

CMD ["crond", "-l", "2", "-f"]
