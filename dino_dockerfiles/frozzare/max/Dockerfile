FROM golang:latest AS build
ADD . /go/src/github.com/frozzare/max
RUN cd /go/src/github.com/frozzare/max && CGO_ENABLED=0 GOOS=linux go build -o max

FROM scratch
WORKDIR /app
COPY --from=build /go/src/github.com/frozzare/max/max /app/
ENTRYPOINT ["/app/max"]