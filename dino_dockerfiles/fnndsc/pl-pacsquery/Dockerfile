#
# Dockerfile for pacquery chrisapp plugin repository.
#
# Build with
#
#   docker build -t <name> .
#
# For example if building a local version, you could do:
#
#   docker build --build-arg UID=$UID -t local/pl-pacsquery .
#
# In the case of a proxy (located at 192.168.13.14:3128), do:
#
#    docker build --build-arg http_proxy=http://192.168.13.14:3128 --build-arg UID=$UID -t local/pl-pacsquery .
#
# To run an interactive shell inside this container, do:
#
#   docker run -ti --entrypoint /bin/bash local/pl-pacsquery
#
# To pass an env var HOST_IP to container, do:
#
#   docker run -ti -e HOST_IP=$(ip route | grep -v docker | awk '{if(NF==11) print $9}') --entrypoint /bin/bash local/pl-pacsquery
#

FROM fnndsc/ubuntu-python3:latest
MAINTAINER fnndsc "dev@babymri.org"

# Pass a UID on build command line (see above) to set internal UID
ARG UID=1001
ENV UID=$UID

ENV APPROOT="/usr/src/pacsquery"  VERSION="1.1.0"
COPY ["pacsquery", "${APPROOT}"]
COPY ["requirements.txt", "${APPROOT}"]
WORKDIR $APPROOT

RUN apt-get update \
  && apt-get install sudo                                             \
  && useradd -u $UID -ms /bin/bash localuser                          \
  && addgroup localuser sudo                                          \
  && echo "localuser:localuser" | chpasswd                            \
  && adduser localuser sudo                                           \
  && apt-get install -y libssl-dev libcurl4-openssl-dev bsdmainutils vim net-tools inetutils-ping \
  && apt-get install -y libssl-dev libcurl4-openssl-dev bsdmainutils \
  && pip install -r requirements.txt


CMD ["pacsquery.py", "--help"]
