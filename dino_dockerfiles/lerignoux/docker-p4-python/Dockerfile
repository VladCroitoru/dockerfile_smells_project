FROM debian:stable-slim
MAINTAINER Erignoux Laurent "lerignoux@gmail.com"

## Adding Perforce to the container ##
RUN apt-get update && apt-get -y install bash curl git python3 python3-dev python3-pip openssl

# not needed anymore ?
# ADD bin/lib-x64.tgz /

ENV VISUAL=vi
ENV P4_VERSION 19.2

RUN curl -sSL -O http://cdist2.perforce.com/perforce/r19.2/bin.linux26x86_64/p4 && mv p4 /usr/bin/p4 && chmod +x /usr/bin/p4

RUN pip3 install --upgrade pip setuptools wheel
RUN pip3 install --upgrade p4python

## End perforce requirements ##

COPY . /app
WORKDIR /app

CMD ["python"]
