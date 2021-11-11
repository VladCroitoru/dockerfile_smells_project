FROM golang:1.4-cross

RUN apt-get update

#imagegemagick
RUN apt-get -y install libmagic-dev ghostscript imagemagick pkg-config yasm

#ffmpeg
RUN wget https://github.com/FFmpeg/FFmpeg/archive/n2.6.3.tar.gz -O - | tar -xzv -C /root

RUN cd /root/FFmpeg-n2.6.3 \
    && ./configure  --enable-shared \
    && make \
    && make install

RUN ldconfig

RUN go get -v github.com/jteeuwen/go-bindata github.com/tools/godep

EXPOSE :8080
