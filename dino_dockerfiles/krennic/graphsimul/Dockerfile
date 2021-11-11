FROM debian

RUN apt-get update &&\
    apt-get install -y --no-install-recommends\
    libboost-all-dev\
    && rm -rf /var/lib/apt/lists/*

COPY log4cpp.tar.gz ~/

RUN tar xvf ~/log4cpp.tar.gz &&\
    cd ~/log4cpp &&\
    ./configure &&\
    make &&\
    make check &&\
    make install