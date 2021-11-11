FROM golang:alpine as build

RUN apk add --no-cache git && \
    wget -O- https://raw.githubusercontent.com/golang/dep/master/install.sh | sh

WORKDIR /go/src/github.com/mhutter/podstalk

COPY . .
RUN ls -la
RUN dep ensure
RUN go install -v ./cmd/...

FROM alpine

ENV PORT=8080
EXPOSE 8080

COPY --from=build /go/bin/podstalk /bin/
COPY --from=build /go/bin/stream /bin/
CMD ["/bin/podstalk"]
