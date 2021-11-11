FROM golang:alpine AS build-env
ADD . /src
RUN cd /src && go build -o server

FROM alpine:3.4
COPY --from=build-env /src/server /
EXPOSE 8080
ENTRYPOINT ["/server"]

