FROM golang:alpine AS builder

RUN apk update && apk add --no-cache git

WORKDIR $GOPATH/src/mypackage/myapp/
COPY . .
RUN go build -o /go/bin/full_cycle_rocks

FROM scratch AS bundler

COPY --from=builder /go/bin/full_cycle_rocks /go/bin/full_cycle_rocks
ENTRYPOINT [ "/go/bin/full_cycle_rocks" ]