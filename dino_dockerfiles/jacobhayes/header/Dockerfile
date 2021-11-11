FROM golang:alpine

ENV WORKDIR="/go/src/header/"
WORKDIR "${WORKDIR}"

COPY *.go .
RUN go install

CMD ["header"]
