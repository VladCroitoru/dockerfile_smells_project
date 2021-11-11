# chinadns
#
# VERSION 0.0.1

FROM ubuntu:14.04
MAINTAINER Yale Huang <yale.huang@trantect.com>

RUN apt-get update && \
    apt-get install -y --no-install-recommends python-pip

RUN pip install chinadns

RUN apt-get clean

EXPOSE 53/udp 53/tcp
CMD ["/usr/local/bin/chinadns", "-b", "0.0.0.0"]
