FROM ubuntu:trusty

ARG VCS_REF
ARG BUILD_DATE

LABEL org.label-schema.build-date="$BUILD_DATE" \
      org.label-schema.name="avr-docker-build" \
      org.label-schema.description="A headless AVR build environment for Ubuntu" \
      org.label-schema.url="e.g. https://github.com/ratmandu/avr-docker-build" \
      org.label-schema.vcs-ref="$VCS_REF" \
      org.label-schema.vcs-url="https://github.com/ratmandu/avr-docker-build.git" \
      org.label-schema.schema-version="1.0"

RUN apt-get update -q && \
    DEBIAN_FRONTEND=noninteractive apt-get install -q -y --no-install-recommends \
        build-essential \
        ca-certificates \
        git \
        openssh-client \
        p7zip \
        gcc-avr \
        binutils-avr \
        gdb-avr \
        avr-libc \
        avrdude \
        unzip \
        zip \
        && apt-get clean

ADD http://www.atmel.com/images/avr32-headers-6.2.0.742.zip /tmp/avr/headers.zip
ADD http://www.atmel.com/images/avr32-gnu-toolchain-3.4.3.820-linux.any.x86.tar.gz /tmp/avr/avr32-toolchain.tar.gz

RUN echo "Extracting AVR32 Toolchain" \
    && cd /tmp/avr/ \
    && tar -xzvf avr32-toolchain.tar.gz \
    && unzip headers.zip

RUN echo "Moving AVR32 Toolchain to /opt" \
    && mv /tmp/avr/avr32-gnu-toolchain-linux_x86 /opt/avr32-tools \
    && mv /tmp/avr/avr32 /opt/avr32-tools/avr32/include

RUN locale-gen en_US.UTF-8 && DEBIAN_FRONTEND=noninteractive dpkg-reconfigure locales

ENV PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:/opt/avr32-tools/bin
