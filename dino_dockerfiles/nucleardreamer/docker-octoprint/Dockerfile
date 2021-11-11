FROM python:2.7

ARG DEBIAN_FRONTEND=noninteractive

ADD http://dl.slic3r.org/linux/slic3r-linux-x86_64-1-2-9-stable.tar.gz /tmp/slic3r.tar.gz
ADD https://johnvansickle.com/ffmpeg/releases/ffmpeg-release-32bit-static.tar.xz /tmp/ffmpeg.tar.xz
ADD https://github.com/Ultimaker/CuraEngine/archive/15.04.6.tar.gz /tmp/cura.tar.gz

COPY rootfs /

RUN apt-get update -y && apt-get install --no-install-recommends -yqq \
      avrdude \
      build-essential \
      imagemagick \
      libav-tools \
      libjpeg62-turbo-dev \
      libv4l-0 \
      libv4l-dev \
      psmisc \
      subversion

# octoprint
RUN cd /opt/octoprint \
    && pip install -r requirements.txt \
    && python setup.py install

# other python packages and octoprint plugins
RUN for package in $(cat /tmp/packages.txt | xargs); do pip install $package; done

# slic3r
RUN tar xzf /tmp/slic3r.tar.gz -C /opt \
    && mv /opt/Slic3r /opt/slic3r \
    && ln -fs /opt/slic3r/bin/slic3r /usr/bin/ \
    && rm /tmp/slic3r.tar.gz

# mjpg-streamer
RUN cd /tmp && svn co https://svn.code.sf.net/p/mjpg-streamer/code mjpg-streamer \
    && cd /tmp/mjpg-streamer/mjpg-streamer \
    && patch -p0 < /tmp/mjpgstreamer-input-lib-uvc.patch \
    && make USE_LIBV4L2=true clean all \
    && make install

# ffmpeg
RUN mkdir -p /opt/ffmpeg \
    && tar xvf /tmp/ffmpeg.tar.xz -C /opt/ffmpeg --strip-components=1

# cura
RUN tar xzf /tmp/cura.tar.gz -C /tmp \
    && cd /tmp/CuraEngine-15.04.6 \
    && mkdir build \
    && make \
    && mv -f ./build /opt/cura/

RUN rm -rf /tmp/* && rm -rf /var/lib/apt/lists/*

CMD ["/usr/local/bin/supervisord"]

VOLUME /config
ENV MJPG_PORT=9999
EXPOSE 9999 5000
