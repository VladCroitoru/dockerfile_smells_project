FROM debian:8

USER root

RUN apt-get update && \
    apt-get upgrade -y && \
    apt-get install -y build-essential curl git python-setuptools ruby && \
    apt-get install -y python-dev

ENV LANG=C.UTF-8 LC_ALL=C.UTF-8

RUN groupadd --system gdal && \
    useradd --system --create-home -g gdal gdal

USER gdal

RUN ruby -e "$(curl -fsSL https://raw.githubusercontent.com/Linuxbrew/install/master/install)" && \
    echo 'export PATH="/home/gdal/.linuxbrew/bin:$PATH"' >> /home/gdal/.bashrc && \
    echo 'export MANPATH="/home/gdal/.linuxbrew/share/man:$MANPATH"' >> /home/gdal/.bashrc && \
    echo 'export INFOPATH="/home/gdal/.linuxbrew/share/info:$INFOPATH"' >> /home/gdal/.bashrc

RUN /home/gdal/.linuxbrew/bin/brew update && \
    /home/gdal/.linuxbrew/bin/brew update && \
    /home/gdal/.linuxbrew/bin/brew install libspatialite --without-test && \
    /home/gdal/.linuxbrew/bin/brew install gdal --with-postgresql
