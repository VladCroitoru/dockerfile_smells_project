FROM wurstmeister/kafka:0.9.0.1

ENV GOLANG_VERSION 1.7.3
ENV GOLANG_DOWNLOAD_URL https://golang.org/dl/go$GOLANG_VERSION.linux-amd64.tar.gz
ENV GOLANG_DOWNLOAD_SHA256 508028aac0654e993564b6e2014bf2d4a9751e3b286661b0b0040046cf18028e

RUN curl -fsSL "$GOLANG_DOWNLOAD_URL" -o golang.tar.gz \
	&& echo "$GOLANG_DOWNLOAD_SHA256  golang.tar.gz" | sha256sum -c - \
	&& tar -C /usr/local -xzf golang.tar.gz \
	&& rm golang.tar.gz

ENV GOPATH /go
ENV PATH $GOPATH/bin:/usr/local/go/bin:$PATH

ADD . $GOPATH/src/prometheus-kafka-consumer-group-exporter

RUN cd $GOPATH/src/prometheus-kafka-consumer-group-exporter \
  && go get . \
  && go build -o prometheus-kafka-consumer-group-exporter .

ENV KAFKA_URL kafka:9092

CMD ["/go/src/prometheus-kafka-consumer-group-exporter/startup.sh"]
