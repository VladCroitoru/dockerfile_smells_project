FROM golang:alpine 
LABEL maintainer "Darwin Smith II <dwin@dlsmi.com>"
LABEL app_version="0.1.0" architecture="amd64"
RUN apk add --no-cache git curl
VOLUME /static
VOLUME /log
ENV GIN_MODE=release

WORKDIR /go/src/app
COPY /app /go/src/app

RUN go-wrapper download
RUN go-wrapper install

EXPOSE 8080
HEALTHCHECK --interval=5m --timeout=3s \
  CMD curl -f http://localhost:8080/json/status || exit 1
CMD ["go-wrapper", "run"] # ["app"]
# docker build . -t dwin/gotestserver:0.1.0
# docker run -d -v ~/Docker/gotestserver/log:/log -v ~/Docker/gotestserver/static:/static -p 8080:8080 --name gotest dwin/gotestserver:0.1.0