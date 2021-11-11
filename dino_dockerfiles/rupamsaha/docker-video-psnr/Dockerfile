FROM ubuntu:14.04

WORKDIR /root/psnr

RUN apt-get update && apt-get install -y wget build-essential libavcodec-dev libavformat-dev libswscale-dev

COPY ./psnr /root/psnr

RUN make

CMD /root/psnr/qpsnr -s $START -m $END -r $VIDEO1 $VIDEO2

