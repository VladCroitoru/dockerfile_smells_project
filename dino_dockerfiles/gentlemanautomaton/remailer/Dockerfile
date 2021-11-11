FROM golang:latest

ARG SOURCE_COMMIT
ENV SOURCE_COMMIT=${SOURCE_COMMIT}

EXPOSE 25

WORKDIR /go/src/github.com/dustywilson/remailer
COPY . .

RUN go get -v github.com/flashmob/go-guerrilla
RUN go install -ldflags "-X main.commitVersion=${SOURCE_COMMIT}" github.com/dustywilson/remailer/cmd/server

WORKDIR /config
CMD ["/go/bin/server"]
