FROM ubuntu:trusty

# need libavformat54
RUN apt-get update && apt-get -y install build-essential libavcodec-dev libavformat-dev libswscale-dev

ADD ./ /qpsnr

RUN cd /qpsnr && make

ENTRYPOINT ["/qpsnr/qpsnr"]
