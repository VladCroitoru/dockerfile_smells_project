FROM golang:1.6.1-alpine

COPY . ./src/mtcnextbus
RUN go install ./src/mtcnextbus

ENTRYPOINT ["mtcnextbus"]
