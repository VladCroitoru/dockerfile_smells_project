FROM golang:1.14 AS build
WORKDIR /go/src/github.com/seanhoughton/git-sync/
COPY go.mod go.sum main.go ./
RUN go build .

FROM alpine:latest
RUN apk --no-cache add \
	ca-certificates \
	git \
	openssh-client

COPY --from=build /go/src/github.com/seanhoughton/git-sync/git-sync /go/bin/git-sync
VOLUME ["/git"]
ENV GIT_SYNC_DEST /git
ADD ./docker-entrypoint.sh /docker-entrypoint.sh
RUN chmod +x /docker-entrypoint.sh
ENTRYPOINT ["/docker-entrypoint.sh"]
CMD ["server"]
