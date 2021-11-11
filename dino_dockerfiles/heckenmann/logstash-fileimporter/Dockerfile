#########################################
FROM golang:1.10-alpine3.7 as build

RUN mkdir -p /opt/lfi
WORKDIR /opt/lfi
COPY logstash-fileimporter.go .
RUN go build logstash-fileimporter.go

#########################################
FROM alpine:3.7
COPY --from=build /opt/lfi/logstash-fileimporter /
CMD /logstash-fileimporter
