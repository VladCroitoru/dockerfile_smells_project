FROM alpine:3.6

RUN apk --no-cache update && \
    apk add --no-cache wget unzip && \
	rm -rf /var/cache/apk/*

ENV PGWEB_VERSION 0.9.11

RUN cd /tmp && \
  wget --no-check-certificate https://github.com/sosedoff/pgweb/releases/download/v$PGWEB_VERSION/pgweb_linux_amd64.zip && \
  unzip pgweb_linux_amd64.zip -d /app && mv /app/pgweb_linux_amd64 /app/pgweb && \
  chmod +x /app/pgweb && \
  rm -f pgweb_linux_amd64.zip

WORKDIR /app

EXPOSE 8080
ENTRYPOINT ["/app/pgweb"]
CMD ["-s", "--bind=0.0.0.0", "--listen=8080"]