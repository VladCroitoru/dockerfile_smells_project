FROM golang:alpine
MAINTAINER Amin Jams <aminjam.software@gmail.com>

RUN apk update && apk add git bash

RUN go get github.com/aminjam/goflat/cmd/goflat
RUN echo "$(goflat --version)"

CMD ["bash"]

# e.g.
# docker run -it aminjam/goflat bash -c 'export EXP=/go/src/github.com/aminjam/goflat/.examples; goflat -t $EXP/template.xml -i $EXP/inputs/private.go -i $EXP/inputs/repos.go'
