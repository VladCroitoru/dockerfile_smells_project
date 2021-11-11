FROM alpine:3.7

ENV PYTHONIOENCODING="UTF-8"

ENV UID 1000
ENV GID 1000
ENV USER htpc
ENV GROUP htpc

ENV MOPIDY_VERSION 2.1.0

COPY mopidy.conf /opt/mopidy/

RUN addgroup -S ${GROUP} -g ${GID} && adduser -D -S -u ${UID} ${USER} -G audio ${GROUP}  && \
    echo "@main http://nl.alpinelinux.org/alpine/edge/main" >> /etc/apk/repositories \
 && echo "@community http://nl.alpinelinux.org/alpine/edge/community" >> /etc/apk/repositories \
 && echo "@testing http://nl.alpinelinux.org/alpine/edge/testing" >> /etc/apk/repositories \
 && apk upgrade --no-cache --available \
 && apk add --no-cache \
        gstreamer \
        gstreamer-tools@main \
        gst-plugins-base@main \
        gst-plugins-good@main \
        gst-plugins-ugly@main \
        gst-plugins-bad@main \
        gst-libav@main \
        py-gst@community \
        py2-pip \
        python2 \
        python2-dev \
        tzdata \
 && pip2 install \
        mopidy==${MOPIDY_VERSION} \
        Mopidy-Iris \
        Mopidy-TuneIn \
        Mopidy-YouTube \
        Mopidy-SoundCloud \
        Mopidy-Local-SQLite \
        youtube-dl && \
        mkdir -p /opt/mopidy/media &&  \
        chown -R ${USER}:${GROUP} /opt/mopidy/ 
        
VOLUME /opt/mopidy/

EXPOSE 6680 6600

USER ${USER}

LABEL version=${MOPIDY_VERSION}
LABEL url=https://github.com/mopidy/mopidy/

CMD /usr/bin/mopidy --config /opt/mopidy/mopidy.conf
