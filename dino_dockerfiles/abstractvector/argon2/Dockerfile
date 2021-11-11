FROM alpine:latest

MAINTAINER Matt Knight

RUN apk --no-cache add --virtual build-dependencies g++ make ca-certificates openssl &&\
    ## Fetches the source code
    wget https://github.com/P-H-C/phc-winner-argon2/archive/20161029.tar.gz -O /tmp/argon2.tar.gz &&\
    ## Untar it
    tar zxvf /tmp/argon2.tar.gz -C /tmp && rm /tmp/argon2.tar.gz &&\
    mkdir -p /usr/src && mv /tmp/phc-winner-argon2-20161029 /usr/src/argon2 &&\
    cd /usr/src/argon2 &&\
    ## make argon2 and install
    make && make bench && make test && make install &&\
    ## make bench and install
    install bench /usr/bin &&\
    ## free space from build dependencies
    apk del build-dependencies

CMD ["sh"]
