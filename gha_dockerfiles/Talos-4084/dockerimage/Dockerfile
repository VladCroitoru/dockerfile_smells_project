# ----------------------------------
# Pterodactyl Core Dockerfile
# Environment: glibc-fsSLk
# Minimum Panel Version: 0.6.0
# ----------------------------------
FROM ubuntu:latest
ARG DEBIAN_FRONTEND=noninteractive
LABEL author="Tweak" maintainer="tweak@talosbot.xyz"
RUN apt update \
   && apt -y install curl git ffmpeg software-properties-common iproute2 libsqlite3-dev python python3-dev python3-pip ca-certificates dnsutils zip graphicsmagick libmagickcore-dev libmagick++-6.q16-dev \
      build-essential libcairo2-dev libpango-1.0-0 libpango1.0-dev libtool libjpeg-dev wget libwebp-dev libpng-dev libgif-dev librsvg2-dev libavcodec-extra\
   && useradd -m -d /home/container container
RUN add-apt-repository ppa:deadsnakes/ppa \
   && apt update \
   && apt -y install python3.10 \
   && update-alternatives --install /usr/bin/python3 python3 /usr/bin/python3.10 2 \
   && update-alternatives --config python3
RUN python3 --version

RUN curl -fsSL https://deb.nodesource.com/setup_17.x | bash - \
   && apt install -y nodejs
RUN npm -v
RUN node -v
RUN wget https://www.imagemagick.org/download/ImageMagick.tar.gz \
    && tar xzvf ImageMagick.tar.gz \
    && cd ImageMagick-7.1.0-13 \
    && ./configure \
		--with-modules \
    && make \
    && make install \
    && ldconfig /usr/local/lib \
    && identify -version
RUN git clone https://github.com/carlobaldassi/liblqr \
		&& cd liblqr \
		&& ./configure \
		&& make \
		&& make install
RUN  apt update && \ 
     apt install -y --no-install-recommends \ 
     libasound2 libatk1.0-0 libc6 libcairo2 libcups2 libdbus-1-3 libgbm-dev \ 
     libexpat1 libfontconfig1 libgcc1 libgconf-2-4 libgdk-pixbuf2.0-0 libglib2.0-0 libgtk-3-0 libnspr4 \ 
     libpango-1.0-0 libpangocairo-1.0-0 libstdc++6 libx11-6 libx11-xcb1 libxcb1 \ 
     libxcursor1 libxdamage1 libxext6 libxfixes3 libxi6 libxrandr2 libxrender1 libxss1 libxtst6 \ 
     libnss3 
USER container
ENV  USER=container HOME=/home/container
WORKDIR /home/container
COPY ./entrypoint.sh /entrypoint.sh
CMD  ["/bin/bash", "/entrypoint.sh"]
