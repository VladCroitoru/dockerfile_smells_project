FROM alpine:latest

RUN apk add --no-cache bash curl
RUN curl -o /tmp/dnetc-current.tar.gz http://http.distributed.net/pub/dcti/current-client/dnetc-linux-x86-elf-uclibc.tar.gz
RUN mkdir -p /opt
RUN cd /tmp && tar -xzvf dnetc-current.tar.gz  && mv dnetc*-linux-x86-elf-uclibc /opt/dnetc

ADD dnetc.ini /opt/dnetc/dnetc.ini

CMD ["/opt/dnetc/dnetc"]

