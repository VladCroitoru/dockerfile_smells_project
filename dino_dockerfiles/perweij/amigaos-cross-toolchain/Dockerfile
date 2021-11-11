# To build and publish image run following commands:
# > docker build -t perweij/amigaos-cross-toolchain:latest .
# > docker login
# > docker push perweij/amigaos-cross-toolchain:latest
FROM i386/debian:buster-slim


RUN rm -rf /var/lib/apt/lists/* &&\
    apt-get -y clean &&\
    apt-get -y update &&\
    apt-get -y upgrade


# build deps
RUN apt-get --no-install-recommends -y install bison git gperf python2.7-dev python-setuptools libncurses-dev ca-certificates stow curl


# extra development tools
RUN apt-get --no-install-recommends -y install build-essential fs-uae gettext python2.7 lhasa libgl1-mesa-dri


WORKDIR /usr/local/src


# some required files do not have reliable sources - get them from here instead,
# and extract inner archives.
RUN mkdir dl &&\
    cd dl &&\
    curl -o libm-src.lha http://nappe.acc.umu.se/mirror/archive/ftp.sunet.se/pub/aminet/dev/gg/libm-src.lha &&\
    lha x libm-src.lha &&\
    gzip libm-5.4-src.tar &&\
    curl -o libamiga.lha http://nappe.acc.umu.se/mirror/archive/ftp.sunet.se/pub/aminet/dev/gg/libamiga.lha &&\
    lha x libamiga.lha &&\
    gzip libamiga-bin.tar


RUN git clone https://github.com/perweij/amigaos-cross-toolchain.git &&\
    cd amigaos-cross-toolchain &&\
    ./toolchain-m68k --prefix=/usr/local/stow/m68k-amigaos build &&\
    stow -d /usr/local/stow m68k-amigaos &&\
    ./toolchain-m68k --prefix=/usr/local/stow/m68k-amigaos install-sdk cgx \
                  guigfx mui mmu mcc_betterstring mcc_nlist mcc_texteditor mcc_thebar render sdi warp3d &&\
    stow -d /usr/local/stow m68k-amigaos --restow &&\
    ./toolchain-m68k --prefix=/usr/local test


# keep sources, for license reasons, and clean up
RUN tar -zcf amigaos-cross-toolchain.tar.gz amigaos-cross-toolchain &&\
    dpkg --purge bison git gperf python2.7-dev python-setuptools libncurses-dev stow curl &&\
    apt-get -y autoremove &&\
    apt-get -y clean &&\
    rm -rf /usr/local/src/dl /usr/local/src/amigaos-cross-toolchain /var/lib/apt/lists/*
