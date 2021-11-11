FROM sdthirlwall/raspberry-pi-cross-compiler

# Install some native build-time tools
#RUN install-debian scons

# Install raspbian development libraries
RUN install-raspbian --update
RUN install-raspbian libtinfo-dev libpng12-dev libavahi-client-dev libavahi-compat-libdnssd1 libqrencode-dev

RUN DEBIAN_FRONTEND=noninteractive apt-get --quiet --yes update \
    && DEBIAN_FRONTEND=noninteractive apt-get --quiet --yes install \
        avr-libc \
        avra \
        avrdude \
        avrp \
        avrprog \
        build-essential \
        binutils-avr \
        python \
        gcc-avr \
        gdb-avr \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists

WORKDIR /tmp

