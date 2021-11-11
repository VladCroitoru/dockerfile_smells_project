FROM golang

# Install deps
RUN go get github.com/lib/pq

# Install microcms
RUN go get github.com/miro662/microcms

# Install microcmsd
RUN go install github.com/miro662/microcms/microcmsd

ENTRYPOINT ["/go/bin/microcmsd", "/microcms"]
EXPOSE 8080