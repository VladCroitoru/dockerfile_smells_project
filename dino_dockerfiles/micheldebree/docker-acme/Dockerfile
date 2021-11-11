FROM alpine:3.6
LABEL maintainer="michel@micheldebree.nl"

# install prerequisites
RUN apk update && apk add gcc g++ make ca-certificates wget && update-ca-certificates

# install acme
WORKDIR /root
RUN wget https://github.com/meonwax/acme/archive/master.zip && \
    unzip master.zip && \
    rm master.zip

WORKDIR /root/acme-master/src/

RUN make &&\
    mv acme /usr/bin/ &&\
    rm -rf /root/acme-master

WORKDIR /root
ENV ACME=/root
ENTRYPOINT ["acme"]
