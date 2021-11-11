FROM golang:alpine as builder
RUN apk add -u git tzdata
RUN go get github.com/ericchiang/pup

FROM alpine:latest
RUN apk add -u jq git
COPY --from=builder /go/bin/pup /usr/local/bin/pup
COPY --from=builder /usr/share/zoneinfo/Europe/London /etc/localtime
COPY towerbridge  /usr/local/bin/towerbridge
RUN chmod a+x /usr/local/bin/towerbridge
RUN echo "Europe/London" >  /etc/timezone
WORKDIR /data
CMD ["towerbridge", "-l"] 
