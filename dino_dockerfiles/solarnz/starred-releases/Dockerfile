FROM golang
ADD . /go/src/github.com/solarnz/starred-releases/
RUN go get github.com/solarnz/starred-releases
RUN go install github.com/solarnz/starred-releases

ENTRYPOINT /go/bin/starred-releases
ENV FEED_HTTP ":80"
ENV FEED_CLIENT_ID ""
ENV FEED_CLIENT_SECRET ""
EXPOSE 80
