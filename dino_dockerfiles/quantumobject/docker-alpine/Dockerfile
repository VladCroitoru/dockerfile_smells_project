FROM alpine:edge
MAINTAINER QuantumObject <angel@quantumobject.com>

ADD . /build

RUN chmod 750 /build/system_services.sh
RUN /build/system_services.sh 

CMD ["/sbin/my_init"]
