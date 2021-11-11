FROM ubuntu:14.04

RUN apt-get update && apt-get install -y \
    wget \
    freeglut3-dev \
    libplib-dev \
    libopenal-dev \
    libpng12-dev \
    zlib1g-dev \
    libogg-dev \
    libvorbis-dev \
    g++ \
    libalut-dev \
    libxi-dev \
    libxmu-dev \
    libxrandr-dev \
    make \
    patch

WORKDIR /tmp

RUN wget https://sourceforge.net/projects/torcs/files/all-in-one/1.3.4/torcs-1.3.4.tar.bz2/download -O torcs-1.3.4.tar.bz2
RUN tar xjf torcs-1.3.4.tar.bz2

WORKDIR torcs-1.3.4

RUN wget https://sourceforge.net/projects/cig/files/SCR%20Championship/Server%20Linux/2.1/scr-linux-patch.tgz/download -O scr-patch.tgz
RUN tar xzf scr-patch.tgz

RUN cd src && \
    patch -p1 -f < ../scr-patch/patch.dat

RUN ./configure

RUN make && make install && make datainstall

CMD ["/usr/local/lib/torcs/torcs-bin"]
