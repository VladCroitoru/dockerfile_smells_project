FROM ubuntu:18.04 as builder
MAINTAINER https://github.com/aronahl
WORKDIR /root/
RUN apt-get update 
RUN apt-get install --no-install-recommends -fy \
        build-essential \
        gconf2 \
        intltool \
        libglib2.0-dev \
        libnss3-dev \
        libidn11-dev \
        libmeanwhile-dev \
        libncurses5-dev \
        libtool \
        libxml2-dev \
        mercurial \
        wget \
        python-minimal
RUN hg clone https://bitbucket.org/pidgin/main
WORKDIR /root/main 
RUN hg update v2.13.0
RUN ./autogen.sh --disable-gtkui --disable-gstreamer --disable-vv --disable-avahi --disable-dbus --disable-perl --disable-tcl
RUN make install
WORKDIR /root
RUN rm -fr main
RUN apt-get install -fy -qq python-pip
RUN pip install dumb-init
VOLUME /root/.purple
ENV LD_LIBRARY_PATH=/usr/local/lib:/usr/lib:/lib
CMD /usr/local/bin/dumb-init /usr/local/bin/finch
WORKDIR /tmp
RUN apt-get install -fy git
RUN git clone https://github.com/kacf/slack-libpurple.git
WORKDIR /tmp/slack-libpurple
RUN make
RUN mkdir -p /usr/local/share/pixmaps/pidgin/protocols/16 /usr/local/share/pixmaps/pidgin/protocols/22 /usr/local/share/pixmaps/pidgin/protocols/48
RUN make install


FROM ubuntu:18.04
ENV LD_LIBRARY_PATH=/usr/local/lib:/usr/lib:/lib \
    DEBIAN_FRONTEND=noninteractive
RUN apt-get update && \
    apt-get install -qq -fy libglib2.0 && \
    apt-get install -qq -fy libidn11 && \
    apt-get install -qq -fy libnss3 && \
    apt-get autoclean -y && \
    apt-get clean -y && \
    apt-get autoremove -y && \
    rm -rf /var/lib/apt/lists/*
COPY --from=builder /usr/local/ /usr/local/
CMD /usr/local/bin/dumb-init /usr/local/bin/finch
