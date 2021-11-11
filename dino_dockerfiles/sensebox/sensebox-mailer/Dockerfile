FROM golang:1.15-alpine as builder

ENV IMPORTPATH=github.com/sensebox/sensebox-mailer

WORKDIR /go/src/${IMPORTPATH}

COPY . ./

RUN apk --no-cache add git && \
  export branch=$(git rev-parse --abbrev-ref HEAD) && \
  export ts=$(TZ=UTC git log --date=local --pretty=format:"%ct" -n 1) && \
  export hash=$(TZ=UTC git log --date=local --pretty=format:"%h" -n 1) && \
  CGO_ENABLED=0 go install -a -tags netgo -ldflags "-extldflags -static -X main.branch=$branch -X main.ts=$ts -X main.hash=$hash" ${IMPORTPATH}/cmd/sensebox-mailer

FROM alpine:3.12

RUN apk add --no-cache git ca-certificates

COPY --from=builder /go/bin/sensebox-mailer /sensebox-mailer

CMD ["/sensebox-mailer"]
