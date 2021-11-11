FROM debian:stretch-slim

LABEL MAINTAINER="beginor <beginor@qq.com>"

COPY src/install.sh /tmp/
RUN /tmp/install.sh

# Default command
CMD [ "mono", "--version" ]
