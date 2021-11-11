FROM ubuntu:latest

RUN apt-get update \
&& apt-get install -y make curl bzip2 python python-pip git

RUN pip install awscli
RUN pip install nrfutil

RUN mkdir -p /usr/local/

RUN curl -L https://developer.arm.com/-/media/Files/downloads/gnu-rm/6_1-2017q1/gcc-arm-none-eabi-6-2017-q1-update-linux.tar.bz2?product=GNU%20ARM%20Embedded%20Toolchain,64-bit,,Linux,6-2017-q1-update -o gcc-arm-none-eabi && \
   tar -xf gcc-arm-none-eabi -C /usr/local/ 

RUN apt-get install -y software-properties-common && \
    add-apt-repository ppa:mfikes/planck && \
    apt-get update && \
    apt-get install -y planck

RUN chmod +x /usr/bin/planck
