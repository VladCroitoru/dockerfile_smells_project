# Docker file for the neuproseg plugin app

FROM fnndsc/ubuntu-python3:latest
MAINTAINER fnndsc "dev@babymri.org"

# Pass a UID on build command line (see above) to set internal UID
ARG UID=1001
ENV UID=$UID

ENV APPROOT="/usr/src/neuproseg" 
COPY ["neuproseg", "${APPROOT}"]
COPY ["requirements.txt", "${APPROOT}"]

WORKDIR $APPROOT

RUN apt-get update \
  && apt-get install sudo                                             \
  && useradd -u $UID -ms /bin/bash localuser                          \
  && addgroup localuser sudo                                          \
  && echo "localuser:localuser" | chpasswd                            \
  && adduser localuser sudo                                           \
  && apt-get install -y libssl-dev libcurl4-openssl-dev bsdmainutils vim net-tools inetutils-ping \
  && apt-get install python3-webob                                    \
  && apt install -y python3-tk     				      \
  && pip install -r requirements.txt 

CMD ["neuproseg.py", "--help"]
