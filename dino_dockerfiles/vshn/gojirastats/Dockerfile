FROM golang:1.9

USER nobody
ENV DIR=/go/src/github.com/vshn/gojirastats

RUN mkdir -p $DIR
WORKDIR $DIR

COPY . $DIR
RUN go-wrapper download && go-wrapper install

CMD ["go-wrapper", "run"]
