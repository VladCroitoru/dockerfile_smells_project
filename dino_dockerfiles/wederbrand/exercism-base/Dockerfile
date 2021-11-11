# exercism base
#
# VERSION               1.0

FROM wederbrand/base
MAINTAINER Andreas Wederbrand andreas@wederbrand.se

# install cli
WORKDIR /usr/local/bin
RUN wget -qO- https://github.com/exercism/cli/releases/download/v2.2.1/exercism-linux-64bit.tgz | tar -zx
RUN chmod +x exercism

RUN mkdir /root/exercism
WORKDIR /root/exercism
RUN exercism configure --dir="/root/exercism"

USER root
CMD bash