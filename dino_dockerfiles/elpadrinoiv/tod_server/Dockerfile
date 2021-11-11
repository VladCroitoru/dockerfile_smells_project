FROM alpine:3.4

ARG BUILD_DATE
ARG BUILD_VCS_REF
ARG BUILD_VERSION

ARG TCP_ENABLED
ARG UDP_ENABLED
ARG LOG_LEVEL
ARG LOG_FORMAT

ENV TCP_ENABLED=${TCP_ENABLED:-true}
ENV UDP_ENABLED=${UDP_ENABLED:-true}
ENV LOG_LEVEL=${LOG_LEVEL:-INFO}
ENV LOG_FORMAT=${LOG_FORMAT:-plain}


LABEL org.label-schema.build-date=$BUILD_DATE \
      org.label-schema.vcs-url="https://github.com/elpadrinoIV/tod_server.git" \
      org.label-schema.vcs-ref=$BUILD_VCS_REF \
      org.label-schema.version=$BUILD_VERSION \
      com.microscaling.license=GPL-3.0


ADD docker /app

ENV GOROOT=/usr/lib/go \
    GOPATH=/gopath \
    GOBIN=/gopath/bin \
    PATH=$PATH:$GOROOT/bin:$GOPATH/bin

WORKDIR /gopath/src/app
ADD . /gopath/src/app

RUN apk add --no-cache git go g++ && \
  go get && \
  go build && \
  cp app /app/tod_server && \
  apk del git go g++ && \
  rm -rf /gopath

WORKDIR /app
ENTRYPOINT ["/app/init.sh"]
