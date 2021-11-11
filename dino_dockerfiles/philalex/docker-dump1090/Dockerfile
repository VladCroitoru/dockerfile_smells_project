FROM debian:jessie
MAINTAINER Philippe ALEXANDRE <alexandre.philippe+github@gmail.com>
ENV DEBIAN_FRONTEND noninteractive
ENV ENV INITRD No
ENV DEBIAN_PRIORITY critical
ENV DEBCONF_NOWARNINGS yes

RUN apt-get update && apt-get upgrade -y && apt-get install -y git make gcc librtlsdr-dev libusb-1.0-0-dev pkg-config
WORKDIR /tmp
RUN git clone https://github.com/antirez/dump1090.git
WORKDIR /tmp/dump1090
RUN make

EXPOSE 8080
EXPOSE 30001
EXPOSE 30002
EXPOSE 30003

ENTRYPOINT ["./dump1090", "--interactive","--aggressive","--net","--metric"]