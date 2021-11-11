FROM ubuntu
MAINTAINER Yukimitsu Yabuki, yukimitsu.yabuki@gmail.com
RUN apt-get update && apt-get -y upgrade \
    && apt-get -y install wget \
    && wget http://ccb.jhu.edu/software/stringtie/dl/stringtie-1.2.3.Linux_x86_64.tar.gz \
    && tar xvfz stringtie-1.2.3.Linux_x86_64.tar.gz \
    && apt-get clean \
    && rm -r /var/lib/apt/lists/* \
    && cp /stringtie-1.2.3.Linux_x86_64/* /usr/local/bin/.
WORKDIR /stringtie-1.2.3.Linux_x86_64
