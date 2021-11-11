# build stage
FROM golang:alpine AS build-env
ADD . /src
RUN cd /src && go build -o slack-bughouse

# Final container
FROM alpine
MAINTAINER <jim@jimturpin.com>

COPY --from=build-env /src/slack-bughouse /
EXPOSE 9090

CMD ["/slack-bughouse"]
