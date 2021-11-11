#
#   Author: Rohith
#   Date: 2015-08-05 01:06:06 +0100 (Wed, 05 Aug 2015)
#
#  vim:ts=2:sw=2:et
#
FROM busybox:latest
MAINTAINER Rohith <gambol99@gmail.com>

ADD https://github.com/gambol99/node-register/releases/download/v0.0.5/node-register_0.0.5_linux_x86_64.gz /node-register.gz
RUN gunzip /node-register.gz && \
    chmod +x /node-register

ENTRYPOINT [ "/node-register" ]
