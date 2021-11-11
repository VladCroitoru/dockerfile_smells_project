From ubuntu:16.04

RUN apt-get update && apt-get install --no-install-recommends -y \
    software-properties-common \
    && add-apt-repository ppa:jonathonf/ffmpeg-3 -y \
    && apt-get update && apt-get install --no-install-recommends -y \
    wget \
    rtmpdump \
    vlc-nox \
    swftools \
    ffmpeg \
&& apt-get clean \
&& rm -rf /var/lib/apt/lists/*

ADD run.sh /run.sh
RUN chmod +x /run.sh
RUN useradd -s /bin/bash -m docker
RUN mkdir -p /media/recorder && chmod 777 /media/recorder 

EXPOSE 8000

USER docker
ENTRYPOINT ["/run.sh"]
