FROM davidsblog/openwrt-build-15-05-ht-tm02

RUN cd /home &&\
    git clone -b master git://github.com/nim-lang/Nim.git  &&\
    cd Nim &&\
    git clone -b master --depth 1 git://github.com/nim-lang/csources &&\
    cd csources && sh build.sh &&\
    cd .. &&\
    bin/nim c koch &&\
    ./koch boot -d:release

COPY config_nim.cfg /home/Nim/config/nim.cfg

ENV STAGING_DIR=/home/openwrt/openwrt/staging_dir/
ENV PATH /home/Nim/bin:/home/openwrt/openwrt/staging_dir/toolchain-mipsel_24kec+dsp_gcc-4.8-linaro_uClibc-0.9.33.2/bin/:$PATH
