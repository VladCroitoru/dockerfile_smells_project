FROM alpine

RUN apk --no-cache add git make gcc libc-dev \
 && git clone git://git.suckless.org/quark \
 && cd quark \
 && make \
 && cp quark /bin/ \
 \
 && cd .. \
 && rm -rf /quark \
 && apk del git make gcc libc-dev \
 \
 && mkdir /data

EXPOSE 80

CMD quark -h 0.0.0.0 -p 80 -d /data
