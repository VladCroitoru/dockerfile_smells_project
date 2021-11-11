FROM ubuntu:20.04
ENV TZ="America/New_York" DEBIAN_FRONTEND=noninteractive
WORKDIR /root

# configure tz, install python & pip
RUN cd /root && echo $TZ > /etc/timezone && \
    apt-get update && \
    apt-get upgrade -y && \
    apt-get install -y python3 python3-pip wget tzdata unzip firefox firefox-geckodriver && \
    pip3 install -U pip && \
    rm /etc/localtime && \
    ln -snf /usr/share/zoneinfo/$TZ /etc/localtime && \
    dpkg-reconfigure -f noninteractive tzdata && \
    apt-get remove -y unzip wget && \
    rm -rf /var/lib/apt/lists/*

# Install Firefox and driver
RUN apt-get update && \
    apt-get install -y firefox firefox-geckodriver && \
    rm -rf /var/lib/apt/lists/*

COPY ./requirements.txt /root/requirements.txt

RUN pip3 install wheel setuptools && pip3 install -r /root/requirements.txt