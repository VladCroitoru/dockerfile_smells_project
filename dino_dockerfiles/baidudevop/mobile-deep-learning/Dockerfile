FROM ubuntu:16.04

RUN apt-get update \
    && apt-get -qq --no-install-recommends install \
        wget \
        libuv1-dev \
        libcurl4-openssl-dev \
    && rm -r /var/lib/apt/lists/* \
    && wget --no-check-certificate https://github.com/baidudevop/mobile-deep-learning/raw/master/libmdl-static.a \
    && wget --no-check-certificate https://github.com/baidudevop/mobile-deep-learning/raw/master/mdltest \
    && chmod +x mdltest

ENTRYPOINT ["./mdltest"]
CMD ["--config=libmdl-static.a"]