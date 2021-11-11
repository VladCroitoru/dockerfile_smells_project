FROM alpine:edge
MAINTAINER frank@groenewoud.me

ENV LANG='en_US.UTF-8' \
    LANGUAGE='en_US.UTF-8' \
    TERM='xterm'

# OS update & package installation
RUN apk -U upgrade && \
    apk -U add \
        bash \
        ca-certificates \
        py2-pip \
        git \
        python \
        python-dev \
        openssl \
        gcc \
        g++ \
        libffi-dev \
        openssl-dev \
        unrar \
        p7zip \
        wget

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
        stevedore \
        python-dateutil \
        deluge-client \
        qtfaststart \
        requirements

WORKDIR /

#NZBget installation
RUN wget -O - http://nzbget.net/info/nzbget-version-linux.json | \
    sed -n "s/^.*stable-download.*: \"\(.*\)\".*/\1/p" | \
    wget --no-check-certificate -i - -O nzbget-latest-bin-linux.run
RUN sh nzbget-latest-bin-linux.run

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
RUN git clone --depth 1 https://github.com/mdhiggins/sickbeard_mp4_automator.git \
    && git clone --depth 1 https://github.com/clinton-hall/nzbToMedia.git \
    && git clone --depth 1 https://github.com/nzbget/VideoSort.git

WORKDIR /config

VOLUME ["/config", "/data"]

EXPOSE 6789

CMD ["/start.sh"]
