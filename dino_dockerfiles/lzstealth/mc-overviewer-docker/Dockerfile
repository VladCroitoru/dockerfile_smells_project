FROM ubuntu:18.04

ENV RENDER=true
ENV POI=false
ENV FORCERENDER=false

RUN apt-get update && \
    apt-get update && apt-get install -y \
    build-essential \
    python3-pil \
    python3-dev \
    python3-numpy \
    git \
    wget \
&& rm -rf /var/lib/apt/lists/*

RUN mkdir /versions
RUN mkdir /tmp/overviewer
WORKDIR /tmp/overviewer

RUN git clone https://github.com/overviewer/Minecraft-Overviewer.git .
RUN python3 setup.py build
COPY start-overviewer.sh /
COPY mcVersionGet.py /
RUN chmod 766 /start-overviewer.sh /mcVersionGet.py

ENTRYPOINT ["/bin/bash", "-c", "/start-overviewer.sh"]
