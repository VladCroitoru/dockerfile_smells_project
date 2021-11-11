FROM fedora:21
LABEL maintainer="Thomas Kärgel kaergel at b1-systems.de"

RUN yum makecache; \
    yum -y group install 'C Development Tools and Libraries'; \
    yum -y install \
    libusb-devel \
    python2 \
    python2-devel \
    python-pip \
    wget \
    svn \
    lm_sensors && \
    pip install py-cpuinfo
RUN wget --no-check-certificate -O serdisplib.tar.gz https://sourceforge.net/projects/serdisplib/files/latest/download && \
    mkdir /serdisplib/ && \
    svn co https://ssl.bulix.org/svn/lcd4linux/trunk lcd4linux
WORKDIR /serdisplib
RUN tar --strip 1 -xvzpf ../serdisplib.tar.gz && \
    sh configure && \
    make all && \
    make install && \
    ln -s /usr/local/lib/libserdisp.so.2 /lib64/libserdisp.so.2
WORKDIR /lcd4linux/
RUN libtoolize && \
    automake --add-missing && \
    ./configure --with-plugins='all,!dbus,!mpris_dbus' --with-python && \
    make || make && \
    make install 

COPY ./entrypoint.sh /
ENTRYPOINT ["/entrypoint.sh"]
CMD ["/lcd4linux/lcd4linux","-F","-v"]
