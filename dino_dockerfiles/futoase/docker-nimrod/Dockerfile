FROM ubuntu

MAINTENER Keiji Matsuzaki <futoase@gmail.com>

RUN apt-get install -y git gcc g++
RUN git clone git://github.com/Araq/Nimrod.git /root/Nimrod
RUN cd /root/Nimrod && git clone --depth 1 git://github.com/nimrod-code/csources
RUN cd /root/Nimrod/csources && chmod +x ./build.sh && ./build.sh
ENV PATH /root/Nimrod/bin:/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin
