FROM golang

RUN apt-get update && apt-get install -y libzmq3-dev
RUN mkdir /go/src/mdgbroker

ADD *.go /go/src/mdgbroker
RUN go get mdgbroker
RUN go install mdgbroker

ENV ADDR 0.0.0.0
ENV PORT 9999

EXPOSE ${PORT}
CMD /go/bin/mdgbroker -addr ${ADDR} -port ${PORT}
