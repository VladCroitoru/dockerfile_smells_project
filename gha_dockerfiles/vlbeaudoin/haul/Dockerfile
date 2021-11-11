FROM golang:1.16

LABEL author="Victor Lacasse-Beaudoin <victor.lacassebeaudoin@gmail.com>"
LABEL license="MIT"
LABEL licensee="The Haul Authors"
LABEL repo="https://github.com/vlbeaudoin/haul"

WORKDIR /go/src/app

COPY . .

RUN go get -d -v . && \
    go install -v . && \
    mkdir /srv/haul /etc/haul

CMD haul -h
