FROM alpine:3.10 as build

ENV SAUCE_VERSION 4.5.4

RUN apk update && apk add wget && rm -rf /var/cache/apk/*

RUN wget https://saucelabs.com/downloads/sc-$SAUCE_VERSION-linux.tar.gz -O - | tar -xz

RUN ls -la
RUN mkdir -p /out/bin && \
  cp sc-$SAUCE_VERSION-linux/bin/sc  /out/bin/

FROM debian:jessie-slim
LABEL maintainer="Joscha Feth <joscha@feth.com>"
COPY --from=build /out /usr/local

RUN apt-get update -qqy \
 && apt-get install -qqy \
      ca-certificates \
 && rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*

ENTRYPOINT ["sc"]

EXPOSE 4445
EXPOSE 8032

CMD ["--version"]
