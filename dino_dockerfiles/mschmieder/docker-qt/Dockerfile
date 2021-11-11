FROM ubuntu:16.04
MAINTAINER Matthias Schmieder <matthias.schmieder@stryker.com>

ENV DEBIAN_FRONTEND noninteractive

# Install core dependencies
RUN apt-get update && \
    apt-get install -y \
        gcc g++ build-essential xorg wget libglib2.0-0 libx11-xcb-dev libglu1-mesa-dev && \
    rm -rf /var/lib/apt/lists/*

COPY install_qt_silent.sh install_qt_silent.qs.template /install/

ARG QT_INSTALL_PACKAGES="qt.qt5.5110.gcc_64"
ARG QT_INSTALL_DIR="/opt/qt"

ENV QT_INSTALL_DIR=$QT_INSTALL_DIR

RUN cd /install && \
    ./install_qt_silent.sh --install-dir "${QT_INSTALL_DIR}" --packages "${QT_INSTALL_PACKAGES}" && \
    rm -rf /install

RUN echo "export PATH=$(dirname $(find ${QT_INSTALL_DIR} -type f -executable -name 'qmake' | tail -n1)):$$PATH" >> /etc/profile
RUN echo "export PATH=$(dirname $(find ${QT_INSTALL_DIR} -type f -executable -name 'qbs' | tail -n1)):$$PATH" >> /etc/profile

COPY entrypoint.sh .
ENTRYPOINT ["./entrypoint.sh"]