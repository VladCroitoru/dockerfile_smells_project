FROM ubuntu:trusty

ARG QT=5.7.1
ARG QTM=5.7
ARG QTSHA=fdf6b4fb5ee9ade2dec74ddb5bea9e1738911e7ee333b32766c4f6527d185eb4
ARG VCS_REF
ARG BUILD_DATE

LABEL org.label-schema.build-date="$BUILD_DATE" \
      org.label-schema.name="qt-build" \
      org.label-schema.description="A headless Qt $QTM build environment for Ubuntu" \
      org.label-schema.url="e.g. https://github.com/garthk/qt-build" \
      org.label-schema.vcs-ref="$VCS_REF" \
      org.label-schema.vcs-url="https://github.com/garthk/qt-build.git" \
      org.label-schema.version="$QT" \
      org.label-schema.schema-version="1.0"

RUN apt-get update -q && \
    DEBIAN_FRONTEND=noninteractive apt-get install -q -y --no-install-recommends \
        ant \
        build-essential \
        ca-certificates \
        default-jdk \
        git \
        libfontconfig1 \
        libice6 \
        libsm6 \
        libX11-xcb1 \
        libxext6 \
        libxrender1 \
        openssh-client \
        p7zip \
        xvfb \
    && apt-get clean

ADD qt-installer-noninteractive.qs /tmp/qt/script.qs
ADD http://download.qt.io/official_releases/qt/${QTM}/${QT}/qt-opensource-linux-x64-${QT}.run /tmp/qt/installer.run

RUN echo "${QTSHA}  /tmp/qt/installer.run" | shasum -a 256 -c \
    && chmod +x /tmp/qt/installer.run \
    && xvfb-run /tmp/qt/installer.run --script /tmp/qt/script.qs \
     | egrep -v '\[[0-9]+\] Warning: (Unsupported screen format)|((QPainter|QWidget))' \
    && rm -rf /tmp/qt

RUN echo /opt/qt/${QTM}/gcc_64/lib > /etc/ld.so.conf.d/qt-${QTM}.conf
RUN locale-gen en_US.UTF-8 && DEBIAN_FRONTEND=noninteractive dpkg-reconfigure locales

ENV PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:/opt/qt/${QTM}/gcc_64/bin
