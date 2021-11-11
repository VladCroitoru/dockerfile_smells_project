FROM alpine:latest
ENV HUGO_VERSION=0.30.2
RUN apk add --no-cache wget ca-certificates \
  && cd /tmp \
  && wget https://github.com/gohugoio/hugo/releases/download/v${HUGO_VERSION}/hugo_${HUGO_VERSION}_Linux-64bit.tar.gz \
  && tar -xvf hugo_*.tar.gz \
  && mv hugo /usr/local/bin \
  && apk del wget ca-certificates \
  && rm -rf /tmp/*
EXPOSE 1313
CMD ["hugo"]