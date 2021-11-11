FROM golang
RUN go get gopkg.in/yaml.v2
RUN go get github.com/robfig/cron
RUN go get github.com/jessevdk/go-flags
RUN go get github.com/bogdanovich/dns_resolver
RUN go get github.com/Azure/azure-sdk-for-go/arm/dns
RUN mkdir /go/azure-dns-sync
COPY ./ /go/azure-dns-sync
WORKDIR /go/azure-dns-sync
RUN go build -o main . \
    && mv /go/azure-dns-sync/main /bin/azure-dns-sync
CMD ["azure-dns-sync"]
