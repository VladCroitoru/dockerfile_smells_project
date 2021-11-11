from resin/raspberry-pi2-golang as builder

env CGO_ENABLED=0
env GOOS=linux

RUN [ "cross-build-start" ]
RUN set -ex; \
      for pkg in elastic/beats/filebeat; \
      do \
        echo $pkg; \
        go get github.com/$pkg; \
        go build -a -installsuffix cgo github.com/$pkg \
        && go install github.com/$pkg \
        && rm -rf /go/src/github.com/$pkg ;\
      done; \
      rm -rf /go/src/*

RUN [ "cross-build-end" ]

FROM resin/raspberry-pi2-alpine

RUN [ "cross-build-start" ]
RUN mkdir /usr/share/filebeat

COPY --from=docker.elastic.co/beats/filebeat:6.2.1 /usr/share/filebeat /usr/share/filebeat

COPY --from=builder /go/bin/filebeat /usr/share/filebeat
RUN [ "cross-build-end" ]

WORKDIR /usr/share/filebeat

CMD /usr/share/filebeat/filebeat -e
