FROM golang:1.10.0-alpine3.7
WORKDIR /go/src/spew
COPY spew.go .
ENV GOBIN=/go/bin
RUN go install spew.go
CMD ["spew"]

