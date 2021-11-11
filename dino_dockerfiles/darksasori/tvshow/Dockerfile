FROM darksasori/golang-dep as builder

WORKDIR /go/src/github.com/darksasori/tvshow

COPY Gopkg.lock Gopkg.lock
COPY Gopkg.toml Gopkg.toml

RUN dep ensure -v -vendor-only

COPY . .

RUN GOOS=linux go build -o tvshow

FROM alpine:3.7

RUN addgroup -S tvshow && adduser -S -g tvshow tvshow

EXPOSE 8080

USER tvshow

ENV TVSHOW_MONGODB="mongodb://localhost:27017/tvshow"

COPY --from=builder /go/src/github.com/darksasori/tvshow/tvshow /usr/bin/tvshow

CMD ["tvshow"]
