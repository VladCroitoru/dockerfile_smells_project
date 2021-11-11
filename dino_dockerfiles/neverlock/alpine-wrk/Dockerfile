FROM alpine
MAINTAINER Chanchai Junlouchai (neverlock.org) "neverlock@gmail.com"

RUN apk add --update alpine-sdk \
        && apk add --update perl \
        && apk add --update libssl1.0
WORKDIR /root
RUN git clone https://github.com/wg/wrk.git
WORKDIR /root/wrk
RUN make \
        && mv /root/wrk/wrk /usr/local/bin \
        && rm -rf /root/wrk \
        && apk del --purge alpine-sdk \
        && apk add libgcc
CMD ["/usr/local/bin/wrk"]
