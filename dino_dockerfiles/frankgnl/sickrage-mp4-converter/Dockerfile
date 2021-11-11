FROM alpine:edge
MAINTAINER frank@groenewoud.me

ENV LANG='en_US.UTF-8' \
    LANGUAGE='en_US.UTF-8' \
    TERM='xterm'

# OS update & package installation
RUN apk -U upgrade && \
    apk -U add \
        py2-pip \
        ca-certificates \
        git \
        python \
        py-libxml2 \
        py-lxml \
        make \
        gcc \
        g++ \
        python-dev \
        openssl \
        openssl-dev \
        libffi-dev \
        unrar \
        tzdata

# pip package installation
RUN pip install --upgrade pip && \
    pip --no-cache-dir install --upgrade setuptools && \
    pip --no-cache-dir install --upgrade pyopenssl \
        requests \
        requests[security] \
        requests-cache \
        cheetah \
        babelfish \
        "guessit<2" \
        "subliminal<2" \
        stevedore==1.19.1 \
        python-dateutil \
        deluge-client \
        qtfaststart \
        requirements

RUN cp /usr/share/zoneinfo/Europe/Amsterdam /etc/localtime

# clone Sickrage
RUN git clone --depth 1 https://github.com/SickRage/SickRage.git /sickrage && \
    apk del make gcc g++ python-dev && \
    rm -rf /tmp && \
    rm -rf /var/cache/apk/*

COPY ./start.sh /start.sh
RUN chmod u+x  /start.sh

WORKDIR /tmp

# clone ffmpeg
RUN wget -q https://johnvansickle.com/ffmpeg/releases/ffmpeg-release-64bit-static.tar.xz && \
    tar xJf ffmpeg-release-64bit-static.tar.xz && \
    mv ffmpeg-*-64bit-static/ffmpeg /usr/local/bin/ && \
    mv ffmpeg-*-64bit-static/ffprobe /usr/local/bin/ && \
    rm -rf ffmpeg*

# clone mp4 automator
RUN git clone --depth 1 https://github.com/mdhiggins/sickbeard_mp4_automator.git

WORKDIR /config

VOLUME ["/config", "/data"]

EXPOSE 8081

CMD ["/start.sh"]
