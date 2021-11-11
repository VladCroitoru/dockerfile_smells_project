FROM python:2.7-slim
LABEL maintainer Bill Boga

ENV STREAMER_INPUT_OPTIONS=
ENV SET_FLAGS=${SET_FLAGS}

EXPOSE 5000
EXPOSE 8088

ARG curaEngineVersion=15.04.6
ARG octoPrintVersion=1.3.12

VOLUME /var/local/octoprint

ADD entrypoint.sh /usr/local/bin/

ENTRYPOINT [ "entrypoint.sh" ]

RUN set -${SET_FLAGS}e \
    && export buildPackages="build-essential cmake unzip wget" \
    && apt-get update \
    && echo "Install development dependencies." \
    && apt-get install -y --no-install-recommends ${buildPackages} \
    && echo "Install application dependencies." \
    && apt-get install -y --no-install-recommends libav-tools libgphoto2-dev libjpeg62-turbo-dev libprotobuf9 libv4l-dev \

    && export octoPrintInstallDirectory="/usr/local/octoprint" \
    && echo "Download OctoPrint." \
    && cd /tmp/ \
    && wget https://github.com/foosel/OctoPrint/archive/${octoPrintVersion}.tar.gz \
    && echo "Install OctoPrint." \
    && tar -zxf ${octoPrintVersion}.tar.gz \
    && mv -f OctoPrint-${octoPrintVersion} ${octoPrintInstallDirectory} \
    && cd ${octoPrintInstallDirectory} \
    && pip install -r requirements.txt \
    && pip install pillow \
    && python setup.py install \

    && echo "Download mjpg-streamer." \
    && cd /tmp/ \
    && wget https://github.com/jacksonliam/mjpg-streamer/archive/master.zip \
    && echo "Install mjpg-streamer." \
    && unzip master.zip \
    && cd mjpg-streamer-master/mjpg-streamer-experimental \
    && make \
    && make install \

    && export curaEngineInstallDirectory="/usr/local/curaengine" \
    && echo "Download CuraEngine." \
    && cd /tmp/ \
    && wget https://github.com/Ultimaker/CuraEngine/archive/${curaEngineVersion}.tar.gz \
    && echo "Install CuraEngine." \
    && tar -zxf ${curaEngineVersion}.tar.gz \
    && cd CuraEngine-${curaEngineVersion} \
    && mkdir build \
    && make \
    && mv -f ./build ${curaEngineInstallDirectory} \
    && mv ${curaEngineInstallDirectory}/CuraEngine ${curaEngineInstallDirectory}/curaengine \

    && echo "Remove build packages and clean-up \`tmp\`-directories." \
    && apt-get purge -y --auto-remove ${buildPackages} \
    && rm -Rf /tmp0/* /var/tmp/*
