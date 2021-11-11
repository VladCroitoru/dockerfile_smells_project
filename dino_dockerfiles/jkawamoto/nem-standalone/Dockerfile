FROM ubuntu:latest
MAINTAINER Junpei Kawamoto <kawamoto.junpei@gmail.com>

ENV TERM vt100
ENV DEBIAN_FRONTEND noninteractive
RUN apt-get update && \
    apt-get install -y unzip default-jre nano wget socat && \
    apt-get upgrade -y && apt-get clean && \
    rm -rf /var/cache/apt/archives/* /var/lib/apt/lists/

WORKDIR /root/
ADD http://bob.nem.ninja/installer/nis-ncc-0.6.84.zip .
RUN unzip nis-ncc-0.6.84.zip

ENV PORT 8989
EXPOSE $PORT
ADD entrypoint.sh .
ENTRYPOINT ["/root/entrypoint.sh"]
