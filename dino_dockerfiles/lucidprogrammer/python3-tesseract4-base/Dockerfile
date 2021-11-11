FROM ubuntu:16.04 as build
LABEL maintainer="Lucid Programmer"
RUN apt-get update && apt-get install -y \
    build-essential \
    checkinstall \
    cmake \
  	git \
  	wget \
  	xzgv \
    # for Tesseract
    # https://github.com/tesseract-ocr/tesseract/wiki/Compiling
    g++ \
  	autoconf \
    automake \
    libtool \
  	autoconf-archive \
    pkg-config \
    # libpng12-dev provides libpng-dev
    libpng12-dev \
    libjpeg8-dev \
    libtiff5-dev \
    zlib1g-dev \
    # for building tesseract-training
    libicu-dev \
    libpango1.0-dev \
    libcairo2-dev \
    # for python build
    libreadline-gplv2-dev \
    libncursesw5-dev \
    libssl-dev \
    libsqlite3-dev \
    tk-dev \
    libgdbm-dev \
    libc6-dev \
    libbz2-dev

RUN mkdir /work
WORKDIR /work

ENV SCRIPTS_DIR /work/scripts
ENV PKG_DIR /home/pkg
ENV BASE_DIR /home/workspace
ENV TESSDATA_FAST ${BASE_DIR}/fast
ENV TESSDATA_BEST ${BASE_DIR}/best
ENV TESSDATA_LEGACY ${BASE_DIR}/legacy


# pin to the specific version of LEPTONICA which is recommended by tesseract
# for tesseract 4 (master branch), as of feb, 2018, it is 1.74.2
ENV LEP_VER 1.74.2
ENV LEP_TAR https://github.com/DanBloomberg/leptonica/archive/"${LEP_VER}".tar.gz
# just in case for later.
ENV LEP_REPO_URL https://github.com/DanBloomberg/leptonica.git
ENV LEP_SRC_DIR ${BASE_DIR}/leptonica
# tesseract
ENV TES_REPO_URL https://github.com/tesseract-ocr/tesseract.git
ENV TES_SRC_DIR ${BASE_DIR}/tesseract


RUN mkdir ${SCRIPTS_DIR}
RUN mkdir ${PKG_DIR}
RUN mkdir ${BASE_DIR}
RUN mkdir ${TESSDATA_FAST}
RUN mkdir ${TESSDATA_BEST}
RUN mkdir ${TESSDATA_LEGACY}

COPY ./container-scripts/* ${SCRIPTS_DIR}/
RUN chmod +x ${SCRIPTS_DIR}/*

# install the latest ImageMagick
RUN wget http://www.imagemagick.org/download/ImageMagick.tar.gz && \
    tar xvf ImageMagick.tar.gz && \
    cd ImageMagick-7* && \
    ./configure && \
    checkinstall -D --install=no -y --pakdir="${PKG_DIR}" --nodoc --pkgname=magick-latest

RUN ${SCRIPTS_DIR}/repos_clone.sh
RUN ${SCRIPTS_DIR}/compile_leptonica.sh
RUN ${SCRIPTS_DIR}/compile_tesseract.sh

ENV PATH /usr/local/bin:$PATH

# http://bugs.python.org/issue19846
# > At the moment, setting "LANG=C" on a Linux system *fundamentally breaks Python 3*, and that's not OK.
ENV LANG C.UTF-8

# runtime dependencies
RUN wget https://www.python.org/ftp/python/3.6.4/Python-3.6.4.tgz && \
    tar xzf Python-3.6.4.tgz && \
    cd Python-3.6.4 && \
    ./configure --enable-optimizations && \
    checkinstall -D --install=no -y --pakdir="${PKG_DIR}" --nodoc --pkgname=python-3_6_4



FROM ubuntu:16.04

RUN mkdir /debtemp
WORKDIR /debtemp

ENV HOME /root
ENV SOURCES /home/workspace
ENV TESSDATA_PREFIX /usr/local/share/tessdata
ENV LANG C.UTF-8

COPY --from=build /home/pkg /debtemp
COPY --from=build /home/workspace "${SOURCES}"

RUN mkdir -p "${TESSDATA_PREFIX}" && \
    apt-get update && apt-get install -y libenchant1c2a libmagickwand-dev && \
    cd /debtemp && dpkg -i *.deb && apt-get install -f && ldconfig && \
    cp "${SOURCES}"/fast/*.traineddata "${TESSDATA_PREFIX}" && \
    mkdir /work && cd /work && rm -rf /debtemp && rm -rf /var/lib/apt/lists/* && \
    echo "alias pip=pip3.6">>"$HOME"/.bashrc && \
    echo "alias python=python3.6">>"$HOME"/.bashrc

WORKDIR /work
