FROM frigg/frigg-test-base:latest

ENV DEBIAN_FRONTEND noninteractive


RUN apt-get update && apt-get install -y \
        postfix \
        htop \
        screen \
        vim \
        git \
        supervisor \
        libffi-dev \
        libmysqlclient-dev \
        build-essential \
        python-setuptools \
        apache2 \
        libapache2-mod-xsendfile \
        apache2-mpm-prefork \
        libapache2-mod-wsgi \
        nfs-common \
        subversion \
        libssl-dev \
        gfortran \
        libatlas-base-dev \
        libxml2-dev \
        libxslt-dev \
        libxslt1-dev \
        python-numpy \
        python-scipy \
        libhdf5-serial-dev \
        gnuplot \
        poppler-utils \
        antiword \
        catdoc \
        wv \
        html2text \
        gettext \
        unzip \
        giflib-tools \
        pstotext \
        sbcl \
        ppthtml \
        xlhtml \
        common-lisp-controller \
        make \
        automake1.9 \
        autoconf \
        sudo \
        ocrodjvu \
        pdf2djvu \
        djvulibre-bin \
        netpbm \
        pdftk \
        nodejs \
        software-properties-common \
        python-software-properties \
        libjpeg-dev \
        libfreetype6-dev \
        libtiff-dev \
        imagemagick \
        libopenjpeg2 \
        oggvideotools \
        vorbis-tools \
        libvpx-dev \
        mediainfo \
        x264 \
        lame \
        libass-dev \
        libgpac-dev \
        libsdl1.2-dev \
        libtheora-dev \
        libtool \
        libx11-dev \
        libva-dev \
        libxext-dev \
        pkg-config \
        texi2html \
        libxfixes-dev \
        zlib1g-dev \
        libvorbis-dev \
        libmp3lame-dev \
        libav-tools

RUN apt-get build-dep python-matplotlib -y

