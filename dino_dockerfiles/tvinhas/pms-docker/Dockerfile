FROM plexinc/pms-docker:plexpass

RUN apt-get update && \
    apt-get upgrade -y && \
    apt-get install -y git build-essential libargtable2-dev autoconf \
    automake libtool libtool-bin ffmpeg libsdl1.2-dev libavutil-dev \
    libavformat-dev libavcodec-dev mkvtoolnix bc && \
    cd /opt && \
    git clone git://github.com/erikkaashoek/Comskip && \
    cd Comskip && \
    ./autogen.sh && \
    ./configure --enable-donator && \
    make

ADD ./adskip.sh /usr/bin/adskip.sh
ADD ./comskip.ini /usr/lib/plexmediaserver/Resources/comskip.ini
RUN chmod 755 /usr/bin/adskip.sh
