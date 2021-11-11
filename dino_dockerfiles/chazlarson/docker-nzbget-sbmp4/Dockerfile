FROM linuxserver/nzbget
MAINTAINER chazlarson

COPY ./sb_mp4/*.*      /tmp/

RUN mkdir /opt && \
    cd /opt && \
    apk add --no-cache --update go git && \
    apk add --no-cache openssh && \
    git clone --depth 1 https://github.com/mdhiggins/sickbeard_mp4_automator.git && \
    cp /tmp/autoProcess.ini sickbeard_mp4_automator && \
    chmod a+w sickbeard_mp4_automator && \
    rm -fr sickbeard_mp4_automator/.git && \
    apk add --no-cache py-setuptools && \
    curl -f -O https://bootstrap.pypa.io/get-pip.py && \
    python get-pip.py && \
    rm -f get-pip.py && \
    apk add --no-cache nano ffmpeg python-dev musl-dev libffi-dev openssl-dev && \
    pip install --no-cache-dir -r /tmp/requirements.txt && \
    chown -R root:root sickbeard_mp4_automator && \
    chmod -R a+w sickbeard_mp4_automator && \
    rm -rf /tmp/*
