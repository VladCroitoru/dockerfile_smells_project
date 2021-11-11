# Dockerfile
FROM debian:bullseye

RUN apt-get clean && apt-get update && apt-get install -y \ 
    gnupg \
    wget \
    && apt-get clean && rm -rf /var/lib/apt/lists/*

RUN echo "deb http://www.yade-dem.org/packages/ bullseye main" >> /etc/apt/sources.list

RUN wget -O - http://www.yade-dem.org/packages/yadedev_pub.gpg | apt-key add 


RUN apt-get clean && apt-get update && \
    apt-get install -y \
    fluxbox \
    net-tools \
    unzip \
    vim \
    x11vnc \
    xvfb \
    yadedaily

RUN apt-get autoclean && \
    apt-get autoremove && \
    rm -rf /var/lib/apt/lists/*

COPY startup /usr/local/bin/

CMD ["bash","startup"]


EXPOSE 5900

